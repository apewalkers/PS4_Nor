# PS4_Nor
Uart Flag for PS4


This is a Script written in Python, checks Nor Dumps and patches
    offset1 = 0x001c9310
    offset2 = 0x001cc310

How to.

Extract PS4 NOR Firmware to PC and put in same Folder as Python Script
Execute the Script
Select your Firmware Backup

  Pay Attention to "Uart Flag"
  
  Once you select Patch it will Create a Backup of your original BIN in a sub Folder called backup - and a Patched/Uart Unlocked Firmware titled "_Patched.bin"
  
  This script has been Tested on 3 Consoles 10/11/12 but nothing else, This is super experimental and adivse you proceed at your own risk.
 
 
I wrote this script to help internally diagnose Blod Errors with allot of insperation from 100s of sources accross Git, PSH & Repair Wiki.

i have hopes and ambitions of pushing further into the PS5 Firmware and enabling the Debug flags once i get more time to work with them.

THIS DOES NOT FIX FIRMWARE CORRUPTION
THIS DOES NOT FIX YOUR CONSOLE
THIS ONLY HELPS YOU UNDERSTAND WHAT IS WRONG WITH YOUR CONSOLE, its a tool designed to give you the ability to work out WHY your console BLODs


      Firmware this has been tested on
 7.x
 8.x
 9.x
 
 
 Tools used to Dump/Flag
 
 Raspberry Pi 
 Jump Wire
https://www.flashrom.org/RaspberryPi


Found this helpful? Why not buy me a coffee. NOT MANDATORY
https://www.buymeacoffee.com/DonyOnline


 
 
