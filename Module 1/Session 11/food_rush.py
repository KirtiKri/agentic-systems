import sqlite3
conn = sqlite3.connect('foodrush.db')
cursor = conn.cursor()
#TASK 1: Restaurant Revenue Report 
print("TASK 1: RESTAURANT REVENUE REPORT")
print("="*50)

query1 = """
SELECT 
    r.restaurant_name, 
    COUNT(o.order_id) AS delivered_orders, 
    SUM(o.order_amount) AS total_revenue
FROM restaurants r
JOIN orders o ON r.restaurant_id = o.restaurant_id
WHERE o.status = 'delivered'
GROUP BY r.restaurant_name
HAVING delivered_orders > 2
ORDER BY total_revenue DESC;
"""


cursor.execute(query1)
results = cursor.fetchall()

print(f"{'Restaurant Name':<20} | {'Orders':<10} | {'Total Revenue':<15}")
print("-" * 50)
for row in results:
    name, orders, revenue = row
    print(f"{name:<20} | {orders:<10} | ₹{revenue:<14.2f}")


print("\n" + "="*40 + "\nTASK 2: CUSTOMER ACTIVITY\n" + "="*40)


query2 = """
SELECT 
    c.customer_name, 
    c.city, 
    COUNT(o.order_id) AS total_orders, 
    IFNULL(SUM(o.order_amount), 0.0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;
"""
cursor.execute(query2)
for row in cursor.fetchall():
    print(f"Customer: {row[0]:<15} | City: {row[1]:<10} | Orders: {row[2]} | Spent: ₹{row[3]}")

# --- TASK 3: DELHI HIGH-SPENDERS ---
print("TASK 3: DELHI LOYALTY CAMPAIGN (HIGH-SPENDERS)")
print("="*50)

query3 = """
SELECT 
    c.customer_name, 
    COUNT(o.order_id) AS total_orders, 
    SUM(o.order_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.city = 'Delhi'
GROUP BY c.customer_name
HAVING total_orders > 1 AND total_spent > 1000
ORDER BY total_spent DESC;
"""

cursor.execute(query3)
results = cursor.fetchall()

# Print Header
print(f"{'Customer Name':<20} | {'Orders':<10} | {'Total Spend':<15}")
print("-" * 50)

# Print Rows
if not results:
    print("No customers in Delhi meet these criteria.")
else:
    for row in results:
        # row[0] = name, row[1] = count, row[2] = sum
        print(f"{row[0]:<20} | {row[1]:<10} | ₹{row[2]:<14.2f}")

        
# TASK 4: MULTI-TABLE BREAKDOWN
print("\n" + "="*40 + "\nTASK 4: DETAILED SPEND BREAKDOWN\n" + "="*40)
query4 = """
SELECT 
    c.customer_name, 
    r.restaurant_name, 
    COUNT(o.order_id) AS orders_at_restaurant, 
    SUM(o.order_amount) AS total_spent_at_restaurant
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY c.customer_name, r.restaurant_name
HAVING total_spent_at_restaurant > 500
ORDER BY c.customer_name ASC, total_spent_at_restaurant DESC;
"""
cursor.execute(query4)
for row in cursor.fetchall():
    print(f"{row[0]} spent ₹{row[3]} at {row[1]}")
# --- IMPORTANT: CLOSE THE CONNECTION AT THE VERY END OF YOUR FILE ---
conn.close()