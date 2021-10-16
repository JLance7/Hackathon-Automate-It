import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.*;

class UserInput
{  
    //Return a boolean after prompting user to enter y/n, yes/no etc.
    public static boolean getyn(String prompt) {
        boolean answer = false;
        boolean done = false;
        while (!done) {
            try {
                System.out.print(prompt);  
                InputStreamReader r=new InputStreamReader(System.in);    
                BufferedReader br=new BufferedReader(r);
                String s= br.readLine();
                //System.out.println(s);
                if (s.compareToIgnoreCase("y") == 0 || s.compareToIgnoreCase("yes") == 0) {
                    //System.out.println("You say yes. ");
                    answer = true;
                    done = true;
                }
                else if (s.compareToIgnoreCase("n") == 0 || s.compareToIgnoreCase("no") == 0) {
                    //System.out.println("You say no. ");
                    answer= false;
                    done = true;
                }
                else {
                    System.out.println("Unable to read");
                }
            } catch (Exception e) {
                System.out.println("Unable to read (" + e + ")");
                done = false;
            }
            
        }
        return answer;
    }

    //Return an int the user is prompted to enter
    public static int getint(String prompt) {
        int answer = 0;
        boolean done = false; 

        while (!done) {
            try {
                InputStreamReader r=new InputStreamReader(System.in);    
                BufferedReader br=new BufferedReader(r);
                System.out.print(prompt);  
                answer = Integer.parseInt(br.readLine()); 
                done = true;
            } catch (Exception e) {
                System.out.println("Unable to read (" + e + ")");
                done = false;
            }
        }
        return answer;
    }
}  