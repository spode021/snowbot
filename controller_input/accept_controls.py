from inputs import *

'''
Function: select_controller_inputs
@param: None
@Return: Device to be used for input
Description: Lists all devices that are detected on system. Allows user to
select which device they will be using to send input. Returns the selected
device with a class type of Gamepad, Keyboard, or Mouse.
'''
def select_inputs():

    starting_index_value = 1

    #Select device. Make sure is valid selection.
    valid_selection = False
    while valid_selection == False:

        #List all available devices detected for input
        print("\n#################################")
        print("## Available devices for input ##")
        print("#################################\n")

        i = 0
        for device in devices:
            print(str(starting_index_value + i) + ": " + str(device))
            #Advance selection index
            i += 1
    # Select device from number list
        try:
            Selection = input("\n Which device do you want to use?: ")

            #cast selection to integer
            Selection = int(Selection)

            if (Selection >= starting_index_value) and (Selection < starting_index_value + i):
                valid_selection = True
            else:
                print("Invalid selection. Select a device from the list.")

        except (ValueError, TypeError):
            print("Not an integer")

    #End while loop

    # Arrays start at 0, so need to subtract starting index to get
    # correct device that was selected.
    Selection = Selection - starting_index_value

    print(str(devices[Selection]) + " has been selected")

    return devices[Selection]

#End select_inputs


'''
Function: get_events
@param: device being used for input
@return: None
Description: Get events from device. Currently assumed for input device to be
a gamepad. Need to look for a good way to discern if input device is a gamepad
or keyboard or any other input device to use. Gamepad input for joysticks is
a little complex. May want to evaluate gamepad input to be
simpler to understand.
'''
def get_events(device):
    while True:
        # read event from device
        events = device.read()
        for event in events:
            # print the event. Used for debugging and developing input use
            print(event.ev_type, event.code, event.state)


# Main function.
if __name__ == "__main__":
    device = select_inputs()

    print("Now using " + str(device))

    get_events(device)
