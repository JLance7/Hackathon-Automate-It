
//To run in command line, cd to the folder with this file, enter 'javac Main.java', then 'java Main'

import java.lang.Math;

class Main
{  
    public static int dailyCheckQs(String stuff) {
        int score = 0;
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
        return score;
    }

    public static int initialCheckQs(String stuff) {
        //Gives a rating 0~ 200 (30+60+11i+30+20)
        int score = 0;
        int i = UserInput.getint("How many times a day do you usually think of using " + stuff + "? (Enter number): ");
        i = (int) (10*Math.log10(i)+2.0); //logarithmic so incidents after already many incidents matter less
        if (i < 0) i = 0; if (i > 30) i = 30;
        score += i;
        
        boolean b = UserInput.getyn("Do you give in to " + stuff + " most days? (Enter Yes or No): ");
        if (b == true) {
            score += 60;
            i = UserInput.getint("How many times do you usually use "+stuff+" a day? (Enter number): ");
            if (i < 1) i = 1;
            if (i > 5) i = 5;
            score += 11*i;
        }
        else {
            i = UserInput.getint("How many days do you usually stay off "+stuff+" between incidents? (Enter number from 0-10): ");
            if (i > 60) i = 60;
            score += (60-i);
        }
        b = UserInput.getyn("Do you feel like you have any alternate ways to cope with stress? (Enter Yes or No): ");
        if (b == false)
            score += 30;
        b = UserInput.getyn("Do friends or family complain about your use of " + stuff + "? (Enter Yes or No): ");
        if (b == true)
            score += 30;
        System.out.println("Your initial " + stuff + " severity score is " + score + ".");
        return score;
    }

    public static void main(String[] args)  
    {  
        String stuff = "alcohol";
        //dailyCheckQs(stuff);
        initialCheckQs(stuff);
        
    }  
}  