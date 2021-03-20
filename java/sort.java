// 记录各种排序算法
import com.sun.scenario.effect.Merge;

import java.util.Arrays;

public class sort {

    //1、直接插入排序
    void paixu_charu(int a[]) {
    int len = a.length;
    String str1 = Arrays.toString(a);
    System.out.printf("原来数组：%s\n",str1);
    for(int i = 1; i < len; i++){
       //在0~j中找出i位置
       int temp = a[i];
       int j;
       for(j = i-1; j >= 0 && temp < a[j]; j--){
          a[j+1] = a[j];
       }
       a[j+1] = temp;
       String str = Arrays.toString(a);
       System.out.println(str);
    }

    }
    // 2、冒泡优化排序
    void paixu_maopao(int a[]) {
        int len = a.length;
        String str1 = Arrays.toString(a);
        System.out.printf("原来数组：%s\n",str1);
        boolean flag = true;
        for(int i = 1; i < len && flag ; i ++){ //循环趟数
            flag = false;
            for(int j = 0; j < len-i ; j++){
                if(a[j] > a[j+1]){ // 是否交换
                    int temp = a[j+1];
                    a[j+1] = a[j];
                    a[j] = temp;
                    flag = true;
                }
            }
            String str = Arrays.toString(a);
            System.out.println(str);
        }
    }
    // 3、快速排序(交换类)
    int sort(int a[], int low, int high){
        int temp = a[low];
        while(low < high){
            while(low < high && temp <= a[high])
                high--;
            a[low] = a[high];
            while(low < high && temp >= a[low])
                low++;
            a[high] = a[low];
        }
        a[low] = temp;  //返回temp的正确位置，并且左侧的比他小右边的比他大
        String str = Arrays.toString(a);
        System.out.println(str);
        return low;
    }
    void paixu_kuaisu(int a[],int low, int high) {
      if(low < high){
        int pos = sort(a,low,high);
        paixu_kuaisu(a,low,pos-1);
        paixu_kuaisu(a,pos+1,high);
      }
    }


    //4、选择类排序
    void paixu_xuanze(int a[]) {
        int len = a.length;
        //循环次数,也是从哪开始找
        for( int i = 0; i < len; i++ ){
            //找到最小的位置，然后进行交换
            int k = i; //默认第一个位置最小
            for(int j = i+1; j < len; j++){
                if (a[k] > a[j])
                    k = j;
            }
            // k和i不一样才需要交换
            if( k != i){
                int temp = a[i];
                a[i] = a[k];
                a[k] = temp;
            }
            String str = Arrays.toString(a);
            System.out.println(str);
        }

    }

    //4、树形排序（选择类）
    void paixu_tree(int a[]) {


    }

    //5、堆形排序（选择类）
    void headmaxheap(int ary[], int parent,int heapSize) //think parent 的含义：开始的父结点；把最大值放在父结点
    {  // heapSize 是堆的长度
        int left = 2*parent+1;//子节点的index
        int right = 2*parent+2;
        int largeIndex = parent;//默认是父结点最大
        if(left < heapSize && ary[largeIndex] < ary[left])
            largeIndex = left;
        if(right < heapSize && ary[largeIndex] < ary[right])
            largeIndex = right;
        //largeIndex 的值为子节点（l/r）数值较大的index
        if (parent != largeIndex)//若默认largeIndex改变 ，否则位置是好的不用交换了
        {
            //父结点与较大子结点交换
            int temp = ary[parent];
            ary[parent] = ary[largeIndex];
            ary[largeIndex] = temp;
            headmaxheap(ary,largeIndex,heapSize); //递归
        }
    }

    void paixu_dui(int arr[]) {
        //创建堆
        for (int i = (arr.length - 1) / 2; i >= 0; i--) {
            //从第一个非叶子结点从下至上，从右至左调整结构
            headmaxheap(arr, i, arr.length);
        }

        //调整堆结构+交换堆顶元素与末尾元素
        for (int i = arr.length - 1; i > 0; i--) {
            //将堆顶元素与末尾元素进行交换
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;

            //重新对堆进行调整
            headmaxheap(arr, 0, i);
        }
    }
    public static void merge(int[] arr, int l, int q, int r) {  //比自己写的好
        /**因为每次切割后左边下标都是（l,q），右边数组的下标是(q+1,r)
         * 所以左边数组的元素个数就是q - l + 1
         * 右边的数组元素个数就是r - q
         * **/
        final int n1 = q-l+1;//切割后左边数组的数据长度
        final int n2 = r-q;//切割后右边数组的数据长度
        /**创建两个新数组将切割后的数组分别放进去，长度加1是为了放置无穷大的数据标志位**/
        final int[] left = new int[n1+1];//加一操作是增加无穷大标志位
        final int[] right = new int[n2+1];//加一操作是增加无穷大标志位
        //两个循环将数据添加至新数组中
        /**左边的数组下标是从l到q**/
        /**遍历左边的数组*/
        for (int i = 0; i < n1; i++) {
            left[i] = arr[l+i];
        }
        for (int i = 0; i < n2; i++) {
            right[i] = arr[q+1+i];
        }

        //将最大的正整数放在两个新数组的最后一位
        left[n1] = Integer.MAX_VALUE;  //这样做避免了坐标一直增加的问题
        right[n2] = Integer.MAX_VALUE;

        int i = 0,j = 0;
        //谁小谁放在前面
        for (int k = l; k <= r; k++) {
            if (left[i]<=right[j]) {
                arr[k] = left[i];
                i = i+1;
            } else {
                arr[k] = right[j];
                j = j+1;
            }
        }
    }
    void Merge(int a[], int l, int z, int r){
        int leftlen = z-l+1;
        int rightlen = r-z;
        int left[] = new int[leftlen];
        int right[] = new int[rightlen];
        //将相应的数据存进去
        for (int i = 0; i <leftlen; i++) {
            left[i] = a[l+i];
        }
        for (int i = 0; i < rightlen; i++) {
            right[i] = a[z+1+i];
        }
        // 根据大小修改a
        int i = 0;
        int j = 0;
        for(int k = l; k <= r ; k++)
            if(i < leftlen && j < rightlen&& left[i] <= right[j] ){
                a[k] = left[i];
                i++;
            }
            else if(i < leftlen && j < rightlen&& left[i] > right[j] ){
                a[k] = right[j];
                j++;
            }
            else if(j == rightlen && i < leftlen ){
                a[k] = left[i];
                i++;
            }
            else if(i == leftlen && i <  rightlen ){
                a[k] = right[j];
                j++;
            }




    }
    //6、归并排序
    void paixu_guibing(int a[], int l, int r) {
        if(l < r){
            int z = (l + r)/2;
            paixu_guibing(a, l, z);
            paixu_guibing(a, z+1, r);
            Merge(a, l, z, r);
            String str = Arrays.toString(a);
            System.out.println(str);
        }

    }










    //解释型语言必须有main函数，并且放在类里
    public static void main(String[] args) {
        int a[] = {4, 3, 7, 9, 0, 2, 1, 6, 5, 8};
        String str = Arrays.toString(a);
        System.out.println(str);
        sort px = new sort();
        int len = a.length;
        // 插入排序
        px.paixu_charu(a);
        // 冒泡排序
        px.paixu_maopao(a);
        // 快速排序
        px.paixu_kuaisu(a,0,len-1);
        // 选择排序
        px.paixu_xuanze(a);
        // 堆排序
        px.paixu_dui(a);
        //归并排序
        px.paixu_guibing(a,0,len-1);//位置不是长度

    }
}

