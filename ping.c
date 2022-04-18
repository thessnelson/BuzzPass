#include <wiringSerial.h>
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <time.h>
#define true 1
#define false 0
#define N 35317


int open_communication() {
    return serialOpen("/dev/serial0", 115200);
    //Open serial communication with baud rate of 115200
}

int power(int base, int exp) {
    if (exp == 0)
        return 1;
    else if (exp % 2)
        return base * power(base, exp - 1);
    else {
        int temp = power(base, exp / 2);
        return temp * temp;
    }
}

int listen_for_code(int fd) {
    char code[50] = "";
    int running = true;
    char c = 0;
    int i = 0;

    while(running) {
        c = serialGetchar(fd);
        if(c == 'Z') {
            break;
        }
        code[i++] = c;
    }
    return atoi(code);
}

int main(int argc, char **argv) {
    int serial_fd = open_communication();
    int c = listen_for_code(serial_fd);
    printf("Code received is %d\n", c);
    if(c == N) {
        printf("Can begin transmission!\n");
        serialPrintf(serial_fd, "K");
        return 0;
    } else {
        printf("WARNING! POSSIBLE INTRUSION!\n");
        return 1;
    }
    return 2;
}