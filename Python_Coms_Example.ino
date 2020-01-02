//Include the library. If the IDE throws an error saying the file doesn't exist, follow the
//"Super quick setup instructions.docx" file, and it'll solve the issue within seconds
#include "Python.h";

Python myPy;

void setup() {
  //Start serial communications with a speed of 9600 bits per second. You can use any value you want,
  // but I just use this one as default.Just make sure that whatever you pick is the same for both
  // the arduino and the python scripts
  Serial.begin(115200);
}

void loop() {
  //In this example, we are just taking data from python, then returning it immediately back to it
  String dataInFromPython = myPy.readLine();
  
  myPy.writeLine(dataInFromPython);
}
