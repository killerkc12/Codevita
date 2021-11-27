package faceprep;

/*

Constellation
Three characters { #, *, . } represents a constellation of stars and galaxies in space. Each galaxy is demarcated by # characters. There can be one or many stars in a given galaxy. Stars can only be in the shape of vowels { A, E, I, O, U }. A collection of * in the shape of the vowels is a star. A star is contained in a 3x3 block. Stars cannot be overlapping. The dot(.) character denotes empty space.
Given 3xN matrix comprising of { #, *, . } character, find the galaxy and stars within them.
Note: Please pay attention to how vowel A is denoted in a 3x3 block in the examples section below.

Constraints
3 <= N <= 10^5
Input
Input consists of a single integer N denoting the number of columns.
Output
The output contains vowels (stars) in order of their occurrence within the given galaxy. The galaxy itself is represented by the # character.

Example 1
Input
18
* . * # * * * # * * * # * * * . * .
* . * # * . * # . * . # * * * * * *
* * * # * * * # * * * # * * * * . *
Output
U#O#I#EA
Explanation
As it can be seen that the stars make the image of the alphabets U, O, I, E, and A respectively.

Example 2
Input
12
* . * # . * * * # . * .
* . * # . . * . # * * *
* * * # . * * * # * . *
Output
U#I#A
Explanation
As it can be seen that the stars make the image of the alphabet U, I, and A.

Possible solution:
Input:
12
* . * # . * * * # . * .
* . * # . . * . # * * *
* * * # . * * * # * . *

 */

public class Q1 {

    public static void main(String[] args) {
	// write your code here

        char[][] ch = {
                {'*', '.', '*', '#', '.', '*', '*', '*', '#', '.', '*', '.'},
                {'*', '.', '*', '#', '.', '.', '*', '.', '#', '*', '*', '*'},
                {'*', '*', '*', '#', '.', '*', '*', '*', '#', '*', '.', '*'}
        };

        find(ch, ch[0].length);
    }

    private static void find(char[][] ch, int length) {
        for (int i=0; i<length;) {
            // checking for #
            if (ch[0][i] == '#') {
                System.out.println('#');
                i++; continue;
            }
            // checking for . operator
            else if (ch[0][i] == '.' && ch[1][i] == '.' && ch[2][i] == '.') {
                i++;
            }
            // checking for A
            else if (ch[0][i] == '.' && ch[0][i+2] == '.' && ch[2][i+1] == '.') {
                System.out.println('A');
                i += 3;
            }
            // checking for U and O
            else if (ch[1][i+1] == '.') {
                // checking for U
                if (ch[0][i+1] == '.'){
                    System.out.println('U');
                    i +=3;
                }
                else {
                    System.out.println('O');
                    i += 3;
                }
            }
            // checking for I
            else if (ch[1][i] == '.' && ch[1][i+2] == '.') {
                System.out.println('I');
                i += 3;
            }
            // by default it is E
            else {
                System.out.println('E');
                i += 3;
            }
        }
    }
}
