import RPi.GPIO as gpio
import time

gpio.setup(3, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
j = str(input("Digite um nome: "))  
time.sleep(1)
        
for i in j:
          if i == "a": # ( .- )
              gpio.output(5, 1)
              time.sleep(0.5)
              gpio.output(5, 0)
              time.sleep(0.5)
              gpio.output(3, 1)
              gpio.output(5, 1)
              gpio.output(7, 1)
              time.sleep(0.5)
              gpio.output(3, 0)
              gpio.output(5, 0)
              gpio.output(7, 0)
              time.sleep(1)
          if i == "b": # ( -... )
              gpio.output(3, 1)
              gpio.output(5, 1)
              gpio.output(7, 1)
              time.sleep(0.5)
              gpio.output(3, 0)
              gpio.output(5, 0)
              gpio.output(7, 0)
              time.sleep(0.5)
              gpio.output(5, 1)
              time.sleep(0.5)
              gpio.output(5, 0)
              time.sleep(0.5)
              gpio.output(5, 1)
              time.sleep(0.5)
              gpio.output(5, 0)
              time.slee
