#include <wiringSerial.h>
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#define true 1
#define false 0

int open_communication() {
    return serialOpen("/dev/serial0", 115200);
    //Open serial communication with baud rate of 115200
}


int listen(int fd) {
    char filename[50] = "";
    int running = true;
    int got_file = false;
    char c = 0;
    int i = 0;
    FILE *output_file = stdout;

    while(running) {
        c = serialGetchar(fd);
        if(c != '\n' && got_file == false) {
            filename[i] = c;
        }
        fputc(c, output_file);
        if(c == '\n' && got_file == false) {
            printf("Reading from file %s\n", filename);
            got_file = true;
            output_file = fopen(filename, "w");
        }

        if(c == '\0' && got_file) {fclose(output_file); break;}
        i += 1;
    }
    return i;
}

int main(int argc, char **argv) {
    printf("Starting the receive.c program\n");
    int b = open_communication();
    printf("Serial communication number: %d\n", b);
    int r = listen(b);
    printf("Received %d bytes\n", r);
    return 0;
}