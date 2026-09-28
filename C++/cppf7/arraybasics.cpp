#include <iostream>

int main() {
    int nums[10];
    int arr[]={1,2,3};
    std::cout << arr[1] << std::endl;
    nums[0] = 0;
    std::cout << sizeof(nums) / sizeof(nums[0]) << std::endl;
    for(int i = 0; i<sizeof(nums) / sizeof(nums[0]); i++) {
        nums[i] = i;
    }
    std::cout << nums << std::endl;
    for(int i = 0; i<sizeof(nums) / sizeof(nums[0]); i++) {
        std::cout << nums[i] << std::endl;
    }
    int* p1 = nums;
    std::cout << *p1 << std::endl;
    std::cout << *(p1+4) << std::endl;
    std::cout << *(p1++) << std::endl;
    std::cout << *p1 << std::endl;
    std::cout << *(p1+9) << std::endl;
    std::cout << nums[10] << std::endl;
}