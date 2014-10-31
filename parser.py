import dataservice
import player

ds = dataservice.DataService()
jake = player.Player('JAKEMUZZIN', ds)
jake.printOverall()
roman = player.Player('ROMANJOSI', ds)
roman.printOverall()
alex = player.Player('ALEXEIYEMELIN', ds)
alex.printOverall()