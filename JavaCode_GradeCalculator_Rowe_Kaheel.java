import javax.swing.JOptionPane;

/**
 * StudentGradeCalculator
 * A simple GUI program that asks for a student's name and three grades,
 * calculates the average, and displays the result using JOptionPane.
 */
public class StudentGradeCalculator {

    /**
     * Main method that runs the program.
     * @param args command-line arguments
     */
    public static void main(String[] args) {
        // Ask for student's name
        String studentName = JOptionPane.showInputDialog(null, "Enter student's name:");

        // Ask for three grades
        String grade1Str = JOptionPane.showInputDialog(null, "Enter first grade:");
        String grade2Str = JOptionPane.showInputDialog(null, "Enter second grade:");
        String grade3Str = JOptionPane.showInputDialog(null, "Enter third grade:");

        // Convert to numbers
        double grade1 = Double.parseDouble(grade1Str);
        double grade2 = Double.parseDouble(grade2Str);
        double grade3 = Double.parseDouble(grade3Str);

        // Calculate average
        double average = (grade1 + grade2 + grade3) / 3.0;

        // Determine letter grade
        String letterGrade;
        if (average >= 90) {
            letterGrade = "A";
        } else if (average >= 80) {
            letterGrade = "B";
        } else if (average >= 70) {
            letterGrade = "C";
        } else if (average >= 60) {
            letterGrade = "D";
        } else {
            letterGrade = "F";
        }

        // Display results
        String message = "Student: " + studentName
                + "\nGrades: " + grade1 + ", " + grade2 + ", " + grade3
                + "\nAverage: " + String.format("%.2f", average)
                + "\nFinal Letter Grade: " + letterGrade;

        JOptionPane.showMessageDialog(null, message);
    }
}