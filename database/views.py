from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import personal_information
from .models import internship_history
from .models import qualifications_on_entry
from django.core.files.storage import FileSystemStorage
import os
from django.shortcuts import redirect
import json
from .models import past_employees
from .models import employment_history
from .models import employee_degrees
from .models import countries
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def new(request):
   
    if request.method == 'POST':
        new=personal_information()
        new.First_Name = request.POST.get('First_Name')
        new.Last_Name = request.POST.get('Last_Name')
        new.Other_Name = request.POST.get('Other_Name')
        new.Date_of_Birth = request.POST.get('DOB')
        new.Gender = request.POST.get('Gender')
        new.Nationality = request.POST.get('Nationality')
        new.Email = request.POST.get('Email')
        new.Home_Telephone = request.POST.get('HomeNumber')
        new.Mobile_Telephone = request.POST.get('MobileNumber')
        new.Permanent_Address_Line1 = request.POST.get('PermanentAddressLine1')
        new.Permanent_Address_Line2 = request.POST.get('PermanentAddressLine2')
        new.Country = request.POST.get('Country')
        new.Current_Address_Line1 = request.POST.get('CurrentAddressLine1')
        new.Current_Address_Line2 = request.POST.get('CurrentAddressLine2')
        new.City = request.POST.get('City')
        
        if request.FILES['Documents']:
            myfile = request.FILES['Documents']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            new.Documents = fs.url(filename) 
                      
        new.save()

        request.session['personal_data'] = new.pk
        


        return redirect('history')

    else:
        return render(request, 'database/new.html', {})
        
@csrf_exempt  
@login_required 
def history(request):
    if request.method == 'POST':
        personal_data = request.session['personal_data']
        history= internship_history()
        history.InternID = personal_information.objects.get(pk=personal_data)
        history.Type_of_Internship = request.POST.get('TypeofInternship')
        history.Area_Assigned = request.POST.get('Area')
        history.Location = request.POST.get('Location')
        history.Supervisor_name = request.POST.get('Supervisor')
        history.Start_date = request.POST.get('Start')
        history.Stop_date = request.POST.get('Stop')
        history.Paid_Period = request.POST.get('PaidPeriod')
        history.Stipend_cost_per_month = request.POST.get('Stipend')
        history.Accomodation_cost_per_month = request.POST.get('Accomodation')
        history.Air_Fare = request.POST.get('AirFare')
        history.Comments = request.POST.get('Comments')
        history.save()

        return redirect('history')
        
    else:
        return render(request, 'database/historyform.html', {})


@csrf_exempt
@login_required
def qualification(request):
    if request.method == 'POST':
        personal_data = request.session['personal_data']
        
        qualification= qualifications_on_entry()
        qualification.InternID = personal_information.objects.get(pk=personal_data)
        qualification.Name_of_Institution = request.POST.get('NameofInstitution')
        qualification.Type_of_Institution = request.POST.get('TypeofInstitution')
        qualification.Level_Attained = request.POST.get('Level')
        qualification.Year_Attained = request.POST.get('Year')
        qualification.Grade = request.POST.get('Grade')
        qualification.Experience = request.POST.get('Experience')
        qualification.save()

        return redirect('qualification')
        
    else:
        return render(request, 'database/qualificationform.html', {})

        

@csrf_exempt
@login_required
def home(request):
    return render(request, 'database/home.html', {})

def login(request):
    return render(request, 'database/login.html', {})
@csrf_exempt
@login_required
def result(request):
    return render(request, 'database/result.html', {})

@csrf_exempt
@login_required
def search(request):
    Personal_Information = personal_information.objects.all()
    if request.method == 'GET':
        search_query = request.GET.get('search_item', '')      
        Personal_Information = personal_information.objects.filter(First_Name__icontains= search_query).order_by('pk') | personal_information.objects.filter(Last_Name__icontains= search_query).order_by('pk')

        page = request.GET.get('page', 1)
        paginator = Paginator(Personal_Information, 20)
         
        try:
            Personal_Information = paginator.page(page)
        except PageNotAnInteger:

            Personal_Information = paginator.page(1)
        except EmptyPage:

            Personal_Information = paginator.page(paginator.num_pages)

        
        return render(request, 'database/search.html', {'Personal_Information': Personal_Information})


@csrf_exempt
@login_required
def view(request, key):

    if request.method == 'POST':
        personal_information.objects.get(pk=key).delete()
        return redirect('search')

    else:
        detail = personal_information.objects.get(pk=key)
        result = internship_history.objects.filter(InternID=key)
        query_set = qualifications_on_entry.objects.filter(InternID=key)

    
    return render(request, 'database/view.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})

def handle_uploaded_file(f):
    with open('media/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'media', request.FILES['Documents'])
    path = default_storage.save(save_path, request.FILES['Documents'])
    return default_storage.path(path)

@login_required
def edit_record(request, key): 
        
        detail = personal_information.objects.get(pk=key)
        result = internship_history.objects.filter(InternID=key)
        query_set = qualifications_on_entry.objects.filter(InternID=key)

    
        return render(request, 'database/edit.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})


@login_required
def update_record(request, key):
    det = personal_information.objects.get(pk=key)
    res = internship_history.objects.filter(InternID=key)
    sett = qualifications_on_entry.objects.filter(InternID=key)
    if request.method == 'POST':
        request.session['personal_data'] = key
        det.First_Name = request.POST.get('two')  
        det.Last_Name = request.POST.get('four') 
        det.Other_Name = request.POST.get('six')  
        det.Date_of_Birth = request.POST.get('ten') 
        det.Gender = request.POST.get('eight')
        det.Nationality = request.POST.get('twelve')
        det.Email = request.POST.get('fourteen')
        det.Home_Telephone = request.POST.get('one')
        det.Mobile_Telephone = request.POST.get('three')
        det.Permanent_Address_Line1 = request.POST.get('five')
        det.Permanent_Address_Line2 = request.POST.get('seven')
        det.City = request.POST.get('nine')
        det.Country = request.POST.get('eleven')
        det.Current_Address_Line1 = request.POST.get('thirteen')
        det.Current_Address_Line2 = request.POST.get('fifteen')
        det.Documents = request.POST.get('sixteen')
        det.save()
        return redirect('/database/edit_record/%s/' % key)

@csrf_exempt
@login_required
def homex(request):
    return render(request, 'database/homex.html', {})
@login_required
def searchx(request):
    Past_Employees = past_employees.objects.all()
    if request.method == 'GET':
        search_query = request.GET.get('search_item', '')       
        Past_Employees = past_employees.objects.filter(First_Name__icontains= search_query).order_by('pk') | past_employees.objects.filter(Last_Name__icontains= search_query).order_by('pk')
        
        page = request.GET.get('page', 1)
        paginator = Paginator(Past_Employees,20)
         
        try:
            Past_Employees = paginator.page(page)
        except PageNotAnInteger:

            Past_Employees = paginator.page(1)
        except EmptyPage:

            Past_Employees = paginator.page(paginator.num_pages)

        
        
        return render(request, 'database/searchx.html', {'Past_Employees': Past_Employees})
@csrf_exempt
@login_required
def viewx(request, keyx):

    if request.method == 'POST':
        past_employees.objects.get(pk=keyx).delete()
        return redirect('searchx')
    else:

        detail = past_employees.objects.get(pk=keyx)
        result = employment_history.objects.filter(PastEmployeeID=keyx)
        query_set = employee_degrees.objects.filter(PastEmployeeID=keyx)
    
    return render(request, 'database/viewx.html', {'past_employees': detail, 'employment_history': result, 'employee_degrees': query_set})
@login_required
@csrf_exempt
def newx(request):

    
   
    if request.method == 'POST':
        newx=past_employees()
        newx.File_Number = request.POST.get('FNUM')
        newx.Title = request.POST.get('title')
        newx.First_Name = request.POST.get('FN')
        newx.Middle_Name = request.POST.get('MN')
        newx.Last_Name = request.POST.get('LN')
        newx.Gender = request.POST.get('Nationality')
        newx.Date_of_Birth = request.POST.get('DOB')
        newx.Nationality = request.POST.get('NAT')
        newx.Date_of_Employment = request.POST.get('DE')
        newx.Place_of_Recruitment = request.POST.get('PR')
        newx.Qualifications_on_Entry = request.POST.get('QE')
        newx.Highest_Level_of_Education = request.POST.get('HLE')
        newx.Date_of_Departure = request.POST.get('DD')
        newx.Reason_for_Departure = request.POST.get('ROD')
        newx.Summary_of_Performance = request.POST.get('SOP')
        newx.Summary_of_Performance1 = request.POST.get('SOP1')
        newx.Summary_of_Performance2 = request.POST.get('SOP2')
        newx.Summary_of_Performance3 = request.POST.get('SOP3')
        newx.Summary_of_Performance4 = request.POST.get('SOP4')
        newx.Special_Comments_Disciplinary_or_Commendation = request.POST.get('SC')
        newx.Final_Salary = request.POST.get('FS')
        newx.Final_Allowance = request.POST.get('FA')
        newx.Job_Status = request.POST.get('JS')
        newx.Verified_By = request.POST.get('VB')
        newx.Verified_Date = request.POST.get('VD')
        newx.Verified = request.POST.get('V')
        newx.Created_By = request.POST.get('CB')
        newx.Created_Date = request.POST.get('CD')
        newx.Remarks = request.POST.get('R')
        


        if request.FILES['Documents']:
            myfile = request.FILES['Documents']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            newx.Documents = fs.url(filename) 
                      
        newx.save()

        request.session['employee_data'] = newx.pk
        


        return redirect('historyx')

    else:
        return render(request, 'database/newx.html', {})
@login_required
@csrf_exempt   
def historyx(request):
    if request.method == 'POST':
        employee_data = request.session['employee_data']
        historyx= employment_history()
        historyx.PastEmployeeID = past_employees.objects.get(pk=employee_data)
        historyx.Job_Title = request.POST.get('JT')
        historyx.Job_Period = request.POST.get('JP')
        historyx.Job_Description = request.POST.get('JD')
        historyx.Achievements = request.POST.get('A')
        historyx.Salary = request.POST.get('S')
        historyx.Job_Level = request.POST.get('JL')
        historyx.Job_Step = request.POST.get('JS')
        historyx.Start_date = request.POST.get('SD')
        historyx.End_date = request.POST.get('ED')

        historyx.save()

        return redirect('historyx')
        
    else:
        return render(request, 'database/historyformx.html', {})
@login_required
@csrf_exempt   
def employee_degreex(request):
    if request.method == 'POST':
        employee_data = request.session['employee_data']
        degreex= employee_degrees()
        degreex.PastEmployeeID = past_employees.objects.get(pk=employee_data)
        degreex.Degree_Acronym = request.POST.get('DA')
        degreex.Degree_Name = request.POST.get('DN')
        degreex.Institution_Name = request.POST.get('IN')
        degreex.Country = request.POST.get('C')
        degreex.Start_date = request.POST.get('SD')
        degreex.End_date = request.POST.get('ED')


        degreex.save()

        return redirect('employee_degreex')
        
    else:
        return render(request, 'database/employee_degreex.html', {})



@login_required
def edit_intern_history(request, key,keyy):
    result = internship_history.objects.get(pk=key)
    detail = personal_information.objects.get(pk=keyy)
    return render(request, 'database/edit_internhistoryform.html', {'internship_history': result, 'personal_information': detail})


@login_required
def edit_intern_qualification(request, key,keyy):
    query_set = qualifications_on_entry.objects.get(pk=key)
    detail = personal_information.objects.get(pk=keyy)
    return render(request, 'database/edit_internqualificationform.html', {'qualifications_on_entry': query_set,'personal_information': detail})


@login_required
def edit_recordx(request, keyx): 
    detail = past_employees.objects.get(pk=keyx)
    result = employment_history.objects.filter(PastEmployeeID=keyx)
    query_set = employee_degrees.objects.filter(PastEmployeeID=keyx)
    query_setx = countries.objects.filter(PastEmployeeID=keyx)
    return render(request, 'database/editx.html', {'past_employees': detail, 'employment_history': result, 'employee_degrees': query_set, 'countries': query_setx})


@login_required
def edit_xemployee_history(request, keyx, keyyx):
    detail = past_employees.objects.get(pk=keyyx)
    result = employment_history.objects.get(pk=keyx)
    return render(request, 'database/edit_xemployeehistoryform.html', {'employment_history': result,'past_employees': detail})


@login_required
def edit_xemployee_degrees(request, keyx, keyyx):
    detail = past_employees.objects.get(pk=keyyx)
    query_set = employee_degrees.objects.get(pk=keyx)
    return render(request, 'database/edit_xemployeedegreesform.html', {'employment_degrees': query_set,'past_employees': detail})


@login_required
def edit_xemployee_countries(request, keyx, keyyx):
    detail = past_employees.objects.get(PastEmployeeID=keyyx)
    result_set = countries.objects.get(CountriesID=keyx)
    return render(request, 'database/edit_xemployeecountriesform.html', {'employment_countries': result_set})







@login_required
def update_intern_history(request, key,keyy):
    res = internship_history.objects.get(pk=key)
    if request.method == 'POST':
        res.Type_of_Internship = request.POST.get('TypeofInternship')
        res.Area_Assigned = request.POST.get('Area') 
        res.Location = request.POST.get('Location') 
        res.Supervisor_name = request.POST.get('Supervisor') 
        res.Start_date = request.POST.get('Start') 
        res.Stop_date = request.POST.get('Stop') 
        res.Paid_Period = request.POST.get('PaidPeriod') 
        res.Stipend_cost_per_month = request.POST.get('Stipend') 
        res.Accomodation_cost_per_month = request.POST.get('Accomodation') 
        res.Air_Fare = request.POST.get('AirFare') 
        res. Comments = request.POST.get('Comments')
        res.save() 
        
        return HttpResponseRedirect('/database/edit_record/%s/' % keyy)




@login_required
def update_intern_qualification(request, key,keyy):
    sett = qualifications_on_entry.objects.get(pk=key)
    if request.method == 'POST':
        sett.Name_of_Institution = request.POST.get('NameofInstitution') 
        sett.Type_of_Institution = request.POST.get('TypeofInstitution') 
        sett.Level_Attained = request.POST.get('Level') 
        sett.Year_Attained = request.POST.get('Year') 
        sett.Grade = request.POST.get('Grade') 
        sett.Experience = request.POST.get('Experience')
        sett.save()

        return HttpResponseRedirect('/database/edit_record/%s/' % keyy)





@login_required
def update_recordx(request, keyx):
    det = past_employees.objects.get(pk=keyx)
    res = employment_history.objects.filter(PastEmployeeID=keyx)
    sett = employee_degrees.objects.filter(PastEmployeeID=keyx)
    output = countries.objects.filter(PastEmployeeID=keyx)
    if request.method == 'POST':
        det.File_Number = request.POST.get('two')
        det.Title = request.POST.get('four')
        det.First_Name = request.POST.get('six')
        det.Middle_Name = request.POST.get('ten') 
        det.Last_Name = request.POST.get('eight')  
        det.Gender = request.POST.get('twelve')
        det.Date_of_Birth = request.POST.get('fourteen') 
        det.Nationality = request.POST.get('sixteen')
        det.Date_of_Employment = request.POST.get('three')
        det.Place_of_Recruitment = request.POST.get('five')
        det.Qualifications_on_Entry = request.POST.get('twenty')
        det.Highest_Level_of_Education = request.POST.get('eighteen')
        det.Date_of_Departure = request.POST.get('seven')
        det.Reason_for_Departure = request.POST.get('nine')
        det.Summary_of_Performance = request.POST.get('fifteen')
        det.Summary_of_Performance1 = request.POST.get('seventeen')
        det.Summary_of_Performance2 = request.POST.get('nineteen')
        det.Summary_of_Performance3 = request.POST.get('twentyone')
        det.Summary_of_Performance4 = request.POST.get('twentythree')
        det.Special_Comments_Disciplinary_or_Commendation = request.POST.get('twentyfive')
        det.Final_Salary = request.POST.get('eleven')
        det.Final_Allowance = request.POST.get('thirteen')
        det.Job_Status = request.POST.get('one')
        det.Verified = request.POST.get('twentysix')
        det.Verified_By = request.POST.get('twentyseven')
        det.Verified_Date = request.POST.get('twentynine')
        det.Created_By = request.POST.get('twentytwo')
        det.Created_Date = request.POST.get('twentyfour')
        det.Remarks = request.POST.get('twentyeight')
        det.save()
        return HttpResponseRedirect('/database/edit_recordx/%s/' % keyx)




@login_required
def update_xemployee_history(request, keyx,keyyx):
    res = employment_history.objects.get(pk=keyx)
    if request.method == 'POST':
        res.Job_Title = request.POST.get('JobTitle')
        res.Job_Period = request.POST.get('JobPeriod')
        res.Job_Description = request.POST.get('JobDescription')
        res.Achievements = request.POST.get('Achievement')
        res.Salary = request.POST.get('salary')
        res.Job_Level = request.POST.get('JobLevel')
        res.Job_Step = request.POST.get('JobStep')
        res.Start_date = request.POST.get('Start')
        res.End_date = request.POST.get('End')
        res.save()
        return HttpResponseRedirect('/database/edit_recordx/%s/' % keyyx)




@login_required
def update_xemployee_degrees(request, keyx,keyyx):
    sett = employee_degrees.objects.get(pk=keyx)
    if request.method == 'POST':
        sett.Degree_Acronym = request.POST.get('DegreeAcronym')
        sett.Degree_Name = request.POST.get('DegreeName')
        sett.Institution_Name = request.POST.get('InstitutionName')
        sett.Country = request.POST.get('country')
        sett.Start_date = request.POST.get('Start')
        sett.End_date = request.POST.get('End')
        sett.save()
        return HttpResponseRedirect('/database/edit_recordx/%s/' % keyyx)
