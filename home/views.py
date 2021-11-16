from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model,login,logout,authenticate
from django.contrib import messages
from pdf417 import encode, render_image
from .models import barcode
from django.conf import settings
from datetime import date

User = get_user_model()

def index(request):
    if request.user.is_authenticated:
        country = ["USA","CANADA","MEXICO"]
        state= ["AL","AK","AB","AS","AZ","AR","BC","CA","CU","CO","CT","DE","DC","FL","GA","GU","HI","HL","ID","IL","IN","IA","KS","KY","LA","ME","MB","MD","MA","MI","MN","MS","MO","MT","NE","NV","NB","NH","NJ","NM","NY","NL","NC","ND","MP","NS","NU","OH","OK","ON","OR","PA","PE","PR","QC","RI","SK","SC","SD","TN","TX","UT","VT","VI","VA","WA","WV","WI","WY","YT"]

        if request.method == "POST":
            country_ = request.POST['country']
            state_ = request.POST['state']
            dlnumber = request.POST['dlnumber']
            firstname = request.POST['firstname']
            middlename = request.POST['middlename']
            lastname = request.POST['lastname']
            address = request.POST['address']
            city = request.POST['city']
            zipcode = request.POST['zipcode']
            dclass = request.POST['dclass']
            rcode = request.POST['rcode']
            ecode = request.POST['ecode']
            dob = request.POST['dob']
            edate = request.POST['edate']
            idate = request.POST['idate']
            udate = request.POST['udate']
            height = request.POST['height']
            weight = request.POST['weight']
            eyeclr = request.POST['eyeclr']
            hairclr = request.POST['hairclr']
            gender = request.POST['gender']
            discriminator = request.POST['discriminator']
            connum = request.POST['connum']

            string1 = f"{country_} {state_} {dlnumber} {firstname} {middlename} {lastname} {address} {city} {zipcode} {dclass} {rcode} {ecode} {dob} {edate} {idate} {udate} {height} {weight} {eyeclr} {hairclr} {gender} {discriminator} {connum}"

            codes = encode(string1)
            image = render_image(codes)
        
            user_data = barcode.objects.create(user=request.user,country=country_,state=state_,dlnumber=dlnumber,firstname=firstname,middlename=middlename,lastname=lastname,address=address,city=city,zipcode=zipcode,dclass=dclass,rcode=rcode,ecode=ecode,dob=dob,edate=edate,idate=idate,udate=udate,height=height,weight=weight,eyeclr=eyeclr,hairclr=hairclr,gender=gender,discriminator=discriminator,connum=connum)

            user_data.save()
            print(settings.MEDIA_ROOT)
            image.save(str(settings.BASE_DIR)+"/media/"+'barcode_{}.jpg'.format(user_data.pk))
            # image.save('barcode_{}.jpg'.format(user_data.pk))
            # user_data.barcode_img = 'barcode_{}.jpg'.format(user_data.pk)
            user_data.barcode_img = 'barcode_{}.jpg'.format(user_data.pk)
            # print(country_,state_,dlnumber,firstname,middlename,lastname,address,city,zipcode,dclass,rcode,ecode,dob,edate,idate,udate,height,weight,eyeclr,hairclr,gender,discriminator,connum,image)
            user_data.save()

            return redirect("profile")

        return render(request,'index.html',{"country":country,"state":state})
    else:
        return redirect("loginProcess")

def loginProccess(request):
    if request.method == "POST":        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        
        if user:
            login(request,user)
            return redirect("index")
        else:
            messages.error(request,"username and Passoword didn't match")            
            return redirect("loginProcess")

    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']        
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not User.objects.filter(username = username).exists():
            if password == confirm_password:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,phonenumber=phonenumber,username=username,password=password)
                
                login(request,user)
                messages.success(request,"Your Account is Created")
                return redirect("index")
            else:
                messages.error(request,"Password and Confirm Passoword didn't match")
                return redirect("signup")
        else:
            messages.error(request,"User Already Exist with this username")
            return redirect("signup")

    return render(request,'signup.html')

def logoutProccess(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("loginProcess")

def profile(request):
    if request.user.is_authenticated:
        barcodes = barcode.objects.filter(user=request.user)
        today = date.today()
        return render(request,"profile.html",{'barcodes':barcodes,"date":today})
    else:
        return redirect("loginProcess")

def works(request):
    return render(request,"works.html")

def contact(request):
    return render(request,"contact.html")

def news(request):
    return render(request,"news.html")