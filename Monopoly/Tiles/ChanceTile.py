import numpy as np
from Tiles.Tile import Tile
import pygame




class ChanceTile:
    """
    Represents a "Chance" tile on the board.
    """

    def __init__(self, attributes: dict):
        """
        Initializes the "Chance" tile.
        """

        
        self.color = 'Blue'
        self.name = '?'
        self.type = 'Chance'
        self.owner = "Bank"
        self.group = 9
        
  
        self.deck = []
        
            
        
        
    def goToGo(player, players):
        player.pos = [0,0]
        player.addMoney(200)
        return True
    
    
    def goIllinoisAve(player, players):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = [2,4]
            return True
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = [2,4]
            return True
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = [2,4]
            player.getMoney(200)
            return True


    def goCharlesPlace(player, players):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = [1,1]
            
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = [1,1]
            player.addMoney(200)
            
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = [1,1]
            player.addMoney(200)
        return True

    def goNearestUtility(player, players):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = [1,2]
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = [2,8]
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = [1,2]  
        return True
    
    def goNearestRailRoad(player, players):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = [1,5]
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = [2,5]
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = [0,5]     
        return True
    def bankDividends(player, players):
        player.addMoney(200)
        
    
    #def getOutOfJail(player):
     #   player.addGetOutOfJail()
        
        
    def goToJail(player, players):
        player.updatePos([1,0])
        return True
        
    def goBackThree(player, players):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = [0,4]
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = [1,9]
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = [3,3]
        return True
    def generalRepairs(player, players):
        r = player.payMoney(100)
        return r
        #player.payMoney(price = player.houses * 25 + player.hotels * 100)
        
        
    def poorTax(player, players):
        r = player.payMoney(15)
        return r
        
        
    def goReadingRailroad(player, players):
        player.pos = np.array([0,5])
        return True
        
    def goBoardwalk(player, players):
        player.pos = np.array([3,9])
        return True
    def boardChairman(player, players):
        count = 0
        for payer in players:
            if(payer != player):
                count += 1
        r = player.payMoney(count*50)
        return r
                
                
    def buildingLoan(player, players):
        player.addMoney(150)
        return True
        
    def crosswordWin(player, players):
        player.addMoney(100)
        return True

