#include <wiringSerial.h>
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <time.h>
#define true 1
#define false 0
#define PACKET_SIZE 1000
#define D 500

int open_communication() {
    return serialOpen("/dev/serial0", 115200);
    //Open serial communication with baud rate of 115200
}

int send_file(FILE* fd, int serial_fd, char *filename) {
    serialPrintf(serial_fd, "%s\n", filename);
    int i = 0; //Iteration variable
    char packet[PACKET_SIZE+1] = "";
    while(fgets(packet, PACKET_SIZE, fd) != NULL) {
        serialPuts(serial_fd, packet);
        delay(D);
        //printf("%s", packet);
        //strcpy("", packet);


    }
    //serialPuts(serial_fd, packet);
    serialPutchar(serial_fd, '\0');
    //serialClose(serial_fd);
    return i;
}

int main(int argc, char **argv) {
    FILE *tosend = fopen(argv[1], "r");
    //printf("Sending file %s\n", argv[1]);
    clock_t begin = clock();
    int serial_fd = open_communication();
    send_file(tosend, serial_fd, argv[1]);
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Code execution time: %f\n", time_spent*1000);
    return 0;
}