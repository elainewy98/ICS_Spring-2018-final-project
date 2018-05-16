import pygame
import sys
from pygame.locals import *
import random

#superman 
class Superman():
     def __init__(self, pos_x, pos_y, speed):  
         #initalize
          self.images = [superman_0_image, superman_1_image, superman_2_image]
          #the number of picture is playing
          self.order = 0  
          #number of pictures to put to make superman move
          self.number = 3   
          self.image = self.images[self.order]
          #initalize a rect to represent picture
          self.rect = self.image.get_rect()  
          #coordinate of the left-up conner
          self.rect.x = pos_x  
          self.rect.y = pos_y
          #detect the position of the superman      
          self.base = pygame.Rect(self.rect.x + 6, self.rect.y + 13, 34, 24)
          self.speed_y = speed
          #situation of crushing
          self.crash = 0  
          #the score
          self.score = 0
          #initialize in open screen, decide the flying direction
          self.direct = 1
          
          
     def draw(self, screen): #draw on the screen
          screen.blit(self.image, (self.rect.x, self.rect.y)) #the move of moving arms of superman
          
     def flap(self):  
          if self.order >= self.number - 1:
              self.order = -1
          self.order += 1
          self.image = self.images[self.order]
          
     def move_y(self):  #how superman moves and record the score
          coin_sound = pygame.mixer.Sound("coin_sound.wav")
          self.rect.y += self.speed_y
          self.speed_y += gravity
          self.base = pygame.Rect(self.rect.x + 6, self.rect.y + 13, 34, 24)
          if self.rect.x == sword_1.rect_up.x or self.rect.x == sword_2.rect_up.x + 1:
               coin_sound.play()
               #determine the score
               self.score = max(sword_1.order, sword_2.order) - 1
               
        #initalize the move of superman,moving up and down
     def up_and_down(self, pos_y):  
          if self.rect.y <= pos_y:
               self.direct = 1
               self.rect.y += self.direct
          elif self.rect.y >= pos_y + 5 :
               self.direct = -1
               self.rect.y += self.direct
          else:
               self.rect.y += self.direct
               
        #when superman fly at the beginning,only moving down
     def soar(self, speed):  
          self.speed_y = speed
          
         #when superman falls
     def drop(self):  
          self.rect.y += self.speed_y
          self.speed_y += gravity
          
          #when superman dies
     def die(self):  
          self.rect.y = 365
          self.image = self.images[2]
          
#class of sword1
class Sword_1():
     def __init__(self): 
         #initialize the sword on both side
          self.images = [sword_up_image, sword_down_image]
          self.rand= random.randrange(50, 270, 20)
          #the sword on the top
          self.rect_up = self.images[0].get_rect()  
          #the sword on the ground
          self.rect_down = self.images[1].get_rect() 
          #the order of the sword (-record score)
          self.order = 1  
          #the position of the sword
          self.rect_up.x = 1 * screen_width  
          self.rect_down.x = 1 * screen_width
          self.rect_up.y = 400 - self.rand
          self.rect_down.y  = - self.rand - 20
          
          #draw the sword on the screen
     def draw(self, screen):  
          screen.blit(self.images[0], (self.rect_up.x, self.rect_up.y))
          screen.blit(self.images[1], (self.rect_down.x, self.rect_down.y))
          
          #the move of the sword
     def move_x(self):  
          if self.rect_up.x > -sword_width:
               self.rect_up.x -= sword_speed
               self.rect_down.x -= sword_speed
          else:
               self.reset()
               
          #when pictures out of screen, reset it back
     def reset(self): 
          self.rand = random.randrange(50, 270, 20)
          self.rect_up.x = screen_width
          self.rect_down.x = screen_width
          self.rect_up.y = 400 - self.rand
          #the distance between two swords
          self.rect_down.y  = -self.rand - 20  
          self.order += 2
          
          #determine the collide situation of superman
     def collide(self, superman_rect): 
          if self.rect_up.colliderect(superman_rect):
               collide_sword = 1
          elif self.rect_down.colliderect(superman_rect):
               collide_sword= 1
          else:
               collide_sword = 0
          return collide_sword

     
#almost same as sword1
class Sword_2():
     def __init__(self):
          self.images = [sword_up_image, sword_down_image]
          self.rand= random.randrange(50, 270, 20)
          self.rect_up = self.images[0].get_rect()
          self.rect_down = self.images[1].get_rect()
          self.order = 0
          self.reset()
     def draw(self, screen):
          screen.blit(self.images[0], (self.rect_up.x, self.rect_up.y))
          screen.blit(self.images[1], (self.rect_down.x, self.rect_down.y))
     def move_x(self):
          if sword_1.rect_up.x < self.rect_up.x:
               self.rect_up.x = sword_1.rect_up.x + (screen_width + sword_width)/2
               self.rect_down.x = sword_1.rect_down.x + (screen_width + sword_width)/2
          elif sword_1.rect_up.x > self.rect_up.x and self.rect_up.x > -sword_width:
               self.rect_up.x -= sword_speed
               self.rect_down.x -= sword_speed
          else:
               self.reset()
     def reset(self):
          self.rand = random.randrange(50, 270, 20)
          self.rect_up.x = sword_1.rect_up.x + (screen_width + sword_width)/2
          self.rect_down.x = sword_1.rect_up.x + (screen_width + sword_width)/2
          self.rect_up.y = 400 - self.rand
          self.rect_down.y  = - self.rand - 20
          self.order += 2
     def collide(self, superman_rect):
          if self.rect_up.colliderect(superman_rect):
               collide_sword = 1
          elif self.rect_down.colliderect(superman_rect):
               collide_sword= 1
          else:
                collide_sword = 0
          return collide_sword

     
###class land
class Land():
     def __init__(self):  
         #initalize
          self.image = land_image
          self.rect = self.image.get_rect()
          self.rect.x = 0
          self.rect.y = 400
          
          #draw it on screen
     def draw(self, screen):  
          screen.blit(self.image, (self.rect.x, self.rect.y))
          
          #the move of the ground-move the picture back when it is out of range
     def move_x(self):  
          if self.rect.x > -300:
               self.rect.x -= sword_speed
          else:
               self.rect.x = 0
               
        #determine the collide of the superman 
     def collide(self, superman_rect):  
          if self.rect.colliderect(superman_rect):
               collide_land = 1
          else:
               collide_land = 0
               
          return collide_land
      

#class of score
class Score():
     def __init__(self):
          self.images = [num_0_image, num_1_image, num_2_image, num_3_image,
                         num_4_image, num_5_image, num_6_image, num_7_image,
                         num_8_image, num_9_image]
          self.hun_pos_3 = 252
          self.dec_pos_3 = 276
          self.dec_pos_2 = 264
          self.uni_pos_3 = 300 
          self.uni_pos_2 = 288
          self.uni_pos_1 = 276
          
          #make the score appear in the center, sort by the digits of the number
     def draw(self, screen, score):  
          if score < 10:  
               screen.blit(self.images[score], (self.uni_pos_1, 0))
          if score >= 10 and score <100:
               screen.blit(self.images[score%10], (self.uni_pos_2, 0))
               screen.blit(self.images[int(score/10)], (self.dec_pos_2, 0))
          if score > 100:
               screen.blit(self.images[score%10], (self.uni_pos_3, 0))
               screen.blit(self.images[int((score%100)/10)], (self.dec_pos_3, 0))
               screen.blit(self.images[int(score/100)], (self.hun_pos_3, 0))

#variables
gamename = "Flappy Superstar"              
screen_width = 600
screen_height = 512
sword_width = 52
sword_height = 320
sword_speed = 3
gravity = 1.2
soar_speed = -5
#superman's position in "play" screen 
play_x = 260
play_y = 200
#superman's position in "ready" screen 
ready_x = 60
ready_y = 250  
#superman's position in "game over" screen 
game_over_x = 60
game_over_y = 365  

#all picture files
background_image = pygame.image.load("super_bg2.jpg")
land_image = pygame.image.load("moonland.png")
sword_up_image = pygame.image.load("sword_up.png")
sword_down_image = pygame.image.load("sword_down.png")
superman_0_image = pygame.image.load("superman.png")
superman_1_image = pygame.image.load("superman2.png")
superman_2_image = pygame.image.load("superman3.png")
#counting score font
num_0_image = pygame.image.load("num_0.png")  
num_1_image = pygame.image.load("num_1.png")
num_2_image = pygame.image.load("num_2.png")
num_3_image = pygame.image.load("num_3.png")
num_4_image = pygame.image.load("num_4.png")
num_5_image = pygame.image.load("num_5.png")
num_6_image = pygame.image.load("num_6.png")
num_7_image = pygame.image.load("num_7.png")
num_8_image = pygame.image.load("num_8.png")
num_9_image = pygame.image.load("num_9.png")
#score board font
score_0_image = pygame.image.load("score_0.png")  
score_1_image = pygame.image.load("score_1.png")
score_2_image = pygame.image.load("score_2.png")
score_3_image = pygame.image.load("score_3.png")
score_4_image = pygame.image.load("score_4.png")
score_5_image = pygame.image.load("score_5.png")
score_6_image = pygame.image.load("score_6.png")
score_7_image = pygame.image.load("score_7.png")
score_8_image = pygame.image.load("score_8.png")
score_9_image = pygame.image.load("score_9.png")
medals_0_image = pygame.image.load("medal_grey.png")
medals_1_image = pygame.image.load("medal_gold.png")
medals_2_image = pygame.image.load("medal_silver.png")
medals_3_image = pygame.image.load("medal_tong.png")
title_image = pygame.image.load("super_title.png")
button_play_image = pygame.image.load("super_play.png")
ready_image = pygame.image.load("super_getready.png")
tutorial_image = pygame.image.load("super_tap.png")
game_over_image = pygame.image.load("super_gameover.png")
score_panel_image = pygame.image.load("score_panel.png")
new_image = pygame.image.load("new.png")

#initalize all classes
sword_1 = Sword_1()
sword_2 = Sword_2()
land = Land()
#control the speed
clock = pygame.time.Clock()  

#the initial page at the very beginning
def initial_page():
     pygame.init()
     #set_screen
     screen = pygame.display.set_mode([screen_width, screen_height]) 
     #set game name
     pygame.display.set_caption(gamename) 
     superman = Superman(play_x, play_y, 0)
     running=True
     while running:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running=False

                    #exit()
                   #pygame.quit()
                   
          mouse_x, mouse_y = pygame.mouse.get_pos()
          #if clicked play button--enter get ready page
          if pygame.mouse.get_pressed()[0] and mouse_x >= 235 and mouse_x <= 360 and mouse_y >= 280 and mouse_y <= 340:
               break
          screen.blit(background_image, (0, 0))
          screen.blit(title_image, (150, 80))
          screen.blit(button_play_image, (242, 284))
          superman.up_and_down(play_y)
          superman.flap()
          superman.draw(screen)
          land.move_x()
          land.draw(screen)
          pygame.display.update()
          clock.tick(30)
     pygame.quit()
     

          
# the get ready page
def ready_page():
     pygame.init()
     screen = pygame.display.set_mode([screen_width, screen_height])
     pygame.display.set_caption(gamename)
     superman = Superman(ready_x, ready_y, 0)
     running=True
     while running:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running=False

                   #exit()
          #if clicked, return the pos of superman to make the transition smooth
          if pygame.mouse.get_pressed()[0]:
               superman.soar(soar_speed)
               return [superman.rect.x, superman.rect.y, superman.speed_y]
               break
           
          screen.blit(background_image, (0, 0))
          screen.blit(ready_image, (190, 80))
          screen.blit(tutorial_image, (200, 250))
          superman.up_and_down(ready_y)
          superman.flap()
          superman.draw(screen)
          land.move_x()
          land.draw(screen)
          pygame.display.update()
          #control the speed
          clock.tick(30)
     pygame.quit()
     
          
###play page, receive info from last state -make move smooth
def start_page(start_x, start_y, start_speed):
     pygame.init()
     #collide sound
     collide_sound = pygame.mixer.Sound("collide_sound.wav")  
     #load backgrounf music
     pygame.mixer.music.load("bg_music.wav")  
     pygame.mixer.music.set_volume(0.5)
     pygame.mixer.music.play(-1)
     screen = pygame.display.set_mode([screen_width, screen_height])
     pygame.display.set_caption(gamename)
     superman = Superman(start_x, start_y, start_speed)
     #initalize in case play game again, prevent the initial pos of swords inheriate the pos
     #of last game
     sword_1.__init__()  
     sword_2.__init__()
     score = Score()
     first_collide = 1
     running=True
     while running:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running=False
               
          screen.blit(background_image, (0, 0))
          #fly normally
          if sword_1.collide(superman.base) == 0 and sword_2.collide(superman.base) ==0 and \
                  land.collide(superman.rect) == 0:
               if pygame.mouse.get_pressed()[0]:
                    superman.soar(soar_speed)

               sword_1.move_x()
               sword_1.draw(screen)
               sword_2.move_x()
               sword_2.draw(screen)
               superman.move_y()
               superman.flap()
               superman.draw(screen)
               land.move_x()
               land.draw(screen)
               score.draw(screen, superman.score)
               
               #collide the sword
          elif (sword_1.collide(superman.base) == 1 or sword_2.collide(superman.base) ==1) and \
                  land.collide(superman.rect) == 0:
               if first_collide == 1:
                    collide_sound.play()
               
               sword_1.draw(screen)
               
               sword_2.draw(screen)
               superman.drop()
               superman.flap()
               superman.draw(screen)
               
               land.draw(screen)
               score.draw(screen, superman.score)
               first_collide = 0
              #fall on the ground
          else:
               sword_1.draw(screen)
               sword_2.draw(screen)
               superman.die()
               superman.draw(screen)

               land.draw(screen)
               score.draw(screen, superman.score)
               #update the picture
               pygame.display.update()
               #send score info to game over page
               return superman.score
           #enter game over page
               break
          pygame.display.update()
          clock.tick(30)
     pygame.quit()


###game overpage, receive info from last status and score-detremine the existence of new record
def game_over_page(score, best, new):
     pygame.init()
     pygame.mixer.music.load("dead_sound.wav")  
     pygame.mixer.music.set_volume(0.5)
     pygame.mixer.music.play()
     
     screen = pygame.display.set_mode([screen_width, screen_height])
     pygame.display.set_caption(gamename)
     superman = Superman(game_over_x, game_over_y, 0)
     restart = 0
     images = [score_0_image, score_1_image, score_2_image, score_3_image,
               score_4_image, score_5_image, score_6_image, score_7_image,
               score_8_image, score_9_image]
     running=True
     while running:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running=False
                    
                   #exit()
          
          mouse_x, mouse_y = pygame.mouse.get_pos()
          #if clickesd paly again
          if pygame.mouse.get_pressed()[0] and mouse_x >= 235 and mouse_x <= 360 and mouse_y >= 334 and mouse_y <= 395:
               restart = 1
               return restart
               break
          screen.blit(background_image, (0, 0))
          
          sword_1.draw(screen)
          
          sword_2.draw(screen)
          superman.die()
          superman.draw(screen)
          
          land.draw(screen)
          screen.blit(game_over_image, (200, 60))
          screen.blit(score_panel_image, (181, 183)) #25 156
          screen.blit(button_play_image, (242, 334))
          #classify the score to make it beautiful
          if score < 10:
               pass
          elif score >= 10 and score < 50:
               screen.blit(medals_3_image, (213, 226)) #57
          elif score >= 50 and score < 100:
               screen.blit(medals_2_image, (213, 226))
          elif score >= 100 and score < 500:
               screen.blit(medals_1_image, (213, 226))
          else:
               screen.blit(medals_0_image, (213, 226))
          if score < 10:
               screen.blit(images[score], (371, 219)) #215
          if score >= 10 and score <100:
               screen.blit(images[score%10], (371, 219))
               screen.blit(images[int(score/10)], (358, 219)) #202
          if score > 100:
               screen.blit(images[score%10], (371, 219))
               screen.blit(images[int((score%100)/10)], (371, 219))
               screen.blit(images[int(score/100)], (345, 219))
          #showthe best score
          if best < 10:
               screen.blit(images[best], (371, 261))
          if best >= 10 and best <100:
               screen.blit(images[best%10], (371, 261))
               screen.blit(images[int(best/10)], (358, 261))
          if best > 100:
               screen.blit(images[best%10], (371, 261))
               screen.blit(images[int((best%100)/10)], (358, 261))
               screen.blit(images[int(best/100)], (345, 261))
          if new == 1:
               screen.blit(new_image, (321, 243))
          pygame.display.update()
          clock.tick(30)
     pygame.quit()
     

#main structure      
def run():
    #play page
     #print('hello game')
     initial_page()  
     restart = 1  
     best = 0
     #restart?
     while restart:  
         #chasing new record
          new = 0  
          #ready page
          [start_x, start_y, start_speed] = ready_page()  
          #start page
          score = start_page(start_x, start_y, start_speed)
          print("This time your score is:",score)
          if score ==0:
              print("Your score is 0? loooooooool")
          if score > best:
               best = score
               new = 1
          print("So far, your best socre is:", best)
          
          if best >10:
              print("That is so good!! You are a genius of FLAPPY SUPERMAN!")
          elif best <5:
              print("Your best score is less than 5? Seriously?")
          print("")
          #game over page
          restart = game_over_page(score, best, new)
     #print('bye')
     return score
     
#start
if __name__ == "__main__":
    run()          

