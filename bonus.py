
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



def main():
   while True:
       try:
         user_input=(input("Enter a temperature and its unit (e.g., 25 \"C\" or 77 \"F\" )"))
         if user_input== "exit":
           break
         temp=user_input.split(" ")
         unit = temp[1]
         value = float(temp [0]) 

         if unit.upper() == 'C':
          print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(value)} F")
         elif unit.upper() == 'F':
          print(f"Temperature in Celsius: {fahrenheit_to_celsius(value)} C")
         else:
          raise TypeError ("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

       except ValueError:
        print("Invalid value. Please make sure to enter a valid number.")
       except TypeError as e:
        print(e)
 
main()




