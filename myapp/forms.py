from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'nama_produk': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Produk'}),
            'harga': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Harga'}),
            'kategori': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Pilih Kategori'}),
            'status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Pilih Status'}),
        }
