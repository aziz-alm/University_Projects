# Practice SQL Exam 3

Third round of SQL practice - covers DISTINCT, MIN aggregation, HAVING with conditions, JOINs, subqueries with IN, and correlated subqueries.

## Database Schema

![Database Schema](../SQL_Imgs/Pasted%20image%2020260703080258.png)

Same pizza database: **menu**, **recipe**, **items**, and **menu2014**.

---

## Q1 - DISTINCT

> List all price categories recorded in the MENU table, eliminating duplicates.

```sql
SELECT DISTINCT price FROM menu
```

DISTINCT removes duplicate price values - gives us every unique price point in the table.

![Q1 Result](../SQL_Imgs/Pasted%20image%2020260703082701.png)

---

## Q2 - MIN with GROUP BY

> Give the cheapest pizzas from each country of origin. Sort your results by country in ascending order.

```sql
SELECT country, MIN(price) least
FROM menu
WHERE country IS NOT NULL
GROUP BY country
ORDER BY country
```

Filter out NULLs first, group by country, then grab the minimum price from each group.

![Q2 Result](../SQL_Imgs/Pasted%20image%2020260703082729.png)

---

## Q3 - WHERE Filter Before Grouping

> Give cheapest price of pizzas from each country of origin, only list countries with cheapest price of less than $7.00.

```sql
SELECT country, MIN(price)
FROM menu
WHERE price < 7 AND country IS NOT NULL
GROUP BY country
```

The WHERE clause filters individual rows with price under 7 before grouping. This effectively ensures each group's min is below $7.

![Q3 Result](../SQL_Imgs/Pasted%20image%2020260703082755.png)

---

## Q4 - JOIN with Type Filter (No Subquery)

> List all 'meat' ingredients used in pizzas, also list the pizza names. Do not use a subquery.

```sql
SELECT r.ingredient, pizza
FROM recipe r
INNER JOIN items t ON r.ingredient = t.ingredient
WHERE t.type = 'meat'
```

Join recipe to items on the ingredient column, then filter by type = 'meat'.

![Q4 Result](../SQL_Imgs/Pasted%20image%2020260703082823.png)

---

## Q5 - Subquery with IN + JOIN

> List pizzas with at least one 'meat' ingredient. You must use a subquery.

```sql
SELECT pizza
FROM menu
WHERE pizza IN (
    SELECT r.pizza
    FROM recipe r
    JOIN items t ON r.ingredient = t.ingredient
    WHERE t.type = 'meat'
)
ORDER BY pizza
```

The subquery finds all pizzas that have at least one meat ingredient (via the join), and the outer query matches those against the menu table.

![Q5 Result](../SQL_Imgs/Pasted%20image%2020260703082903.png)

---

## Q6 - Scalar Subquery Comparison

> List all pizzas that cost less than 'siciliano' pizza, also give their prices.

```sql
SELECT pizza, price
FROM menu
WHERE price < (SELECT price FROM menu WHERE pizza = 'siciliano')
```

Subquery returns siciliano's price, outer query grabs everything cheaper.

![Q6 Result](../SQL_Imgs/Pasted%20image%2020260703082935.png)

---

## Q7 - Correlated Subquery for Max per Group

> List the ingredients, and for each ingredient, also list the pizza that contains the largest amount of this ingredient.

```sql
SELECT ingredient, pizza, amount
FROM recipe r
WHERE amount = (
    SELECT MAX(amount)
    FROM recipe
    WHERE ingredient = r.ingredient
)
```

For each row, the correlated subquery checks if that row's amount is the max for its ingredient. Only rows where it matches get returned.

![Q7 Result](../SQL_Imgs/Pasted%20image%2020260703083022.png)
