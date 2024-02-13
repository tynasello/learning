import java.util.List;
import java.util.ArrayList;

class MyCalendarTwo {
    public static void main(String[] args) {
        int arr[][] = { { 10, 20 }, { 50, 60 }, { 10, 40 }, { 5, 15 }, { 5, 10 }, { 25, 55 } };

        for (int[] interval : arr) {
            int start = interval[0];
            int end = interval[1];
            MyCalenderTwo obj = new MyCalenderTwo();
            System.out.println(obj.book(start, end));
        }
    }
}

class MyCalenderTwo {

    List<int[]> singleBooked;
    List<int[]> doubleBooked = new ArrayList<int[]>();

    public void MyCalendarTwo() {
        singleBooked = new ArrayList<int[]>();
    }

    public boolean book(int start, int end) {
        for (int[] interval : doubleBooked) {
            int s = interval[0];
            int e = interval[1];
            if (s < end && e > start) {
                return false;
            }
        }
        for (int[] interval : singleBooked) {
            int s = interval[0];
            int e = interval[1];
            if (s < end && e > start) {
                int addStart = Math.max(s, start);
                int addEnd = Math.min(e, end);
                doubleBooked.add(new int[] { addStart, addEnd });
            }
        }

        singleBooked.add(new int[] { start, end });
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo(); boolean param_1 =
 * obj.book(start,end);
 */