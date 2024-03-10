CREATE TABLE product_category (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    desc TEXT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP
);

CREATE TABLE product_inventory (
    id INT PRIMARY KEY,
    quantity INT NOT NULL,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP
);

CREATE TABLE discount (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    desc TEXT,
    discount_percent DECIMAL(5, 2) NOT NULL,
    active BOOLEAN NOT NULL,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP
);

CREATE TABLE product (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    desc TEXT,
    SKU VARCHAR(255) UNIQUE NOT NULL,
    category_id INT NOT NULL,
    inventory_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    discount_id INT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_category (id) ON DELETE SET NULL,
    FOREIGN KEY (inventory_id) REFERENCES product_inventory (id) ON DELETE SET NULL,
    FOREIGN KEY (discount_id) REFERENCES discount (id) ON DELETE SET NULL
);
