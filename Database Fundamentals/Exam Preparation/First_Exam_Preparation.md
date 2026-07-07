
![[Pasted image 20260703081830.png]]

# Q1
List pizzas with the substring 'i' anywhere within the pizza name.
# My asnwer
```SQL
select pizza from menu where pizza like '%i%'
```

![[Pasted image 20260703081916.png]]

# Q2
Give the average price of pizzas from each country of origin.

Change the column name related to average price to "average".

# My answer
``
```SQL
select country, AVG(PRICE) average from menu 
WHERE country IS NOT NULL group by country
```
![[Pasted image 20260703082011.png]]

# Q3 
Give the average price of pizzas from each country of origin, do not list countries with only one pizza.
# My answer
```SQL
select country, AVG(PRICE) from menu 
where country is not null Group by country having count(*)>1
```

![[Pasted image 20260703082109.png]]

# Q4
List all ingredients and their types for the 'margarita' pizza. Do not use a subquery.

# My answer 
```SQL
select r.ingredient, i.type from recipe r 
join items i on r.ingredient=i.ingredient where r.pizza='margarita'
```
![[Pasted image 20260703082156.png]]

# Q5
Give pizzas and prices for pizzas that are more expensive than all Italian pizzas.

# My answer 
```SQL
select m.pizza, m.price from menu m 
where m.price>(select max(price) from menu m1 where m1.country='italy')
```

![[Pasted image 20260703082244.png]]

# Q6 
Give all pizzas that originate from the same country as the 'siciliano' pizza.

Do not include 'siciliano' pizza in your result table.

Sort your results based on pizza.

# My answer
```SQL
select pizza from menu where country=(select country from 
menu where pizza='siciliano') and pizza!='siciliano'  order by pizza
```
![[Pasted image 20260703082335.png]]

# Q7
List each ingredient and the pizza that contains the largest amount of this ingredient.
# My answer
```SQL
select r1.ingredient, pizza, mm amount  from recipe r2 join 
(select r1.ingredient, max(r1.amount) mm from recipe r1 
group by ingredient) r1 on r1.ingredient=r2.ingredient and r1.mm=r2.amount
```
![[Pasted image 20260703082419.png]]
