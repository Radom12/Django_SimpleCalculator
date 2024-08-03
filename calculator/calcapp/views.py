from django.shortcuts import render
from django.http import HttpResponse

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operator = request.POST['operator']

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operator"

        return render(request, 'calcapp/index.html', {'result': result})
    return render(request, 'calcapp/index.html') 
