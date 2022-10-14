from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer

from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
# ------------------------------------------------- without class singup-----------------------------------------
# def validateCustomer(customer):
#     error_massage = None
#     if (not customer.frist_name):
#         error_massage = 'first name required !'
#     elif len(customer.frist_name) < 3:
#         error_massage = 'Enter above or more letter'
#     elif (not customer.last_name):
#         error_massage = 'last name required !'
#     elif len(customer.last_name) < 3:
#         error_massage = 'Enter above or more letter'
#     elif (not customer.phone):
#         error_massage = 'phone number required !'
#     elif len(customer.phone) != 10:
#         error_massage = 'Invalid'
#     elif len(customer.email) < 5:
#         error_massage = 'Email Must longer then '
#     elif len(customer.password) < 4:
#         error_massage = 'Email Must longer then '
#     elif customer.isExists():
#         error_massage = 'Email already exists'
#     return error_massage

# def registerUser(request):
#         postData = request.POST
#         frist_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')
#         customer = Customer(frist_name=frist_name,
#                             last_name=last_name,
#                             phone=phone,
#                             email=email,
#                             password=password)
#         value = {'frist_name': frist_name,
#                  'last_name': last_name,
#                  'phone': phone,
#                  'email': email}
#
#         error_massage = validateCustomer(customer)
#
#         if not error_massage:
#             customer.password=make_password(customer.password)
#             customer.register()
#
#             return redirect('homepage')
#         else:
#             data = {'error': error_massage,
#                     'values': value}
#             return render(request, "signup.html", data)


# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerUser(request)
