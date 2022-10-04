''' this is a 8 ball'''
import random
import time

question = input('ask me a yes or no question')

pick = random.randint(1,5)

print("Thinking......")
time.sleep(1.5)
print("Thinking.......")
time.sleep(1.5)
print("Thinking.......")
time.sleep(1.5)
print("Thinking.......")
time.sleep(1.5)
print("The answer is:")
time.sleep(1.5)

if pick == 1:
    print("Yes!")
if pick == 2:
    print ("No!")
if pick == 3:
    print("Maybe")
if pick == 4:
    print("It is ok")
if pick == 5:
    print("Ahhhhhhhhh")

    
