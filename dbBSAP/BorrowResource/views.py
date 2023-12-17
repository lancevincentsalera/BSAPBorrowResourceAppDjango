from django.http import *
from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
from .forms import *
from .models import Resource
from CreateAccount.models import Resident, Organization


def index(request):
    return HttpResponse("WELCOME")


class Register(View):
    template = 'register.html'

    def get(self, request):
        form = RegistrationForm()
        request.session.clear()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            request.session['user_type'] = user_type
            if user_type == 'R':
                return redirect('resident_registration')
            elif user_type == 'O':
                return redirect('organization_registration')

        return render(request, self.template, {'form': form})


class ResidentRegistration(View):
    template = 'resident_registration.html'

    def get(self, request):
        form = ResidentRegistrationForm()
        try:
            utype = request.session['user_type']
        except:
            return HttpResponseRedirect('/account/register')

        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ResidentRegistrationForm(request.POST)
        if form.is_valid():
            utype = request.session['user_type']
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            bdate = form.cleaned_data['birth_date']
            paddress = form.cleaned_data['present_address']

            args = [username, pwd, utype, fname, lname, bdate, paddress]
            msg = cursor_handler('RegisterResident', args)

            if msg[0][0] == "Successfully Registered!":
                request.session['username'] = username
                return redirect('resource')

            return render(request, self.template, {'form': form, 'msg': msg[0][0]})


class OrganizationRegistration(View):
    template = 'organization_registration.html'

    def get(self, request):
        form = OrganizationRegistrationForm()
        try:
            utype = request.session['user_type']
        except:
            return HttpResponseRedirect('/account/register')

        return render(request, self.template, {'form': form})

    def post(self, request):
        form = OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            utype = request.session['user_type']
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            org_name = form.cleaned_data['organization_name']

            args = [username, pwd, utype, org_name]
            msg = cursor_handler('OrgRegistration', args)

            if msg[0][0] == "Successfully Registered!":
                request.session['username'] = username
                return redirect('resource')

            return render(request, self.template, {'form': form, 'msg': msg[0][0]})


def registration_success(request):
    return render(request, 'registration_success.html')


class Login(View):
    template_name = 'login.html'

    def get(self, request):
        login_form = LoginForm()
        request.session.clear()
        return render(request, self.template_name, {'form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            result = cursor_handler('CheckCreds',[username, password])

            if result[0][0] == 1:
                request.session['username'] = username
                request.session['user_type'] = result[0][1]
                return redirect('resource')

        login_form.add_error(None, f'Invalid credentials. Please try again.')
        return render(request, self.template_name, {'form': login_form})


def resource_type(request):
    try:
        username = request.session['username']
    except:
        return HttpResponseRedirect('/account/login')

    if request.session['user_type'] == 'R':
        user = Resident.objects.get(username=username)
    else:
        user = Organization.objects.get(username=username)

    request.session['user_id'] = user.user_id

    result = cursor_handler('DisplayAvailableResources', [])
    if request.method == 'POST':
        resource_id = request.POST['resource_id']
        if resource_id:
            request.session['borrowed_resource_id'] = resource_id
            return redirect('borrow')

    return render(request, "resource.html", {'resource': result, 'user': user})


class Borrow(View):
    template = 'borrow.html'

    def get(self, request):
        try:
            borrowed_resource_id = request.session['borrowed_resource_id']
        except:
            return HttpResponseRedirect('/account/login')

        resource = Resource.objects.get(pk=borrowed_resource_id)
        form = BorrowResourceForm()
        return render(request, self.template, {'form': form, 'resource': resource})

    def post(self, request):
        form = BorrowResourceForm(request.POST)
        if form.is_valid():
            r_id = request.session['borrowed_resource_id']
            user_id = request.session['user_id']
            user_type = request.session['user_type']
            qnty = request.POST['quantity']
            b_date = request.POST['borrow_date']
            r_date = request.POST['return_date']

            cursor_handler('BorrowResources', [r_id, user_id, user_type, qnty, b_date, r_date])

            return redirect('borrowed')


def dashboard(request):
    try:
        username = request.session['username']
    except:
        return HttpResponseRedirect('/account/login')

    if request.method == "POST":
        returnee_id = request.POST['borrowed_id']
        if returnee_id:
            cursor_handler('ReturnBorrowed', [int(returnee_id)])

    result = cursor_handler('DisplayBorrowed', [request.session['username'], request.session['user_type']])

    if request.session['user_type'] == 'R':
        user = Resident.objects.get(username=username)
    else:
        user = Organization.objects.get(username=username)

    return render(request, "borrowed.html", {'borrowed_data': result, 'user': user})


class Logout(View):

    def get(self,request):
        request.session.clear()
        return HttpResponseRedirect('/account/login')


def cursor_handler(proc_name, args):
    cursor = connection.cursor()
    cursor.callproc(proc_name, args)
    result = cursor.fetchall()
    cursor.close()

    return result
