# Write python script to continuously send commands ('ON' or 'OFF') to control an LED on Arduino.

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)
def send_cmd(cmd):
    arduino.write(cmd.encode())
    print("Sent:", cmd)
while True:
    x = input("Enter ON / OFF / q: ").upper()
    if x in ["ON", "OFF"]:
        send_cmd(x)
    elif x == "Q":
        print("Exit")
        break
    else:
        print("Invalid")

Arduino Code: 
String cmd;
void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available()) {
    cmd = Serial.readString();

    if (cmd == "ON") {
      digitalWrite(13, HIGH);
    } 
    else if (cmd == "OFF") {
      digitalWrite(13, LOW);
    }
  }
}
