from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from .models import mensajes
def home(request):
    if request.method == "POST":
        a = mensajes()
        a.nombre = request.POST.get('nombre','')
        a.correo = request.POST.get('correo','')
        a.mensaje = request.POST.get('mensaje','')
        a.save()
    return render(request,'core/home.html')