//LDR gives out analog voltage when connected to 5v(VCC)

//servo motor 
#include <Servo.h> 
Servo myservo;  // create servo object to control a servo
int pos = 0;

//ldr and bulb control pins
const int ledPin=13;
const int ldrPin=A5; //analog input

void setup()
{
  Serial.begin(9600);
  
  pinMode(ledPin,OUTPUT);
  pinMode(ldrPin,INPUT);
  
  myservo.attach(9);
  myservo.write(pos);
}
void loop()
{
    //Control Bulb based on LDR
  int ldrStatus=analogRead(ldrPin);
  Serial.println(ldrStatus);
  if(ldrStatus<=550)   //when it's dark less conductivity(low voltage)
  {
    digitalWrite(ledPin,1);
    Serial.println("Dark outside, Bulb is ON");
  }
  else
  {
    digitalWrite(ledPin,0);
    Serial.println("Bright outside");
  }
  
  
    //Unlock and lock door(servo motor mechanism) based on Face Recognition
  if(Serial.available())
  {
    char char_data=Serial.read(); //read one byte from serial buffer and save it to the variable
    if(char_data=='o')
    {
      openlock();
    }
    else if(char_data=='c')
    {
      closelock();
    }
    delay(500);
  }  
}

void openlock()
{
  if(pos==0)
  {
    pos=90;
    myservo.write(pos);
    Serial.println("DOOR OPEN");
  }
  else
  {
    Serial.println("DOOR ALREADY OPEN");
  }
}

void closelock()
{
  if(pos==90)
  {
    pos=0;
    myservo.write(pos);
    Serial.println("Door CLOSED");
  }
  else
  {
    Serial.println("DOOR ALREADY CLOSED");
  }
}
