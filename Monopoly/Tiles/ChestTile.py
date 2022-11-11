import numpy as np
import pygame
import random
from Tiles.Tile import Tile
from Player import Player
from Tiles.JailTile import JailTile
class ChestTile:
    """
    Represents a "Community Chest" tile on the board.
    """

    def __init__(self, attributes, players):
        """
        Initializes the "Community Chest" tile.
        """
        #self.deck = []
        self.players = players
        self.color = 'DarkGreen'
        self.name = 'Chance'
        self.type = attributes['Space']
        self.owner = "Bank"
        self.group = 9
    def goToGo(player,players):
        
        player.updatePos([0,0])
        player.addMoney(200)
    def bankError(player,players):
        player.addMoney(200)
    def doctorsFees(player):
        r = player.payMoney(50)
        return r
    #def getOutOfJail(player,players):
        #player.addGetOutOfJail()
    def goToJail(player):
        player.updatePos([1,0])
    """
    Collects 50 from all players
    """
    #def grandOperaNight(player, players):
     #   for payer in players:
      #      if(payer != player):
       #         payer.payTax(50,player)

    def Holiday(player,players):
        player.addMoney(200)
    def incomeTaxRefund(player,players):
        player.addMoney(200)
    # TODO: Implement this function
    #def yourBirthday(player, players):
     #   for payer in players:
      #      if(payer != player):
       #         r = payer.payTax(player, 10)
    def insuranceMatures(player,players):
        player.addMoney(100)
    def hospitalFees(player,players):
        r = player.payMoney(50)
        return r
    def schoolFees(player,players):
        r = player.payMoney( 50)
        return r
    def consultancyFee(player,players):
        player.addMoney(25)
    # TODO: Add a separate attributes in player class in order to make this function a lot easier
    def streetRepairs(player,players):
        r = player.payMoney(100)
        return r
        # player.payTax(price = player.houses * 40 + player.hotels * 115)
    def beautyContest(player,players):
        #Only second place tho :(
        player.addMoney(10)
    def inheritMoney(player,players):
        player.addMoney(100)
    
    
