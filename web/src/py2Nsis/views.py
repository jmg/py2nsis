'''
Created on 25/12/2010

@author: ubugtu
'''
from django.shortcuts import render_to_response

def index(req):
    return render_to_response("main.html")

def try_it(req):
    return render_to_response("try_it.html")

def contact(req):
    return render_to_response("contact.html")