
int led=13;
int ldr_input=A5;

void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  pinMode(ldr_input,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
      //Control Bulb based on LDR
  int ldrStatus=analogRead(ldr_input);
  Serial.println(ldrStatus);
  if(ldrStatus<=550)   //when it's dark less conductivity(low voltage)
  {
    digitalWrite(led,1);
    Serial.println("Dark outside, Bulb is ON");
  }
  else
  {
    digitalWrite(led,0);
    Serial.println("Bright outside");
  }
//  Serial.println(ldrStatus);
}
