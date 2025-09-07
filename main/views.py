from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495565',
        'name': 'Ghozam Muliawan Sholihin',
        'class': 'PBP C',
        'Aplikasi' : 'SlopShop'
    }

    return render(request, "main.html", context)
