import java.net.*;
import java.io.*;
class serv
{
public static void main(String args[])
{
	
	try
	{ServerSocket ss=new ServerSocket(9999);
	
	Socket s=ss.accept();
	System.out.println("connnected");
	DataInputStream di =new DataInputStream(s.getInputStream());
	String text="";
	while(!text.equals("exit"))
	{
	
	
	text=di.readUTF();
	System.out.println(text);

	}
	
	di.close();
	s.close();
	}
	catch(IOException e)
	{
		
	}
	
	
}

}