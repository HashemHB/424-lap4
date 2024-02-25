from django.shortcuts import render

tax_rate = 15 #15 %

def default(request):
    return render(request, "taxapp/default.html")

def calculate(request, num):
    return render(request, "taxapp/calculate.html", {"number": num, "tax": tax_rate, "after_tax":((num*tax_rate) / 100) + num})

def tax(request):
    return render(request, "taxapp/tax.html", {"tax":tax_rate})