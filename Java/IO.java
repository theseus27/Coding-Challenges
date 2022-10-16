import java.io.*;
import java.util.Scanner;

public class IO{
    public static void main(String[] args) throws IOException {
    //INPUT
        //Buffered Reader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String name = br.readLine();
        //Scanner
        Scanner sc = new Scanner(System.in);
        String pokemon = sc.nextLine();

        //Console
        String age = System.console().readLine();

        //Command Line Input
        //String cmd = args[0];
    
    //OUTPUT
        System.out.println(name);
        System.out.println(pokemon);
        System.out.println(age);
    }
}
