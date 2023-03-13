import subprocess

def get_current_rotation():
    output = str(subprocess.check_output(["display64.exe", '/device', '1', '/properties'])) # get the current information about the display
    current_rotation = int(output.split('Orientation')[1].split('\\xb0')[0].split(': ')[1]) # split the output, narrowing down to just the rotation number
    return current_rotation

def rotate_screen(rotation):
    subprocess.call(["display64.exe", '/device', '1', '/rotate', str(rotation)]) # call display64.exe with the rotation argument

rotation = get_current_rotation()
if rotation == 0:
    # if the screen is landscape, rotate to portrait
    rotate_screen(270)
elif rotation == 270:
    # if the screen is portrait, rotate to landscape
    rotate_screen(0)