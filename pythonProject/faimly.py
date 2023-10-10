def FunctionName():
    my_age = 21
    a = f"my name is avinash kashyap {my_age}"
    print(a)
    mother_age = 40
    b = f"my mother name is kushmani lata kashyap {mother_age}"
    print(b)
    father_age = 47
    c = f"my father name is laxmi prasad kashyap and his age is {father_age}"
    print(c)
    subhi_age = 15
    d = f"My sister name is subhi and her age is {subhi_age}"
    print(d)


    if my_age >mother_age and my_age >father_age and my_age >subhi_age:
        print(my_age,'is greater')
    elif mother_age>my_age and mother_age>father_age and mother_age>subhi_age:
        print(mother_age,'is greater')
    elif father_age>my_age and father_age>mother_age and father_age>subhi_age:
        print(father_age,'is greater')
    else:
        print(subhi_age,'is greater')

    return "FAMILY DETAILS PRINTED"

print(FunctionName())


