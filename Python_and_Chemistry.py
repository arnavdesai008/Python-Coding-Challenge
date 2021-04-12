# Program to show the output of a chemical reaction after accepting two elements from the user (out of oxygen, carbon, hydrogen and chlorine) and combining them.
# Author - Arnav Desai

# Taking input of the first element to combine in the reaction
elem1 = input("Enter the name of the first chemical to be combined from the set given (Oxygen, Carbon, Hydrogen, Chlorine): ").lower()

# Checking whether first element entered is valid or not
if elem1 == "oxygen" or elem1 == "hydrogen" or elem1 == "carbon" or elem1 == "chlorine":

    # Taking input of the second element to combine in the reaction
    elem2 = input("Enter the name of the second chemical to be combined from the set given (Oxygen, Carbon, Hydrogen, Chlorine): ").lower()

    # Checking whether second element entered is valid or not
    if elem2 == "oxygen" or elem2 == "hydrogen" or elem2 == "carbon" or elem2 == "chlorine":

        # All combinations of oxygen with all the other elements
        if elem1 == "oxygen":
            if elem2 == "carbon":
                result = "Carbon Dioxide(CO2)"
            elif elem2 == "hydrogen":
                result = "Water(H2O)"
            elif elem2 == "chlorine":
                result = "Chlorine Heptoxide(Cl2O7)"
            elif elem2 == "oxygen":
                result = "Oxygen(O2)"

        # All combinations of hydrogen with all the other elements
        elif elem1 == "hydrogen":
            if elem2 == "carbon":
                result = "Methane(CH4)"
            elif elem2 == "oxygen":
                result = "Water(H2O)"
            elif elem2 == "chlorine":
                result = "Hydrogen Chloride(HCl)"
            elif elem2 == "hydrogen":
                result = "Hydrogen(H2)"

        # All combinations of carbon with all the other elements
        elif elem1 == "carbon":
            if elem2 == "hydrogen":
                result = "Methane(CH4)"
            elif elem2 == "oxygen":
                result = "Carbon Dioxide(CO2)"
            elif elem2 == "chlorine":
                result = "Carbon Tetrachloride(CCl4)"
            elif elem2 == "carbon":
                result = "Carbon(C)"

        # All combinations of chlorine with all the other elements
        elif elem1 == "chlorine":
            if elem2 == "oxygen":
                result = "Chlorine Dioxide(ClO2)"
            elif elem2 == "hydrogen":
                result = "Hydrogen Chloride(HCl)"
            elif elem2 == "carbon":
                result = "Carbon Tetrachloride(CCl4)"
            elif elem2 == "chlorine":
                result = "Chlorine(Cl2)"

        # Printing output (result of the reaction)
        print("The result of the chemical reaction after both elements are combined is", result)

    else:
        # Invalid input if elem2 is incorrect
        print("The second element entered (", elem2, ")is invalid")

else:
    # Invalid input if elem1 is incorrect 
    print("The first element entered (", elem1, ")is invalid")
