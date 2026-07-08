# The task

**Lab 5 – Classes: Store**

A store sells a single product (`Sticky tape`, starting stock **200**, price **$2.99**) and keeps all takings in a cash register. The clerk drives it with a menu: **sell, restock, view stock, view cash, exit**. Selling is only allowed when there's enough stock. The logic is spread across three classes: `Store`, `Product` and `CashRegister`.

**Sample run**

```
Choice (s/r/v/c/x): v
200 Sticky tape at $2.99
Choice (s/r/v/c/x): s
Number: 10
Choice (s/r/v/c/x): c
Cash register: $29.90
Choice (s/r/v/c/x): x
```


---

# Python Solution

## CashRegister.py
```Python
class CashRegister:
    def __init__(self):
        self.cash = 0.0

    def __str__(self):
        if self.cash == 0:
            return "Cash register: empty"
        else:
            return "Cash register: $" + "{:.2f}".format(self.cash)
```

## Store.py
```Python
from Product import Product
from CashRegister import CashRegister

class Store:
    def __init__(self):
        self.product = Product("Sticky tape", 200, 2.99)
        self.register = CashRegister()

    def use(self):
        choice = input("Choice (s/r/v/c/x): ")
        while choice != "x":
            if choice == "?":
                print("Menu options")
                print("s = sell")
                print("r = restock")
                print("v = view stock")
                print("c = view cash")
                print("x = exit")
            elif choice == "v":
                print(self.product)
            elif choice == "c":
                print(self.register)
            elif choice == "s":
                num = int(input("Number: "))
                if num <= self.product.stock:
                    self.product.stock -= num
                    self.register.cash += num * self.product.price
                else:
                    print("Not enough stock")
            elif choice == "r":
                num = int(input("Number: "))
                self.product.stock += num
            
            choice = input("Choice (s/r/v/c/x): ")

if __name__ == "__main__":
    store = Store()
    store.use()
    
```


## Product.py

```Python
class Product:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    def __str__(self):
        return str(self.stock) + " " + self.name + " at $" + str(self.price)
        
```


# Java Solution 

## In.java
```Java
import java.util.*;
import java.io.*;

/**
 * This class provides static methods for easily reading
 * input from STDIN:
 *
 * nextLine reads a string
 * nextInt reads an integer
 * nextDouble reads a double
 * nextChar reads a character
 *
 * All methods consume the end-of-line character.
 */
public class In {
	/**
	 * A singleton instance of Scanner used for reading all input
	 * from STDIN.
	 */
	private static final Scanner scanner;
	
    static {
		try {
    	    File inputFile = new File("/home/Input.txt");
    	    if (inputFile.length() > 1) { 
    	        System.setIn(new FileInputStream(inputFile));
    	    }
    	    scanner = new Scanner(System.in);
    	} catch (FileNotFoundException e) {
    	    throw new RuntimeException(e);
    	}
	}

	/**
	 * The constructor is private because no instances of this
	 * class should be created. All methods are static and can
	 * be directly invoked on the class itself.
	 */
	private In() {}

	/**
	 * Read the next line of text.
	 *
	 * @return the line as a String
	 */
	public static String nextLine() {
		return scanner.nextLine();
	}

	/**
	 * Read the next line as an integer.
	 *
	 * @return the integer that was read
	 */
	public static int nextInt() {
		int value = scanner.nextInt();
		scanner.nextLine(); // read the "\n" as well
		return value;
	}

	/**
	 * Read the next line as a double.
	 *
	 * @return the double that was read
	 */
	public static double nextDouble() {
		double value = scanner.nextDouble();
		scanner.nextLine();
		return value;
	}

	/**
	 * Read the first character of the next line of text.
	 *
	 * @return the character that was read
	 */
	public static char nextChar() {
		return scanner.nextLine().charAt(0);
	}
}
```
## Store.java

```Java
public class Store {
    private Product product;
    private CashRegister register;

    public static void main(String[] args) {
        Store store = new Store();
        store.use();
    }

    public Store() {
        this.product = new Product("Sticky tape", 200, 2.99);
        this.register = new CashRegister();
    }

    public void use() {
        char choice;
        System.out.print("Choice (s/r/v/c/x): ");
        while ((choice = In.nextChar()) != 'x') {
            if (choice == 's') {
                sell();
            } else if (choice == 'r') {
                restock();
            } else if (choice == 'v') {
                viewStock();
            } else if (choice == 'c') {
                viewCash();
            } else if (choice == '?') {
                help();
            }
            System.out.print("Choice (s/r/v/c/x): ");
        }
    }

    private void sell() {
        System.out.print("Number: ");
        int amount = In.nextInt();
        if (amount <= product.getStock()) {
            double money = product.sell(amount);
            register.add(money);
        } else {
            System.out.println("Not enough stock");
        }
    }

    private void restock() {
        System.out.print("Number: ");
        int amount = In.nextInt();
        product.restock(amount);
    }

    private void viewStock() {
        System.out.println(product);
    }

    private void viewCash() {
        System.out.println(register);
    }

    private void help() {
        System.out.println("Menu options");
        System.out.println("s = sell");
        System.out.println("r = restock");
        System.out.println("v = view stock");
        System.out.println("c = view cash");
        System.out.println("x = exit");
    }
}
```

## Product.java

```Java
import java.text.*;

public class Product {
    private String name;
    private int stock;
    private double price;

    public Product(String name, int stock, double price) {
        this.name = name;
        this.stock = stock;
        this.price = price;
    }

    public int getStock() {
        return stock;
    }

    public double sell(int n) {
        this.stock -= n;
        return n * this.price;
    }

    public void restock(int n) {
        this.stock += n;
    }

    @Override
    public String toString() {
        return this.stock + " " + this.name + " at $" + String.format("%.2f", this.price);
    }
}

```

## CashRegister.java

```Java
import java.text.*;

public class CashRegister {
    private double cash;

    public CashRegister() {
        this.cash = 0.0;
    }

    public void add(double amount) {
        this.cash += amount;
    }

    @Override
    public String toString() {
        if (this.cash == 0) {
            return "Cash register: empty";
        }
        return "Cash register: $" + String.format("%.2f", this.cash);
    }
}
```