from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def task_create(request):
    response = """
    <h1>Yangi vazifa yaratish</h1>
    <form method="post">
            <h3>Vazifa nomi: <input type="text" name="task_name"></h3>
            <h3>Tavsif: <textarea type="text" name="description"></textarea></h3>
            <h3>Muddati: <input type="date" name="deadline"></h3>
            <h3>Muhimlik darajasi: <input type="text" name="priority"></h3>
            <button type="submit">Vazifani saqlash</button>
    </form>
    """
    return HttpResponse(response)
