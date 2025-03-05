import random
import numpy as np

def Simulation(number_of_people = 32):
    #Start with the inital number of people being subjected to experiment
    #Initialise an array with FALSE, representing if the element is sick or not, with length equal to the number of people
    people = np.zeros(number_of_people)
    #Assign an inital contagious carrier
    people[random.randint(0,len(people)-1)]= 1
    #Will continue loop until the number of infected matches the number of total people (Everyone is infected)
    day = 0
    day_data = []
    infected_data = []
    #There is one initially infected
    infected = 1 
    while infected != number_of_people:
        day += 1
        #Loops for x number of infected people (The RNG of infecting is repeated for every  currently sick person)
        for i in range(0,infected):
            #Generates a random number within the indexing range of all current 
            #Boundary is len(people)-1 because of its boundaries are inclusive
            random_index = np.random.randint(0, number_of_people)
            #If the random person isn't sick, make them sick---
            if people[random_index] == 0:
                people[random_index] = 1
                #And increase the amount of infected recorded
                infected += 1
        #Adds data from simluation to an array
        day_data.append(day) 
        infected_data.append(infected)
    #Returns the data gained from the format [[day, num_infected],...]
    return [day_data, infected_data]