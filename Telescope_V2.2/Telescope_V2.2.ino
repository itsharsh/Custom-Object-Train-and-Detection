/* Relay Control
  Index Arduino
   0 <-> A7;   // [220vAC]IN4: Pan F
   1 <-> A6;   // [220vAC]IN3: Pan R
   2 <-> A3;   // [220vAC]IN2: Tilt F
   3 <-> A2;   // [220vAC]IN1: Tilt R
   4 <-> A1;   // [12vDC]IN1: Thermal Camera Transmitter
   5 <-> A0;   // [12vDC]IN2: Zoom Camera Transmitter
   6 >-> 13;   // [12vDC]IN3: LED
*/
#include<Wire.h>

#define RELAY_TOTAL_CHANNEL 7
#define RELAY_PAN_LEFT_INDEX 0
#define RELAY_PAN_RIGHT_INDEX 1
#define RELAY_TILT_UP_INDEX 2
#define RELAY_TILT_DOWN_INDEX 3
#define RELAY_LED_INDEX 4
#define RELAY_THERMAL_TRANS_INDEX 5
#define RELAY_ZOOM_TRANS_INDEX 6
byte relay_pin[RELAY_TOTAL_CHANNEL] = {A6, A5, A4, A3, A2, A1, A0};
byte relay_value[RELAY_TOTAL_CHANNEL] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};

/*RC Channel Pins to Arduino
  Index Channel   Nano    Function          (Taranis) (RadioLink)
    0 <--> 1  <--> 12 <-> Linear Actuator      SB         C            2-way
    1 <--> 2  <--> 11 <-> LED                  SH         H            1-way
    2 <--> 3  <--> 10 <-> PAN                  SA         E            2-way
    3 <--> 4  <--> 09 <-> TILT                 SD         g            2-way
    4 <--> 5  <--> 08 <-> Camera Zoom          SC         VR(A)        Pot
    5 <--> 6  <--> 07 <-> Camera Focus         S2         VR(C)        Pot
    6 <--> 7  <--> 06 <-> Thermal Camera       SF         A            1-way
    7 <--> 8  <--> 05 <1->Zoom Camera          S1         B            1-way
*/
#define RC_TOTAL_CHANNEL 8
#define RC_LINEAR_ACTUATOR_INDEX 0
#define RC_LED_INDEX 1
#define RC_THERMAL_TRANS_INDEX 2
#define RC_ZOOM_TRANS_INDEX 3
#define RC_PAN_INDEX 4
#define RC_TILT_INDEX 5
#define RC_CAM_ZOOM_INDEX 6
#define RC_CAM_FOCUS_INDEX 7

const uint16_t RC_channel_pin[] = {50, 51, 52, 53, 10, 11, 12, 13}; // an array to identify the PWM input pins (the array can be any length)
// first pin is channel 1, second is channel 2...etc

volatile int RC_channel_value[RC_TOTAL_CHANNEL] = {0, 0, 0, 0, 0, 0, 0, 0};
volatile int prev_RC_channel_value[RC_TOTAL_CHANNEL] = {0, 0, 0, 0, 0, 0, 0, 0};
int RC_pulse_min = 980;
int RC_pulse_max = 1995;
volatile  int mapped_data[RC_TOTAL_CHANNEL] = {0, 0, 0, 0, 0, 0, 0, 0};


//LMD18200_Driver -->> 48V DC Motor Driver
byte actuator_pwm_pin = 3;   //initializing pin 11 as pwm
byte actuator_dir_pin = 4;     //initializing pin 12 as direction
byte actuator_brake_pin = 5;   //initializing pin 13 as brak
byte actuator_pwm_value = 255;

//ZOOM Camera -->> Control pins ZFC
byte FPV_ZOOM_PIN = A7;    // Initializing pin A10 as zoom   (Z)
byte FPV_FOCUS_PIN = A8;   // Initializing pin A9 as focus  (F)
byte FPV_COM_PIN = A9;   // Initializing pin A8 as Common (C)

//LRF
#define slave_ID 0x10
#define buffer_length 10
unsigned char buffer_s[buffer_length];
unsigned char buffer_r[buffer_length];
unsigned int distance = 0;
int temp = 0;

//For single ranging
#define range_inst 0x83
#define range_insdes 0x00
#define range_checksum 0x7D
#define range_dl 4
//For Stop Ranging
#define srange_inst 0x84
#define srange_checksum 0x7C
#define srange_dl 3

byte prev_led_RC;

void setup() {
  Wire.begin();
  Serial.begin(115200);
  Serial1.begin(19200);
  setup_RCRead();


  initRC();
  initRelay();
  initCamera();
  //initLinearActuator();
}

void loop() {
//functions to be called if controlling wirelessly
//    getDataFromRC();
//    print_RCValue();
//    mapRCData();

//function to be called if controlling serially
    serialControl();
    
    printMappedData();
//    activateLRF();
//    activateLinearActuator();
    activateThermalCamera();
    activateZoomCameraTrans();
    activateZoomFocus();
    activatePanTilt();
    activateLED();

    writeToRelay();
    Serial.println();
}
