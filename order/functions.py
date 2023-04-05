from .models import Order
import datetime

def get_latest_orderno():
    year = str(datetime.datetime.now().year)[-2:]
    filter_year = f"{year}-"
    orderno = ""
    order = Order.objects.values('order_no').order_by('-order_no')
    if order.count() > 0:
        # get the last order_no        
        lastrec = order.first()['order_no']
    else:
        # initial value if there are no orders yet
        lastrec = f"{year}-0000"
        
    prod_id = int(lastrec[3:])
    new_id = prod_id + 1
    if prod_id > 1 and prod_id <= 9:
        orderno = f"{year}-000{new_id}"
    elif prod_id >= 10 and prod_id<=99:
        orderno = f"{year}-00{new_id}"
    elif prod_id >=100 and prod_id <= 999:
        orderno = f"{year}-0{new_id}"
    elif prod_id >=1000:
        orderno = f"{year}-{new_id}"
    print(orderno)
    return orderno