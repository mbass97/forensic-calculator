from sympy import symbols, diff
from sympy import symbols, integrate
import math


print("Welcome to forensic calculator detective Holmes!\n")

bodyTemp1 = input("Please input the temperature of the body when it was found(in celcius):\n")
roomTemp = input("what was the room temperature when you took the temperature of the body?:\n")

print("Now we wait awhile to test the body's temperature again so we can calculate exactly when the victim passed away.\n")

bodyTemp2 = input("what was the body's temperature after waiting(in celcius)?:\n")
time2 = input("How long did you wait before testing the bodys temperature again(in hours)?:\n")
timeOfDayFound = input("What time was it when you found the body(in military time, without colon)?:\n")
            
normBodyTemp = 37
time1 = 0
try:
    integralConstant = (bodyTemp1 - roomTemp)
    eKonstant = (((bodyTemp2 - roomTemp) / integralConstant)**(1/time2))
    eKonstantNoExp = ((bodyTemp2 - roomTemp) / integralConstant)
    timeSinceDeath = (time2 * math.log((normBodyTemp - roomTemp) / integralConstant)) / math.log(eKonstantNoExp)

    timeElapsed = timeSinceDeath * 60
    timeOfDeath = ((timeOfDayFound * 60) + timeElapsed) / 60
    toMinutes = (timeOfDeath % 1)
    todHour = timeOfDeath - toMinutes
    toMinutes = toMinutes * 60
    print("final time of death was " + str(int(todHour)) + ":" + str(int(toMinutes)))
except:
    print("Bad value in input")

