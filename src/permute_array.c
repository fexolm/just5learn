#include <assert.h>
#include <stddef.h>
#include "utility.h"

// please implement function here
void permute_array(int *arr, size_t len) {
    // interchange odd and even elements of arrays
    // e.g. array {1,2,3,4,5} should become {2,1,4,3,5}
}

int main() {
    int arr[] = {1,5,2,6,7,2,9,10};
    size_t len = sizeof(arr) / sizeof(arr[0]); // please don't use it for non-static arrays
    print_array_int(arr, len);
    permute_array(arr, len);
    print_array_int(arr, len);
}
