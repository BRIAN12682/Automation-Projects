#This automates the search of google maps and returns the browser with it
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Getting content from the command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get the clipboard content.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)