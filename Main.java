// How often are you thinking of using &?
// Are you able to resist the urge to use &?
// Are you neglecting your responsibilities because of &?
// Are friends or family complaining about your use of &?
// Are you able to stop using & whenever you want to?

//To run in command line, cd to the folder with this crap, enter 'javac Main.java', then 'java Main'
import java.lang.Math;

class Main
{  
    

    public static void main(String[] args)  
    {  
        int score = 0;
        String stuff = "alcohol";

        int i = UserInput.getint("How many times have you though of using " + stuff + " today? (Enter number): ");
        i = (int) (10*Math.log10(i)+2.0); //logarithmic so incidents after already many incidents matter less
        if (i < 0) i = 0; // (i practically maxes around ~45)
        score += i;
        
        boolean b = UserInput.getyn("Were you able to resist using " + stuff + " today? (Enter Yes or No): ");
        if (b == false)
            score += 40;
        else {
            i = UserInput.getint("How likely did you feel you were to give into " + stuff + " today? (Enter number from 0-10): ");
            if (i < 0) i = 0;
            if (i > 10) i = 10;
            score += i;
        }
        b = UserInput.getyn("Did you feel like you had any alternate ways to cope with stress? (Enter Yes or No): ");
        if (b == false)
            score += 20;
        b = UserInput.getyn("Did friends or family complained about your use of " + stuff + " today? (Enter Yes or No): ");
        if (b == true)
            score += 20;
        System.out.println("Your " + stuff + " severity check is " + score + ".");
        
    }  
}  