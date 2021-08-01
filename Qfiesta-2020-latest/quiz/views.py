from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from . import models
from django.contrib.auth.models import User
from .models import Profile, Question,Audio,Video, Image
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    ##after timer
    return render(request, 'quiz/index.html')
    #return render(request, 'quiz/Front.html')


def index2(request):
    return render(request, 'quiz/index2.html')
    #return render(request, 'quiz/Front.html')

@login_required
def index3(request):
    return render(request, 'quiz/index3.html')


@login_required
def audio(request):
    return render(request, 'quiz/audio.html')


@login_required
def video(request):
    return render(request, 'quiz/video.html')

@login_required
def image(request):
    return render(request, 'quiz/image.html')




def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'quiz/signup2.html', args)


def login_view(request):
    message = 'Log In'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index2')
            else:
                message = 'Not Activated'
        else:
            message = 'Invalid Login'
    context = {'message': message}
    return render(request, 'quiz/login.html', context)

#-------------------------------------------------->
def update_user_social_data(strategy, *args, **kwargs):
  response = kwargs['response']
  backend = kwargs['backend']
  user = kwargs['user']

  if response['picture']:
    url = response['picture']
    userProfile_obj = Profile.objects.get(user=user)
    
    userProfile_obj.image = url
    userProfile_obj.save()


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def timeout(request):
    user = User.objects.get(username = request.user.username)
    profile = Profile.objects.get(user = user)
    profile.curr_round = profile.curr_round + 1
    profile.save()
    return redirect('get_question')


def leaderboard(request):
    people = []
    profiles = Profile.objects.order_by("-score", "submit_time")
    for i in profiles:
        myuser = User.objects.get(id=i.user_id)
        people.append({
            'username': myuser.first_name+" "+myuser.last_name,
            'score': i.score,
            'time': i.submit_time,
            'image':i.image,
        })
    return render(request, 'quiz/leaderboard.html', {'people': people})

def get_question(request):

    user = User.objects.get(username=request.user.username)
    
    
    if request.method == 'POST':
        answers = request.POST['answers']
        answers = answers.replace(" ","")
        answers = answers.lower()
        print(answers)
        round = Question.objects.get(round=user.profile.curr_round)
        if answers == round.ans:
            print("correct")
            user.profile.curr_round += 1
            print(user.profile.curr_round)
            user.profile.score += 10
            user.save()
            user.profile.submit_time = timezone.now()
            print(user.profile.submit_time)
            user.save()
            return redirect('quiz1')
        else:
            return redirect('quiz2')
    else:
        if user.profile.curr_round <= 55 and user.profile.score>=280:
            round = Question.objects.get(round=user.profile.curr_round)
            if round.my_field == 'none':
                print("none")
                return render(request, 'quiz/get_question.html', {'round': round})
            elif round.my_field == 'audio':
                audiofile = Audio.objects.get(Question = round)
                print("audio")
                return render(request, 'quiz/audio.html', {'round': round , 'file':audiofile.track.url})
            elif round.my_field == 'video':
                print("video")
                videofile = Video.objects.get(Question = round)
                return render(request, 'quiz/video.html', {'round': round,'file':videofile.content.url})

            elif round.my_field == 'image':
                print("image")
                imagefile = Image.objects.get(Question = round)
                return render(request, 'quiz/image.html', {'round': round,'file':imagefile.content})



        else:
            if user.profile.curr_round > 55:
                return render(request,'quiz/endpage.html')
            else:
                return render(request, 'quiz/endpage2.html')

@login_required
def end_page(request):
    return render(request, 'quiz/endpage.html')

@login_required
def quiz1(request):
    return render(request, 'quiz/quiz1.html')

@login_required
def quiz2(request):
    return render(request, 'quiz/quiz2.html')


@login_required
def end_page(request):
	return render(request,'quiz/endpage.html')
