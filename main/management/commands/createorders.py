from django.core.management.base import BaseCommand
from main.models import Product, Category, Brand, Salesman, Customer
from order.models import Order, OrderItem
from faker import Faker
import faker.providers
import random


class Command(BaseCommand):
    help = "Generate series of fake data for the project such as random categories, products, customer, orders etc.."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE(f"Generating fake data to play with"))
        fake = Faker()
        
        salesman = Salesman.objects.all()
        salesman_ids = salesman.values_list('id',flat=True)
                
        customer = Customer.objects.all()        
        customer_ids = customer.values_list('id', flat=True)        

        products = Product.objects.all()
        product_ids = products.values_list('id', flat=True)
        
        # GENERATE RANDOM ORDER
        for _ in range(100):
            amount =  round(random.uniform(100.99, 2999.99),2)
            vat_amount = amount * 0.20
            net_amount = amount - vat_amount
            Order.objects.create(   
                order_no = f"23-" + str(fake.unique.pyint()),
                order_date = fake.date(),
                po_no = fake.text(max_nb_chars=5),
                order_amount = amount,
                vat_amount  = vat_amount,
                net_amount  = net_amount,
                salesman_id = random.choice(salesman_ids),
                customer_id = random.choice(customer_ids)
            ) 

        order_count = Order.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Orders: {order_count}"))
        
        # GENERATE RANDOM ORDER ITEMS
        for _ in range(300):
            prod_id = random.choice(product_ids)
            product_obj = Product.objects.get(id=prod_id)
            prod_price = product_obj.price1
            qty = random.randint(1,3)
            discount = random.uniform(0.0, 5.9)
            total = (prod_price * qty) - discount
            
            OrderItem.objects.create(
                order_id = random.randint(1,50),
                product = product_obj,
                price = prod_price,
                quantity = qty,
                discount_amount = discount,
                line_total = total,
            )


