from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def user_login(request):

  if request.method == "POST" : 
    
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user) 
        # Redirect to a success page.
        return redirect('/')
  return render(request, 'login.html')
