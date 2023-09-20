#include <Servo.h>

Servo servo1;
Servo servo2;
int servo1Pin = 4;
int servo2Pin = 5;
int servoPos1 = 0;
int servoPos2 = 90;

int cambien = 7;
int gtcambien;



int dulieu = 0;

void setup() 
{
  Serial.begin(9600);

  pinMode(cambien, INPUT);



  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  servo1.write(servoPos1);
  servo2.write(servoPos2);
}
void nhanData()
{

        if(Serial.available() > 0)
        {
          dulieu = Serial.read();
            if (dulieu=='1'){
            Serial.println("CAN");
            servo_1();
            
          }
            if (dulieu=='2')
          {
            Serial.println("BOTTLE");  
            servo_2();
         
          }
        delay(100);
        }
}
void servo_1()
{
         for (servoPos1=0; servoPos1<=120; servoPos1=servoPos1+1){
        servo1.write(servoPos1);  
        delay(30);  
        }
        for(servoPos1=120; servoPos1>=0; servoPos1=servoPos1-1){
        servo1.write(servoPos1);  
        delay(30);
        }
}
void servo_2()
{
        for (servoPos2=90; servoPos2>=0; servoPos2=servoPos2-1){
        servo2.write(servoPos2);  
        delay(50);  
        }
        for(servoPos2=0; servoPos2<=90; servoPos2=servoPos2+1){
        servo2.write(servoPos2);  
        delay(50);
        }
   
        
}
void loop() 
{
  gtcambien = digitalRead(cambien);  
  if(gtcambien ==0 )
  {
    Serial.println("CB1 CÓ VẬT CẢN: ");
    nhanData();
  }
  else 
  {
    Serial.println(" CB1 KHÔNG CÓ VẬT CẢN: ");

    
  }
  
}