#include <stdio.h>
#include <stdlib.h>
#define SIZE 100000

void swap(int* arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

int partition(int* arr, int start, int end) {
    int pivot = arr[end];
    int i = start;
    for (int j = start; j < end; j++) {
        if (arr[j] < pivot) {
            swap(arr, i, j);
            i++;
        }
    }
    swap(arr, i, end);
    return i;
}

void quicksort(int* arr, int start, int end) {
    if (start < end) {
        int p = partition(arr, start, end);
        quicksort(arr, start, p - 1);
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