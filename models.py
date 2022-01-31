from django.shortcuts import render
from django.core.mail import send_mail
from .forms import MemberForm

def submit_form(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST)

        if member_form.is_valid():
            first_name = member_form.cleaned_data['first_name']
            last_name = member_form.cleaned_data['last_name']
            email = member_form.cleaned_data['email']
            phone = member_form.cleaned_data['phone']
            recipients = ['vaatiesther@gmail.com']
            message = f"Details are :\n {first_name} {last_name} \n {email}\n {phone} "

            send_mail(
                'New Member from Member Form', message,'', recipients
                )
            member_form.save()
            print('Successful')
            return render(request, 'members/success.html') 
        else:
            print('Fails')

    else:
        form = MemberForm
        return render(request, 'members/member_form.html',{"form":form})
