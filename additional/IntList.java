package additional;


public class IntList {
    private int[] data;
    private int size = 0;
    private int capacity = 1;

    IntList(){
        data = new int[2];
        capacity = 2;
        size = 0;
    }

    public void add(int number){
        if (size == capacity){
            int[] tmp;
            tmp = new int[capacity];
            System.arraycopy(data, 0, tmp, 0, size);
            capacity *= 2;
            data = new int[capacity];
            System.arraycopy(tmp, 0, data, 0, size);
        }
        data[size] = number;
        size++;
    }

    public void remove(int indx){
        System.arraycopy(data, indx + 1, data, indx, size - indx - 1);
        size--;

    }

    public boolean find(int number){
        for (int i = 0; i < size; i++) {
            if (data[i] == number){
                return true;
            }   
        }
        return false;
    }

    public int size(){
        return size;
    }
}