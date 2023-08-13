with open('file_1.txt') as f:
    my_list = f.readlines()
    print(my_list)

    print()
    
    a = [i.strip() for i in my_list]
    print(a)