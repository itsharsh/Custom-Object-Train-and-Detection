void activateLinearActuator() {
  if (mapped_data[RC_LINEAR_ACTUATOR_INDEX] < 2) {
    noInterrupts();
    digitalWrite(actuator_brake_pin, LOW);
    digitalWrite(actuator_dir_pin, HIGH);
    analogWrite(actuator_pwm_pin, actuator_pwm_value);
    interrupts();
  }
  else if (mapped_data[RC_LINEAR_ACTUATOR_INDEX] > 3) {
    
    digitalWrite(actuator_brake_pin, LOW);
    digitalWrite(actuator_dir_pin, LOW);
    analogWrite(actuator_pwm_pin, actuator_pwm_value);
  }
  else {
    digitalWrite(actuator_brake_pin, HIGH);
    digitalWrite(actuator_pwm_pin, 0);
  }
}

void activateThermalCamera() {
  if (mapped_data[RC_THERMAL_TRANS_INDEX] > 3) {
    relay_value[RELAY_THERMAL_TRANS_INDEX] = LOW;
    //    Serial.print("\tThermalON");
  }
  else {
    relay_value[RELAY_THERMAL_TRANS_INDEX] = HIGH;
    //    Serial.print("\tThermalOFF");
  }
}

void activateZoomCameraTrans() {
  if (mapped_data[RC_ZOOM_TRANS_INDEX] > 3) {
    relay_value[RELAY_ZOOM_TRANS_INDEX] = LOW;
    //    Serial.print("\tZoomON");
  }
  else {
    relay_value[RELAY_ZOOM_TRANS_INDEX] = HIGH;
    //    Serial.print("\tZoomOFF");
  }
}

void activateZoomFocus() {
  //Zoom
  if (mapped_data[RC_CAM_ZOOM_INDEX] < 2) {         //Zoom In
    digitalWrite(FPV_COM_PIN, LOW);
    digitalWrite(FPV_ZOOM_PIN, HIGH);
    //    Serial.print("\tZoomIN");
  }
  else if (mapped_data[RC_CAM_ZOOM_INDEX] > 3) {      //Zoom Out
    digitalWrite(FPV_COM_PIN, HIGH);
    digitalWrite(FPV_ZOOM_PIN, LOW);
    //    Serial.print("\tZoomOUT ");
  }

  //Focus
  else if (mapped_data[RC_CAM_FOCUS_INDEX] < 2) {         //Focus 1
    digitalWrite(FPV_COM_PIN, LOW);
    digitalWrite(FPV_ZOOM_PIN, LOW);
    digitalWrite(FPV_FOCUS_PIN, HIGH);
    //    Serial.print("\tFocus1");
  }
  else if (mapped_data[RC_CAM_FOCUS_INDEX] > 3) {         //Focus 2
    digitalWrite(FPV_COM_PIN, HIGH);
    digitalWrite(FPV_ZOOM_PIN, HIGH);
    digitalWrite(FPV_FOCUS_PIN, LOW);
    //    Serial.print("\tFocus2");
  }

  else {
    digitalWrite(FPV_COM_PIN, LOW);
    digitalWrite(FPV_ZOOM_PIN, LOW);
    digitalWrite(FPV_FOCUS_PIN, LOW);
  }
}

void activatePanTilt() {
  //PAN
  if (mapped_data[RC_PAN_INDEX] < 2) {
    relay_value[RELAY_PAN_LEFT_INDEX] = HIGH;
    relay_value[RELAY_PAN_RIGHT_INDEX] = LOW;
    Serial.print("\tPANLeft");
  }
  else if (mapped_data[RC_PAN_INDEX] > 3) {
    relay_value[RELAY_PAN_LEFT_INDEX] = LOW;
    relay_value[RELAY_PAN_RIGHT_INDEX] = HIGH;
    Serial.print("\tPANRight");
  }
  else {
    relay_value[RELAY_PAN_LEFT_INDEX] = HIGH;
    relay_value[RELAY_PAN_RIGHT_INDEX] = HIGH;
  }

  //TILT
  if (mapped_data[RC_TILT_INDEX] < 2) {
    relay_value[RELAY_TILT_UP_INDEX] = LOW;
    relay_value[RELAY_TILT_DOWN_INDEX] = HIGH;
    Serial.print("\tTiltUP");
  }
  else if (mapped_data[RC_TILT_INDEX] > 3) {
    relay_value[RELAY_TILT_UP_INDEX] = HIGH;
    relay_value[RELAY_TILT_DOWN_INDEX] = LOW;
    Serial.print("\tTiltDOWN");
  }
  else {
    relay_value[RELAY_TILT_UP_INDEX] = HIGH;
    relay_value[RELAY_TILT_DOWN_INDEX] = HIGH;
  }
}

void activateLED() {
  if (mapped_data[RC_LED_INDEX] > 3 && mapped_data[RC_LED_INDEX] != prev_led_RC) {
    relay_value[RELAY_LED_INDEX] = !relay_value[RELAY_LED_INDEX];
    //    Serial.print("\tLEDTrig");
  }
}

void writeToRelay() {
  for (int i = 0; i < RELAY_TOTAL_CHANNEL; i++) {
    digitalWrite(relay_pin[i], relay_value[i]);
  }
}
