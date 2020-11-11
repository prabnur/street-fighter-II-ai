# street-fighter-II-ai
Making an AI to beat Street Fighter II's campaign using Lua, Gym and Keras-RL.

This is using the Bizhawk Emulator version 2.5.2, and the SF II - The World Warrior Rom.

To set up working with the Lua script:
Put the Save State from the Save State folder in the Bizhawk/SNES/State folder
Start the emulator with cmd with the following command:
Emuhawk.exe --socket_ip=127.0.0.1 --socket_port=8080
Load the ROM.
Load the lua script by going to tools and clicking on Lua Console.
Click the open script button and load the sf2.lua script.
If done correctly, it should start with Ryu and Ken fighting

Other useful tools:
RAM Watch and RAM Search helps with identifying memory addresses, and verifying data.