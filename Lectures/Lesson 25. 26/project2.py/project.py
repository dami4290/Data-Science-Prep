def doesExist(lst,query):
    """ 
    Check if the queried value exists within the range of the list values.

    Args:
        lst (list): A sorted list of numbers.
        query (int/float): The number you're searching for.

    Returns:
        bool: True if the query lies within the range of the list values, otherwise False.
    """

    if len(lst)==0:
        return False
    elif query>lst[len(lst)-1]:
        return False
    elif query<lst[0]:
        return False
    else :
        print("Proceeding with the ternary search")
        return True
       


def computeMidpoints(low, high):
    """ 
    Calculate the two midpoints for ternary search.

    Args:
        low (int): The lower index of the current search space.
        high (int): The upper index of the current search space.

    Returns:
        tuple: Two midpoints dividing the current search space into three segments.
    """
    mid_1=int(low+(high-low)/3)
    mid_2=int(low+2*(high-low)/3)
    return mid_1, mid_2

def ternarySearch(lst, query, mid_1, mid_2):
    """ 
    Search for a query value in a sorted list using the ternary search algorithm.

    Args:
        lst (list): A sorted list of numbers.
        query (int/float): The number you're searching for.

    Returns:
        int: The index of the query value if it exists in the list, otherwise -1.
    """
   
    if not doesExist(lst, query):
        print("invalid value")
        return -1
    
    my_list=[]
    if mid_2>query>mid_1:
        for x in range(mid_1+1,mid_2):
            my_list.append(lst[mid_1+1])
    elif lst[0]<query<mid_1:
        for x in range(lst.index(mid_1)):
            my_list.append(lst[x])
    elif lst[len(lst)-1]>query>mid_2:
        for x in range(mid_2,len(lst)):
            my_list.append(lst[x])
    else:
        print("invalid")
        return -1

       
    for x in range(len(my_list)):
        if query<my_list[x]:
            my_list.insert(x,query)
            print(my_list)
            break

    

def gameRanking(score_lst, player_score):
    """ 
    Find the player's rank and the points gap to the next rank.

    Args:
        score_lst (list): A list of player scores sorted from highest to lowest.
        player_score (int/float): The score of the player in question.

    Returns:
        tuple: Player's rank and the points needed to surpass the next player.
            Returns (-1, -1) if the player isn't ranked.
    """
    for x in range(len(score_lst)):
        if player_score>score_lst[x]:
            score_lst.insert(x,player_score)
            print(score_lst)
            break
    rank=score_lst.index(player_score)
    gap=score_lst[rank-1]-player_score
    return rank, gap
            
def main():
    # test ternary search
    # lst = [1, 10, 23, 48, 99, 200, 323]
    lst=[]
    query = int(input("What is your score?"))
    a, b=computeMidpoints(0,(len(lst)-1))
    ternarySearch(lst,query,a,b)

    # # # test video game score ranking function
    # lst_score = [9999, 8700, 7433, 7423, 5888, 3201, 3000, 323, 23, 1]
    # current_score = int(input("Please type your score: "))
    # rank, gap=gameRanking(lst_score, current_score)
    # if rank == -1:
    #     print("You are not ranked!")
    # else:
    #     print("You are ranked " + str(rank) + " out of " + str(len(lst_score)) + " players.")
    #     print("You need " + str(gap) + " extra points to rank up!")
    
if __name__ == "__main__": # Run the main!
    main()