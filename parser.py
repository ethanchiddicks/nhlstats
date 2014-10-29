import dataservice
import player

ds = dataservice.DataService()
jake = player.Player('JAKEMUZZIN', ds)
jake.printYearOnYear()
roman = player.Player('ROMANJOSI', ds)
roman.printYearOnYear()
alex = player.Player('ALEXEIYEMELIN', ds)
alex.printYearOnYear()