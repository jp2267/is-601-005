a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

#creating a negative number
negative_number = -1

#creating 4 list to store positive values
positive_number_a1 = []
positive_number_a2 = []
positive_number_a3 = []
positive_number_a4 = []

def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    # setting conditions for 4 different list
    if num == 1:
        for i in arr:
            if(i<0):
                a = i * negative_number
                positive_number_a1.append(a)
            else:
                positive_number_a1.append(a)
        print(positive_number_a1)

    elif num == 2:
        for i in arr:
            if(i<0):
                a = i * negative_number
                positive_number_a2.append(a)
            else:
                positive_number_a2.append(a)
        print(positive_number_a2)

    elif num == 3:
        for i in arr:

            if(i<0):
                a = i * negative_number
                positive_number_a3.append(a)
            else:
                positive_number_a3.append(a)
        print(positive_number_a3)
    
    else:
        for i in arr:
            casted_number = int(i)

            if(casted_number<0):
                a = casted_number * negative_number
                positive_number_a4.append(a)
            else:
                positive_number_a4.append(a)
        print(positive_number_a4)


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)