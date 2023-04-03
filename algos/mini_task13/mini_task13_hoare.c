#include <stdio.h>
#include <stdlib.h>
#define SIZE 100000
int partition(int* arr, int start, int end) {
    int r = rand() % 12;
    int pivot = arr[r];
    int i = start;
    int j = end;
    while (1) {
        while (arr[i] < pivot) {
            i++;
        }
        while (arr[j] > pivot) {
            j--;
        }
        if (i >= j) {
            return j;
        }
        int tmp = arr[j];
        arr[j] = arr[i];
        arr[i] = tmp;
        i++;
        j--;
    }
}
void quicksort(int* arr, int start, int end) {
    if (start < end) {
        int p = partition(arr, start, end);
        quicksort(arr, start, p);
        quicksort(arr, p + 1, end);
    }
}
int main() {
    int* arr = (int*)malloc(SIZE * sizeof(int));
    for (int i = 0; i < SIZE; i++){
        arr[i] = rand() % 200;
    }
    quicksort(arr, 0, SIZE - 1);
    // for (int i = 0; i < SIZE - 1; i++) {
    //     printf("%d ", arr[i]);
    // }
    return 0;
}