#function to find the sequence of jobs
def job_seq(arr, max_deadline):
    m = len(arr)
    # Sort all jobs in decreasing order of profits
    arr.sort(key = lambda i : i[1], reverse = True)
    
    # To store result
    job_schedule = [None]*max_deadline
    count = 0

    for item in arr:
        #loop exit condition
        if count >= max_deadline:
            break

        # Find a free slot
        for i in range(item[2] - 1, -1, -1):
            if job_schedule[i] is None:
                job_schedule[i] = (item[0], item[1])
                break
    # return job schedule
    return job_schedule


#Driver Code
n = int(input("Enter total number of jobs: "))
print("\n")

#profit input
profit = []
for i in range(n):
    p = int(input(f"Enter the profit for 'job{i+1}': "))
    profit.append(p)
print("\nThe list of profit:",profit)
print("\n")

#deadline input
deadline = []
for j in range(n):
    d = int(input(f"Enter the deadline for 'job{j+1}': "))
    deadline.append(d)
print("\nThe list of deadline:", deadline)

# print list of tuples (job id, profit, deadline) using list comprehension
s_a = [(f'job{i+1}', profit[i], deadline[i]) for i in range(n)]
print("\nThe list of tuples: ", s_a)

#calling the function and printing sequence of jobs
print("\nThe job execution will takes place in this order:", job_seq(s_a, max(deadline)))