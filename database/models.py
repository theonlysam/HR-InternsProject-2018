from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class personal_information(models.Model):
    created_date = models.DateTimeField(
            default=timezone.now)
    edited_date = models.DateTimeField(
            blank=True, null=True)
    #InternID = models.IntegerField(primary_key=True, null=False, blank=True)
    First_Name = models.CharField(max_length=200, blank=True)   
    Last_Name = models.CharField(max_length=200, null=True, blank=True)
    Other_Name = models.CharField(max_length=200, null=True, blank=True)
    Date_of_Birth = models.CharField(max_length=20,default=timezone.now, null=True, blank=True)
    Gender = models.CharField(max_length=20, null=True, blank=True)
    Nationality = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=254, null=True, blank=True)
    Home_Telephone = models.CharField(max_length=50, null=True, blank=True)
    Mobile_Telephone = models.CharField(max_length=50, null=True, blank=True)
    Permanent_Address_Line1 = models.CharField(max_length=254, null=True, blank=True)
    Permanent_Address_Line2 = models.CharField(max_length=254, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Current_Address_Line1 = models.CharField(max_length=200, null=True, blank=True)
    Current_Address_Line2 = models.CharField(max_length=200, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Documents = models.FileField(upload_to='uploads/', null=True)



    def __str__(self):
        return "%s %s" % (self.First_Name, self.Last_Name)



class internship_history(models.Model):
   # HistoryID = models.IntegerField(primary_key=True,  null=False, blank=True)
    InternID = models.ForeignKey('personal_information', on_delete=models.CASCADE)
    Type_of_Internship = models.CharField(max_length=50, null=True, blank=True)
    Area_Assigned = models.CharField(max_length=50, null=True, blank=True)
    Location = models.CharField(max_length=50, null=True, blank=True)
    Supervisor_name = models.CharField(max_length=50, null=True, blank=True)
    Start_date = models.CharField(max_length=20,null=True, blank=True)
    Stop_date = models.CharField(max_length=20,null=True, blank=True)
    Paid_Period = models.CharField(max_length=50, null=True, blank=True)
    Stipend_cost_per_month = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, blank=True)
    Accomodation_cost_per_month = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, blank=True)
    Air_Fare = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, blank=True)
    Comments =models.TextField(null=True, blank=True)


    def __str__(self):
        return "%s %s" % (self.Type_of_Internship, self.Area_Assigned)


class qualifications_on_entry(models.Model):
  #  QualificationID = models.IntegerField(primary_key=True, null=False, blank=True)
    InternID = models.ForeignKey('personal_information', on_delete=models.CASCADE)
    Name_of_Institution = models.CharField(max_length=100, null=True, blank=True)
    Type_of_Institution = models.CharField(max_length=100, null=True, blank=True)
    Level_Attained = models.CharField(max_length=50, null=True, blank=True)
    Year_Attained = models.CharField(max_length=50, null=True, blank=True)
    Grade = models.CharField(max_length=50, null=True, blank=True)
    Experience = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return "%s %s" % (self.Level_Attained, self.Type_of_Institution)

class past_employees(models.Model):
    #PastEmployeeID = models.IntegerField(primary_key=True, null=False)
    File_Number = models.CharField(max_length=200, blank=True)
    Title = models.CharField(max_length=20, null=True, blank=True) 
    First_Name = models.CharField(max_length=200, null=True) 
    Middle_Name = models.CharField(max_length=200, null=True, blank=True) 
    Last_Name = models.CharField(max_length=200, null=True)
    Gender = models.CharField(max_length=20, null=True)
    Date_of_Birth = models.CharField(max_length=20,default=timezone.now, null=True, blank=True)
    Nationality = models.CharField(max_length=200, null=True, blank=True)
    Date_of_Employment = models.CharField(max_length=20,null=True, blank=True)
    Place_of_Recruitment = models.CharField(max_length=200, null=True, blank=True)
    Qualifications_on_Entry = models.TextField(null=True, blank=True)
    Highest_Level_of_Education = models.CharField(max_length=200, null=True, blank=True)
    Date_of_Departure = models.CharField(max_length=20,null=True, blank=True)
    Reason_for_Departure = models.CharField(max_length=200, null=True, blank=True)
    Summary_of_Performance = models.CharField(max_length=254, null=True, blank=True)
    Summary_of_Performance1 = models.CharField(max_length=254, null=True, blank=True)
    Summary_of_Performance2 = models.CharField(max_length=254, null=True, blank=True)
    Summary_of_Performance3 = models.CharField(max_length=254, null=True, blank=True)
    Summary_of_Performance4 = models.CharField(max_length=254, null=True, blank=True)
    Special_Comments_Disciplinary_or_Commendation = models.TextField(null=True, blank=True)
    Final_Salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Final_Allowance = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    Job_Status = models.CharField(max_length=100, null=True)
    Verified = models.CharField(max_length=50, null=True, blank=True)
    Verified_By = models.CharField(max_length=50, null=True, blank=True)
    Verified_Date = models.CharField(max_length=20,null=True, blank=True)
    Created_By = models.CharField(max_length=50, null=True, blank=True)
    Created_Date = models.CharField(max_length=20,null=True, blank=True)
    Remarks = models.CharField(max_length=200, null=True, blank=True)
    Documents = models.FileField(upload_to='uploads/', null=True)

    def __str__(self):
        return "%s %s" % (self.First_Name, self.Last_Name)



class employment_history(models.Model):
    #EmploymentHistoryID = models.IntegerField(primary_key=True, default="1")
    PastEmployeeID = models.ForeignKey('past_employees', on_delete=models.CASCADE)
    Job_Title = models.CharField(max_length=100, null=True, blank=True)
    Job_Period = models.CharField(max_length=50, null=True, blank=True)
    Job_Description = models.CharField(max_length=200, null=True, blank=True)
    Achievements = models.CharField(max_length=200, null=True, blank=True)
    Salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Job_Level = models.CharField(max_length=25, null=True, blank=True)
    Job_Step= models.CharField(max_length=50)   
    Start_date = models.CharField(max_length=20,null=True, blank=True)
    End_date = models.CharField(max_length=20,null=True, blank=True)
    

    def __str__(self):
        return self.Job_Title

class employee_degrees(models.Model):
    #DegreeID = models.IntegerField(primary_key=True, default="1")
    PastEmployeeID = models.ForeignKey('past_employees', on_delete=models.CASCADE)
    Degree_Acronym = models.CharField(max_length=100, blank=True)
    Degree_Name = models.CharField(max_length=200, blank=True)
    Institution_Name = models.CharField(max_length=100, blank=True)
    Country = models.CharField(max_length=100, null=True)
    Start_date = models.CharField(max_length=20,null=True, blank=True)
    End_date = models.CharField(max_length=20,null=True, blank=True)
     


    def __str__(self):
        return self.Degree_Acronym


class countries(models.Model):
    #CountriesID = models.IntegerField(primary_key=True, null=False)
    PastEmployeeID = models.ForeignKey('past_employees', on_delete=models.CASCADE)
    Country_Name = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.Country_Name



    



    
