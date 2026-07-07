# Practice SQL Exam 2

Second set of practice SQL questions - more work with NULLs, correlated subqueries, JOINs with type filtering, and GROUP BY with HAVING.

## Database Schema

![Database Schema](../SQL_Imgs/Pasted%20image%2020260703080258.png)

Same pizza database: **menu**, **recipe**, **items**, and **menu2014**.

---

## Q1 - IS NULL

> List all pizzas, giving pizza name, price and country of origin where the country of origin has NOT been recorded (i.e. is missing).

```sql
SELECT pizza, price, country
FROM menu
WHERE country IS NULL
```

Can't use `= NULL` here - NULL isn't a value, so you need `IS NULL`.

![Q1 Result](../SQL_Imgs/Pasted%20image%2020260703080407.png)

---

## Q2 - Correlated Subquery for Max per Group

> Give the most expensive pizza price from each country of origin. Sort your results by country in ascending order.

```sql
SELECT country, price max
FROM menu m
WHERE price = (SELECT MAX(price) FROM menu WHERE country = m.country)
ORDER BY country ASC
```

The correlated subquery finds the max price for the same country as the outer row. This returns actual rows (not just the aggregate), so you get the country paired with the max price.

![Q2 Result](../SQL_Imgs/Pasted%20image%2020260703080513.png)

---

## Q3 - LIKE + GROUP BY + ORDER BY

> Give the average price of pizzas from each country of origin, only list countries with 'i' in the country's name. Sort your results based on country in ascending order.

```sql
SELECT country, AVG(price)
FROM menu
WHERE country LIKE '%i%'
GROUP BY country
ORDER BY country
```

The WHERE with LIKE filters countries before grouping - only countries containing 'i' make it through.

![Q3 Result](../SQL_Imgs/Pasted%20image%2020260703080736.png)

---

## Q4 - JOIN with Type Filter (No Subquery)

> List all 'fish' ingredients used in pizzas, also list the pizza names. Do not use a subquery.

```sql
SELECT r.ingredient, r.pizza
FROM recipe r
JOIN items i ON r.ingredient = i.ingredient
WHERE i.type = 'fish'
```

Join recipe to items to get the type, then filter for fish.

![Q4 Result](../SQL_Imgs/Pasted%20image%2020260703080844.png)

---

## Q5 - Subquery with IN

> List all ingredients for the Mexican pizza (i.e. country = 'mexico'). You must use a subquery.

```sql
SELECT DISTINCT ingredient
FROM recipe
WHERE pizza IN (SELECT pizza FROM menu WHERE country = 'mexico')
```

The subquery grabs all Mexican pizzas from menu, then the outer query pulls their ingredients from recipe. DISTINCT avoids duplicates if any ingredient appears in multiple Mexican pizzas.

![Q5 Result](../SQL_Imgs/Pasted%20image%2020260703080948.png)

---

## Q6 - Scalar Subquery Comparison

> List all pizzas that cost more than 'stagiony' pizza, also give their prices. Sort the results based on prices in descending order.

```sql
SELECT pizza, price
FROM menu
WHERE price > (SELECT price FROM menu WHERE pizza = 'stagiony')
```

The subquery returns stagiony's price as a single value, and we compare everything else against it.

![Q6 Result](../SQL_Imgs/Pasted%20image%2020260703081117.png)

---

## Q7 - GROUP BY + HAVING for Shared Ingredients

> List ingredients used in more than one pizza. Sort your results in ascending order.

```sql
SELECT ingredient
FROM recipe
GROUP BY ingredient
HAVING COUNT(ingredient) > 1
ORDER BY ingredient ASC
```

Group by ingredient then use HAVING to keep only those appearing in more than one pizza.

![Q7 Result](../SQL_Imgs/Pasted%20image%2020260703081212.png)
