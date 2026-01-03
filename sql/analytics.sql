SELECT
count(order_id) as total_orders,
sum(order_value) as total_orders,
 from fact_sales
group by order date;
order by order date;
