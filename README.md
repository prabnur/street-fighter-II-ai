# street-fighter-II-ai
Making an AI to beat Street Fighter II's campaign using Lua, Gym and Keras-RL.

## Technologies Used
* Bizhawk Emulator v2.5.2
* SF II - The World Warrior ROM

## Initial Setup
1. Copy the Save State files from the `Save State` folder to `Bizhawk/SNES/State` folder
1. `pip install -r requirements.txt`
1. Create directory `stats` in Python
1. Put the Bizzhawk emulator folder (`Bizhawk-2.5.2`) and rom in `emulator and rom`

## Start Up
1. Double Click `startup.bat` if you use Windows, or run `python socket_server.py` and `Emuhawk.exe --socket_ip=127.0.0.1 --socket_port=8080`
1. Load the ROM.
1. Load the lua script by going to tools and clicking on Lua Console.
1. Click the open script button and load the `sf2.lua` script.

If done correctly, it should start with Ryu and Ken fighting

## Useful Tools
RAM Watch and RAM Search helps with identifying memory addresses, and verifying data.