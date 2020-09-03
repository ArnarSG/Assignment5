n = int(input("Enter the length of the sequence: ")) # Do not change this line
first_n = 3
second_n = 2
third_n = 1
counter = 0
the_sum = 0
while counter < n:
    if counter < 3:
        the_sum += 1
        counter += 1
        print(the_sum)
    else:
        the_sum = first_n + second_n + third_n
        third_n = second_n
        second_n = first_n
        first_n = the_sum
        counter += 1
        print(the_sum)
        
    

    
