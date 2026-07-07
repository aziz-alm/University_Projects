# Practice SQL Exam 1

Prep questions for the first SQL practice exam - covers basic SELECT, filtering, aggregation, JOINs, and subqueries using the pizza database.

## Database Schema

![Database Schema](../SQL_Imgs/Pasted%20image%2020260703081830.png)

Three main tables: **menu** (pizza, price, country, base), **recipe** (pizza, ingredient, amount), and **items** (ingredient, type). There's also a **menu2014** table with the same structure as menu.

---

## Q1 - LIKE Pattern Matching

> List pizzas with the substring 'i' anywhere within the pizza name.

```sql
SELECT pizza FROM menu WHERE pizza LIKE '%i%'
```

Simple wildcard filter - `%i%` catches 'i' at any position in the name.

![Q1 Result](../SQL_Imgs/Pasted%20image%2020260703081916.png)

---

## Q2 - AVG with Column Alias

> Give the average price of pizzas from each country of origin. Change the column name related to average price to "average".

```sql
SELECT country, AVG(price) average
FROM menu
WHERE country IS NOT NULL
GROUP BY country
```

Filter out NULLs first with WHERE, then group. The alias `average` renames the computed column.

![Q2 Result](../SQL_Imgs/Pasted%20image%2020260703082011.png)

---

## Q3 - HAVING with COUNT

> Give the average price of pizzas from each country of origin, do not list countries with only one pizza.

```sql
SELECT country, AVG(price)
FROM menu
WHERE country IS NOT NULL
GROUP BY country
HAVING COUNT(*) > 1
```

HAVING filters *after* grouping - so we can exclude countries that only have a single pizza entry.

![Q3 Result](../SQL_Imgs/Pasted%20image%2020260703082109.png)

---

## Q4 - JOIN (No Subquery)

> List all ingredients and their types for the 'margarita' pizza. Do not use a subquery.

```sql
SELECT r.ingredient, i.type
FROM recipe r
JOIN items i ON r.ingredient = i.ingredient
WHERE r.pizza = 'margarita'
```

Straightforward join between recipe and items on the ingredient column, filtered to margarita only.

![Q4 Result](../SQL_Imgs/Pasted%20image%2020260703082156.png)

---

## Q5 - Subquery with MAX

> Give pizzas and prices for pizzas that are more expensive than all Italian pizzas.

```sql
SELECT m.pizza, m.price
FROM menu m
WHERE m.price > (SELECT MAX(price) FROM menu m1 WHERE m1.country = 'italy')
```

"More expensive than ALL Italian pizzas" means the price has to beat the max Italian price - hence `MAX()` in the subquery.

![Q5 Result](../SQL_Imgs/Pasted%20image%2020260703082244.png)

---

## Q6 - Subquery for Same-Country Lookup

> Give all pizzas that originate from the same country as the 'siciliano' pizza. Do not include 'siciliano' pizza in your result table. Sort your results based on pizza.

```sql
SELECT pizza
FROM menu
WHERE country = (SELECT country FROM menu WHERE pizza = 'siciliano')
  AND pizza != 'siciliano'
ORDER BY pizza
```

The subquery grabs siciliano's country, then the outer query finds all other pizzas from that country.

![Q6 Result](../SQL_Imgs/Pasted%20image%2020260703082335.png)

---

## Q7 - Correlated Subquery / Self-Join for Max per Group

> List each ingredient and the pizza that contains the largest amount of this ingredient.

```sql
SELECT r1.ingredient, pizza, mm amount
FROM recipe r2
JOIN (
    SELECT r1.ingredient, MAX(r1.amount) mm
    FROM recipe r1
    GROUP BY ingredient
) r1 ON r1.ingredient = r2.ingredient AND r1.mm = r2.amount
```

The inner query finds the max amount per ingredient, then we join back to recipe to get the pizza name that matches that max.

![Q7 Result](../SQL_Imgs/Pasted%20image%2020260703082419.png)
