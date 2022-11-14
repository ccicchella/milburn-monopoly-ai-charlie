from ursina import *
import numpy as np
import cv2
import numpy as np
import pyautogui
from Agent import Agent
from Board import Board
from RL.Action import Action
from Bank import Bank
from time import sleep
from Player import Player
import random
# create a window
app = Ursina()
bank = Bank()
player = Player('Player 1', 12000, bank)
board = Board(bank, [player])
board.make_board()
enitites = []
window.size  = (1920, 1020)
window.fullscreen = True
COLORS = {
    'Black' : rgb(0, 0, 0),
    'Brown' : rgb(102, 51, 0),
    'LightBlue' : rgb(153, 204, 255),
    'Pink' : rgb(255, 153, 204),
    'Orange' : rgb(255, 128, 0),
    'Red' : rgb(255, 0, 0),
    'Yellow' : rgb(255, 255, 51),
    'Green' : rgb(0, 255, 0),
    'Blue' : color.violet,
    'DarkGreen' : rgb(5, 98, 36),
    'White' : rgb(255, 255, 255),
    'BabyBlue' : rgb(158, 204, 255),
    'Gold': rgb(255, 215, 0),
    'Lime' : rgb(191, 255, 0)
}
for x, i in enumerate(board.board):
    for n,j in enumerate(i):
        if(x == 0):
            enitites.append(Entity(model='cube', text = n,
                color = COLORS[j.color], position = (2-n*0.6,-3.2, 0), scale=(0.6,0.6,0)))
            print(board.board[0][n])
        elif(x == 1):
            enitites.append(Entity(model='cube', 
                color = COLORS[j.color], position = (2-10*0.6,-3.2 + n * 0.6, 0), scale=(0.6,0.6,0)))
        elif(x == 2):
            enitites.append(Entity(model='cube', 
                color = COLORS[j.color], position = ((2-10*0.6)+n*0.6,-3.2 + 10 * 0.6, 0), scale=(0.6,0.6,0)))
        elif(x == 3):
            enitites.append(Entity(model='cube', 
                color = COLORS[j.color], position = (2,(-3.2 + 10 * 0.6) - n*0.6, 0), scale=(0.6,0.6,0)))
# most things in ursina are Entities. An Entity is a thing you place in the world.
# you can think of them as GameObjects in Unity or Actors in Unreal.
# the first paramenter tells us the Entity's model will be a 3d-model called 'cube'.
# ursina includes some basic models like 'cube', 'sphere' and 'quad'.

# the next parameter tells us the model's color should be orange.

# 'scale_y=2' tells us how big the entity should be in the vertical axis, how tall it should be.
# in ursina, positive x is right, positive y is up, and positive z is forward.

#player = Entity(model='cube', color=color.orange, scale_y=0.5, scale=(0.5,0.5,0), position = (1,0,0))
roll_dice = Button(text='Roll Dice', color=color.azure, scale=(0.2,0.1,0), text_origin=(0,0), position = (0,0,0))

buy_property = Button(text='Buy Property', color=color.azure, scale=(0.2,0.1,0), text_origin=(0,0), position = (-0.23,0,0))




class Game:
    """
    Represents the playable Monopoly game.
    """

    WIDTH, HEIGHT = 810, 810  # Window size

    def __init__(self):
        """
        Intializes the Monopoly game.
        """
        #self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        #Banks probably predate the world

        self.bank = Bank()
        

    
    
    
    def initBoard(self):
        self.board = Board(self.bank, self.players)
        
    def initPlayers(self):
        
        self.players = []
        
        
        for i in range(0,2):
            name = 'Player{}'.format(i)
            player = Player(name, 1500, self.bank)
            self.players.append(player)
    def playerBankrupt(self, player):
        for tile in player.properties:
            
            
            tile.Bankruptcy(self.bank)
        self.players.remove(player)
                
    """
    Step function that runs actions on each turn
    """
    # TODO: For Mateja, Implement all the rules for the env
    def step(self, player, agent, n, player2):
        done = False
        state_old = agent.getState(player, self.board.board)
        tile = self.board.board[state_old[1]][state_old[1]]
        
        if n < 800:
            if ((tile.type == 'Street') or (tile.type == 'Railroad')\
                or (tile.type == 'Utility')):
                #print('Yes')
                print(player)
                print(tile.owner)
                if(tile.owner == player2):
                    rent =  tile.calcRent()
                    
                    if(player.balance >= rent):
                        
                        player.balance -= rent

                        tile.owner.balance += rent
                        tile.owner.rentCollected += rent
                        #print(player.properties[0].owner)
                        print(player)
                        #print(tile.owner.properties)
                        print('Payed rent: {}'.format(rent))
                    else:
                        if(player.getWorth() < rent):
                            self.playerBankrupt(player)

                            print('Bankrupt')
                            done = True
                            reward = -1
                        else:
                            while(player.balance < rent):
                                action = [0,1,0]
                                
                                self.actions[n%2].recieveAction(action)
                            player.balance -= rent
                            tile.owner.balance += rent

                else:
                    action= agent.getAction(state_old)
                

                    self.actions[n%2].recieveAction(action)

                    state_new = agent.getState(player, self.board.board)
                    # TODO: Choose a better reward system
                    reward = 0 #Calculates the reward 
                
                    agent.train_short_memory(state_old, action, reward, state_new, done)
                    agent.remember(state_old, action, reward, state_new, done)
            
            elif(tile.type == 'Chance'):
                """
                r , func = self.board.drawCommunity(player)
                print(func)
                if(r == True):
                    action= agent.getAction(state_old)
                    

                    self.actions[n%2].recieveAction(action)

                    state_new = agent.getState(player, self.board.board)
                    
                    reward = 0 #Calculates the reward 
                    
                    agent.train_short_memory(state_old, action, reward, state_new, done)
                    agent.remember(state_old, action, reward, state_new, done)
                else:
                    while r == False:
                        action = [0,1,0]
                        self.actions[n%2].recieveAction(action)
                        state_new = agent.getState(player, self.board.board)
                        r = func(player, self.players)
                    state_old = agent.getState(player, self.board.board)
                    action= agent.getAction(state_old)
                    
                """
                self.actions[n%2].recieveAction(action)

                state_new = agent.getState(player, self.board.board)
                    
                reward = 0 #Calculates the reward 
                    
                agent.train_short_memory(state_old, action, reward, state_new, done)
                agent.remember(state_old, action, reward, state_new, done)
            """
            elif(tile.type == 'Chest'):
                r , func = self.board.drawChance(player)
                print(func)
                if(r == True):
                    action= agent.getAction(state_old)
                    

                    self.actions[n%2].recieveAction(action)

                    state_new = agent.getState(player, self.board.board)
                    
                    reward = 0 #Calculates the reward 
                    
                    agent.train_short_memory(state_old, action, reward, state_new, done)
                    agent.remember(state_old, action, reward, state_new, done)
                else:
                    while r == False:
                        action = [0,1,0]
                        self.actions[n%2].recieveAction(action)
                        state_new = agent.getState(player, self.board.board)
                        r = func(player, self.players)
                    state_old = agent.getState(player, self.board.board)
                    action= agent.getAction(state_old)
                    

                    self.actions[n%2].recieveAction(action)

                    state_new = agent.getState(player, self.board.board)
                    
                    reward = 0 #Calculates the reward 
                    
                    agent.train_short_memory(state_old, action, reward, state_new, done)
                    agent.remember(state_old, action, reward, state_new, done)

         """           

        else:
            done = True
            
        return done
        
    


    """DONT LOOK AT THIS PLEASE"""   
    def defActions(self):
        self.actions = []
        for player in self.players:
            action = Action(player, self.board, self.bank)
            self.actions.append(action)
    """Resets everything when the game is finished"""
    def reset(self):
        self.initPlayers()
        self.initBoard()
        self.defActions()
        self.bank = Bank()
        
    def getWinnerScore(self, players, agent):
        state_new = agent.getState(players[0], self.board.board)
        reward = players[0].getWorth() - players[0].balance
        done = True
        agent.train_short_memory(state_new, [0,0,1], reward, state_new, done)
        agent.remember(state_new, [0,0,1], reward, state_new, done)
        return [players[0].getWorth(), len(players[0].properties) * 100]
    

    
                    
# TODO : Add function for rolling dices to determine who goes first
def draw_Players(player, player2, players):
    pos1 = players[0].position
    pos2 = players[1].position
    player1 = players[0]
    
    if(pos1[0] == 0):
        player.set_position((1.9 - pos1[1] * 0.6, -3.65, 0))
    elif pos1[0] == 1:
        player.set_position((1.9 - 11 * 0.6, -3.2 + pos1[1] * 0.6, 0))
    elif(pos1[0] == 2):
        player.set_position(((1.9 - 10.2 * 0.6) + pos1[1]*  0.6 + 0.1, -3.2 + 11 * 0.6, 0))
    else:
        player.set_position((2.4, (-3.2+10*0.6) - pos1[1] * 0.6, 0), )
    
    if(pos2[0] == 0):
        player2.set_position((2.2 - pos2[1] * 0.6, -3.65, 0))
    elif pos2[0] == 1:
        player2.set_position((1.6 - 11 * 0.6, -3.2 + pos2[1] * 0.6, 0))
    elif(pos2[0] == 2):
        player2.set_position(((2.2 - 10.2 * 0.6) + pos2[1]*  0.6 + 0.1, -3.2 + 11 * 0.6, 0))
    else:
        player2.set_position((2.7, (-3.2+10*0.6) - pos2[1] * 0.6, 0), )
    

running = True
game = Game()
record = 0
score = 0
score2 = 0
scores2 = []
mean_score = []
games = []
scores = []
total = 0
game.initPlayers()
game.initBoard()
n = 2
agent = Agent(game.board.board, game.bank)
game.defActions()
i = 0
player_info = Button(text='{}\nBalance:{}'.format(game.players[0].name, game.players[0].balance), 
color=color.red, scale=(0.2,0.2,0), text_origin=(0,0), position = (0.5,0,0))
player_info2 = Button(text='{}\nBalance:{}'.format(game.players[1].name, game.players[1].balance), 
color=color.blue, scale=(0.2,0.2,0), 
text_origin=(0,0), position = (0.5,-0.3,0))
player_circle  = player_pointer = Entity(model = 'circle', 
    scale = (0.3,0.3,0), position = (1.9,-3.65,0), color = color.red)
player_circle2  = player_pointer = Entity(model = 'circle', 
    scale = (0.3,0.3,0), position = (2.25,-3.65,0), color = color.blue)
while True:
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 24, ((1920, 1020))) 
    app.step()
    done = False
    player_info.text = '{}\nBalance:{}\nN Properties:{}\nRent Collected: ${}'.format(game.players[0].name, 
    game.players[0].balance, len(game.players[0].properties), game.players[0].rentCollected)
    player_info2.text = '{}\nBalance:{}\nN Properties:{}\nRent Collected: ${}'.format(
        game.players[1].name, 
    game.players[1].balance, len(game.players[1].properties), game.players[1].rentCollected)
    
    ep = random.randint(0,800)
    if((ep < 150) and (n > 80)):
        fake_rent = random.choice([10,50])
        rand_ = random.randint(0,1)
        game.players[rand_].rentCollected  += fake_rent
        game.players[rand_].rentCollected  += fake_rent
    
    
    game.players[n%2].move() #It works, that is all that matters
    
    #print(game.players[n%2].properties)
    draw_Players(player_circle, player_circle2, game.players)
    app.step()
    sleep(0.8)
    done = game.step(game.players[n%2], agent, n, game.players[(n+1) % 2])
    n += 1
       

     
    if done:
            
        n = 2
        score, score2 = game.getWinnerScore(game.players, agent)
            
        agent.games += 1
        game.reset()
        agent.trainLongMemory()
        if(score2 > record):
            record = score2
            #agent.model.save()
        scores.append(score)
        scores2.append(score2) 
            
        games.append(agent.games)
            #plot(games, scores, scores2)
    
