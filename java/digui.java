// M个苹果放在N个盘子里
public class digui {

    static int  func (int m,int n){
        if(n>m)
            return func(m,m); //盘子>苹果数时
        if(m == 0)
            return 1;
        if(n == 0)
            return 0;
        return func(m,n-1) + func(m-n, n); //盘子<苹果树时 =有盘子为空的方法+没盘子为空的放法

    }

    public static void main(String[] args) {
       int ans = func(5,5);
       System.out.println(ans);

    }









}
