
#KNAPSACK GREEDY APPROACH
def greedy_knap(weights, profits, max_weight):

    #n stores the min size among the weights and profits list
    n = min(len(weights), len(profits))

    # arr is list of tuple denoting (weight, profit)
    arr = [(weights[i], profits[i]) for i in range(n)]

    # sorted in reverse order based on profits
    arr = sorted(arr, key = lambda arr:arr[1], reverse = True)
    
    max_profit = 0 #stores max profits
    result = [] #stores tuples of max profits

    # loop through arr to find adequate tuples
    for item in arr:

        #check if each item weight <= max weight
        if item[0] <= max_weight:

            #if above is true, add the profit to max profit
            max_profit += item[1]

            #modify the remaining max weight
            max_weight -= item[0]

            #append the item to result list
            result.append(item)

    return (result, max_profit)

#Driver Code
weight_list = [7, 1, 9, 4]
profit_list = [40, 30, 33, 22]
weight_cap = 5

print(greedy_knap(weight_list, profit_list, weight_cap))