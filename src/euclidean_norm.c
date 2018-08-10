#include <assert.h>
#include <stddef.h>
#include <stdio.h>
#include <math.h> // some useful math functions are present here

// please implement function here
float euclidean_norm(float *arr, size_t len) {
    // calculate Euclidean norm of a vector
    // (square root of the sum of squared array elements)
    float sum = 0;
    for (size_t i = 0; i < len; i++)
        sum += arr[i] * arr[i];
    return sqrtf (sum);
}

int main() {
    float arr[] = {1.f,2.f,3.f,4.f,-5.f,};
    size_t len = sizeof(arr) / sizeof(arr[0]); // please don't use it for non-static arrays
    float norm = euclidean_norm(arr, len);
    printf("vector norm is %.7f\n", norm);
    assert(fabsf(norm-7.416198487f)<1e-6 && "wrong result");
}
