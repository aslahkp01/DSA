# Write your MySQL query statement below
SELECT eu.unique_id,e.name
FROM Employees e LEFT JOIN employeeUNI eu ON e.id=eu.id

