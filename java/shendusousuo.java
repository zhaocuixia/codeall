import java.util.Arrays;
import static sun.swing.MenuItemLayoutHelper.max;

public class shendusousuo {
    //求有多少个连通子图及最大是多少
    static int row = 5;
    static int col = 5;
    static int roomNum  = 0;
    static int maxroomArea  = 0;
    static int roomArea = 0;

    static int [][]rooms = new int [row][col]; //决定往哪走
    static int [][]color = new int [row][col]; //决定能不能走
    static void dfs(int i,int j){
        if(i>=0 && j>=0 && i<row && j<col){ //边界的控制
            if(color[i][j] != 0){
                return;
            }
            color[i][j] = roomNum;
            roomArea++;
            if((rooms[i][j] & 1) == 0){
                dfs(i,j-1); //向西走；
            }
            if((rooms[i][j] & 2) == 0){
                dfs(i-1,j); //向北走；
            }
            if((rooms[i][j] & 4) == 0){
                dfs(i,j+1); //向东走；
            }
            if((rooms[i][j] & 8) == 0){
                dfs(i+1,j); //向南走；
            }
        }

    }
    public static void main(String[] args) { //main 必须是静态的，调用的类中方法也要是静态的或将类实例化再调用
       //        int [ ][ ]arr = new int [60][ ]; //动态创建第一维
       //        for( int i = 0; i < 60; i++){
       //            arr [i] = new int [60];    //动态创建第二维
       //            for(int j=0; j < 60; j++) {
       //                arr [i][j] = j; //赋值了
       //            }
       //        }
       // int [][]arry  = new int [10][10]; //可以直接这样创建
        for( int i = 0; i <5; i++){
            for(int j=0; j < 5; j++) {
                rooms[i][j] = 15; //赋值了1111 表示东南西北都有墙
                color[i][j] = 0;
//              System.out.println(rooms [i][j]);
//              System.out.println(color[i][j]);
            }
        }
        for( int i = 0; i < 5; i++){
            for(int j=0; j < 5; j++) {
                if(color[i][j] == 0){
                    roomNum++; //有多少个区域，并用这个数值对区域进行区分
                    roomArea=0; //区域有多大
                    dfs(i,j);
                    maxroomArea = max(maxroomArea, roomArea); //最大区域的个数
                }
            }
        }

        System.out.println(maxroomArea);
        System.out.println(roomNum);

        for( int i = 0; i < 5; i++){
            for(int j=0; j < 5; j++) {
                System.out.println(rooms [i][j]);
                System.out.println(color[i][j]);
            }
        }
    }



}
