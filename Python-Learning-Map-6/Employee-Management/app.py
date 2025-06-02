from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from models import Employee
from fastapi import Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from bson import ObjectId

app = FastAPI()

app.mongodb_client = MongoClient("mongodb://localhost:27017/")
app.database = app.mongodb_client["employee_management"]
app.employees_collection = app.database["employees"]

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Employee Management System"}

@app.get("/employees", response_class=HTMLResponse)
async def list_employees(request: Request):
    employees = []
    for emp in request.app.employees_collection.find():
        employees.append(emp)
    return templates.TemplateResponse("list_employees.html", {"request": request, "employees": employees})

@app.get("/employees/add", response_class=HTMLResponse)
async def show_add_form(request: Request):
    return templates.TemplateResponse("add_employee.html", {"request": request})

@app.post("/employees/add", response_class=RedirectResponse)
async def add_employee(
    request: Request, 
    name: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
    position: str = Form(...),
    department: str = Form(...),
    salary: float = Form(...),
    join_date: str = Form(None)
):
    employee = {
        "name": name,
        "email": email,
        "age": age,
        "position": position,
        "department": department,
        "salary": salary,
        "join_date": join_date
    }
    result = request.app.employees_collection.insert_one(employee)
    return RedirectResponse(url="/employees", status_code=303)

@app.get("/employees/edit/{employee_id}", response_class=HTMLResponse)
async def show_edit_form(request: Request, employee_id: str):
    employee = request.app.employees_collection.find_one({"_id": ObjectId(employee_id)})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return templates.TemplateResponse("edit_employee.html", {"request": request, "employee": employee})

@app.post("/employees/edit/{employee_id}", response_class=RedirectResponse)
async def update_employee(
    request: Request,
    employee_id: str,
    name: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
    position: str = Form(...),
    department: str = Form(...),
    salary: float = Form(...),
    join_date: str = Form(None)
):
    updated_employee = {
        "name": name,
        "email": email,
        "age": age,
        "position": position,
        "department": department,
        "salary": salary,
        "join_date": join_date
    }
    result = request.app.employees_collection.update_one(
        {"_id": ObjectId(employee_id)},
        {"$set": updated_employee}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return RedirectResponse(url="/employees", status_code=303)

@app.get("/employees/delete/{employee_id}", response_class=RedirectResponse)
async def delete_employee(request: Request, employee_id: str):
    result = request.app.employees_collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return RedirectResponse(url="/employees", status_code=303)