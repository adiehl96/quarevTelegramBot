# quarevTelegramBot
A Telegram Bot that performs the [quarev](https://github.com/adiehl96/quarev) bitstream reversion on Quartus FPGA bitstream files for the Arduino MKR Vidor 4000.

# Setup
Create a python environment with telepot and wget installed. Get a telegram token as outlined [here](https://telepot.readthedocs.io/en/latest/).

# Usage
`python bot.py -t Your_Token` where `Your_Token` should be replaced by the token you have created earlier.

# Windows compatibility
This script can be run under windows with a correctly setup conda environment. To create a standalone executable file, add pyinstaller to your conda environment and run the command `pyinstaller bot.py --onefile`.

To run this bot from startup, create a shortcut to the executable file (bot.exe) that you created earlier. Right click the shortcut and open the properties window. In the window prefixed by the word "Target" is the target path to the executable file. Here you can add flags. Your target path should look like this: `...\bot.exe -t Your_token` where again `Your_Token` should be replaced by the token you have created earlier. Now add the shortcut to the startup folder as described in this tutorial [here](https://www.thewindowsclub.com/startup-folder-in-windows-8). Double clicking on this shortcut or rebooting your system should now start the quarev telegram bot.
