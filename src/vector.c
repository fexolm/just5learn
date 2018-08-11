#include "vector.h"
#include <stdlib.h>

struct Vector * Vector_alloc(size_t len) {
    void *mem = malloc(sizeof(struct Vector) + sizeof(float) * len);
    struct Vector *vect = mem;
    vect->buf_ = mem + sizeof(struct Vector);
    return vect;
}

void Vector_free(struct Vector *v) {
    free(v);
}
