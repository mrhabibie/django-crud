# myapp/views.py
import requests
import hashlib
import pytz
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from rest_framework import viewsets
from .models import Produk, Kategori, Status
from .forms import ProdukForm
from .serializers import ProdukSerializer

@csrf_exempt
def external_api_request(request):
    if request.method == 'GET':
        data_produk = Produk.objects.all()
        data_status = Status.objects.all()
        data_kategori = Kategori.objects.all()
        if data_produk.count() <= 0 & data_status.count() <= 0 & data_kategori.count() <= 0:
            url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
            current_date = datetime.now().astimezone(pytz.timezone('Asia/Jakarta'))
            formatted_date = current_date.strftime('%d%m%y')
            formatted_date2 = current_date.strftime('%d-%m-%y')
            password = hashlib.md5(f'bisacoding-{formatted_date2}'.encode()).hexdigest()
            rounded_time = current_date.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
            data = {
                'username': f'tesprogrammer{formatted_date}C{rounded_time.strftime('%H')}',
                'password': password,
            }
            try:
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    response_data = response.json()
                    data_list = response_data.get("data", [])
                    if not isinstance(data_list, list):
                        return JsonResponse({"error": "Invalid data format"}, status=400)

                    for data in data_list:
                        id_produk = data.get("id_produk")
                        nama_produk = data.get("nama_produk")
                        harga = data.get("harga")
                        kategori_nama = data.get("kategori")
                        status_nama = data.get("status")

                        kategori_obj, _ = Kategori.objects.get_or_create(nama_kategori=kategori_nama)

                        status_obj, _ = Status.objects.get_or_create(nama_status=status_nama)

                        Produk.objects.update_or_create(
                            id_produk=id_produk,
                            defaults={
                                "nama_produk": nama_produk,
                                "harga": harga,
                                "kategori": kategori_obj,
                                "status": status_obj
                            }
                        )
                else:
                    return JsonResponse({'error': 'Failed to fetch data from external API'}, status=response.status_code)
            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def produk_list(request):
    if request.method == 'GET':
        produk = Produk.objects.select_related('kategori', 'status').all().order_by('kategori', 'nama_produk')

        if produk.count() <= 0:
            external_api_request(request)

        produk = produk.filter(status__nama_status='bisa dijual')

        context = {
            'title': 'List Produk',
            'data': produk
        }

        return render(request, 'myapp/list_produk.html', context)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def produk_create(request):
    if request.method == "POST":
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()

    context = {
        'title': 'Tambah Produk',
        'form': form
    }
    
    return render(request, 'myapp/form.html', context)

def produk_edit(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == "POST":
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)

    context = {
        'title': 'Edit Produk',
        'form': form
    }

    return render(request, 'myapp/form.html', context)

def produk_delete(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    return redirect('produk_list')

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
