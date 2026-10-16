from django.shortcuts import render
from catalog.models import Product  # Импортируем только продукты


def home_view(request):
    """Контроллер главной страницы"""
    # 1. Извлекаем последние 5 продуктов из базы данных
    latest_products = Product.objects.all().order_by('-id')[:5]

    # 2. Выводим их в консоль терминала PyCharm (Первая часть доп. задания)
    print("\n--- ПОСЛЕДНИЕ 5 ПРОДУКТОВ В КОНСОЛИ ---")
    for product in latest_products:
        print(f"ID: {product.id} | {product.name} | Цена: {product.price} руб.")
    print("---------------------------------------\n")

    # 3. Передаем их в шаблон под ключом 'products'
    return render(request, 'catalog/home.html', {'products': latest_products})


def categories_view(request):
    """Контроллер для страницы категорий"""
    return render(request, 'catalog/21-2_home2.html')


def orders_view(request):
    """Контроллер для страницы заказов"""
    return render(request, 'catalog/21-2_home3.html')


def contacts_view(request):
    """Контроллер страницы контактов"""
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Новое сообщение!")
        print(f"Имя: {name} | Email: {email}")
        print(f"Текст: {message}")
        print("-" * 20)

        context['success_message'] = 'Спасибо! Ваше сообщение успешно отправлено.'

    return render(request, 'catalog/contacts.html', context)



# from django.shortcuts import render
#
#
# def home_view(request):
#     """Контроллер главной страницы"""
#     return render(request, 'catalog/home.html')
#
#
# def categories_view(request):
#     """Контроллер для страницы категорий"""
#     return render(request, 'catalog/21-2_home2.html')
#
#
# def orders_view(request):
#     """Контроллер для страницы заказов"""
#     return render(request, 'catalog/21-2_home3.html')
#
#
# def contacts_view(request):
#     #     """Контроллер страницы контактов"""
#     context = {}
#     if request.method == 'POST':
#         # Django забирает данные из HTML-полей по их атрибутам name="..."
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#
#         # Выводим данные в консоль терминала PyCharm для проверки
#         print(f"Новое сообщение!")
#         print(f"Имя: {name} | Email: {email}")
#         print(f"Текст: {message}")
#         print("-" * 20)
#
#         # Передаем текст сообщения в HTML-шаблон
#         context['success_message'] = 'Спасибо! Ваше сообщение успешно отправлено.'
#
#     return render(request, 'catalog/contacts.html', context)