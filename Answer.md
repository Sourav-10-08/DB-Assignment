1. Relationship between "Product" and "Product_Category": The relationship between "Product" and "Product_Category" is a many-to-one relationship. 
This is indicated by the line between the two tables with a '1' on the product_category side and no specific notation on the product side. 
This means that each product entry references one product_category through the category_id foreign key,
but a single product_category can be referenced by many product entries.



2. Ensuring a valid category for each product: To ensure that each product in the "Product" table has a valid category assigned to it,
3. you can set up a few database constraints and checks:Foreign Key Constraint: Implement a foreign key constraint on the category_id field of the product table
4. that references the id of the product_category table.
This ensures that each product's category must exist in the product_category table.
NOT NULL Constraint: Apply a NOT NULL constraint on the category_id field to ensure that every product must have a category assigned.
Referential Integrity Checks: Enforce referential integrity within the database to make sure that any insert, update, or delete operation does not leave a product without a valid category.
