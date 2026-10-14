from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Home view for /emp/
def emp_home(request):
    return HttpResponse("""
        <h1>Employee App Home</h1>
        <p>Welcome to the Employee Directory.</p>
        <p><a href='/emp/search/'>Go to Employee Search</a></p>
        <p><a href='/admin/'>Go to Admin Panel</a></p>
    """)

# Search view for /emp/search/
def search_employee(request):
    keyword = request.GET.get("technology", "").strip()
    employees = []
    message = ""

    if request.method == "GET":
        # Validation rules as per BRD
        if not keyword:
            message = "Please enter technology to search."
        elif keyword.isspace():
            message = "Search value cannot be blank."
        elif len(keyword) < 2:
            message = "Please enter at least 2 characters."
        elif len(keyword) > 50:
            message = "Search value cannot exceed 50 characters."
        elif not all(c.isalnum() or c in [' ', '+', '#', '.'] for c in keyword):
            message = "Invalid characters in search."
        else:
            # ORM query: case-insensitive partial match + active filter
            employees = Employee.objects.filter(
                technology__icontains=keyword,
                status="Active"
            ).order_by("employee_name")

            if not employees:
                message = f'No employees found for "{keyword}".'

    return render(request, "search.html", {
        "employees": employees,
        "message": message,
        "keyword": keyword
    })
