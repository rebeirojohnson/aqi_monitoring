String readdata;
long rememberTime=0;// this is used by the code

void setup()
{
  // mq-3 -  Alcohol, Benzine, CH4, Hexane, LPG, CO
  // mq-7 - Co and Coal gas
  // mq -9 Methane, Propane, and CO
  // mq -135 Ammonia (NH3), sulfur (S), Benzene (C6H6), CO2, and other harmful gases and smoke.
  // mq - 6 LPG, iso-butane, propane 
  
 Serial.begin(9600);        //Begin the Serial Communcation at Baud Rate of 9600

 //Declare the pinmode for all the sensors
 pinMode(A1, INPUT);
 pinMode(A2, INPUT);
 pinMode(A3, INPUT);
 pinMode(A4, INPUT);
 pinMode(A5, INPUT);
}
void loop(){
  if( (millis()- rememberTime) >= 5000){ 
  //Reading all the Sensor values
  float CH4 = analogRead(A1);
  float Coal = analogRead(A2);
  float CO = analogRead(A3);
  float Sulfur = analogRead(A4);
  float butane = analogRead(A5);
  
  String data = "{\"ch4\":\""+String(CH4)+"\",\"Coal\":\""+String(Coal)+"\",\"CO\":\""+String(CO)+"\",\"Sulfur\":\""+String(Sulfur)+"\",\"butane\":\""+String(butane)+"\"}";
  Serial.println(data);     
  rememberTime=millis();// remember Current millis() time

 }
}

