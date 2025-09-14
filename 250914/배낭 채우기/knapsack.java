import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] nm=br.readLine().split(" ");
        int n=Integer.parseInt(nm[0]);
        int m=Integer.parseInt(nm[1]);
        int[] w = new int[n+1];
        int[] v = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            String[] line=br.readLine().split(" ");
            w[i] = Integer.parseInt(line[0]);
            v[i] = Integer.parseInt(line[1]);
        }

        //시작
        int[][] dp=new int[n+1][m+1];
        for(int i=1;i<n+1;i++){
            for(int j=1;j<m+1;j++){
                if(j>=w[i]){
                dp[i][j]=Math.max(dp[i-1][j-w[i]]+v[i],dp[i-1][j]);
                }
                else{
                    dp[i][j]=dp[i-1][j];
                }
            }
        }

        System.out.println(dp[n][m]);
       
    }
}