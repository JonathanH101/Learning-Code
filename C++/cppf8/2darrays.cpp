#include <iostream>

int main() {
    int arr[10][10];
    // int arr2[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
    int numrows = sizeof(arr)/(sizeof(arr[0]));
    int numcols = sizeof(arr[0])/sizeof(arr[0][0]);

    std::cout << numrows << std::endl;
    std::cout << numcols << std::endl;
    arr[4][2] = 42;
    std::cout << arr[4][2] << std::endl;
    for(int i = 0; i<numrows; i++) {
        for(int j = 0; j < numcols; j++) {
            arr[i][j] = i+j;
            std::cout << arr[i][j] << std::endl;
        }
    }
}

