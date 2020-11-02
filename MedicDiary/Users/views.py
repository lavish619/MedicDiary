from django.shortcuts import render

# Create your views here.
def patientregister(request):
    if request.method =='POST':
        #after pressing the submit button this function runs again..
        #this is checking if the function has been run once.. because
        #that way the metod will become POST..
        form = RegisterForm(request.POST)
        #this makes the info of the previously filled form be stored in
        #the variable form..
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request,f"Welcome {username}, account successfully created")
            # login(request, user)
            return redirect('patientlogin')
    else:
        form = RegisterForm()
    return render(request,'patient/patientregister.html',{'form':form})


def makeprofilepage(request):
    if request.method =='POST':
        #after pressing the submit button this function runs again..
        #this is checking if the function has been run once.. because
        #that way the metod will become POST..
        form = ProfileForm(request.POST)
        #this makes the info of the previously filled form be stored in
        #the variable form..
        if form.is_valid():
            form.save()
            # messages.success(request,f"Welcome {username}, account successfully created")
            # login(request, user)
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'patient/makeprofilepage.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')
