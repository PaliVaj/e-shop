from django.forms import ModelForm, DateField, CharField, IntegerField, ModelChoiceField, ImageField, Textarea

from viewer.models import Product, Transmission, Fuel, Brand


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    title = CharField(max_length=128)
    produced = DateField()
    price = IntegerField()
    color = CharField(max_length=55)
    description = CharField(widget=Textarea)
    transmission = ModelChoiceField(queryset=Transmission.objects)
    fuel = ModelChoiceField(queryset=Fuel.objects)
    brand = ModelChoiceField(queryset=Brand.objects)
    image = ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'