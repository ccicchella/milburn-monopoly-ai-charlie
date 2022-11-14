
import pygame


pygame.font.init()


class Tile:
    """
    Represents a tile on the board.
    """

    COLORS = {
        'Black' : (0, 0, 0),
        'Brown' : (102, 51, 0),
        'LightBlue' : (153, 204, 255),
        'Pink' : (255, 153, 204),
        'Orange' : (255, 128, 0),
        'Red' : (255, 0, 0),
        'Yellow' : (255, 255, 51),
        'Green' : (0, 255, 0),
        'Blue' : (0, 128, 255),
        'DarkGreen' : (5, 98, 36),
        'White' : (255, 255, 255),
        'BabyBlue' : (158, 204, 255),
        'Gold' : (255, 215, 0),
        'Lime' : (191, 255, 0)
    }

    WIDTH, HEIGHT = 70,70  # Tile size
    FONT = pygame.font.SysFont('segoeui', 7, True)



    FONT = pygame.font.SysFont('segoeui', 12, True)  # Tile font


    def __init__(self):
        """
        Initializes the tile.
        """

        self.players_on_tile = 0
        self.group_list = ['Black' ,'Brown' ,\
        'LightBlue' ,
        'Pink' ,
        'Orange' ,
        'Red' ,
        'Yellow' ,
        'Green' ,
        'Blue', 
        'White', 
        'DarkGreen',
        'BabyBlue',
        'Red',
        'Gold',
        'Black',
        'Lime']
        self.group = self.group_list.index(self.color)
        
    def goJail(player):
        player.updatePos([1,0])
    def addPlayer(self):
        self.players_on_tile += 1
    def removePlayer(self):
        self.players_on_tile -= 1
    def getPlayerOnTile(self):
        return self.players_on_tile
    def isCompletedGroup(self, board, player):
        b = True
        for tile in board.group[self.color]:
            if(tile.owner  != player):
                b = False
            
        return b
        

        


    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS[self.color],
            (x, y, self.WIDTH, self.HEIGHT),
            2
        )

        text = self.FONT.render( self.name, 1, self.COLORS['Black'] )
        window.blit( text, (
            x + self.WIDTH / 2 - text.get_width() / 2,
            y + self.HEIGHT / 2 - text.get_height() / 2
        ))
