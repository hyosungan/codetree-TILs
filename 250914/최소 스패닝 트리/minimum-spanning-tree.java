import java.io.*;
import java.util.*;

public class Main {
    static int[] uf;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] nm=br.readLine().split(" ");
        int N=Integer.parseInt(nm[0]);
        uf=new int[N+1];  //0번은 안씀
        for (int i = 1; i < N+1; i++) {
            uf[i]=i;
        }
        int M=Integer.parseInt(nm[1]);
        int[][] edges=new int[M][3];
        for (int i = 0; i < M; i++) {
            String[] sew=br.readLine().split(" ");
            edges[i][0]=Integer.parseInt(sew[0]);
            edges[i][1]=Integer.parseInt(sew[1]);
            edges[i][2]=Integer.parseInt(sew[2]);
        }
        int ans=0;
        Arrays.sort(edges, (a,b)->a[2]-b[2]);
        for (int i = 0; i < edges.length; i++) {
            if(find(edges[i][0])!=find(edges[i][1])){
                ans+=edges[i][2];
                union(edges[i][0],edges[i][1]);
            }
        }
        System.out.println(ans);

    }

    static int find(int x){
        if(uf[x]==x) return x;
        int parent=find(uf[x]);
        uf[x]=parent;
        return parent;
    }

    static void union(int x,int y){
        int X=find(x);
        int Y=find(y);
        uf[X]=Y;
    }
}
