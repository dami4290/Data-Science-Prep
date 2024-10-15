import csv
import math
from matplotlib import pyplot as plt 

def read_database(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            for i in range(len(row)):
                if(row[i].strip().isdecimal()):
                    row[i] = int(row[i].strip())
            data.append(row)
        return data
    
def EuclideanDistance(person1, person2):
    """ This function computes the Euclidean
    distance between the characterists of 
    tow persons
    
    Args:
        person1 (list): Age1, Height1, Income1
        person1 (list): Age2, Height2, Income2
    
    Returns:
        float: the distance between the two inputs
    """
    distance=math.sqrt((person1[0]-person2[0])**2+(person1[1]-person2[1])**2+(person1[2]-person2[2])**2)
    
    return distance

def ComputeAllDistances(candidates_list, client):
    """ This function computes the Euclidean
    distance between the characterists of 
    two persons
    
    Args:
        candidates_list (nested lists): List of candidates Name, Age, Height, Income
        client (list): Age, Height, Income
    
    Returns:
        list: return all the distances between our client
        and the candidates in the database
    """
    my_list=[]
    for x in range(len(candidates_list)):
        print(candidates_list[x][1:])
        distanceBetweenClient=EuclideanDistance(candidates_list[x][1:],client)
        my_list.append(distanceBetweenClient)
    return my_list


def FindMin(list1):
    """ This function returns the minimum value
    in a list as well as its index
    
    Args:
        list (list): List of numbers (float or int)
    
    Returns: 
        a tuple with: (float, int)
            float: value of the minimum
            int  : index of the minimum value
    """
    minVal= 0
    for x in range(len(list1)-1):
        if list1[x]<list1[x+1]:
            minVal=list1[x]
        else:
            minVal=list1[x+1]
    return list1.index(minVal)
        


def main():
    # 1. Read the database (either the males or females!)
    # name | age | height | income(k$)
    candidates_list = read_database('list_males.csv')
    #candidates_list = read_database('list_females.csv')
    candidates_list = candidates_list[1:] # the remove the first row that contain the labels
    age_list=[]
    height_list=[]
    for x in range(len(candidates_list)):
        age_list.append(candidates_list[x][1])
        height_list.append(candidates_list[x][2])
    
    plt.scatter(age_list, height_list)
    plt.show()
    # 2. Here are characteristics of the clients (Pamela or George)
    Pamela = [25, 157, 65]
    #George = [27, 168, 51]

    # 3. Compute the distance between the client and one person
    person = ["Madison", 30, 178, 45]
    dist = EuclideanDistance(Pamela, person[1:])
    print (dist)
    # 4. Compute the distance between the client and the candidates
    
    list_dist = ComputeAllDistances(candidates_list, Pamela)
    
    # 5. Find the best candidate! (minimum in the list)
    idx = FindMin(list_dist)
    print(candidates_list[idx]) # Print the best candidate for the client
    
if __name__ == "__main__": # Run the main!
    main()
        