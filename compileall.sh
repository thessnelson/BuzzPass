echo "Compiling for send_file"
gcc send_file.c -o send_file -lwiringPi
echo "Compilation complete"

echo "Compiling for receive"
gcc receive.c -o receive -lwiringPi
echo "Compilation complete"

echo "Compiling for ping"
gcc ping.c -o ping -lwiringPi
echo "Compilation complete"