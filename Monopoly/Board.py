from inspect import getmembers, isfunction
from Tiles.ChestTile import ChestTile as chest
from Tiles.Tile import Tile
from inspect import getmembers, isfunction
from Tiles.GoTile import GoTile
from Tiles.StreetTile import StreetTile
from Tiles.ChestTile import ChestTile
from Tiles.TaxTile import TaxTile
from Tiles.RailroadTile import RailroadTile
from Tiles.ChanceTile import ChanceTile
from Tiles.JailTile import JailTile
from Tiles.UtilityTile import UtilityTile
from Tiles.ParkingTile import ParkingTile
from Tiles.GoToJailTile import GoToJailTile
from Tiles.ChanceTile import ChanceTile as chance
import pandas as pd
import pygame
import random

pygame.font.init()

class Board:
    """
    Represents the Monopoly game board.
    """
    
    COLORS = {
        'Black' : (0, 0, 0),
        'LightGray' : (219, 219, 219)
    }

    FONT = pygame.font.SysFont('segoeui', 100)  # Title font

    def __init__(self, bank, players):
        """
        Initializes the game board.
        """
        
        
        self.players = players
        self.group = dict()        
        self.bank = bank    
        # Initializes board as a list of the board's sides and tiles.
        self.board = self.make_board()
        #Initializes the deck for the Community Chest
        self.community = []
        self.chance = []
        for func in getmembers(chest, isfunction):
            self.community.append(func[1])
        for func in getmembers(chance, isfunction):
            self.chance.append(func[1])
        random.shuffle(self.chance)
        # TODO: Add attribute to store all the players in the game

    def draw(self, window: pygame.Surface):
        """
        Draws the game board. 
        """
        # Fills screen with background color, wiping the screen of artifacts
        window.fill(self.COLORS['LightGray'])

        # Renders title header
        title = self.FONT.render( "monopoly", 1, self.COLORS['Black'] )
        window.blit( title, (
            window.get_width() / 2 - title.get_width() / 2,
            window.get_height() / 2 - title.get_height() / 2
        ))

        padding = 20  # Distance between board and window
        board_width = window.get_width() - padding * 2  # Board width
        board_height = window.get_height() - padding * 2  # Board height

        # Draw board tiles
        for s, side in enumerate(self.board):
            for t, tile in enumerate(side):

                # Tiles are drawn on their according side
                if s == 0:
                    tile.draw(
                        window,
                        padding + board_width - (t + 1) * tile.WIDTH,
                        padding + board_height - tile.HEIGHT
                    )
                elif s == 1:
                    tile.draw(
                        window,
                        padding,
                        padding + board_height - (t + 1) * tile.HEIGHT
                    )
                elif s == 2:
                    tile.draw(
                        window,
                        padding + t * tile.WIDTH,
                        padding
                    )
                elif s == 3:
                    tile.draw(
                        window,
                        padding + board_width - tile.WIDTH,
                        padding + t * tile.HEIGHT
                    )

    def make_board(self):
        """
        Reads board information from CSV file.
        """
        data = pd.read_csv('Data/newboard.csv')
        board = [ [], [], [], [] ]

        for index, row in data.iterrows():
            side = index // 10
            attributes = dict(row)

            # TODO: Currently uses default (empty) Tile constructors; should be
            #       changed to take attributes as an argument (see StreetTile).

            if row['Space'] == "Go":
                tile =GoTile(attributes, len(self.players))
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "Street":
                tile = StreetTile(attributes, self.bank)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            
            elif row['Space'] == "Chest":
                tile = ChestTile(attributes, self.players)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "Tax":
                tile = TaxTile(attributes)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "Railroad":
                tile = RailroadTile(attributes, self.bank)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "Chance":
                tile = ChanceTile(attributes)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "Jail":
                tile = JailTile(attributes)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "Utility":
                tile = UtilityTile(attributes, self.bank)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "Parking":
                tile = ParkingTile(attributes)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            elif row['Space'] == "GoToJail":
                tile = GoToJailTile(attributes)
                board[side].append(tile)
                if(attributes['Color'] in self.group):
                    self.group[attributes['Color']].append(tile)
                else:
                    self.group[attributes['Color']] = [tile]
            else:
                raise KeyError(f"Invalid tile type in CSV: {row['Space']}")
        
        return board
    """
    Functions for drawing community chest and chance cards 
    """
    def drawCommunity(self, player):
        try:
            func = self.community[0]
            
            r= func(player, self.players)
            self.community.pop(0)
            self.community.append(func)
        except:
            
            
            
            self.community.pop(0)
            func = self.community[0]
            r= func(player, self.players)
            self.community.pop(0)
            self.community.append(func)

        return r, func 
    def drawChance(self, player):
        try:
            func = self.chance[0]
            
            r= func(player, self.players)
            self.chance.pop(0)
            self.chance.append(func)
        except:
            
            
            
            self.chance.pop(0)
            func = self.chance[0]
            r= func(player, self.players)
            self.chance.pop(0)
            self.chance.append(func)
        return r, func