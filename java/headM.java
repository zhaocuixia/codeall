import java.util.Arrays;

public class headM {

    static int Partition( int input[], int begin, int end)//找到了begin的正确位置
    {
        if (begin<=end) {
            int low = begin;
            int high = end;
            int pivot = input[low]; //取第一个值
            while (low < high) {
                while (pivot <= input[high] && low < high)
                    high--;
                input[low] = input[high];
                while (input[low] <= pivot && low < high)
                    low++;
                input[high] = input[low];
            }
            input[low] = pivot;
            return low;
        }
        else
            return -1;
    }

    static void GetLeastNumbers_Solution(int input[], int k) {
        int len = input.length;
        int pos = len - k; //找到这个元素的位置，则包含这个往右都是需要的
        int start = 0;
        int end = len - 1;
        int index = Partition(input, start, end);
        while (index != (pos - 1)) //如果等于说明正好找到了
        {
            if (index > pos - 1) {
                end = index - 1;
                index = Partition(input, start, end);  //在前面找k-1位置
            } else {
                start = index + 1;
                index = Partition(input, start, end); //在后面找k-1位置
            }
        }
    }
    static void arrangRight(int input[], int start,int end,int k){
        if (start<=end) {
            int index = Partition(input, start, end);
            int cnt = end - index + 1; //右边的个数 //这里不太对呢之前是len-1
            if (cnt == k) //如果等于说明正好找到了{}
            {
                return;
            } else if (cnt > k) {
                arrangRight(input, index+1, end, k);  //在前面找k-1位置
            } else {

                arrangRight(input, start, index - 1, k - cnt); //在后面找k-1位置
            }


        }

    }

    public static void main(String[] args) {
        int []arry={1,2,6,3,7,9,5,4,8,0};
        // GetLeastNumbers_Solution(arry,4); //找出k个较大数
        arrangRight(arry,0,arry.length-1,5);
        String s = Arrays.toString(arry);
        System.out.println(s);
    }
}

