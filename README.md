# PeachRP
Peach RP is a small program that uses discord-rpc to create a custom rich presence/game on discord.
<br>Using just a simple configuration file and the power of Python.

## Using

First you need to register the Rich Presence app in discord

1. Come here https://discordapp.com/developers/applications/me
2. Create a new app 
<br>*The app name will be the main name for Rich Presence*
3. Enable Rich Presence for your app and add some resources 
4. Download the latest version of PeachRP from here https://github.com/IgorSlot/PeachRP/releases
5. Before starting, you need to configure the config.ini file
<br>*The example is in the category [Example](https://github.com/IgorSlot/PeachRP#exmaple)*
6. Run the PeachRP executable file (it should open a cmd window)

- **Error**
<br> If not, add the exe file as a game to discord, and the path to the file should change to your presence. You can edit the configuration at any time while the program is running to change the presence (be sure to save the file)

- **Timestamps**
<br>The start and end timestamps are specified in unix epoch/time. The desired values can be found here. For the elapsed time, set only the StartTimestamp mark. For the remaining time, install both. Although discord seems to only care about hours/minutes/seconds. Since in any case it does not exceed 24 hours _(ツ)_/

## Exmaple
[Identifiers]
<br>ClientID=987972733759529040

[State]
<br>State=Hello World!
<br>Details=Python 3.10.9
<br>StartTimestamp=1677915313
<br>EndTimestamp=1677915313

[Images]
<br>LargeImage=1
<br>LargeImageTooltip=Visual Studio Code
<br>SmallImage=2
<br>SmallImageTooltip=Python

## Build

1. git clone https://github.com/IgorSlot/PeachRP
2. pip install pypresencepip
3. pip install configparser
4. And run the file main.py
