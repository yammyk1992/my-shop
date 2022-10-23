from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """Форма оформления заказа"""

    # в форме меняем название поля Order Date
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Дата получения заказа'
    # вместо поля Даты, выводим календарь
    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment')
