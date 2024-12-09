def food_bank_donation():
    print("[How far your donation goes]\n")
    
    # Prompt user for quantity per item
    soup_cans = int(input("How many cans of soup? "))
    rice_bags = int(input("how many bags of rice? "))
    vegetable_cans = int(input("How many cans of vegetables? "))
    peanut_butter_cans = int(input("how many cans of peanut butter? "))
    
    # Calc the num of people fed from each item
    people_fed_soup = soup_cans * 2
    people_fed_rice = rice_bags * 4
    people_fed_vegetables = vegetable_cans * 3.5
    people_fed_peanut_butter = peanut_butter_cans * 7
    
    # Calc the total num of ppl fed
    total_people_fed = (people_fed_soup + people_fed_rice + people_fed_vegetables + people_fed_peanut_butter)
    
    # Print results
    print("\nYour donation will help feed {:.1f} people!".format(total_people_fed))
    print(f"{people_fed_soup} people with the {soup_cans} can(s) of soup")
    print(f"{people_fed_rice} people with the {rice_bags} bag(s) of rice")
    print(f"{people_fed_vegetables} people with the {vegetable_cans} can(s) of vegetables")
    print(f"{people_fed_peanut_butter} people with the {peanut_butter_cans} can(s) of peanut butter")

# Call the function
food_bank_donation()
