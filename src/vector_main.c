#include "vector.h"

int main() {
    struct Vector *v = Vector_alloc(15);
    Vector_free(v);
}
