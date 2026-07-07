
![[Pasted image 20260703080258.png]]
# Q1
List all pizzas, giving pizza name, price and country of origin where the country of origin has NOT been recorded (i.e. is missing).

# My answering 

```SQL
select pizza, price, country from menu where country is  null
```
![[Pasted image 20260703080407.png]]


# Q2
Give the most expensive pizza price from each country of origin.

Sort your results by country in ascending order.

# My answer

```SQL
select country, price max from menu m  where price=(select max(price) 
from menu where country=m.country) order by country asc
```

![[Pasted image 20260703080513.png]]

# Q3
Give the average price of pizzas from each country of origin, only list countries with 'i' in the country's name.

Sort your results based on country in ascending order.

# My answer

```SQL
select country ,avg(price) from menu   
where country like '%i%' group by country order by country
```


![[Pasted image 20260703080736.png]]


# Q4 
List all 'fish' ingredients used in pizzas, also list the pizza names. Do not use a subquery.

# My answer

```SQL
select r.ingredient,r.pizza from recipe r 
join items i on r.ingredient=i.ingredient where i.Type='fish'
```
![[Pasted image 20260703080844.png]]



# Q5 
List all ingredients for the Mexican pizza (i.e. country = 'mexico'). You must use a subquery.

# My answer

```SQL
select distinct ingredient from recipe 
where pizza in (select pizza from menu where country= 'mexico')
```

![[Pasted image 20260703080948.png]]


# Q6
List all pizzas that cost more than 'stagiony' pizza, also give their prices. Sort the results based on prices in descending order.

# My answer 

```SQL
select pizza,price from menu where price>
(select price from menu where pizza='stagiony')
```

![[Pasted image 20260703081117.png]]


# Q7 
List ingredients used in more than one pizza.

Sort your results in ascending order.


# My answer

```SQL
select ingredient from recipe group 
by ingredient having count(ingredient)>1 order by ingredient asc
```
![[Pasted image 20260703081212.png]]

