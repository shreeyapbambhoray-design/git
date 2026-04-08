print("hello world")
public class FCFS {
    public static void main(String[] args) {

        int[] burstTime = {40, 10}; // Task 1 (long), Task 2 (short)
        int time = 0;

        for (int i = 0; i < burstTime.length; i++) {
            time += burstTime[i];
            System.out.println("Process " + i + " finished at " + time);
        }
    }
}
