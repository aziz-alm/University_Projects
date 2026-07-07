# Part C - SQL Assessment (Pine Valley Furniture Company)

Part C of the assignment was delivered as a timed, auto-graded SQL test on Ed against the **Pine Valley Furniture Company (PVFC)** database. Each query was checked against hidden test cases.

> **Result: 4/4 questions passed all test cases.**

## The database

PVFC is a furniture-manufacturer schema: customers and their orders, the products on those orders, the raw materials each product uses, the vendors that supply those materials, and the employees (and their skills) who work across the operation. Table names carry a `_T` suffix (e.g. `Customer_T`).

![PVFC entity–relationship diagram](Pasted%20image%2020260703060835.png)

Tables used in these questions:
- `RawMaterial_T`, `Supplies_T`, `Vendor_T` - materials, per-unit supply prices, and suppliers
- `Employee_T`, `EmployeeSkills_T`, `Skill_T` - employees and their skills

---

## Q1 - Filtering with a subquery *(1 mark)*

**Task**
- Show all materials supplied at a per-unit price above 100 and below 300.
- Return `materialId` (aliased as `materialCode`) and `materialName`.
- Sort by material ID.

```sql
SELECT materialId AS materialCode, materialName
FROM RawMaterial_T
WHERE materialId IN (
    SELECT materialId
    FROM Supplies_T
    WHERE supplyUnitPrice BETWEEN 100 AND 300
);
```

**Approach:** an uncorrelated subquery finds the material IDs with a qualifying supply price; the outer query returns the requested columns for those materials.

![Q1 test cases passed](Pasted%20image%2020260703061103.png)

---

## Q2 - Multi-table join with `GROUP BY … HAVING` *(1 mark)*

**Task**
- Find the employees who have more than one skill.
- Show `employeeName` and `skillDescription`.
- Sort by `employeeName`, then `skillDescription`.

```sql
SELECT employeeName, skillDescription
FROM Employee_T e
JOIN EmployeeSkills_T es ON e.EmployeeID = es.EmployeeID
JOIN Skill_T sk ON es.SkillID = sk.SkillID
WHERE e.EmployeeID IN (
    SELECT EmployeeID
    FROM EmployeeSkills_T
    GROUP BY EmployeeID
    HAVING COUNT(SkillID) > 1
)
ORDER BY e.employeeName, sk.skillDescription;
```

**Approach:** the three-table join resolves each employee's skill descriptions, while the `HAVING COUNT(SkillID) > 1` subquery restricts the result to employees holding more than one skill.

![Q2 test cases passed](Pasted%20image%2020260703061314.png)

---

## Q3 - Derived table for a per-employee count *(1 mark)*

**Task**
- Same as Q2, but also show **the number of skills each employee has**.
- Sort by `employeeName`, then `skillDescription`.

```sql
SELECT employeeName, skillDescription, sk1.count
FROM Employee_T e
JOIN EmployeeSkills_T es ON e.EmployeeID = es.EmployeeID
JOIN Skill_T sk ON es.SkillID = sk.SkillID
JOIN (
    SELECT EmployeeID, COUNT(skillID) AS count
    FROM EmployeeSkills_T
    GROUP BY EmployeeID
    HAVING COUNT(SkillID) > 1
) AS sk1 ON e.employeeID = sk1.EmployeeID
ORDER BY e.employeeName, sk.skillDescription;
```

**Approach:** the skill count is computed once in a derived table (`sk1`) and joined back to the main query, so it both filters the employees *and* exposes the count as a selectable column.

![Q3 test cases passed](Pasted%20image%2020260703061541.png)

---

## Q4 - Cheapest vendor per material *(2 marks)*

**Task**
- For each material, find the cheapest vendor (lowest `supplyUnitPrice` for that material).
- Show material name, vendor name, and supply unit price.
- Sort by material name.

```sql
SELECT m.MaterialName,
       v.VendorName,
       f.minprice AS supplyUnitPrice
FROM Supplies_T s
JOIN Vendor_T v ON s.VendorID = v.VendorID
JOIN RawMaterial_T m ON s.MaterialID = m.MaterialID
JOIN (
    SELECT MaterialID, MIN(SupplyUnitPrice) AS minprice
    FROM Supplies_T
    GROUP BY MaterialID
) f ON s.MaterialID = f.MaterialID
   AND s.SupplyUnitPrice = f.MinPrice
ORDER BY m.MaterialName;
```

**Approach:** a derived table (`f`) computes the minimum supply price per material; joining `Supplies_T` back on both `MaterialID` **and** the matching minimum price isolates the exact vendor offering that price, then the joins resolve the material and vendor names.

![Q4 test cases passed](Pasted%20image%2020260703061711.png)
