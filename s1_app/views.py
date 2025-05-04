from django.shortcuts import render,redirect
from django.http import HttpResponse
from s1_app.models import Person
from django.contrib import messages
import sweetify
# Create your views here.
def index(request):
    name = "Methawi."
    age = 20
    allPerson = Person.objects.all()
    return render(request,"index.html",{"name":name,"age":age})

def about(request):
    
    return render(request,"about.html")
def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        print(name,age)
        person = Person.objects.create(
            name=name ,
            age=age
        )
        person.save()
        sweetify.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/report")
    else :
        return render(request,"register.html")
def report(request):
    allPerson = Person.objects.all()
    return render(request,"report.html",{"allPerson":allPerson})
def edit (request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        sweetify.success(request,"แก้ไขข้อมูลเรียบร้อย")
        return redirect ("/report")
    else:
        person = Person.objects.get(id=person_id)
        print(person)
        return render(request,"edit.html",{"person":person})
def delete (request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    sweetify.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/report")