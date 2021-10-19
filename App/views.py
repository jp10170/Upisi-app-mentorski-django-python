from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required,login_required
from .models import korisnici,predmeti,upisi
from .forms import editForm,createForm,deleteForm
# Create your views here.

def register_request(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.SUCCESS
            return redirect("http://127.0.0.1:8000/login")
        messages.error(request,"Unsuccesfull registration. Invalid information.")
    form=NewUserForm
    return render (request=request, template_name="app/register.html", context={"register_form":form})

def login_request(request):  
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user.role=="STUDENT":
                login(request, user)
                return redirect('upisi',pk=user.id)
            elif user.role=="MENTOR":
                
                login(request, user)
                return redirect('predmeti')
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="app/login.html", context={"login_form":form})

def logoutView(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/login/")

@login_required
def view_subjects(request,pk):
    user=korisnici.objects.get(id=pk)
    user_status=user.status
    moji_pred=upisi.objects.filter(student_id = user.id)
    svi_pred=predmeti.objects.all()
    pred_red=upisi.objects.filter(student_id = user.id).order_by('predmet_id__sem_redovni')
    pred_izv=upisi.objects.filter(student_id = user.id).order_by('predmet_id__sem_izvanredni')
    predmetis={}
    pred_sem=dict()
    for svi in svi_pred:
        x=0
        for moji in moji_pred:
            if(svi.ime == moji.predmet_id.ime):
                x=1
        if(x==0):
            predmetis.update({svi.ime:svi.id})
    if(user_status=="REDOVNI"):
        for m in pred_red:
            if m.predmet_id.sem_redovni in pred_sem:
                pred_sem[m.predmet_id.sem_redovni].append({m.predmet_id.ime:m.status})
            else:
                pred_sem[m.predmet_id.sem_redovni]=[{m.predmet_id.ime:m.status}]    
    if(user_status=="IZVANREDNI"):
        for m in pred_izv:
            if m.predmet_id.sem_izvanredni in pred_sem:
                pred_sem[m.predmet_id.sem_izvanredni].append({m.predmet_id.ime:m.status})
            else:
                pred_sem[m.predmet_id.sem_izvanredni] = [{m.predmet_id.ime:m.status}]    
    return render(request,template_name='app/upisi.html',context={'predmetis':predmetis,'pred_sem':pred_sem})

@login_required
def upisiPredmet(request,pid,pk):
    preds=predmeti.objects.all()
    user=korisnici.objects.get(id=pk)
    for pred in preds:
        if pred.id==pid:
            upis=upisi(student_id=user,predmet_id =  predmeti.objects.get(pk=pred.id),status='enrolled')
            upis.save()
    return redirect('upisi',pk=pk)
    
@login_required
def ispisiPredmet(request,pname,pk):
    upis=upisi.objects.all()
    user=korisnici.objects.get(id=pk)
    for u in upis:
        if u.predmet_id.ime==pname and user.username==u.student_id.username:
            u.delete()
    return redirect('upisi',pk=pk)

@login_required   
def promijeniPredmet(request,pname,pk):
    upis=upisi.objects.all()
    user=korisnici.objects.get(id=pk)
    for u in upis:
        if u.predmet_id.ime==pname and user.username==u.student_id.username:
            if u.status=="enrolled":
                up=upisi.objects.filter(student_id=user.id, predmet_id=u.predmet_id)
                up.update(status='polozen')
            if u.status=="polozen":
                up=upisi.objects.filter(student_id=user.id, predmet_id=u.predmet_id)
                up.update(status='enrolled')
    return redirect('upisi',pk=pk)

@login_required
def sviPredmeti(request):
    preds=predmeti.objects.all()
    return render(request,template_name='app/predmeti.html',context={'preds':preds})

@permission_required("is_superuser")
def editPredmet(request,pk):
    predmet = get_object_or_404(predmeti, pk=pk)
    if request.method == "POST":
        form = editForm(request.POST,
                        instance=predmet)
        if form.is_valid():
            form.save()
            return redirect('/predmeti')
    else:
        form = editForm(instance=predmet)

    return render(request,template_name='app/editPredmet.html',context={'form': form,'predmet': predmet})

@permission_required("is_superuser")
def createPredmet(request):
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/predmeti')
    else:
        form = createForm()

    return render(request,template_name='app/createPredmet.html',context={'form': form})

@permission_required("is_superuser")
def predmetDetails(request,pk):
    predmet=predmeti.objects.filter(id=pk)
    return render(request,template_name='app/predmetDetails.html',context={'predmet':predmet})

@permission_required("is_superuser")
def sviStudenti(request):
    studenti=korisnici.objects.filter(role="STUDENT")
    return render(request,template_name='app/sviStudenti.html',context={'studenti':studenti})

@permission_required("is_superuser")
def deletePredmet(request,pk):
    predmet = get_object_or_404(predmeti, pk=pk)
    if request.method=="POST":
        form = deleteForm(request.POST,instance=predmet)
        if form.is_valid():
            predmet.delete()
            return redirect('/predmeti')
    else:
        form = deleteForm(instance=predmet)
        
    return render(request,template_name='app/deletePredmet.html',context={'form': form})
    
            
            
        
            
        
 

    
    
    
    
    
    