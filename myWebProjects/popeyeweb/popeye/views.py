from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from popeye.forms import SignupForm, ContentRequestForm, WebsiteRequestForm, ProfileInfo,PasswordChange, UserChange, resetForm
from .models import Profile, User, ContentWriting, WebsiteBuilding

# Create your views here.

def home(request):
    return render(request, "popeye/home.html", {})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        country = ProfileInfo(request.POST)
        if form.is_valid() and country.is_valid():
            form.save()
            if form.save():
                data = form.cleaned_data
                temp = User.objects.filter(username=data['username']).values()
                createprofile = country.save(commit=False)
                createprofile.user_id = temp[0]['id']
                createprofile.save()
                return redirect('/login')
        else:
            return render(request, "popeye/signUp.html",
                          {'form': form,
                           'country': country
                           })
    else:
        form = SignupForm()
        country = ProfileInfo()
        return render(request, "popeye/signUp.html",
                      {'form': form,
                       'country': country
                       })


@login_required(login_url='login')
def myProfile(request):
        writing = ContentRequestForm()
        web = WebsiteRequestForm()
        articles = ContentWriting.objects.filter(user_id=request.user.id, is_done=1)
        pending = ContentWriting.objects.filter(user_id=request.user.id, is_done=0)
        websites = WebsiteBuilding.objects.filter(user_id=request.user.id)
        return render(request, "popeye/myProfile.html",
                      {'ArticleRequestForm': writing,
                       'WebRequestForm': web,
                       'articles': articles,
                       'pending': pending,
                       'websites': websites
                       })


def edit_profile(request):
    if request.method == 'POST':
        profile = UserChange(request.POST, instance=request.user)
        extra = ProfileInfo(request.POST, request.FILES, instance=request.user.profile)
        if profile.is_valid() and extra.is_valid():
            profile.save()
            extra.save()
            return redirect('/edit_profile')
        else:
            return render(request, "popeye/edit_profile.html", {'form': profile, 'form2': extra})
    else:
        profile = UserChange(instance=request.user)
        extra = ProfileInfo(instance=request.user.profile)
        return render(request, "popeye/edit_profile.html",
                      {'form': profile,
                       'form2': extra})


@login_required(login_url='login')
def mywallet(request):
    writing = ContentRequestForm()
    web = WebsiteRequestForm()
    return render(request, 'popeye/wallet.html',
                  {'ArticleRequestForm': writing,
                   'WebRequestForm': web})


@login_required(login_url='login')
def passwordchange(request):
    if request.method == 'POST':
        password_change = PasswordChange(request.POST)
        if password_change.is_valid():
            password_change.save()
            return redirect('/myaccount')
        else:
            return render(request, "popeye/myAccount.html",
                          {'form': password_change
                           })
    else:
        password_change = PasswordChange()
        return render(request, 'popeye/password_change.html',
                      {'form': password_change
                       })



@login_required(login_url='login')
def articles(request):
    if request.method == 'POST':
        form = ContentRequestForm(request.POST)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.user_id = request.user.id
            writing.save()
            return redirect('/articles')
        else:
            return render(request, "popeye/articles.html", {'form': form})
    else:
        form = ContentRequestForm()
        return render(request, 'popeye/articles.html', {"form": form})


def articles_request(request):
    if request.method == 'POST':
        form = ContentRequestForm(request.POST)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.user_id = request.user.id
            writing.save()
            return redirect('/articles_request')
        else:
            return render(request, "popeye/articles_request.html", {'form': form})
    else:
        form = ContentRequestForm()
        return render(request, 'popeye/articles_request.html', {"form": form})


@login_required(login_url='login')
def web(request):
    if request.method == 'POST':
        form = WebsiteRequestForm(request.POST)
        if form.is_valid():
            web = form.save(commit=False)
            web.user_id = request.user.id
            web.save()
            return redirect('/web')
        else:
            return render(request, "popeye/web.html", {'form': form})
    else:
        form = WebsiteRequestForm()
        return render(request, 'popeye/web.html', {"form": form})




def pricing(request):
    return render(request, "popeye/pricing.html", {})


def contact(request):
    return render(request, "popeye/contact.html", {})


def tests(request):
    return render(request, 'popeye/pricingtest.html',{})

def edit_request(request, article_id):
    data = {}
    if request.method == 'POST':
        form = ContentRequestForm()
        if form.is_valid():
            form.save()
            return redirect('/article/'+ article_id)
        else:
            return render(request, 'popeye/edit_request.html', {'form': form})
    else:
        articleObj = ContentWriting.objects.filter(id=article_id)
        for articleObj in articleObj:
            data = {'topic': articleObj.topic,
                    'title': articleObj.title,
                    'keywords': articleObj.keywords,
                    'description': articleObj.description,
                    'word_count': articleObj.word_count,
                    'article_cost': articleObj.article_cost
                    }
        form = ContentRequestForm(data)
        return render(request, 'popeye/edit_request.html',{'form': form, 'id': articleObj.id})
