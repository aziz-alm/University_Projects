
![[Pasted image 20260703080258.png]]
# Q1
List all price categories recorded in the MENU table, eliminating duplicates.

# My answering 

```SQL
select distinct price from menu
```


![[Pasted image 20260703082701.png]]
# Q2
Give the cheapest pizzas from each country of origin.

Sort your results by country in ascending order.

# My answer

```SQL
select country,min(price) least  from menu 
where country is not null group by country order by country 
```

![[Pasted image 20260703082729.png]]

# Q3
Give cheapest price of pizzas from each country of origin, only list countries with cheapest price of less than $7.00

# My answer

```SQL
select country,min(price) from menu 
where price<7 and country is not null group by country 
```


![[Pasted image 20260703082755.png]]


# Q4 
List all 'meat' ingredients used in pizzas, also list the pizza names. Do not use a subquery.
# My answer

```SQL
select r.ingredient,pizza from recipe r 
inner join items t on r.ingredient=t.ingredient where t.type='meat'
```

![[Pasted image 20260703082823.png]]


# Q5 
List pizzas with at least one 'meat' ingredient.You must use a subquery.
# My answer

```SQL
select pizza from menu where pizza IN 
(select  r.pizza from recipe r join items t on 
r.ingredient=t.ingredient where t.type='meat')order by pizza
```
![[Pasted image 20260703082903.png]]


# Q6
List all pizzas that cost less than 'siciliano' pizza, also give their prices.

# My answer 

```SQL
select pizza, price from menu 
where price<(select price from menu where pizza='siciliano')
```

![[Pasted image 20260703082935.png]]

# Q7 
List the ingredients, and for each ingredient, also list the pizza that contains the largest amount of this ingredient.


# My answer

```SQL
SELECT ingredient, pizza, amount FROM recipe r 
WHERE amount = (SELECT MAX(amount)FROM 
recipe WHERE ingredient = r.ingredient)
```
![[Pasted image 20260703083022.png]]

