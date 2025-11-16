from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Feedback
from .forms import SubmitFeedback


# Create your views here.

def home(request):
    return render(request, 'home.html')


def submit(request):
    if request.method == 'POST':
        student = SubmitFeedback(request.POST)
        if student.is_valid():
            student.save()
            return HttpResponse("""
                <h2>Thank you for feedback!</h2>
                <br>
                <a href='/' style="
                    padding: 8px 15px;
                    background: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 4px;
                ">Go Back to Home</a>
            """)
    else:
        student = SubmitFeedback()

    con = {'form': student}
    return render(request, 'submit.html', con)


def view(request):
    student = Feedback.objects.all()
    con = {'feedbacks': student}
    return render(request, 'view.html', con)


def delete(request, id):
    student = get_object_or_404(Feedback, id=id)
    student.delete()
    return redirect('view')


def update(request, id):
    student = get_object_or_404(Feedback, id=id)
    if request.method == 'POST':
        f = SubmitFeedback(request.POST, instance=student)
        if f.is_valid():
            f.save()
            return redirect('view')
    else:
        f = SubmitFeedback(instance=student)

    con = {'form': f}
    return render(request, 'submit.html', con)
