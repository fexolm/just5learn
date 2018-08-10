#include <assert.h>
#include <stddef.h>
#include "utility.h" // please implement function here


void reverse_array(int *arr, size_t len) {
    // reverse array inplace
}

int main() {
    int arr[] = {1,5,2,6,7,2,9,10};
    size_t len = sizeof(arr) / sizeof(arr[0]); // please don't use it
    print_array_int(arr, len);
    reverse_array(arr, len);
    print_array_int(arr, len);
}
