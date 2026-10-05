#include <iostream>

int sumArray(int arr[]);
int minArray(int arr[]);
int** multTable(int n);
int* avgArray(int arr[][]);

int main() {
    
}

int sumArray(int arr[]) {
    int total = 0;
    for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
        total += arr[i];
    }
    return total;
}

int minArray(int arr[]) {
    int min = arr[0];
    for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
        if(arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

int** multTable(int n) {
    int arr[n][n];
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            arr[i][j] = i*j;
        }
    }
    return arr;
}

int* avgArray(int arr[][]) {

}
