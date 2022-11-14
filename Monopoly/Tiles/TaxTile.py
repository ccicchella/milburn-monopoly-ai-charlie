from Tiles.Tile import Tile
import pygame
class TaxTile(Tile):
    """
    Represents a tax tile on the board.
    """

    def __init__(self, attributes: dict):
        """
        Initializes the tax tile.
        """
        self.owner = 'IRS'
        self.color = 'Gold'
        self.name = attributes['Name']
        self.type = attributes['Space']
        super().__init__()
 
    def incomeTax(self):
        #if player lands on Income Tax tile
        return 75

    def luxuryTax(self):
        #if player lands on the Luxury Tax tile
        return 200
    def getTax(self, position):
        pass
