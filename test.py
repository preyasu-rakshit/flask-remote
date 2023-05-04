import pygame

pygame.init()
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

button_keys={
  "1": 0,
  "2": 1,
  "3": 2,
  "4": 3,
  "L2": 4,
  "R2": 5,
  "L1": 6,
  "R1": 7,
  "select": 8,
  "start": 9,
  "up_arrow": 10,
  "down_arrow": 11,
  "left_arrow": 12,
  "right_arrow": 13
}
def get_joystick():
    """To read the joystick buttons this fun return button"""
    for event in pygame.event.get():
        button = ''
        # right buttons and joystick
        key = '1','2','3','4'
        stop_key = '1x','2x','3x','4x'
        if event.type == pygame.JOYBUTTONDOWN:
            for i,val in enumerate(key):
                if event.button == button_keys[key[i]]:
                    button = key[i]
                    return button

        if event.type == pygame.JOYBUTTONUP:
            for i, val in enumerate(key):
                if event.button == button_keys[key[i]]:
                    button = stop_key[i]

        return button


while True:
    print(get_joystick())