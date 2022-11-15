def create_list():
    my_list_start = int(input("Enter initial number: "))
    end_number = int(input("Enter the end point number: "))
    my_list = []
    for i in range(my_list_start, end_number + 1):
        if my_list_start >= end_number:
            print("Error!!,the last number should be bigger: ")
            break
        else:
            my_list.append(i)

    sum_of_list = 0
    for n in my_list:
        sum_of_list += n

    print(f'\tSum of numbers from {my_list_start} to {end_number} is \n\t total: {sum_of_list}')


create_list()
