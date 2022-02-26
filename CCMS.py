import random
import string
import time
import os
import sys
import pymysql

from two import progressBar , Quit
import getpass
import stdiomask

import warnings                     # For ingoring warnings in Python IDLE
warnings.filterwarnings("ignore")
#######################################################################      COLOURING PART      ###########################################################################################
from colorit import *

# Use this to ensure that ColorIt will be usable by certain command line interfaces
init_colorit()


############################################################################################################################################################################################



script_version = '7.0.0'
window_title   = f"Coaching Classes Management Software  (by MANAN and VEDANT) (version {script_version})"
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' + window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')

############################################################################# $$$$$$ COACHING CLASS $$$$$$ ##################################################################################

print()
print()




logo ='''
         ██████████████████████████████████████████████████████████████████████████████████████████
         █─▄▄▄─█─▄▄─██ ▄─██─▄▄▄─█─█─█▄─▄█▄─▀█▄─▄█─▄▄▄▄███─▄▄▄─█▄─▄████ ▄─██─▄▄▄▄█─▄▄▄▄█▄─▄▄─█─▄▄▄▄█
         █─███▀█─██─██─▀─██─███▀█─▄─██─███─█▄▀─██─██▄─███─███▀██─██▀██─▀─██▄▄▄▄─█▄▄▄▄─██─▄█▀█▄▄▄▄─█
         █▄▄▄▄▄█▄▄▄▄█▄▄█▄▄█▄▄▄▄▄█▄█▄█▄▄▄█▄▄▄██▄▄█▄▄▄▄▄███▄▄▄▄▄█▄▄▄▄▄█▄▄█▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄█'''


print('\033[91m' + logo + '\033[0m')
print()
print()
print()
print()



                                                                         

pswd = stdiomask.getpass(prompt=  '\33[94m' + '        Enter your MySQL Password :'  , mask= '*')



################################################################################## DATABASE CONNECTION ####################################################################################

connection = pymysql.connect(host="localhost", user="root", password=pswd)
cursor = connection.cursor()
a=cursor.execute("SHOW DATABASES LIKE 'coaching'")

################################################################################# [ Main Program ] #########################################################################################

start =100
while start==100:
    print()        
    choice_D = input('\33[33m' + "        Do you have Database And Tables Required ? (Y/N) : " +  '\33[0m')
    if choice_D == "n" or choice_D == "N" or choice_D == "no" or choice_D == "NO":
        if a == 1  :
            print()
            print (  '\33[31m' + "        Error you have database named '''coaching''' , {returning back.....}" +  '\33[0m' )
            print()
            print('\33[45m' +"-------------------------------------------------------------------------------------------------------"+  '\33[0m')
            continue
        else:
            print()
            print ('\33[33m' + "        Okay That's Not So Cool  :( , (check out next query) " +  '\33[0m')
            print()
            print()
            f = input('\33[92m' + "        Do you want to create new database required? (Y/N) : " +  '\33[0m')
            if f == "y" or f == "Y" or f == "yes" or f =="YES":
                    cursor.execute("create database Coaching;")
                    cursor.execute("use Coaching;")
                    cursor.execute("create table Students_sr (Adm_no bigint primary key , First_Name varchar(50) not null , Last_Name varchar(50) not null , Father_Name varchar(50) not null, Mother_Name varchar(50) not null , DOB date not null, gender varchar(20) not null , contact_no_Primary bigint not null ,contact_no_Secondary bigint , D_O_Joining date not null , Class int not null , optional_subject varchar(50) not null) ;")     
                    progressBar()
                    cursor.execute("create table Students_HigherSr (Adm_no bigint primary key , First_Name varchar(50) not null , Last_Name varchar(50) not null , Father_Name varchar(50) not null , Mother_Name varchar(50) not null , DOB date not null , gender varchar(20) not null , contact_no_Primary bigint not null ,contact_no_Secondary bigint , D_O_Joining date not null , Class int not null , optional_subject varchar(50) not null ) ;") 
                    cursor.execute("create table Teachers (ID_no bigint primary key ,First_Name varchar(50) not null , Last_Name varchar(50) not null , DOB date not null , D_O_Joining date not null , subject varchar(50) not null, years_of_experience int not null , contact_no bigint not null , gender varchar(20) not null , Salary bigint not null ) ;")
                    cursor.execute("create table Staff (Staff_ID bigint primary key ,First_Name varchar(50) not null ,Last_Name varchar(50) not null , DOB date not null , D_O_Joining date not null , Department varchar(50) not null , contact_no bigint not null , gender varchar(20) not null);")
                    cursor.execute("create table fee_structure (Class int not null, Original_Fee bigint not null ,Marks_PreviousClass int not null ,Marks_AptitudeTest int not null ,Scholarship_percent int not null ,Reduced_Amt bigint not null ,Payable_Fee bigint not null );")
                    print()
            if f == "n" or f == "N" or f == "no" or f =="NO":
                    print()
                    Quit()
                    print( '\33[104m' +"--------------------------Coaching Classes--------------------------" + '\33[0m')
                    print()
                    print('\33[36m'+"        ############################################### END ###############################################"+  '\33[0m')
                    exit()
            else:
                    break
            break
    elif choice_D == "y" or choice_D == "Y" or choice_D == "yes" or choice_D == "YES":
        if a != 1  :
            print()
            print (  '\33[31m' + "        Error you DON'T have database named '''coaching''' , {returning back.....}" +  '\33[0m' )
            print()
            print('\33[45m' +" -------------------------------------------------------------------------------------------------------"+  '\33[0m')
            continue
        else:
            print()
            p = input( '\33[93m' +'''        What do you want to do ?
                                     1) Continue with the program
                                     
                                     2) Delete all database and tables to start fresh :

                                                                    Enter corresponding number (1/2) :'''+  '\33[0m')
            if p == "2":
                 print()
                 x = input( '\33[31m'+ "        CAUTION YOU WANTED TO DELETE ALL DATABASE AND TABLES WRITE 'DELETE' TO CONTINUE [ CAPITALS ONLY ]: "+  '\33[0m')
                 if x == "DELETE" :
                     print()
                     progressBar()
                     print()
                     print("        YOUR DATABASE HAS BEEN DELETED AS PER YOUR REQUEST , sorry to see you leaving  :/ , wanna return ,check out next query !  ")
                     print()
                     cursor.execute("        Drop database Coaching; ")
                     q=input('\33[33m' +"        Do you want to create new database required? (Y/N) : "+  '\33[0m')
                     if q == "y" or q == "Y" or q == "yes" or q=="YES":                 
                         print()
                         cursor.execute("create database Coaching;")
                         cursor.execute("use Coaching;")
                         cursor.execute("create table Students_sr (Adm_no bigint primary key , First_Name varchar(50) not null , Last_Name varchar(50) not null , Father_Name varchar(50) not null, Mother_Name varchar(50) not null , DOB date not null, gender varchar(20) not null , contact_no_Primary bigint not null ,contact_no_Secondary bigint , D_O_Joining date not null , Class int not null , optional_subject varchar(50) not null) ;")     
                         cursor.execute("create table Students_HigherSr (Adm_no bigint primary key , First_Name varchar(50) not null , Last_Name varchar(50) not null , Father_Name varchar(50) not null , Mother_Name varchar(50) not null , DOB date not null , gender varchar(20) not null , contact_no_Primary bigint not null ,contact_no_Secondary bigint , D_O_Joining date not null , Class int not null , optional_subject varchar(50) not null ) ;") 
                         progressBar()
                         cursor.execute("create table Teachers (ID_no bigint primary key ,First_Name varchar(50) not null , Last_Name varchar(50) not null , DOB date not null , D_O_Joining date not null , subject varchar(50) not null, years_of_experience int not null , contact_no bigint not null , gender varchar(20) not null , Salary bigint not null ) ;")
                         cursor.execute("create table Staff (Staff_ID bigint primary key ,First_Name varchar(50) not null ,Last_Name varchar(50) not null , DOB date not null , D_O_Joining date not null , Department varchar(50) not null , contact_no bigint not null , gender varchar(20) not null);")
                         cursor.execute("create table fee_structure (Class int not null, Original_Fee bigint not null ,Marks_PreviousClass int not null ,Marks_AptitudeTest int not null ,Scholarship_percent int not null ,Reduced_Amt bigint not null ,Payable_Fee bigint not null );")
                         print()
                         print('\33[45m' +"        Your Database has been created"+  '\33[0m')
                         print()
                         print('\33[45m' +"        You Good to Go"+  '\33[0m')
                         print()
                         break
                     if q == "n" or q == "N" or q == "no" or q=="NO":
                             print()
                             Quit()
                             print( '\33[104m' +"--------------------------Coaching Classes--------------------------" + '\33[0m')
                             print()
                             print('\33[m' +"        ############################################### END ###############################################"+  '\33[0m')
                             exit()          
                     else:
                         print()
                         print()
                         input()
                         exit
                         break
                 else:
                     print()
                     print('\33[31m'+ "        ""ERROR !!!"" NOT DELETING DATABASE AND TABLES YOU DIDN'T ENETR CORRECT PHRASE !!! " +  '\33[0m')
                     print(" ------------------------------------------------------------------------------------------------------")
                     continue
                    

            if p == "1" :
                print()
                print()
                print(   '\33[96m' + "        Loading the program to you , please wait...." + '\33[30m')
                cursor.execute("Use Coaching ;")
                progressBar()
                print()
                print()
            break

    else :
        continue
print()
start = 1
while start == 1:
    print( '\33[104m' +"--------------------------Coaching Classes--------------------------" + '\33[0m')
    print()
    print('\33[92m' + " |      Select an Option                                           |"+  '\33[0m')       
    print('\33[92m' + " |      1. Add New Details                                         |"+  '\33[0m')
    print('\33[92m' + " |      2. View all details of a Tables                            |"+  '\33[0m')
    print('\33[92m' + " |      3. Get details of a particular person                      |"+  '\33[0m')
    print('\33[92m' + " |                                                                 |"+  '\33[0m')
    choice0 = int(input("        Enter choice: "+  '\33[0m'))
    print('\33[92m' + " --------------------------------------------------------------------"+  '\33[0m')
    print()
    while choice0 == 1:
        print('\33[92m' + " -------------------------------------------------------------------"+  '\33[0m')
        print('\33[92m' + " |      1. Add Student Details                                     |"+  '\33[0m')
        print('\33[92m' + " |      2. Add Teachers Details                                    |"+  '\33[0m')
        print('\33[92m' + " |      3. Add Staff Details                                       |"+  '\33[0m')
        print('\33[92m' + " |      4. Add Fee Structure                                       |"+  '\33[0m')
        print('\33[92m' + " |                                                                 |"+  '\33[0m')    
        choice1 = int(input("        Enter choice: "+  '\33[0m'))
        print('\33[92m' + " --------------------------------------------------------------------"+  '\33[0m')
        print()
        
################################################################################# STUDENT DETAILS ##########################################################################################            

        if choice1 == 1:
            print('\33[92m' + " -------------------------Student Details---------------------------------------"+  '\33[0m')
            Adm_no = int(input('\33[92m' + "        Enter Admission number :"+  '\33[0m'))
            First_Name = input('\33[92m' + "        Enter First Name : "+  '\33[0m')
            Last_Name = input('\33[92m' + "        Enter Last Name : "+  '\33[0m')
            Father_Name = input('\33[92m' + "        Enter Father's Name : "+  '\33[0m')
            Mother_Name = input('\33[92m' + "        Enter Mother's Name : "+  '\33[0m')
            DOB = input('\33[92m' + "        Enter Date of Birth (YYYY/MM/DD) : "+  '\33[0m')
            gender = input('\33[92m' + "        Enter Student's Gender : "+  '\33[0m')
            contact_no_Primary = int(input('\33[92m' + "        Enter Primary contact number : "+  '\33[0m'))
            contact_no_Secondary = int(input('\33[92m' + "        Enter Secondary contact number : "+  '\33[0m'))
            D_O_Joining = input('\33[92m' + "        Enter Date of Joining (YYYY/MM/DD) : "+  '\33[0m') 
            Class = int(input('\33[92m' + "        Enter Class : "+  '\33[0m'))
            if Class==9 or Class==10:
                optional_subject = input('\33[92m' + '''        Optional suject
                                            A. Social Studies,
                                            B. English,
                                            Enter the corresponding alphabet (A/B) : ''' +  '\33[0m')
                if optional_subject == 'a' or optional_subject == 'A' :
                    optional_subject = 'Social Studies'
                elif optional_subject == 'b' or optional_subject == 'B' :
                    optional_subject = 'English'
                else :
                    print()
                    print ('\33[31m' +'        "Error" enter either A or B '+  '\33[0m')
                    print()
                    continue
                insertStudents_sr="INSERT INTO Students_sr VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(Adm_no,First_Name,Last_Name,Father_Name,
                                                                                                                                                Mother_Name,DOB,gender,contact_no_Primary,
                                                                                                                                                contact_no_Secondary,D_O_Joining,
                                                                                                                                                Class ,optional_subject)
                cursor.execute(insertStudents_sr)
                connection.commit()
                print()
                print('\33[92m' +" -------------------------Student Details---------------------------------------"+  '\33[0m')
            elif Class==11 or Class==12:
                optional_subject = input('\33[92m' +'''        Optional suject
                                            A. Commputer Science,
                                            B. Physical Education,
                                            Enter the corresponding alphabet (A/B) : ''' +  '\33[0m')
                if optional_subject == 'a' or optional_subject == 'A' :
                    optional_subject = 'Computer Science'
                elif optional_subject == 'b' or optional_subject == 'B' :
                    optional_subject = 'Physical Education'
                else :
                    print()
                    print ('\33[31m' +'        "Error" enter either A or B'+  '\33[0m')
                    print()
                    continue
                insertStudents_highersr="INSERT INTO Students_highersr VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(Adm_no,First_Name,Last_Name,Father_Name,
                                                                                                                                                Mother_Name,DOB,gender,contact_no_Primary,
                                                                                                                                                contact_no_Secondary,D_O_Joining,
                                                                                                                                                Class ,optional_subject)
                cursor.execute(insertStudents_highersr)
                connection.commit()
                print()
                print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
            else :
                print('\33[31m' +'        "Error" in Class, Enter from Class 9 to 12'+  '\33[0m')
                continue

#################################################################################     TEACHERS     #########################################################################################

        if choice1 == 2:
            print('\33[92m' +"--------------------------Teachers Details--------------------------"+  '\33[0m')
            print()
            ID_no = input('\33[92m' +"        Enter Identification number : "+  '\33[0m')
            First_Name = input('\33[92m' +"        Enter First Name : "+  '\33[0m')
            Last_Name = input('\33[92m' +"        Enter Last Name : "+  '\33[0m')
            DOB = input('\33[92m' +"        Enter Date of Birth (YYYY/MM/DD) : "+  '\33[0m')
            D_O_Joining = input('\33[92m' +"        Enter Date of Joining (YYYY/MM/DD) : "+  '\33[0m')
            subject = input('\33[92m' +"        Enter Subject : "+  '\33[0m')
            years_of_experience = int(input('\33[92m' +"        Enter Years of Experience : "+  '\33[0m'))
            contact_no = int(input('\33[92m' +"        Enter contact number : "+  '\33[0m'))
            gender = input('\33[92m' +"        Enter Teacher's gender : "+  '\33[0m')
            salary = int(input('\33[92m' +"        Enter Teacher's Salary : "+  '\33[0m'))
            insertTeachers="INSERT INTO TEACHERS VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(ID_no,First_Name,Last_Name,DOB,D_O_Joining,subject,
                                                                                                                    years_of_experience,contact_no,gender,salary)
            cursor.execute(insertTeachers)
            connection.commit()
            print()
            print('\33[92m' +"--------------------------Teachers Details--------------------------"+  '\33[0m')

#################################################################################       STAFF      #########################################################################################

        if choice1 == 3:
            print('\33[92m' +"--------------------------Staff Details--------------------------"+  '\33[0m')
            print()
            Staff_ID = int(input('\33[92m' +"        Enter Staff_ID : "+  '\33[0m'))
            First_Name = input('\33[92m' +"        Enter First Name : "+  '\33[0m')
            Last_Name = input('\33[92m' +"        Enter Last Name : "+  '\33[0m')
            DOB = input('\33[92m' +"        Enter Date of Birth (YYYY/MM/DD) : "+  '\33[0m')
            D_O_Joining = input('\33[92m' +"        Enter Date of Joining (YYYY/MM/DD) : "+  '\33[0m')
            Department = input('\33[92m' +"        Enter Department :"+  '\33[0m')
            contact_no = int(input('\33[92m' +"        Enter contact number : "+  '\33[0m'))
            gender = input('\33[92m' +"        Enter Staff's gender : "+  '\33[0m')
            insertStaff="INSERT INTO Staff VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(Staff_ID,First_Name,Last_Name,DOB,
                                                                                                        D_O_Joining,Department,contact_no,gender)
            cursor.execute(insertStaff)
            connection.commit()
            print()
            print('\33[92m' +"--------------------------Staff Details--------------------------"+  '\33[0m')

#################################################################################   FEE STRUCTURE  #########################################################################################

        if choice1 == 4:
            print('\33[92m' +"--------------------------Fee Structure--------------------------"+  '\33[0m')
            print()
            Class = int(input('\33[92m' +"        Enter Class : "+  '\33[0m'))
            if Class==9 or Class==10:
                Original_Fee=100000
            elif Class==11 or Class==12:
                Original_Fee=150000
            else :
                print()
                print('\33[31m' +'        "Error" in Class, Enter from Class 9 to 12'+  '\33[0m')
                print()
                continue
            Marks_PreviousClass = int(input('\33[92m' +"        Enter Marks Obtained in previous class out of 100 : "+  '\33[0m'))
            Marks_AptitudeTest = int(input('\33[92m' +"        Enter Marks obtained in Aptitude test out of 100 : "+  '\33[0m'))
            if Marks_PreviousClass>=80:
                Scholarship_percent = ((Marks_PreviousClass/10)+(Marks_AptitudeTest/1.6))
                Reduced_Amt = ((Scholarship_percent/100)*Original_Fee)
                Payable_Fee = (Original_Fee-Reduced_Amt)
            else :
                Scholarship_percent = (Marks_AptitudeTest/1.6)
                Reduced_Amt = ((Scholarship_percent/100)*Original_Fee)
                Payable_Fee = (Original_Fee-Reduced_Amt)
            print('\33[92m' +'        Your Payble Fee is = ',Payable_Fee)
            insertfee_structure="INSERT INTO fee_structure VALUES('{}','{}','{}','{}','{}','{}','{}');".format(Class,Original_Fee,Marks_PreviousClass,Marks_AptitudeTest,
                                                                                                                   Scholarship_percent,Reduced_Amt,Payable_Fee)
            cursor.execute(insertfee_structure)
            connection.commit()
            print()
            print('\33[92m' +"--------------------------Fee Structure--------------------------"+  '\33[0m')
        if choice1>4:
            print()
            print('\33[31m' +'        "Error" enter value from 1 to 4'+  '\33[0m')
            print()
            continue
        else:
            break

#################################################################################   VIEWING DETAILS  #######################################################################################

    while choice0 == 2 :
        print('\33[92m' +"        1. To view Secondary Student Details"+  '\33[0m')
        print('\33[92m' +"        2. To view Higher Secondary Student Details "+  '\33[0m')
        print('\33[92m' +"        3. To view Teachers' Details "+  '\33[0m')
        print('\33[92m' +"        4. To view Staff Details "+  '\33[0m')
        print('\33[92m' +"        5. To view Fee Structure "+  '\33[0m')
        print()
        choice2 = int(input("        Enter choice : "+  '\33[0m'))
        print()
        if choice2 == 1 :
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
            print()
            viewStudents_Sr="SELECT * FROM Students_Sr;"
            cursor.execute(viewStudents_Sr)
            details = cursor.fetchall()
            for detail in details:
                    print()
                    print(detail)
            print()
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
        if choice2 == 2 :
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
            print()
            viewStudents_Highersr="SELECT * FROM Students_Highersr;"
            cursor.execute(viewStudents_Highersr)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
        if choice2 == 3 :
            print('\33[92m' +"--------------------------Teachers Details--------------------------"+  '\33[0m')
            print()
            viewTEACHERS="SELECT * FROM TEACHERS;"
            cursor.execute(viewTEACHERS)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Teachers Details--------------------------"+  '\33[0m')
        if choice2 == 4 :
            print('\33[92m' +"--------------------------Staff Details--------------------------"+  '\33[0m')
            print()
            viewStaff="SELECT * FROM Staff;"
            cursor.execute(viewStaff)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Staff Details--------------------------"+  '\33[0m')
        if choice2 == 5 :
            print('\33[92m' +"--------------------------Fee Structure--------------------------"+  '\33[0m')
            print()
            viewfee_structure="SELECT * FROM fee_structure;"
            cursor.execute(viewfee_structure)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Fee Structure--------------------------"+  '\33[0m')
        if choice2>5:
            print()
            print( '\33[31m' +'        "Error" enter value from 1 to 5'+  '\33[0m')
            print()
            continue
        else:
            break

###############################################################################  GETTING DETAILS  #########################################################################################

    while choice0 == 3:
        print('\33[92m' +"        1. To get a particular Secondary Student's Details "+  '\33[0m')
        print('\33[92m' +"        2. To get a particular Higher Secondary Student's Details "+  '\33[0m')
        print('\33[92m' +"        3. To get a particular Teacher's Details "+  '\33[0m')
        print('\33[92m' +"        4. To get a particular Staff's Details "+  '\33[0m')
        print()
        choice3 = int(input("        Enter choice : "+  '\33[0m'))
        print()     
        if choice3 == 1:
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
            print()
            Adm_no = input('\33[92m' +"        Enter Student's Admission Number : "+  '\33[0m')
            searchStudents_Sr="SELECT * FROM Students_Sr WHERE Adm_no= '{}';".format(Adm_no)
            cursor.execute(searchStudents_Sr)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
        if choice3 == 2:
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
            print()
            Adm_no = input('\33[92m' +"        Enter Student's Admission Number : "+  '\33[0m')
            searchStudents_HigherSr="SELECT * FROM Students_HigherSr WHERE Adm_no= '{}';".format(Adm_no)
            cursor.execute(searchStudents_HigherSr)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Student Details--------------------------"+  '\33[0m')
        if choice3 == 3:
            print('\33[92m' +"--------------------------Teachers Details--------------------------"+  '\33[0m')
            print()
            ID_no = input('\33[92m' +"        Enter Teacher's Identification Number : "+  '\33[0m')
            searchTeachers="SELECT * FROM Teachers WHERE ID_no= '{}';".format(ID_no)
            cursor.execute(searchTeachers)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Teachers Details--------------------------"+  '\33[0m')
        if choice3 == 4:
            print('\33[92m' +"--------------------------Staff Details--------------------------"+  '\33[0m')
            print()
            Staff_ID = input('\33[92m' +"        Enter Staff_ID : "+  '\33[0m')
            searchStaff="SELECT * FROM Staff WHERE Staff_ID= '{}';".format(Staff_ID)
            cursor.execute(searchStaff)
            details = cursor.fetchall()
            for detail in details:
                print()
                print(detail)
            print()
            print('\33[92m' +"--------------------------Staff Details--------------------------"+  '\33[0m')
        if choice3>4:
            print()
            print('\33[31m' +'        "Error" enter value from 1 to 4'+  '\33[0m')
            print()
            continue
        else:
            break

##########################################################################           SALUTAION         ####################################################################################

    if choice0>3:
        print()
        print('\33[31m' +'        "Error" enter value from 1 to 3'+  '\33[0m')
        print()
        continue
    print()
    choice_E = input(   '\33[93m' +"        Do you want to continue?  :" + '\33[0m')
    if choice_E == "y" or choice_E == "Y":
        continue
    else:
        start = 0
        connection.commit()
        connection.close()
        choice_C = input(    '\33[93m' +  "        Do you Want to View Copyright Information ? :" + '\33[0m' )
        if choice_C == "y" or choice_C == "Y":
            import webbrowser
            webbrowser.open("https://drive.google.com/file/d/1w6mj0hCJIGB7E5K9mjlqEy1XzXMF2G-U/view?usp=sharing")
            print()
            Quit()
            print()
            print()
            print('\33[104m' +"--------------------------Coaching Classes--------------------------"+  '\33[0m')
            print()
            print('\33[36m'+"##################################################################################################### END ####################################################################################################"+  '\33[0m')
            input(  '\33[95m' +"Press enter to Exit :"+  '\33[0m')
            exit()
        else:
            print()
            Quit()
            print()
            print()
            print( '\33[104m' +"--------------------------Coaching Classes--------------------------" + '\33[0m')
            print()
            print('\33[36m'+"#################################################################################################### END ######################################################################################################"+  '\33[0m')
            
            input(  '\33[95m' +"Press enter to Exit :"+  '\33[0m')
            exit()
                     

#######################################################################         ENDED         #############################################################################################









