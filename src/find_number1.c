#include <assert.h>
#include <stddef.h>
#include <stdbool.h>
bool contains(int *arr, int len, int num) {
    // returns true if arr contains num
}

int find_index(int *arr, int len, int num) {
    // returns -1 if contains(arr, num)==false, else returns index
    // of first occurence num in arr
}

int main() {
    int arr[] = {1,5,2,6,7,2,9,10};
    size_t len = sizeof(arr) / sizeof(arr[0]); // please don't use it
    // it works just for static arrays, not for pointers
    assert(contains(arr, len, 9) == true && "array contains 9"); // == true just for readability here
    assert(contains(arr, len, 123) == false && "array not contains 123");
    assert(find_index(arr, len, 2) == 2 && "arr[2] == 2");
    assert(find_index(arr, len, 123) == -1 && "123 is not in array");
}
