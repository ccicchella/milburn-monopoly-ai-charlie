class Chest:


    def __init__():
        pass
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