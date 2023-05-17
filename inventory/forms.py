from django import forms
from inventory.models import Product, Inventory
from main import functions

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku','name','barcode','brand','unit','category','supplier','tax','purchased_price','retail_price','image']

    def __init__(self,*args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        UNITS = functions.get_units()
        unit_list = [(unit['id'], unit['unit']) for unit in UNITS]
        print(unit_list)
        self.fields['unit'] = forms.ChoiceField(choices=unit_list, required=True)
    
    """def form_valid(self, form):
        newproduct = super(ProductForm, self).form_valid(form)
        default_loc = functions.get_default_location_id()
        product_inv  = Inventory(product = newproduct, stock_level=0, location=default_loc)
        product_inv.save()

        return newproduct"""