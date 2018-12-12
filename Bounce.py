
import arcade
import math
import Constants
from Point import Point
from Ball import Ball
from Arrow import Arrow
from miscellaneous import Misc
from Obstacles import Obstacle
import Cible
import Button

MENU_MAIN = 0
GAME_RUNNING = 1
GAME_OVER = 2
WELL_PLAYED = 3

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        self.ball = Ball(Constants.START_pos_X, Constants. START_pos_Y, 0, 0, Constants.CIRCLE_RADIUS, Constants.GREEN)
        self.arrow = Arrow(0, 0, 280, 280, 320, 320, [255, 0, 0, 120])  # color red transparent
        self.started = False
        self.listObstacles = []
        self.listCibles = []
        self.button_list = []
        self.current_state = 0

    def addObstacle(self, obstacle):
        self.listObstacles.append(obstacle)
    
    def addCible(self, cible):
        self.listCibles.append(cible)

    def createObstacles (self,A,B,color,width):
        obstacle = Obstacle( A,B, color, width)
        self.addObstacle(obstacle)

    def createCible(self,position):
        cible = Cible.Cible(position)
        self.addCible(cible)

    def createStartingButton(self,x,y,function):
         button = Button.StartTextButton(x, y, function)
         self.addButton(button)

    def createQuitButton(self,x,y,function):
        button =  Button.StopTextButton(x,y,function)
        self.addButton(button)

    def addButton(self,button):
        self.button_list.append(button)

    def startGame(self):
        self.current_state = GAME_RUNNING

    def stopGame(self):
         arcade.window_commands.close_window()

    def gameState(self):
        compteur = 0
        for cible in self.listCibles:
            if cible.color[0] == Constants.RED[0] and cible.color[1] == Constants.RED[1] and cible.color[2] == Constants.RED[2]:
                compteur = compteur+1
        if compteur == len(self.listCibles):
            self.current_state = WELL_PLAYED
        if self.ball.getActualSpeed()==0 and self.started:
            self.current_state = GAME_OVER

    def on_draw(self):
        arcade.start_render()
        if self.current_state == MENU_MAIN : self.draw_main_menu()
        elif self.current_state == GAME_RUNNING:  self.draw_game()
        elif self.current_state == GAME_OVER: self.draw_game_over()
        elif self.current_state == WELL_PLAYED: self.draw_well_played()
        
    def draw_well_played(self):
        output = "Congratulations !"
        arcade.draw_text(output, 180, 300, arcade.color.WHITE, 30)
        output = "Click for next level"
        arcade.draw_text(output, 180, 240, arcade.color.WHITE, 24)       
        
    def draw_main_menu(self):
        for button in self.button_list:
            button.draw()
        output = "Launch the ball and hit all the targets !"
        arcade.draw_text(output, 100, 200, arcade.color.WHITE, 16 )

    def update(self, delta_time):
        self.gameState()
        if self.current_state == GAME_RUNNING:
            self.ball.update()
            for obs in self.listObstacles:
                obs.update(self.ball)
            for cible in self.listCibles:
                cible.update(self.ball)

    
    def setup(self):
        arcade.set_background_color([0,128,255])
        #Obstacles
        self.createObstacles(Point(50,400), Point(200, 600), Constants.obstacle_color, Constants.obstacle_width)
        self.createObstacles(Point(350,300), Point(450, 300), Constants.obstacle_color, Constants.obstacle_width)
        #Cibles
        self.createCible(904)
        self.createCible(1200)
        self.createCible(1800)
        self.createCible(2100)
        self.createCible(20)
        self.createCible(200)
        #Buttons
        self.createStartingButton(300, 355, self.startGame)
        self.createQuitButton(300, 300, self.stopGame)

    def on_mouse_motion(self, x, y, dx, dy):
        #update only when mouse is out of the ball and the game is not started
        if (Misc.isBetween(self, (Constants.SCREEN_X/2)-Constants.CIRCLE_RADIUS, (Constants.SCREEN_X/2) + Constants.CIRCLE_RADIUS, x) and
                Misc.isBetween(self, (Constants.SCREEN_Y/2)-Constants.CIRCLE_RADIUS, (Constants.SCREEN_Y/2)+Constants.CIRCLE_RADIUS, y)) == False:
                if not self.started :   #save computing time
                    self.arrow.update(x, y)

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.current_state == MENU_MAIN:
            Button.check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.current_state == MENU_MAIN:
            Button.check_mouse_release_for_buttons(x,y,self.button_list)
        elif self.current_state == GAME_RUNNING :
            if button == arcade.MOUSE_BUTTON_LEFT and not self.started:
                self.ball.launch(x,y)
                self.started = True

    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 200, 300, arcade.color.WHITE, 30)
        output = "Click to restart"
        arcade.draw_text(output, 200, 240, arcade.color.WHITE, 24)

    def draw_game(self):
        self.ball.draw()
        self.arrow.draw()
        for obs in self.listObstacles:
            obs.draw()
        for cible in self.listCibles:
            cible.draw(self.ball)
