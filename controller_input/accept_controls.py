from inputs import devices

'''
Function: select_controller_inputs
@param: None
@Return: Input selection
Description: Lists all devices that are detected on system. Allows user to
select which device they will be using to send input. Returns the selected
device
'''
def select_controller_inputs():

    i = 0
    #List all available devices detected for input
    print("#################################")
    print("## Available devices for input ##")
    print("#################################\n")
    for device in devices:
        print(device)


# Main function.
if __name__ == "__main__":
    select_controller_inputs()
