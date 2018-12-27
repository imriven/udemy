import sys

def convert ():
    convert_unit = input("Would you like to convert to Fahrenheit or Celsius? Please use F or C: ")
    convert_number = input("What number would you like to convert?: ")
    if not str.isdigit(convert_number):
        sys.exit("That's not a number")
    if str.lower(convert_unit)  == "f":
        f_temp =(convert_number * 9/5) + 32
        print (str(convert_number) + " Celsius converts to " + str(f_temp) +" Fahrenheit")
    elif str.lower(convert_unit) == "C" or "c":
        c_temp = (convert_number - 32) * 5/9 
        print (str(convert_number) + "Fahrenheit converts to " + str(f_temp) +" Celsius")
    else:
        print("Invalid entry, Please enter C for Celsius or F for Fahrenheit!")
        
convert()


