int x;
void setup() 
{
 Serial.begin(9600);  //same baud-rate as the python side
}
void loop() 
{
  if(Serial.available())
  {
    char char_data=Serial.read(); //read one byte from serial buffer and save it to the variable
    if(char_data=='o')
    {
      Serial.println("DOOR is open");
    }
    else if(char_data=='c')
    {
      Serial.println("DOOR is Closed");    
    }
    delay(500); 
  }



}
