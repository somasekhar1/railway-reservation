from django.shortcuts import render
from .models import registrationpage
from .models import ticketbooking
from .models import payment

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def Register(request):
    return render(request,"registration.html")

def Registration(request):
    firstname=request.POST.get("t1")
    lastname=request.POST.get("t2")
    surname=request.POST.get("t3")
    fathername=request.POST.get("t4")
    cno=request.POST.get("t5")
    email=request.POST.get("t6")
    username=request.POST.get("t7")
    password=request.POST.get("t8")
    address=request.POST.get("address")
    rp=registrationpage(firstname=firstname,lastname=lastname,surname=surname,fathername=fathername,cno=cno,email=email,username=username,password=password,address=address)
    rp.save()
    return render(request,"ticketsbooking.html",{"reg":"Details Saved in Sqlite Database"})


def AlreadyAccoutExist(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    r=registrationpage.objects.filter(username=username,password=password)
    if not r:
        return render(request,"alreadyaccountexist.html")
    else:
        return render(request,"ticketsbooking.html")


def TicketsBooking(request):
    fromplace=request.POST.get("fromplace")
    toplace=request.POST.get("toplace")
    date=request.POST.get("t1")
    journeydate=request.POST.get("t2")
    searchtrain=request.POST.get("searchtrains")
    tb=ticketbooking(fromplace=fromplace,toplace=toplace,date=date,journeydate=journeydate,searchtrain=searchtrain)
    tb.save()
    return render(request,"searchtrain.html",{"tickect":"Details Saved in Sqlite Database"})

def searchtrain(request):
    return render(request,"searchtrain.html")

def GeneralReservation(request):
    return render(request,"generaldetailsform.html")


def searchseatsavailabilty(request):
    return render(request,"searchseatavailabilty.html")

def payment1(request):
    return render(request,"payment.html")



def paymentdetails(request):
    cardtype = request.POST.get("cardtype")
    bankname = request.POST.get("bankname")
    cardholdername = request.POST.get("t1")
    cardnumber = request.POST.get("t2")
    cvvno = request.POST.get("t3")
    p = payment(cardtype=cardtype, bankname=bankname, cardholdername=cardholdername, cardnumber=cardnumber, cvvno=cvvno)
    p.save()
    return render(request, "paymentsuccess.html", {"pay": "Details Saved in sqlite 3"})


def LadiesReservation(request):
    return render(request,"ladies.html")


def TatkalReservation(request):
    return render(request,"tatkal.html")


def LowerBerthReservation(request):
    return render(request,"lowerberth.html")


def SrCitizenReservation(request):
    return render(request,"seniorcitizen.html")


def PermimumTatkalReservation(request):
    return render(request,"permimumtatkal.html")


def Logout(request):
    return render(request,"index.html")