#include<Servo.h>

Servo Door;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
  Door.attach(5); //Attach Vertical Servo to Pin 5
