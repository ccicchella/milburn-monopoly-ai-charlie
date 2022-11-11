from re import L
import matplotlib.pyplot as plt
from Tiles.ChestTile import ChestTile as chest
from Tiles.ChanceTile import ChanceTile as chance
from Bank import Bank
from Board import Board
from Player import Player
import pygame
from time import sleep
from Agent import Agent
from Actions import Actions
from RL.Action import Action
import matplotlib.pyplot as plt
from helper import plot
# Initializes window and title
pygame.init()
pygame.display.set_caption("Monopoly")
PROPERTIES_BOUGHT = 0
class Game:
    """
    Represents the playable Monopoly game.
    """

    WIDTH, HEIGHT = 810, 810  # Window size

    def __init__(self):
        """
        Intializes the Monopoly game.
        """
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        #Banks probably predate the world

        self.bank = Bank()
        

    def drawBoard(self):
        """
        Draws game onto the window.
        """
        #self.board.draw(self.window)


        #pygame.display.update()
    
    def drawPlayers(self):
        
        padding = 20  # Distance between board and window
        board_width = self.window.get_width() - padding * 2  # Board width
        board_height = self.window.get_height() - padding * 2  # Board height
        for player in self.players:
            tile = self.board.board[player.position[0]][player.position[1]]
            player.currentTile(tile)
            tile.addPlayer()
            
            if player.position[0] == 0:
                    player.draw(
                        self.window,
                        padding + board_width - (player.position[1] + 1) * 70 + 5,
                        padding + board_height - 70
                    )
            elif player.position[0] == 1:
                player.draw(
                self.window,
                padding,
                padding + board_height - (player.position[1] + 1) * 70,

                )
            elif player.position[0] == 2:
                player.draw(
                    self.window,
                    padding + player.position[1] * 70,
                    padding
                )
            elif player.position[0] == 3:
                player.draw(
                    self.window,
                    padding + board_width - 70,
                    padding + player.position[1] * 70
                )
            
        pygame.display.update()
    def initBoard(self):
        self.board = Board(self.bank, self.players)
        
    def initPlayers(self):
        
        self.players = []
        
        
        for i in range(0,2):
            name = 'Player{}'.format(i)
            player = Player(name, 2500, self.bank)
            self.players.append(player)
    def playerBankrupt(self, player):
        for tile in player.properties:
            
            
            tile.Bankruptcy(self.bank)
        self.players.remove(player)
                
    """
    Step function that runs actions on each turn
    """
    # TODO: For Mateja, Implement all the rules for the env
    def step(self, player, agent, n):
        done = False
        state_old = agent.getState(player, self.board.board)
        tile = self.board.board[state_old[1]][state_old[1]]
        if n < 800:
            if ((tile.type == 'Street') or (tile.type == 'Railroad')\
                or (tile.type == 'Utility')):
                if((tile.owner != player) and (tile.owner.__class__ != self.bank.__class__)):
                    rent = tile.calcRent()
                    if(player.balance >= rent):
                        
                        player.balance -= rent
                        tile.owner.balance += rent
                        
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
                    

                    self.actions[n%2].recieveAction(action)

                    state_new = agent.getState(player, self.board.board)
                    
                    reward = 0 #Calculates the reward 
                    
                    agent.train_short_memory(state_old, action, reward, state_new, done)
                    agent.remember(state_old, action, reward, state_new, done)
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
def main():
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
    while True:
        
        
        done = False
        
        
        
        game.players[n%2].move() #It works, that is all that matters

        done = game.step(game.players[n%2], agent, n)
        n += 1
        


        if done:
            
            n = 2
            score, score2 = game.getWinnerScore(game.players, agent)
            
            agent.games += 1
            game.reset()
            agent.trainLongMemory()
            if(score2 > record):
                record = score2
                agent.model.save()
            scores.append(score)
            scores2.append(score2) 
            
            games.append(agent.games)
            #plot(games, scores, scores2)

if __name__ == "__main__":
    main()
