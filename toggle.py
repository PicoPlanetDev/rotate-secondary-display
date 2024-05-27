import subprocess
import argparse

DEFAULT_DISPLAY = 1
LANDSCAPE = 0
PORTRAIT = 270

def get_rotation(display: int):
    output = str(subprocess.check_output(["display64.exe", '/device', str(display), '/properties'])) # get the current information about the display
    current_rotation = int(output.split('Orientation')[1].split('\\xb0')[0].split(': ')[1]) # split the output, narrowing down to just the rotation number
    return current_rotation

def set_rotation(display: int, rotation: int):
    subprocess.call(["display64.exe", '/device', str(display), '/rotate', str(rotation)]) # call display64.exe with the rotation argument

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", help="Display number to rotate")
    args = parser.parse_args()

    if args.display:
        display = int(args.display)
    else:
        display = DEFAULT_DISPLAY
        print(f"No display number provided, defaulting to {display}")
    
    current_rotation = get_rotation(display)
    if current_rotation == LANDSCAPE: set_rotation(display, PORTRAIT) # if the screen is landscape, rotate to portrait
    elif current_rotation == PORTRAIT: set_rotation(display, LANDSCAPE) # if the screen is portrait, rotate to landscape
