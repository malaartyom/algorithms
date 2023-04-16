#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <cstdlib>
#include <ctime>
#define SIZE 100000000
static const size_t SORT_THRESHOLD = 16;

 
void shuffle(int* arr, int N)
{
    srand(time(NULL));

    for (int i = N - 1; i >= 1; i--)
    {
        int j = rand() % (i + 1);
 
        int tmp = arr[j];
        arr[j] = arr[i];
        arr[i] = tmp;
    }
}

void swap(int *i, int *j)
{
    int tmp = *i;
    *i = *j;
    *j = tmp;
}

int* lomuto_partition_branchfree(int* first, int* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    --last;
    if (*first > *last)
        swap(first, last);
    auto pivot_pos = first;
    auto pivot = *first;
    do {
        ++first;
        assert(first <= last);
    } while (*first < pivot);
    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        auto smaller = -int(x < pivot);
        auto delta = smaller & (read - first);
        first[delta] = *first;
        read[-delta] = x;
        first -= smaller;
    }
    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}

template<typename It>
void unguarded_linear_insert(It last) {
    auto val = *last;
    --last;
    auto x = *last;
    if (val >= x)
        return;
    for (;;) {
        last[1] = x;
        --last;
        x = *last;
        if (val >= x)
            break;
    }
    last[1] = val;
}
template<typename It>
void insertion_sort(It first, It last) {
    assert(first <= last);
    for (auto i = first + 1; i < last; ++i) {
        auto val = *i;
	    if (val < *first) {
            size_t n = i - first - 1;
            do {
                first[n + 1] = first[n];
            }
            while (n--);
	        *first = val;
	    }
	    else
	        unguarded_linear_insert(i);
	}
}
template <class It>
void sort(It first, It last) {
    while (last - first > size_t(SORT_THRESHOLD)) {
        auto cut = lomuto_partition_branchfree(first, last);
        assert(cut >= first);
        assert(cut < last);
	    sort(cut + 1, last);
	    last = cut;
	}
    insertion_sort(first, last);
}

int main() {
    int* arr = (int*)malloc(SIZE * sizeof(int));
    for (int i = 0; i < SIZE; i++){
        arr[i] = i;
    }

    shuffle(arr, SIZE);

    // for (int i = 0; i < SIZE - 1; i++) {
    //     printf("%d ", arr[i]);
    // }

    sort(&arr[0], &arr[SIZE - 1]);

    // for (int i = 0; i < SIZE - 1; i++) {
    //      printf("%d ", arr[i]);
    // }
    return 0;
}