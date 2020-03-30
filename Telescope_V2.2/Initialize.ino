void initRC() {
  //Setting RC_Channel_Pin as INPUT Mode
  for (int i = 0; i < RC_TOTAL_CHANNEL; i++) {
    pinMode(RC_channel_pin[i], INPUT);
    //    attachInterrupt(digitalPinToInterrupt(RC_channel_pin[i], , HIGH));

  }
}

void initRelay() {
  for (int i = 0; i < RELAY_TOTAL_CHANNEL; i++) {
    pinMode(relay_pin[i], OUTPUT);
    if(i!=6) relay_value[i] = HIGH;
    else relay_value[i] = LOW;
    digitalWrite(relay_pin[i], relay_value[i]);
  }
}

void initCamera() {
  //FPV Zoom Camera Control Pins
  pinMode(FPV_ZOOM_PIN, OUTPUT);
  pinMode(FPV_FOCUS_PIN, OUTPUT);
  pinMode(FPV_COM_PIN, OUTPUT);
  //Initializing FPV Zoom Camera control pins to LOW( Stable Feed)
  digitalWrite(FPV_COM_PIN, LOW);
  digitalWrite(FPV_ZOOM_PIN, LOW);
  digitalWrite(FPV_FOCUS_PIN, LOW);
}

void initLinearActuator() {
  //LMD18200_DRIVER Control Pins
  pinMode(actuator_pwm_pin, OUTPUT) ;  //we have to set PWM pin as output
  pinMode(actuator_dir_pin, OUTPUT) ; //Direction pin is set as output
  pinMode(actuator_brake_pin, OUTPUT) ; //Brake pin is set as output
  noInterrupts();
  digitalWrite(actuator_brake_pin, HIGH);
  analogWrite(actuator_pwm_pin, 0);
  interrupts();
}
