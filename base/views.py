from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from base.filters import IlanFilter
from base.forms import IlanForm, UserCreateForm, updateListingForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, HttpResponseRedirect
def home(request):

    listing = Ilan.objects.all()
    filter = IlanFilter(request.GET,queryset = listing)
    user = User.objects.all()
    context = {'ilan':listing,'user':user,'filter':filter,}
    return render(request,'base/home.html',context)

def listing(request,pk):
    ilan = Ilan.objects.get(id=pk)
    eski = Fiyat.objects.filter(ilan_id=pk)
    yorum = ilan.yorum_set.all()
    fav = Kaydet.objects.filter(user__id=request.user.id)
    if request.method == 'POST':
        comment = Yorum.objects.create(
            user=request.user,
            ilan=ilan,
            text=request.POST.get('yorum')
        )
        return redirect('ilan',pk=ilan.id)
    benzer = Ilan.objects.all()
    context = {'ilan':ilan,'benzer':benzer,'yorum':yorum,'fav':fav,'eski':eski}
    return render(request,'base/detail.html',context)

@login_required(login_url='giris')
def createListing(request):
    form = IlanForm()
    sahip = Ilan(host = request.user)
    if request.method == 'POST':
        form = IlanForm(request.POST,request.FILES,instance=sahip)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/create-listing.html',context)
@login_required(login_url='giris')
def updateListing(request,pk):
    listing = Ilan.objects.get(id=pk)
    if request.user.email==listing.host.email:
        form = IlanForm(instance=listing)
        if request.method=='POST':
            form = IlanForm(request.POST,request.FILES,instance=listing)
            if form.is_valid():
                form.save()
            return redirect('ilan',pk=listing.id)
    else:
        return redirect('ilan',pk=listing.id)
    return render(request,'base/update-listing.html',{'form':form,'listing':listing})
@login_required(login_url='giris/')
def deleteListing(request,pk):
    listing = Ilan.objects.get(id=pk)
    if request.user.id==listing.host.id:
        if request.method == 'POST':
            listing.delete()
            return redirect('home')
    else:
        return redirect('home')
    return render(request,'base/delete.html',{'listing':listing})

@login_required(login_url='giris')
def deleteComment(request,pk):
    yorum = Yorum.objects.get(id=pk)
    if request.user.id == yorum.user.id:
        if request.method=='POST':
            yorum.delete()
            return redirect('ilan',pk=yorum.ilan.id)
    else:
            return redirect('ilan',pk=yorum.ilan.id)
    return render(request,'base/delete-comment.html',{'yorum':yorum})

def profileCheck(request,pk):
    user = User.objects.get(id=pk)
    ilan = Ilan.objects.filter(host=pk)
    comment = Yorum.objects.filter(user__id = user.id)
    if user.id == request.user.id:
        return redirect('profile')
    context = {'user':user,'ilan':ilan,'yorum':comment}
    return render(request,'base/profil.html',context)

def userProfile(request):
    ilanlar = Ilan.objects.filter(host__email = request.user.email)
    user = User.objects.filter(email=request.user.email)
    comment = Yorum.objects.filter(user__id = request.user.id)
    favori=Kaydet.objects.filter(user__id=request.user.id).distinct()
    context = {'ilan':ilanlar,'user':user,'yorum':comment,'favori':favori,}

    return render(request,'base/profile.html',context)

def loginPage(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        try:
            user = User.objects.get(username==username)
        except:
            messages.error(request,'')
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'email veya şifre hatalı.')
    return render(request,'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('giris')

def registerPage(request):

    form = UserCreateForm()
    if request.method=='POST':
        form=UserCreateForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            user.save()
            login(request,user)
            return redirect('home')
    return render(request,'base/signup.html',{'form':form})

@login_required(login_url='giris')
def favori(request,pk):
    list= Kaydet.objects.all()
    user = request.user
    ilan=Ilan.objects.get(id=pk)
    if request.method == 'POST':
        favori=Kaydet.objects.get_or_create(
            user=user,
            ilan=ilan,
        )
        return redirect('ilan',pk=ilan.id)
    fav = Kaydet.objects.filter(user__id=user.id)
    context = {'user':user,'ilan':ilan,'fav':fav,'list':list}
    return render(request,'base/favori.html',context)

@login_required(login_url='giris')
def favoriSil(request,pk):

    sil = Kaydet.objects.get(id=pk)
    if request.method=='POST':
        sil.delete()
        return redirect('home')
    return render(request,'base/delete-fav.html',{'sil':sil}) 
