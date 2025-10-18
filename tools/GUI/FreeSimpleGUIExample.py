import FreeSimpleGUI as sg  # type: ignore # Part 1 - The import


def feet_to_inches(feet, inches):
    """Convert feet and inches to total inches"""
    if feet < 0 or inches < 0:
        raise ValueError("Measurements cannot be negative")
    if inches >= 12:
        raise ValueError("Inches should be less than 12")
    return feet * 12 + inches


# Define the window's contents
layout = [
    [sg.Text("Enter feet"), sg.Input(key="-FEET-")],  # Part 2 - The Layout
    [sg.Text("Enter inches"), sg.Input(key="-INCHES-")],
    [sg.Text("Total inches"), sg.Text(size=(15, 1), key="-OUTPUT-")],
    [sg.Text(size=(40, 1), text_color="red", key="-ERROR-")],
    [sg.Button("Calculate"), sg.Button("Quit")],
]

# Create the window
window = sg.Window("Feet to Inches Converter", layout)  # Part 3 - Window Definition

while True:
    event, values = window.read()

    # Clear any previous error message
    window["-ERROR-"].update("")

    if event == "Calculate":
        try:
            feet = int(values["-FEET-"])
            inches = int(values["-INCHES-"])
            total_inches = feet_to_inches(feet, inches)
            window["-OUTPUT-"].update(total_inches)
            window["-ERROR-"].update("")
        except ValueError as e:
            if str(e).startswith("invalid literal"):
                window["-ERROR-"].update("Please enter valid numbers")
            else:
                window["-ERROR-"].update(str(e))
            window["-OUTPUT-"].update("")

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break


# Finish up by removing from the screen
window.close()
