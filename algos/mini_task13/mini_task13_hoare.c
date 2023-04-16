#include <stdio.h>
#include <stdlib.h>
#define SIZE 100000000
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
        arr[i] = i;
    }

    shuffle(arr, SIZE);

    quicksort(arr, 0, SIZE - 1);
    // for (int i = 0; i < SIZE - 1; i++) {
    //     printf("%d ", arr[i]);
    // }
    return 0;
}