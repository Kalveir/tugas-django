from django.shortcuts import render, HttpResponse
# pernjumlahan
def tambah(request, num1, num2):
	context = {
		'tittle' : 'Kalkulator Penjumlahan',
		'result' : f"{num1} + {num2} = {num1+num2}"
	}
	return render(request, 'kalkulator/index.html', context)
# pengurangan
def kurang(request, num1, num2):
	context = {
		'tittle' : 'Kalkulator Pengurangan',
		'result' : f"{num1} - {num2} = {num1-num2}"
	}
	return render(request, 'kalkulator/index.html', context)
# perkalian
def kali(request, num1, num2):
	context = {
		'tittle' : 'Kalkulator Perkalian',
		'result' : f"{num1} * {num2} = {num1*num2}"
	}
	return render(request, 'kalkulator/index.html', context)
#pembagian
def bagi(request, num1, num2):
	context = {
		'tittle' : 'Kalkulator Pembagian',
		'result' : f"{num1} / {num2} = {num1//num2}"
	}
	return render(request, 'kalkulator/index.html', context)
# Create your views here.
