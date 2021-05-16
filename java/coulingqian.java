import static java.lang.Math.min;

public class dongtaiguihua {


    static int dp1(int[] coins, int n) {
        //base case
        if (n == 0) return 0;
        if (n < 0) return -1;
        //求最小值，所以初始化为正无穷
        int res = 1000000000;
        for (int i = 0; i < coins.length; i++) {

            int subproblem = 1 + dp1(coins, n - coins[i]);
            if (subproblem == 0) //think,dp=-1
                continue;
            res = min(res, 1 + subproblem);

        }
        if (res != 1000000000)  //不知道这个程序有什么问题呢？，这里没有return 造成的，一开始将这个写在for循环里面了
            return res;
        else
            return -1;

    } //看了下原因，for循环里写return编译器不承认，因为不一定会执行

    static int[] memo = new int[1000];
    //# 带备忘录的递归
    static int dp2(int[] coins, int n) {
        //base case
        if (n == 0) return 0;
        if (n < 0) return -1;
        if (memo[n] != 0)
            return memo[n];
        //求最小值，所以初始化为正无穷
        int res = 1000000000;
        for (int i = 0; i < coins.length; i++) {

            int subproblem = 1 + dp2(coins, n - coins[i]);
            if (subproblem == 0)
                continue;
            res = min(res, 1 + subproblem);

        }
        memo[n] = res;
        if (memo[n] != 1000000000)  //不知道这个程序有什么问题呢？，这里没有return 造成的，一开始将这个写在for循环里面
            return memo[n];
        else  //必须有else，否则条件不满足没有return
            return -1;

    } //看了下原因，for循环里写return编译器不承认，因为不一定会执行


    int coinChange(int []coins, int amount) {
        // 数组大小为 amount + 1，初始值也为 amount + 1
        int []dp = new int [amount + 1];
        for (int i =0; i < dp.length; i++)
            dp[i] = amount+1;

        // base case
        dp[0] = 0;
        // 外层 for 循环在遍历所有状态的所有取值
        for (int i = 0; i < dp.length; i++) {//由小到大
            // 内层 for 循环在求所有选择的最小值
            for (int coin : coins) {
                // 子问题无解，跳过
                if (i - coin < 0) continue;
                dp[i] = min(dp[i], 1 + dp[i - coin]); //找某个钱数张数最小的
            }
        }
        return (dp[amount] == amount + 1) ? -1 : dp[amount];
    }








    public static void main(String[] args) {
        int [] coins = {1,5,10,20,100};
        int ans = dp1(coins,251);
        System.out.print(ans);
    }





}
