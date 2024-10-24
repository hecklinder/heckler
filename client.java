import java.net.*;
import java.io.*;
import java.util.*;

public class client {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("localhost", 9999);
            System.out.println("Connected to server");

            // Reading input from user
            Scanner sc=new Scanner(System.in);
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());

            String line = "";

            while (!line.equals("exit")) {
                try {
                    // Read user input
                    line = sc.nextLine();
                    // Send to server
                    dout.writeUTF(line);
                    dout.flush();
                } catch (IOException e) {
                    System.out.println(e);
                }
            }

            System.out.println("Closing connection");
            
            dout.close();
            s.close();
        } catch (UnknownHostException u) {
            System.out.println(u);
        } catch (IOException i) {
            System.out.println(i);
        }
    }
}
