int count=0;
int currentOn=7;
void setup()
{

 
  for (int i=2; i<12; i++){
  digitalWrite(i,HIGH);
  delay(100);
  digitalWrite(i,LOW);}
 
  for (int i=12; i>1; i--){
  digitalWrite(i,HIGH);
  delay(100);
  digitalWrite(i,LOW);}
  introSeq();
  count=0;
  introSeq();
  count=0;
  introSeq();
  count=0;
 
  digitalWrite(currentOn,HIGH);
}

void loop() {
  int right = analogRead(0);
  int left = analogRead(1);
 
  Serial.println(right);
  delay(100);
  if (right == 0)
  {
    digitalWrite(currentOn,LOW);
    currentOn-=1;
    digitalWrite(currentOn,HIGH);
  }

  if (left == 0)
  {
    digitalWrite(currentOn,LOW);
    currentOn+=1;
    digitalWrite(currentOn,HIGH);
  }
 
}

void introSeq(){ 
  for(int j=6; j>1; j--){
  digitalWrite(j,HIGH);
  digitalWrite(j+1+count,HIGH);
  delay(200);
  digitalWrite(j,LOW);
  digitalWrite(j+1+count,LOW);
  count += + 2;}}