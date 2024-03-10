# Importing necessary functions from sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Creating a base class
Base = declarative_base()

# Defining the ProductCategory model
class ProductCategory(Base):
    _tablename_ = 'product_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

# Defining the ProductInventory model
class ProductInventory(Base):
    _tablename_ = 'product_inventory'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

# Defining the Discount model
class Discount(Base):
    _tablename_ = 'discount'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    discount_percent = Column(Numeric(5, 2), nullable=False)
    active = Column(Boolean, nullable=False)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

# Defining the Product model
class Product(Base):
    _tablename_ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    SKU = Column(String(255), nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey('product_category.id'), nullable=False)
    inventory_id = Column(Integer, ForeignKey('product_inventory.id'), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    discount_id = Column(Integer, ForeignKey('discount.id'))
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)
    
    # Defining relationships
    category = relationship("ProductCategory")
    inventory = relationship("ProductInventory")
    discount = relationship("Discount")

# Main entry point
if _name_ == '_main_':
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///sqlalchemy_example.db')

    # Create all tables by issuing CREATE TABLE commands to the database.
    Base.metadata.create_all(engine)
