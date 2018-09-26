import pygame
import time
import random
import sys
from pygame.locals import *

pygame.display.set_caption('Game')

class Game(object):
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]


    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        self.state = self.states[self.state_name]
        self.state.startup

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()    
        self.state.update(dt)

    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(60)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
            
class GameState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(None, 24)
        
    def startup(self):
        """put your class specific syntax here (the stuff that doesent fit into
        events, updates or draw)"""   
    
    def update(self, dt):
#   evaluates anything you insert into function per frame
        pass
##
##    
##    
class Menu(GameState):
    def __init__(self):
        super(Menu, self).__init__()
        self.title = self.font.render("Menu", True, pygame.Color("dodgerblue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "GAMEPLAY"
        
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
#        if event.type == pygame.KEYUP:
        elif event.type == pygame.MOUSEBUTTONUP:
            self.done = true
    
    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)
        
class Gameplay(GameState):
    def __init__(self):
        super(Gameplay, self).__init__()
        
    def startup(self,):
        self.title = self.font.render(text, True, pygame.Color("gray10"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
#        elif event.type == pygame.MOUSEBUTTONUP:
        
    def update(self, dt):
            pass
                 
    def draw(self, surface):
        surface.fill("white")
        
    
if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    states = {"Menu": Menu(),
              "GAMEPLAY": Gameplay()}
    game = Game(screen, states, "Menu")
    
    game.run()
    pygame.quit()
    sys.exit()

