# My Tax Calculation Program!
# write a function that calculates the different tax rates applied
# to different incomes, genders, singles/couples, kids/no kids, etc.
# block input errors

# 1. income below or equal 1500€ tax is 10% if female, 12.5% if male --without kids
                                       # 8% if female, 10% if male --with kids
# 2. income below or equal 2000€ tax is 15% if female, 17.5% if male
                                       # 12.5% if female, 15% if male --with kids
# 3. income over 3000€ tax is 20% if female, 22.5% if male
                                       # 17.5% if female, 20% if male --with kids

while input != "q":
    print("Please enter your income:> €", end=' ')
    income = input()
    try:
        income = int(income)
    except:
        print("Incorrect Input. Please enter your income:> €", end=' ')
        income = int(input())


    print("Please enter your gender(m=1,f=2):> ", end=' ')
    gender = input()
    try:
        gender = int(gender)
    except:
        print("Incorrect Input. Please enter 1 for m, 2 for f:> ", end=' ')
        gender = int(input())

    print("Do you have children(yes=1,no=2)?:> ", end=' ')
    children = input()
    try:
        children = int(children)
    except:
        print("Incorrect Input. Please enter 1 for children, 2 for no children:> ", end=' ')
        children = int(input())

    if gender == 1 and children == 1:
        if income <= 1500:
            tax = income * 0.1
        elif income <= 2000:
            tax = income * 0.15
        elif income >= 3000:
            tax = income * 0.2
    else:
        if income <= 1500:
            tax = income * 0.125
        elif income <= 2000:
            tax = income * 0.175
        else:
            tax = income * 0.225
    if gender == 2 and children == 1:
        if income <= 1500:
            tax = income * 0.08
        elif income <= 2000:
            tax = income * 0.125
        elif income >= 3000:
            tax = income * 0.175
    else:
        if income <= 1500:
            tax = income * 0.1
        elif income <= 2000:
            tax = income * 0.15
        else:
            tax = income * 0.2

    print("Your tax is € ", tax)
    q = input('q')
    if input == q:
        break

# trying to solve github problem




