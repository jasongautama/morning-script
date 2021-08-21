#!/usr/bin python3
# History:
#   - JG completed v1.0 | 8/21/2021

import sys  # python version
import os  # execute cmd line
import webbrowser  # open browser (chrome) page

# Goal: to open the necessary application that I need when I start my work:
# This includes:
#   1. open Chrome (calendar.google.com, gmail.com, Rick Roll)
#   3. open Spotify

# takes in argument for website pages


def openWebPages():
    constURL = "https://"
    URLs = ["gmail.com", "calendar.google.com",
            "www.youtube.com/watch?v=dQw4w9WgXcQ",
            "open.spotify.com/track/1F7iIQGzyVMcie8L95BfW1?si=8eed53356ca14820"]

    for url in URLs:
        webbrowser.get().open_new(constURL + url)


def openDefaultApps():
    print("Opening Browser..")
    # Future improvement:
    # ask user input for websites they want to visit
    openWebPages()
    print("Opening WhatsApp..")
    os.system("cd /Applications && open Whatsapp.app")
    print("Opening Spotify..")
    os.system("cd /Applications && open Spotify.app")
    return


def versionPy():
    print("Running Python " + sys.version)


def main():
    openDefaultApps()
    print("Happy Hacking!")
    versionPy()


if __name__ == "__main__":
    main()
