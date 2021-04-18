import java.util.Arrays;

public class nixu {

    static   int InversePairs(int[] data) {
        int length  = data.length;
        return mergeSort(data, 0, length-1);
    }

    static   int mergeSort(int []data, int start, int end) {
        // 递归终止条件
        if (start<=end){
            if(start == end) {
                return 0;
            }

            // 递归
            int mid = (start + end) / 2;
            int leftCounts = mergeSort(data, start, mid);
            int rightCounts = mergeSort(data, mid+1, end);

            // 归并排序，并计算本次逆序对数
            int[] copy = new int[10]; // 数组副本，用于归并排序,think副本数应该多大
            int foreIdx = mid;     // 前半部分的指标
            int backIdx = end;     // 后半部分的指标
            int counts = 0;        // 记录本次逆序对数
            int idxCopy = end;     // 辅助数组的下标
            //-------------
            //加了这块统计你逆序的
            while(foreIdx>=start && backIdx >= mid+1) {
                if(data[foreIdx] > data[backIdx]) {
                    copy[idxCopy--] = data[foreIdx--];
                    counts += backIdx - mid;
                } else {
                    copy[idxCopy--] = data[backIdx--];
                }
            }
            //-------------------------
            while(foreIdx >= start) {
                copy[idxCopy--] = data[foreIdx--];
            }
            while(backIdx >= mid+1) {
                copy[idxCopy--] = data[backIdx--];
            }
            for(int i=start; i<=end; i++) {
                data[i] = copy[i];
            }

            return (leftCounts+rightCounts+counts);
        }
        else
            return -1;
    }

    public static void main(String[] args) {
        int []arry={1,2,3,4,5,6,7,8,9,10};
        int a = InversePairs(arry);
        //String s = Arrays.toString(arry);

        System.out.println(a);
    }




}