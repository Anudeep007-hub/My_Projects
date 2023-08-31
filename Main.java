import java.util.*;

class Grade_Calculator {
    float sum_numerator = 0.0f, sum_denominator = 0.0f;

    public float grade_cal = 0.0f;

    void grade_calculator(int credit, int grade) {

        sum_numerator += credit*grade;
        sum_denominator += credit;
        grade_cal = sum_numerator/sum_denominator;

        System.out.println("Your grade is: " + grade_cal);


    }
}


public class Main {
    public static void main(String[] args) {
        int a, b;
        Scanner scan = new Scanner(System.in);
        Grade_Calculator User = new Grade_Calculator();

        while(true) {
            System.out.print("Enter your course credit:  ");
            a = scan.nextInt();
            System.out.print("Enter your course grade(In numbers):  ");
            b = scan.nextInt();
            User.grade_calculator(a,b);

        }





    }


}