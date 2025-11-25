# Write a Python script to send a message from the PC to Arduino using PySerial.
	
String msg;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}
void loop() {
  while (!Serial.available());
  msg = Serial.readString();
  Serial.println("Received: " + msg);
}
Python Code:
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.1)
def send_message(msg):
    arduino.write(bytes(msg, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    text = input("Enter message: ")
    response = send_message(text)
    print(response)
