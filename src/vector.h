#include <stddef.h>
#include <assert.h>
struct Vector {
    float *buf_;
    size_t len;
};

struct Vector *Vector_alloc(size_t len);

void Vector_free(struct Vector *v);

inline float Vector_get(struct Vector *v, size_t ind) {
    assert(ind >= 0 && ind < v->len);
    return v->buf_[ind];
}

inline void Vector_set(struct Vector *v, size_t ind, float val) {
    assert(ind >=0 && ind < v->len);
    v->buf_[ind] = val;
}

// TODO: implement Vector_sum, Vector_mult, Vector_dot, Vector_print
