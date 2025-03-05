#Call matplotlib w Simulation program
import matplotlib.pyplot as plt
import Simluation
import functools
#Design a function to decompose data in the form [[day, num_infected],...]]
def ConvertData(data_set):
    #initialize arrays as private variables
    days = data_set[0]
    num_infected = data_set[1]


    #Functions gives data in the form [days], [num_infected]
    return days, num_infected

#Define MAIN function
def Main():
    #Ask for number of trials
    try:
        number_of_trials = int(input("How many trials would you like to perform: "))
        population = int(input("Enter population size: "))
    except:
        number_of_trials = 1

    #initialise day and infected data
    day_data = []
    infected_data = []

    
    #Perform simulation x number of times
    for i in range(0, number_of_trials):
        #perform simluation -- returns [[day, infected],...]
        data_set = Simluation.Simulation(population)
        #Convert data to [day]
        day_data += ConvertData(data_set)[0]
        infected_data += ConvertData(data_set)[1]

    #find the highest number of days needed to infect all 
    highest_day = 0
    for i in day_data:
        if i > highest_day:
            highest_day = i

    #find the highest number of infected in a simulation
    highest_infected = population

    plt.plot(day_data, infected_data, 'ro')
    plt.axis((0,highest_day+2,0,highest_infected * 11/10))

    #For every coordinate, print it on the screen
    plt.show()



Main()