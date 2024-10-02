# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit
import pygame
from LunarLander import *
import csv
counter=0
fuelList= []

env = LunarLander()
env.reset()
exit_program = False
while not exit_program:
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                env.reset()

    # INSERT YOUR CODE HERE
    #
    # Implement a Lunar Lander AI 
    # Control the rocket by writing a list of if-statements that control the 
    # three rockets on the lander 
    #
    # The information you have available are x, y, xspeed, and yspeed
    # 
    # You control the rockets by setting the variables boost, left, and right
    # to either True or false
    #
    # Example, to get you started. If the rocket is close to the ground, turn
    # on the main booster
    # if x > 3 >-3:
    #     right = False
    #     Left = False 
        
    # if yspeed > 10:
    #     boost = True
    # else:
    #     boost = False
    
    # if  xspeed > 5:
    #     left = False 
    
    # if xspeed < -5:
    #     right=False

    # if x < 0: 
    #     left = True
    #     right = False
    # else:
    #     right=True
    #     left =False
    
    if yspeed > 10:
        boost = True
    else:
        boost = False
    
    
    if x < -5: 
        left = True
        right = False
    elif x>5:
        right=True
        left =False
    
    if  xspeed > 5:
        left = False 
    
    if xspeed < -5:
        right=False

    
    

  
    if done:
        counter +=1
        print(counter)
        fuelList.append(round(reward * 100) / 100)
        if (counter==1288):

            print(fuelList)
            print(sum(fuelList)/len(fuelList))
            with open('fuel_data.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Fuel'])
                for fuel in fuelList:
                    writer.writerow([fuel]) 

        else:
            env.reset()




#[16.39999999999953, 19.199999999999527, 35.79999999999959, 28.799999999999514, 24.199999999999502, 0, 16.399999999999537, 24.39999999999951, 0, 28.799999999999578, 22.7999999999995, 27.19999999999954, 25.39999999999951, 14.399999999999539, 17.99999999999953, 34.599999999999596, 35.1999999999996, 34.39999999999958, 17.99999999999953, 16.99999999999953, 34.3999999999996, 12.399999999999531, 18.39999999999952]
    



    # Modify and add more if-statements to make the rocket land safely
    # END OF YOUR CODE
print(fuelList)
env.close()