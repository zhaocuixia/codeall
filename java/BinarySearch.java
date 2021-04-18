import java.util.Arrays;

public class BinarySearch {
    static int  binnarysearch(int a[], int len, int p) {
        int l = 0;
        int r = len-1;
        while(l<=r){
            int m = l + (r-l)/2;
            if (p == a[m])
                return m;
            else if (p<a[m])
                r= m-1; //这里一开始赋值没哟加减1
            else
                l = m+1;
        }
    return -1;

    }
    static int  lowbound(int a[], int len, int p) {
        int l = 0;
        int r = len-1;
        while(l<=r){
            int m = l + (r-l)/2;
            if (p == a[m])
                if (m-1>=0)
                    return m-1;
                else
                    return -1;
            else if (p<a[m])
                r= m-1; //这里一开始赋值没哟加减1
            else
                l = m+1;
        }
        return -1;

    }


    public static void main(String[] args) {
        int[] arr1 = {1,2,3,4,5};
        int pos = lowbound(arr1,arr1.length,10);
        System.out.println(pos);


    }




}
