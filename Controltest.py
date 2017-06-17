import pygame, sys
from pygame.locals import *
from gpiozero import Motor, OutputDevice

motor1 = Motor(27, 24)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(22, 6)
motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(16, 23)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1)

pygame.init()

### Tells the number of joysticks/error detection
joystick_count = pygame.joystick.get_count()
print ("There is ", joystick_count, "joystick/s")
if joystick_count == 0:
    print ("Error, I did not find any joysticks")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    lh_axis_pos = my_joystick.get_axis(0)
    lv_axis_pos = my_joystick.get_axis(1)
    rh_axis_pos = my_joystick.get_axis(2)
    rv_axis_pos = my_joystick.get_axis(3)
    print (lh_axis_pos, lv_axis_pos,rh_axis_pos, rv_axis_pos)

    motor1.value = lv_axis_pos
    motor4.value = lv_axis_pos

    motor2.value = rv_axis_pos
    motor3.value = rv_axis_pos
