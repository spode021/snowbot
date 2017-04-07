from inputs import devices

'''
Function: select_controller_inputs
@param: None
@Return: Device to be used for input
Description: Lists all devices that are detected on system. Allows user to
select which device they will be using to send input. Returns the selected
device
'''
def select_controller_inputs():

    starting_index_value = 1
    i = 0
    #List all available devices detected for input
    print("#################################")
    print("## Available devices for input ##")
    print("#################################\n")

    for device in devices:
        print(str(starting_index_value + i) + ": " + str(device))
        #Advance selection index
        i += 1

    # Select device from number list
    Selection = input("\n Which device do you want to use?: ")

    # Arrays start at 0, so need to subtract starting index to get
    # correct device that was selected.
    Selection = int(Selection) - starting_index_value

    print(str(devices[Selection]) + " has been selected")

    return devices[Selection]
# Main function.
if __name__ == "__main__":
    device = select_controller_inputs()

    print("Now using " + str(device))
