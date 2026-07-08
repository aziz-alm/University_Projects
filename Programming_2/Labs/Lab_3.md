# The task

**Lab 3 – NumberToWords** *(worth 4%)*

Read integers from **0–999** until the user enters `-1`. For each number, print it both **in words** and as a **Roman numeral**. Print `Done` when `-1` is entered. Uses Australian English spelling (e.g. "four", "forty").

**Sample run**

```
Number: 17
In Words: seventeen
In Roman: XVII
Number: 103
In Words: one hundred and three
In Roman: CIII
Number: -1
Done
```


---

# Python Solution 

```Python
def int_to_words(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n == 0: return "zero"
    if n < 10: return units[n]
    if n < 20: return teens[n-10]
    if n < 100: return tens[n//10] + (" " + units[n%10] if n%10 != 0 else "")
    if n < 1000:
        res = units[n//100] + " hundred"
        if n % 100 != 0:
            res += " and " + int_to_words(n % 100) 
        return res

def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syb[i]
            num -= val[i]
    return roman_num
if __name__ == '__main__':
    user_input = input('Number: ')
    number = int(user_input) 
    while number !=-1:
        print('In Words: ' + int_to_words(number))
        print('In Roman: ' + int_to_roman(number))
        user_input = input('Number: ')
        number = int(user_input) 
        
    print('Done')
        
```


# Java Solution

```Java
import java.util.Scanner;

public class NumberToWords {

    private static final String[] units = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    private static final String[] teens = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    private static final String[] tens = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    public static String intToWords(int num) {
        if (num == 0) return "zero";
        
        if (num < 10) return units[num];
        
        if (num < 20) return teens[num - 10];
        
        if (num < 100) {
            // Using the Ternary Operator (?) to decide if we need a space
            return tens[num / 10] + (num % 10 != 0 ? " " + units[num % 10] : "");
        }
        
        if (num < 1000) {
            String res = units[num / 100] + " hundred";
            if (num % 100 != 0) {
                res += " and " + intToWords(num % 100);
            }
            return res;
        }
        
        return "Number too large";
    }

    public static String intToRoman(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < values.length; i++) {
            while (num >= values[i]) {
                sb.append(symbols[i]);
                num -= values[i];
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    while (true) {
        System.out.print("Number: ");
        
        // Check if the input is actually a number
        if (sc.hasNextInt()) {
            int number = sc.nextInt();
            
            // 1. Check for the exit condition first
            if (number == -1) {
                System.out.println("Done");
                break; // This exits the while loop
            }
            
            // 2. Otherwise, process the number
            System.out.println("In Words: " + intToWords(number));
            System.out.println("In Roman: " + intToRoman(number));
            //System.out.println(); // Adds a blank line for readability
            
        } else {
            // If user types "abc", we need to clear the invalid input
            System.out.println("Please enter a valid integer.");
            sc.next(); // Consume the "bad" input to avoid an infinite loop
        }
    }
    
    sc.close();
}
}
```
