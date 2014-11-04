import dataservice
import player
import yearlyscrapeprovider2014

ds = dataservice.DataService()
patrice = player.Player('8470638', ds)
patrice.printYearOnYear()
kyle = player.Player('8474068', ds)
kyle.printYearOnYear()
alex = player.Player('8470257', ds)
alex.printYearOnYear()