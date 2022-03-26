#pip install keyboard
import keyboard
i=0
while i != 100:
    keyboard.write("HOLA", delay=0.1)
    keyboard.send("enter")
    i+=1
    print(i)

    