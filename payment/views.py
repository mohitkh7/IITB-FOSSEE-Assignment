import calendar

from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import TutorialDetail, User


def index(request):
    return redirect('tutorial_list', month=4, year=2018)


class TutorialList(ListView):
    model = TutorialDetail
    template_name = 'payment/tutorialdetail_list.html'
    month = None
    year = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month_value'] = self.month
        context['month_name'] = calendar.month_name[self.month]
        context['year'] = self.year
        return context

    def get_queryset(self):
        self.month = self.kwargs['month']
        self.year = self.kwargs['year']
        new_context = TutorialDetail.objects.filter(
            actual_submission_date__month=self.month,
            actual_submission_date__year=self.year,
        ).order_by('actual_submission_date')
        return new_context


def payment_list(request, month, year):
    context = {}
    # If incorrect month is entered
    if month < 1 or month > 12:
        context['error'] = True
        context['error_msg'] = 'Invalid Month Value : '+str(month)+'. Enter value in url i.e. between 1 to 12'
        return render(request,'payment/payment_list.html',context)

    context['month_value'] = month
    context['month_name'] = calendar.month_name[month]
    context['year'] = year
    context['payments'] = calculate_payment(month, year)
    return render(request, "payment/payment_list.html", context)

def calculate_number_of_tutorials(user, month, year):
    return TutorialDetail.objects.filter(
        user=user,
        actual_submission_date__month=month,
        actual_submission_date__year=year,
    ).count()

def calculate_payment(month, year):
    pay_per_tutorial = 1000
    payment_arr = []
    user_arr = User.objects.all()
    for user in user_arr:
        payment = {}
        payment['name'] = user.name
        payment['number_of_tutorials'] = calculate_number_of_tutorials(user, month, year)
        payment['amount'] = payment['number_of_tutorials']*pay_per_tutorial
        if payment['amount'] > 0:
            payment_arr.append(payment)
    return payment_arr
