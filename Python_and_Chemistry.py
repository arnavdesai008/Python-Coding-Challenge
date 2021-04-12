elem1 = input("Enter the first chemical to be combined (Oxygen, Carbon, Hydrogen, Chlorine): ").lower() #1st element input
elem2 = input("Enter the second chemical to be combined (Oxygen, Carbon, Hydrogen, Chlorine): ").lower() #2nd element input

if elem1 == "oxygen" or elem1 == "hydrogen" or elem1 == "carbon" or elem1 == "chlorine":        #checking invalid input or not
    if elem2 == "oxygen" or elem2 == "hydrogen" or elem2 == "carbon" or elem2 == "chlorine":     #checking invalid input or not
        if elem1 == "oxygen":
            if elem2== "carbon":
                result="carbon dioxide(CO2)"
            elif elem2== "hydrogen":
                result="Water(H2O)"
            elif elem2== "chlorine":
                result="Chlorine Heptoxide(Cl2O7)"
            elif elem2== "oxygen":
                result="Oxygen(2O2)"           #All combinations of oxygen

        elif elem1== "hydrogen":
            if elem2== "carbon":
                result="Methane(CH4)"
            elif elem2== "oxygen":
                result="Water(H2O)"
            elif elem2== "chlorine":
                result="Hydrogen Chloride(HCl)"
            elif elem2== "hydrogen":
                result="Hydrogen(2H2)"               #All combinations of hydrogen

        elif elem1== "carbon":
            if elem2== "hydrogen":
                result="Methane(CH4)"
            elif elem2== "oxygen":
                result="Carbon Dioxide(CO2)"
            elif elem2== "chlorine":
                result="Carbon Tetrachloride(CCl4)"
            elif elem2== "carbon":
                result="Carbon(C)"                 #All combinations of carbon

        elif elem1== "chlorine":
            if elem2== "oxygen":
                result="Chlorine Dioxide(ClO2)"
            elif elem2== "hydrogen":
                result="Hydrogen Chloride(HCl)"
            elif elem2== "carbon":
                result="Carbon Tetrachloride(CCl4)"
            elif elem2== "chlorine":
                result="Chlorine(2Cl2)"                #All combinations of chlorine

        print("The Result is", result)               #printing output (result of the reaction)







    else:
        print("Invalid Input")           #invalid input if elem2 is incorrect
else:
    print("Invalid Input")              #invalid input if elem1 is incorrect