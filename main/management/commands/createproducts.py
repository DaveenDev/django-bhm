from django.core.management.base import BaseCommand
from inventory.models import Product, Category, Supplier,InvLocation,Inventory, Unit
from faker import Faker
import faker.providers
import random

CATEGORIES = [
    'ALTERNATOR',
    'ANTENNA',
    'AUTO CLIPS',
    'AXLE BOOTS',
    'BALL JOINT',
    'BATTERY',
    'BEARING',
    'BELL CRANK ASSY',
    'BRAKE FLUID',
    'BRAKES',
    'CALIPER',
    'CAP',
    'CARBURETOR'
]

BRANDS = [
    'ARROW',
    'BANDAI',
    'BOZEN',
    'CHITAS',
    'CRYSTAL'
]

UNITS = [
    'PC'
]

LOCATIONS = [
    'Default',
    'Supplier Warehouse'    
]

BINRACK = ['A1','A2','B1','B2','C1','D1',]

PRODUCTS = [
    'BELL CRANK ASSY',
    'BATTERY-LM INDONESIA',
    'CALIPER CLIP-SUZUKI',
    'CARB.ASSY-78MM BASE',
    'DIST.CAP-CLIP TYPE',
    'ENGINE VALVE-INT-SUZUKI(3/SET)',
    'OIL FILTER(PRIM)ME014833',
    'FUEL PUMP-ELECT 12V C-TYPE',
    'CYL HEAD GASKET-SUZUKI',
    'VALVE COVER GASKET W/O EARS',
    'VALVE COVER GASKET',
    'AUTO BULB 12V 1C-BIG',
    'TAIL LIGHT ASSY 12V',
    'BEARING-TAPERED ROLLER',
    'PISTON SET STD-SUZUKI',
    'PISTON RING 0.75-SUZUKI',
    'TIE ROD END INN MB564853',
    'VALVE SPRING-OUTSIDE',
    'STRUT BAR BUSH B2200/E2200',
    'SOLENOID SW 12V SS1682 F5A NM',
    'TEMP SENDER-SUZUKI BIG',
    'WATER PUMP BEARING',
    'WH.CYL.ASSY 15/16"FNT/LH/LOW',
    'B/M ASSY 3/4"W/O RES',
    'PISTON RING 0.50 THIN-SUZUKI',
    'SUSP ARM ASSY-RH4X2 50FAR',
    'STEERING COUPLING W/JOINT',
    'TENSIONER BRG-SUZUKI',
    'VALVE GUIDE-INT/EXH(6/SET)',
    'WH.CYL PISTON 7/8"FNT"',
    'WATER PUMP SEAL KIT'
]

class CustomProvider(faker.providers.BaseProvider):
    def getRandomCategory(self):
        return self.random_element(CATEGORIES)
    
    def getRandomBrand(self):
        return self.random_element(BRANDS)
    
    def getRandomUnit(self):
        return self.random_element(UNITS)
    
    def getRandomProduct(self):
        return self.random_element(PRODUCTS)
    
    def getRandomLocation(self):
        return self.random_element(LOCATIONS)
    
    def getRandomBINRACK(self):
        return self.random_element(BINRACK)

class Command(BaseCommand):
    help = "Generate series of fake data for the project such as random categories, products, customer, orders etc.."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(f"Generating fake data to play with"))
        fake = Faker()
        fake.add_provider(CustomProvider)

        suppliers = Supplier.objects.all()
        suppliers_ids = suppliers.values_list('id', flat=True)
        
        locations = InvLocation.objects.all()
        locations_ids = locations.values_list('id', flat=True)

        categories = Category.objects.all()
        category_ids = categories.values_list('id', flat=True)        

        # GENERATE RANDOM PRODUCT
        prodid = 1
        for _ in range(20000):
            prod_code = fake.bothify('###', letters='ABCDE') + str(prodid)
            Product.objects.create(
                sku = prod_code,
                name = fake.getRandomProduct(),                
                unit = fake.getRandomUnit(),
                retail_price = round(random.uniform(100.99, 2999.99),2),
                purchased_price = round(random.uniform(100.99, 2999.99),2),
                tax = 20,
                brand = fake.getRandomBrand(),
                category_id= random.choice(category_ids),
                supplier_id= random.choice(suppliers_ids)
            )
            prodid += 1

        products = Product.objects.all()
        product_count = products.count()
        product_ids = products.values_list('id', flat=True)
        self.stdout.write(self.style.SUCCESS(f"Number of Products: {product_count}"))

        # GENERATE PRODUCT the STOCK LEVELS
        for id in product_ids:            
            Inventory.objects.create(
                product_id = id,
                stock_level = random.randint(1,10),
                bin_rack = fake.getRandomBINRACK(),
                location_id = random.choice(locations_ids)
            )

