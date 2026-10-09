#include <iostream>

int sumArray(int *arr, int row, int col);
int minArray(int *arr, int row, int col);
int** multTable(int n);
float* avgArray(float *arr, int row, int col);

int main() {
    int array[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    std::cout << sumArray((int*)array, 3, 3) << std::endl;
    std::cout << minArray((int*)array, 3, 3) << std::endl;
    int** array2 = multTable(5);
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            std::cout << array2[i][j] << " ";
        }
        std::cout << std::endl;
    }
    float array4[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    float* array3 = avgArray((float*)array4, 3, 3);
    for(int i = 0; i < 3; i++) {
        std::cout << array3[i] << std::endl;
    }
}

// int sumArray(int arr[]) {
//     int total = 0;
//     for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
//         total += arr[i];
//     }
//     return total;
// }

int sumArray(int *arr, int row, int col) {
    int total = 0;
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            total += *((arr+i*col) + j);
        }
    }
    return total;
}

int minArray(int *arr, int row, int col) {
    int min = *arr;
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            if(*((arr+i*col) + j) < min) {
                min = *((arr+i*col) + j);
            }
        }
    }
    return min;
}

// int minArray(int arr[]) {
//     int min = arr[0];
//     for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
//         if(arr[i] < min) {
//             min = arr[i];
//         }
//     }
//     return min;
// }

int** multTable(int n) {
    int** arr = 0;
    arr = new int*[n];
    for(int i = 0; i <= n; i++) {
        arr[i] = new int[n];
        for(int j = 0; j <= n; j++) {
            arr[i][j] = (i+1)*(j+1);
        }
    }
    return arr;
}

float* avgArray(float *arr, int row, int col) {
    float* arr2 = 0;
    arr2 = new float[row];
    float number;
    for(int i = 0; i < row; i++) {
        number = 0;
        for(int j = 0; j < col; j++) {
            number += *((arr+i*col) + j);
        }
        arr2[i] = number/col;
    }
    return arr2; 
}
