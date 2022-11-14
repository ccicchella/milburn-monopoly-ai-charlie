from Tiles.Tile import Tile
import pygame
class StreetTile(Tile):
    """
    Represents a street tile in the Monopoly game.
    """

   

    def __init__(self,attributes, bank):
        self.name = attributes['Name']
        self.price = attributes['Price']
        
        self.mortgage_value = self.price / 2
        self.is_mortgaged = False
        self.position = [attributes['Position(X)'], attributes['Position(Y)']]
        self.type = attributes['Space']
        self.house_count = 0
        self.hotel_count = 0
        self.color = attributes['Color']
        
        self.rent = [attributes['Rent'],
        attributes['RentBuild1'],
        attributes['RentBuild2'],
        attributes['RentBuild3'],
        attributes['RentBuild4'],
        attributes['RentBuild5']
        ]
        self.price_build = attributes['PriceBuild']
        
        self.owner = 0
        super().__init__()
    # set the owner to a Player object
    def setOwner(self, player):
        self.owner = player
    """
    This function will be used to check all available houses to build a house on
    """
    
    def checkAddHouseValidity(self, board):
        validity = True
        other_tiles = []
        for tile in board.group[self.color]:
            
            if(tile.owner != self.owner):
                validity = False
            else:
                if tile != self:
                    other_tiles.append(tile)
        
        if validity:
            
            if (len(other_tiles) == 1):
                if(((self.house_count + 1) - other_tiles[0].house_count <= 1) and (self.house_count + 1 <= 4)):
                    if(self.hotel_count == 0):
                        return True
                else:
                    return False
            else:
                if(((self.house_count + 1) - other_tiles[0].house_count <= 1) and (self.house_count + 1 <= 4)):
                    if((self.house_count + 1) - other_tiles[1].house_count <= 1):
                        return True
                    else:
                        return False 
                else:
                    return False


    """
    Checks for all the tiles where a hotel can be built/sold
    """
    def addHotelValidity(self, board):
        validity = True
        other_tiles = []
        for tile in board.group[self.color]:
            
            if(tile.owner != self.owner):
                validity = False
            else:
                if tile != self:
                    other_tiles.append(tile)
            if (self.color == 'Blue' or self.color == 'Brown'):
                    if((self.house_count ==4 ) and (other_tiles[0].house_count == 4 
                    or other_tiles[0].hotel_count == 1)):
                        return True
                    else:
                        return False
            else:
                if(self.house_count ==4 ): 
                    if(other_tiles[0].house_count == 4 or other_tiles[0].hotel_count == 1):
                        if(other_tiles[1].house_count == 4 or other_tiles[1].hotel_count == 1):
                            return True
                     
                else:
                    return False
        

    def getWorth(self):
        # worth of a property if it has 1, 2, 3, or 4 houses
        # brown & light blue: $50/house
        # purple & orange: $100/house
        # red & yellow: $150/house
        # green & blue: $200/house
        if self.house_count != 0:
            if self.color == 'Brown' or self.color == 'LightBlue':
                return self.price + self.house_count * 50 / 2
            elif self.color == 'Purple' or self.color == 'Orange':
                return self.price + self.house_count * 100 / 2
            elif self.color == 'Red' or self.color== 'Pink':
                return self.price + self.house_count * 150 / 2
            else:
                return self.price + self.house_count * 200 / 2

        # worth of a property if it has 1 hotel (cost of 1 hotel = 1 house)
        elif self.house_count == 0 and self.hotel_count == 1:
            if self.color == 'Brown' or self.color == 'LightBlue':
                return self.price + (self.house_count + 1) * 50 / 2
            elif self.color == 'Purple' or self.color == 'Orange':
                return self.price + (self.house_count + 1) * 100 / 2
            elif self.color == 'Red' or self.color == 'Yellow':
                return self.price + (self.house_count + 1) * 150 / 2
            else:
                return self.price + (self.house_count + 1) * 200 / 2

        # worth of a property if it has 0 house and 0 hotel
        else:
            return self.price

    def sellHouse(self, player, n = 1):
        if self.house_count - n >= 0:
            self.house_count -= n
            player.bank.addHouse(n)
            player.addMoney(n * self.price_build / 2)

    def addHotel(self, player):
        self.house_count = 0
        self.hotel_count = 1
        player.bank.addHouse(4)
        player.bank.sellHotel()

    def addHouse(self, player):
        self.house_count += 1
        player.bank.sellHouse(1)
        print('Bought House')

        
    def sellHotel(self, player):
        self.hotel_count = 0
        player.addMoney(self.price_build / 2)
        player.bank.addHotel()
        self.house_count = 4
        player.bank.sellHouse(4)

    def mortgage(self, player):
        
        player.addMoney(self.mortgage_value)
        player.bank.addHouse(self.house_count)
        player.bank.addHotel(self.hotel_count)
        self.is_mortgaged = True
        self.house_count = 0
        self.hotel_count = 0

    def unMortgage(self, player):
        self.is_mortgaged = False
        return self.price * 1.1

    def calcRent(self):
        if self.hotel_count == 0:
            return self.rent[self.house_count]
        elif self.hotel_count == 1:
            return self.rent[-1]
    def Bankruptcy(self, bank):
        bank.addHouse(self.house_count)
        bank.addHotel(self.hotel_count)
        self.setOwner(bank)
        self.house_count = 0
        self.hotel_count = 0
    def getMortVal(self):
        return self.mortgage_value + self.house_count * self.price_build / 2 + self.hotel_count * self.price_build / 2
        