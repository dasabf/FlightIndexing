from Utilities.IO import *

airline_list = []
def add(flightName):
    airline_list.append(flightName)

def viewFlightName():
    counter=0
    for flight in airline_list:
        writeInFile("Flight Number "+str(counter+1)+" :: "+flight+"\n")
        counter+=1