#function to find the sequence of jobs
def job_seq(arr):
    arr.sort(key = lambda i : i[2], reverse = True)
    print("\nAfter sorting:", arr)

    max_deadline = arr[0][2]
    job_exe = []

    for i in range(max_deadline):
        max_item = arr[0]
        for item in arr:
            if item[2] == (i + 1) and item[1] > max_item[1]:
                max_item = item

        job_exe.append((max_item[0], max_item[1]))
    return job_exe


#Driver Code
n = int(input("Enter the list size: "))

profit = []
for i in range(n): #profit input
    p = int(input(f'Enter the profit for j{i+1}:'))
    profit.append(p)
print("\nThe list of profit:",profit)

deadline = []
for j in range(n): #deadline input
    d = int(input(f'Enter the deadline for j{j+1}:'))
    deadline.append(d)
print("\nThe list of deadline:", deadline)

# print list of tuples (job id, profit, deadline) using list comprehension
s_a = [(f"j{i+1}", profit[i], deadline[i]) for i in range(n)]
print("\nThe list of tuples: ", s_a)

#calling the function and printing sequence of jobs
print("\nThe job execution will takes place in this order:", job_seq(s_a))