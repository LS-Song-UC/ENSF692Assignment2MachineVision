# input_processing.py
# <Letian Song>, ENSF 692 Spring 2025


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self, Light='Green', Pedestrian=False, Vehicle=False):
        self.Light = Light
        self.Pedestrian = Pedestrian
        self.Vehicle = Vehicle

  

    # Update_status takes in an object of class Sensor and reassigns values to each attribute based on input arguments.
    def update_status(self, Light, Pedestrian, Vehicle):
       self.Light = Light
       self.Pedestrian = Pedestrian
       self.Vehicle = Vehicle
        
        
   



# The sensor object should be passed to this function to print the action message and current status
# Function print_message takes in an object of class Sensor and the recorded input from user prompted during execution in 'main'.
# This function loops until status has been successfully updated or the user terminates the program using the input'0'.
# This function prompts the user for and option out of 3 categories of status updates, Light, Pedestrian and Vehicle.
# There are built-in handling procedures for invalid/unexpected input types/values, wherein the program will re-direct the user back to the beginning menu.
# Once a status has been updated, the function will print out the current recorded status of the object of class Sensor, as well as give a recommended course of action based on the current status.
# Note: the recommendation is given based on the entire range of attributes currently stored inside the object, for instance, if a user updates Vehicle status from True to False,
# but legacy input for other attributes prevent affirmative action such as Pedestrian still being stored as "True", the function will
# "Evaluate", then inform the user to "STOP!" even if the last updated status changed to encourage affirmative action.
# In other words, when and only when all 3 attributes allow the user to proceed or proceed with caution, will the function output the corresponding statement.
    def print_message(self, Status):
            Warningmessage = False
            while True: 
                Light = self.Light   # Note: The following variables are initiated under the infinite loop because they need to retain their values each time a loop is executed, if they were one level above, the same statements will cause the object's default values to take over. I also needed to reset the status of warningmessage each time for it to be accurately used in status evaluation later on in the function.
                Pedestrian = self.Pedestrian
                Vehicle = self.Vehicle
                
                if Status == 1:
                    Light = input("What color is the traffic light displaying? You may enter 'Red', 'Yellow', or 'Green'.")
                    if (Light.lower() != 'red') and (Light.lower() !='green') and (Light.lower() != 'yellow'):
                        print("Invalid input! Please enter 'Red','Green', or 'Yellow'.")
                        continue
                    if Light.lower() == 'red':
                        Warningmessage = True
                        print("STOP!")
                        Light = 'Red'
                        self.update_status(Light, Pedestrian, Vehicle)
                        break
                    elif Light.lower() =='green':
                        print("Evaluating...")
                        Light = 'Green'
                        self.update_status(Light, Pedestrian, Vehicle)
                        break
                    elif Light.lower() =='yellow':
                        print("Caution, Evaluating...")
                        Light = 'Yellow'
                        self.update_status(Light, Pedestrian, Vehicle)
                        break

                
            
                elif Status == 2:
                        Pedestrian = input("Are there pedestrians detected? 'Yes' or 'No'")
                        if Pedestrian.lower() == 'yes':
                            Warningmessage = True
                            print("STOP!")
                            Pedestrian = True
                            self.update_status(Light, Pedestrian, Vehicle)
                            break
                        elif Pedestrian.lower() == 'no':
                            print("Evaluating...")
                            Pedestrian = False
                            self.update_status(Light, Pedestrian, Vehicle)
                            break
                        else:
                            print("Invalid input! Please try again.")
                            continue
                elif Status == 3:
                        Vehicle = input("Are there any vehicles detected? 'Yes' or 'No'")
                        if Vehicle.lower() == 'yes':
                            Vehicle = True
                            Warningmessage = True
                            print("STOP!")
                            self.update_status(Light, Pedestrian, Vehicle)
                            break
                        elif Vehicle.lower() == 'no':
                            print("Evaluating...")
                            Vehicle = False
                            self.update_status(Light, Pedestrian, Vehicle)
                            break
                        else:
                            print("Invalid input! Please try again.")
                            continue
            # This section achieves the 'evaluation' functionality previously mentioned, it gives recommendations based on the final and overall status of all 3 attributes instead of that of the most recently updated.
            print("Current Status:", "Light: ", self.Light, " Pedestrian: ", self.Pedestrian, " Vehicle: ", self.Vehicle)
            if not Warningmessage and (self.Light == 'Red' or self.Pedestrian == True or self.Vehicle == True):
                print("STOP!")
            elif not Warningmessage and self.Light =='Green' and self.Pedestrian == False and self.Vehicle == False:
                print("Action recommended: Proceed.")
            elif not Warningmessage and self.Light =='Yellow' and self.Pedestrian == False and self.Vehicle == False:
                print("Action recommended: Proceed with caution.")
            elif not Warningmessage and self.Light =='Yellow' and (self.Pedestrian or self.Vehicle):
                print("STOP!")



# main function defines and object of class Sensor then prompts user for an integer input for which status they intend to update.
# Once collected, these two arguments are passed to function print_message which internally calls update_status throughout.
# main handles invalid input types by casting input to integer and raising ValueError when user types in alternative data types.
# main handles invalid integer input values by causing loop to continue if input isn't 0,1,2 or 3.
# main also implements a kill-switch which allows exit from the execution loop if the user types in '0' as stated in the prompt.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n") 
    DefaultSensor = Sensor()
    check_all_combinations()
"""     while True:
        try:
            status = int(input("Is there a status to update? '1' for light, '2' for Pedestrians and '3' for Vehicles, '0' to quit."))
            if status == 0:
                print("Thank you for your input.Goodbye.")
                break
            elif status not in range(4):
                print("Please use numbers 0, 1, 2, or 3!")
                continue
            DefaultSensor.print_message(status)
        except ValueError:
            print("Invalid input type. Please enter an integer 0, 1, 2, or 3!") """
from itertools import product

def check_all_combinations():
    count = 0
    # Possible values for each category (including invalid)
    light_values = ['Red', 'Yellow', 'Green', 'Invalid']
    pedestrian_values = [True, False, 'Invalid']
    vehicle_values = [True, False, 'Invalid']

    # Get all possible combinations (36 combinations)
    combinations = product(light_values, pedestrian_values, vehicle_values)
    
    print("\nChecking all possible combinations...\n")
    
    # Process valid and invalid combinations
    for light, pedestrian, vehicle in combinations:
        print(f"Combination: Light = {light}, Pedestrian = {pedestrian}, Vehicle = {vehicle}")
        print("Evaluating:")
        
        # Handle invalid input for each category
        if light == 'Invalid' or pedestrian == 'Invalid' or vehicle == 'Invalid':
            print("Invalid input detected! Please enter a valid value.")
        else:
            # Evaluate the status based on the current combination
            if light == 'Red' or pedestrian is True or vehicle is True:
                print("STOP!")
            elif light == 'Yellow':
                print("Proceed with caution.")
            elif light == 'Green' and not pedestrian and not vehicle:
                print("Proceed.")
        count+=1
        print("-" * 50)
        print(count)

    # Process invalid combinations (to simulate incorrect inputs)
def test_invalid_inputs():
    # Simulate invalid inputs for each category (Light, Pedestrian, Vehicle)
    invalid_values = ['abc', '@', '123', '...', '?']

    print("\nSimulating invalid inputs...\n")
    
    # Test invalid inputs for Light
    print("Testing Light input:")
    for invalid_value in invalid_values:
        print(f"Invalid Light input: {invalid_value}")
        if invalid_value.lower() not in ['red', 'yellow', 'green']:
            print(f"Invalid input '{invalid_value}' for Light! Please enter 'Red', 'Yellow', 'Green' or 'Invalid'.")
        print("-" * 50)

    # Test invalid inputs for Pedestrian
    print("Testing Pedestrian input:")
    for invalid_value in invalid_values:
        print(f"Invalid Pedestrian input: {invalid_value}")
        if invalid_value.lower() not in ['true', 'false']:
            print(f"Invalid input '{invalid_value}' for Pedestrian! Please enter 'True', 'False' or 'Invalid'.")
        print("-" * 50)

    # Test invalid inputs for Vehicle
    print("Testing Vehicle input:")
    for invalid_value in invalid_values:
        print(f"Invalid Vehicle input: {invalid_value}")
        if invalid_value.lower() not in ['true', 'false']:
            print(f"Invalid input '{invalid_value}' for Vehicle! Please enter 'True', 'False' or 'Invalid'.")
        print("-" * 50)
        
if __name__ == '__main__':
    main()

