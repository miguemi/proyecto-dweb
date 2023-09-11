from django.forms import ModelForm, TextInput, Textarea

from core.base.models import Category


class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Ingrese un nombre',
            }),
            'desc': Textarea(attrs={
                'placeholder': 'Ingrese una descripcion',
                'rows': 3,
                'cols': 3
            })
        }
