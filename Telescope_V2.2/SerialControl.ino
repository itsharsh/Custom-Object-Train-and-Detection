/*
            ********* Bit Description *********

  Index   Index Name    Stands for              Value Mean
  0       MR            Mode Recognition Bit    0 - Manual    1 - Automatic
  1       LE           LED Enable Bit          0 - Disable   1 - Enable
  2       TCE           Thermal Cam Enable Bit  0 - Disable   1 - Enable
  3       ZCE           Zoom Cam Enable Bit     0 - Disable   1 - Enable
  4       PE            Pan Enable Bit          0 - Disable   1 - Enable
  5       TE            Tilt Enable Bit         0 - Disable   1 - Enable
  6       ZE            Zoom Enable Bit         0 - Disable   1 - Enable
  7       FE            Focus Enable Bit        0 - Disable   1 - Enable
  8       PLR           Pan Left/Right          0 - Right     1 - Left
  9       TUD           Tilt Up/Down            0 - Down      1 - Up
  10      ZIO           Zoom In/Out             0 - Out       1 - In
  11      FIO           Focus In/Out            0 - Out       1 - In

*/

//   indices
#define FIO 11
#define ZIO 10
#define TUD 9
#define PLR 8
#define FE 7
#define ZE 6
#define TE 5
#define PE 4
#define ZCE 3
#define TCE 2
#define LE 1
#define MR 0


uint16_t controlByte = (0 << FIO) | (0 << ZIO) | (0 << TUD) | (0 << PLR) | (0 << FE) | (0 << ZE) | (0 << TE) | (0 << PE) | (0 << ZCE) | (0 << TCE) | (0 << LE) | (0 << MR);
//int RC_TOTAL_CHANNEL = 8;
//int  mapped_data[] = {0, 0, 0, 0, 0, 0, 0, 0};
int bitarr[sizeof(controlByte) * 8];


void serialControl() {
  while (!Serial.available());    //hold till the Serial data is not available
  
  controlByte = Serial.parseInt();   //store the received data in a 16 bit variable
  for (int i = MR; i <= sizeof(controlByte) * 8 - 1; i++)   //store the binary values to an array
    bitarr[i] = bitRead(controlByte, i);
//for (int i = sizeof(controlByte)*8 - 1; i >= MR; i--)     //print the received data in binary 
//  Serial.print(bitarr[i]);
  
  decodeBit();
}

void decodeBit() {
  //type of mode
  if (bitarr[MR] == 0)  Serial.println("Manual Mode");
  else  Serial.println("Automatic Mode");

  for (int i = LE; i <= FE; i++) {
    if (bitarr[i] == 0) {
//    Serial.println("Stopping block");
      if (i < PE)  mapped_data[i] = 0;
      else  mapped_data[i] = 2;
    }
    else {
//    Serial.println("Actuation block");
      if (i < PE)   mapped_data[i] = 4;
      else if (bitarr[i + 4] == 0)  mapped_data[i] = 0;
      else  mapped_data[i] = 4;
    }
  }
}
