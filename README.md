# BuzzPass
Experiments were run on a raspberry Pi zero W, connected over SSH.<br>
To run this code:<br>
-Install wiringpi on the raspberry pi<br>
-Enable Serial (the serial login feature should be off)<br>
-Solder connections from the FTDI to the 5V, Gnd, UART_TX and UART_RX pins of the raspberry pi<br>
-Clone this code<br>
-Run the compile_all.sh script (our equivalent of a makefile)<br>
<br>
Several programs are available:<br>
The c programs allow for file transfer (receive must be run before send_file)<br>
Zigcomm.py is used for communication debugging, especially useful to make sure after an update of the firmware running on both devices still allows for communication. This was used in debugging to ensure that the issue was coming from the devices and changes made as opposed to the code.
