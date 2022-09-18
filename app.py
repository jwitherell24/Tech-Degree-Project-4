from models import (Base, session, 
                    Product, engine)
import datetime
import csv 
import time


def menu():
    while True:
        print("""
              \nKINGMA'S MARKET INVENTORY
              \r1) View product details (Press 'v' and 'enter')
              \r2) Add a new product (Press 'a' and 'enter')
              \r3) Make a backup of database (Press 'b' and 'enter')""")
        choice = input("What would you like to do?  ")


def clean_price(price_str):
    try:
        price_float = float((price_str).split("$")[1])
    except ValueError:
        input("""
              \n****** PRICE ERROR ******
              \rThe price should be a number without a currency symbol.
              \rEx. 10.99
              \rPress enter to try again.
              ***************************""")
    else:
        return int(price_float * 100)


def clean_date(date_str):
    split_date = date_str.split("/")
    try:
        month = int(split_date[0])
        day = int(split_date[1])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except ValueError:
        input("""
              \n****** DATE ERROR ******
              \rThe date format should include a valid Month/Day/Year (M/D/YYYY) from the past
              \rEx. 3/15/2022
              \rPress enter to try again.
              ***************************""")
        return
    else:
        return return_date
    
    

def add_csv():
    with open("inventory.csv") as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            product_in_db = session.query(Product).filter(Product.product_name==row[0]).one_or_none()
            if product_in_db == None:
                name = row[0]
                price = clean_price(row[1])
                quantity = row[2]
                date = clean_date(row[3])
                new_book = Product(product_name=name, product_price=price, product_quantity=quantity, date_updated=date)
                session.add(new_book)
        session.commit()
                   

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # add_csv()
    # app()