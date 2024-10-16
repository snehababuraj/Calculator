from django.shortcuts import render
from django.views.generic import View

from operations.forms import EmiForm,TempartureForm

# Create your views here.
class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)+int(num2)
        print(result)
        return render(request,"add.html",{"data":result})
    
class SubtractionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):

        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)-int(num2)
        print(result)
        return render(request,"sub.html",{"data":result})

class MultiplicationView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"multiple.html")
    
    def post(self,request,*args,**kwargs):

        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)*int(num2)
        print(result)

        return render(request,"multiple.html",{"data":result})
    
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"factorial.html")
        
    def post(self,request,*args,**kwargs):
        num=int(request.POST.get("box"))
        result=1
        for i in range(1,num+1):
            result=result*i
        return render(request,"factorial.html",{"data":result})
    
class PrimenumberView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        num=int(request.POST.get("box"))
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        return render(request,"prime.html",{"data":is_prime})


class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"bmi.html")
    def post(self,request,*args,**kwargs):
        height=int(request.POST.get("hbox"))
        weight=int(request.POST.get("wbox"))
        height_in_m=height/100
        bmi=weight/(height_in_m)**2
        bmi=round(bmi,2)

        result=""
        if bmi<19:
            result="Underweight"
        elif bmi<25:
            result="Normalweight"
        elif bmi<30:
            result="Overweight"
        elif bmi>30:
            result="Obese"
        
        
        return render(request,"bmi.html",{"data":result})


class EmiView(View):

    def get(self,request,*args, **kwargs):

        form=EmiForm()

        return render(request,"emi.html",{"form":form})
    
    def post(self,request,*args, **kwargs):

        amount=int(request.POST.get("amount"))

        interest=int(request.POST.get("interest"))

        tenure=int(request.POST.get("tenure"))

        form=EmiForm()

        print(amount,interest,tenure)

        n=tenure*12

        r=interest/(12*100)

        emi=(amount*r*(1+r)*n)/((1+r)*n-1)

        print(emi)

        return render(request,"emi.html",{"form":form})
    
class TempartureView(View):
    def get(self,request,*args,**kwargs):
        form=TempartureForm
        return render(request,"temp.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        
        form_instance=TempartureForm(request.POST)
        if form_instance.is_valid():
            print("no error")
            print(form_instance.cleaned_data)
        else:
            print("error")
        return render(request,"temp.html",{"form":form_instance})




