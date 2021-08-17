#Name      : CPGA_Calculator.py 
#Purpose   : IF EVERYONE HAPPY , THEN I HAPPY
#Modules   : json , os , sys, platform , webbrowser, getpass, distutils.util , strtobool
#Date      : 10th July 2021 - 1st August 2021 (version 1.0) , 16th - 17th August 2021 for adding some new features (version 1.7)
#Programmer: Gawr Gura

"""[Modules]
"""
import json
import platform
import os
import sys
import webbrowser
from getpass import getpass
from distutils.util import strtobool

"""[Variables]
"""
loop = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"]

def clear_screen():
    if platform.uname().system == "Linux":
        os.system("clear")
    elif platform.uname().system == "Windows":
        os.system("cls")

def print_student_stream():
    if student_stream[0] in ("1","2","3","4","5","6","7"):
        if student_stream[0] == "1":
            print("\n\t"+"-"*29+"\n\tStream 1 : Biological Science\n\t"+"-"*29+"\n\tFHHM1022 Effective Communication Skills\n\tFHEL1012 English for Academic Study\n\tFHMM1014 Mathematics I\n\tFHMM1024 Mathematics II\n\tFHMM1034 Mathematics III\n\tFHSC1124 Organic Chemistry\n\tFHSC1114 Physical Chemistry\n\tFHSC1214 Fundamentals of Cell Biology\n\tFHSC1134 Inorganic Chemistry\n\tFHSC1224 Introduction to Physiological Systems\n\tFHSC1234 Modern Biology\n\tFHSP1014 Physics I\n\tFHSP1024 Physics II\n\tFHCT1022 Programming Concepts\n")
        elif student_stream[0] == "2":
            print("\n\t"+"-"*49+"\n\tStream 2 : Physical Science (Engineering Science)\n\t"+"-"*49+"\n\tFHHM1022 Effective Communication Skills\n\tFHEL1012 English for Academic Study\n\tFHMM1014 Mathematics I\n\tFHMM1024 Mathematics II\n\tFHMM1034 Mathematics III\n\tFHSC1124 Organic Chemistry\n\tFHSC1114 Physical Chemistry\n\tFHSC1014 Mechanics\n\tFHSC1024 Thermodynamics and Electromagnetism\n\tFHSC1034 Waves and Modern Physics\n\tFHSC1134 Inorganic Chemistry\n\tFHCT1022 Programming Concepts\n\tFHSB1214 Biology I\n\tFHSB1224 Biology II\n")
        elif student_stream[0] == "3":
            print("\n\t"+"-"*51+"\n\tStream 3 : Physical Science (Technological Science)\n\t"+"-"*51+"\n\tFHHM1022 Effective Communication Skills\n\tFHEL1012 English for Academic Study\n\tFHMM1014 Mathematics I\n\tFHMM1024 Mathematics II\n\tFHMM1034 Mathematics III\n\tFHSC1124 Organic Chemistry\n\tFHSC1114 Physical Chemistry\n\tFHCT1012 Computing Technology\n\tFHCT1014 Introduction to Data Analytics\n\tFHCT1024 Programming Concepts and Design\n\tFHBM1114 Management\n\tFHSC1014 Mechanics\n\tFHSC1024 Thermodynamics and Electromagnetism\n\tFHSB1214 Biology I\n")
        elif student_stream[0] == "4":
            print("\n\t"+"-"*37+"\n\tStream 4 : Accountancy and Management\n\t"+"-"*37+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHBM1214 Financial Accounting\n\tFHBM1224 Financial Management\n\tFHMM1314 Mathematics for Business I\n\tFHMM1324 Mathematics for Business II\n\tFHBM1024 Microeconomics and Macroeconomics\n\tFHBM1014 Principles of Economics\n")
        elif student_stream[0] == "5":
            print("\n\t"+"-"*52+"\n\tStream 5 : Arts and Social Science (Chinese Studies)\n\t"+"-"*52+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHHM1134 Introduction to Social Psychology\n\tFHHM1114 Introduction to Sociology\n\tFHMM1214 Mathematics for Social Science\n\tXXXXXXXX Introduction to Chinese Literature\n\tXXXXXXXX Introduction to Chinese Writing\n\tXXXXXXXX Selected Texts of Modern Chinese Literature\n")
        elif student_stream[0] == "6":
            print("\n\t"+"-"*51+"\n\tStream 6 : Arts and Social Science (Social Science)\n\t"+"-"*51+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHHM1134 Introduction to Social Psychology\n\tFHHM1114 Introduction to Sociology\n\tFHMM1214 Mathematics for Social Science\n\tFHBM1024 Microeconomics and Macroeconomics\n\tFHBM1014 Principles of Economics\n\tFHHM1124 Socialization as a Process\n")
        elif student_stream[0] == "7":
            print("\n\t"+"-"*96+"\n\tStream 7 : Arts and Social Science (Graphic Design and Multimedia, Game Design and Architecture)\n\t"+"-"*96+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHAD1024 Analytical Drawing\n\tFHAD1014 Design Fundamentals\n\tFHAD1034 Figure Drawing\n\tFHHM1134 Introduction to Social Psychology\n\tFHHM1114 Introduction to Sociology\n\tFHMM1214 Mathematics for Social Science\n")

    else:
        print("\n\t\tInvalid Stream !!!\n\tPlease edit your stream in 'Edit your account' option ...\n")

def print_courses():
    if data[student_id[0]]['courses'] == None:
        print("-"*3+"Course Codes"+"-"*3+"Marks"+"-"*3+"Grades"+"-"*3+"Points"+"-"*3+"Subjects"+"-"*3)
        print("\n\t--------Empty Here--------")
    else:
        print("-"*3+"Course Codes"+"-"*3+"Marks"+"-"*3+"Grades"+"-"*3+"Points"+"-"*3+"Subjects"+"-"*3)
        for courses in data[student_id[0]]['courses']:
            print("    ",courses,"    ",
            data[student_id[0]]['courses'][courses]['mark'],"    ",
            data[student_id[0]]['courses'][courses]['grade'],"    ",
            data[student_id[0]]['courses'][courses]['point'],"    ",
            data[student_id[0]]['courses'][courses]['subject'])

def print_all():
    loop[16] = True
    while loop[16]:
        key_in_student_details()

        # Options
        print("\t"+"-"*40+"\n\t\t"+"Choose one option"+"\n\t"+"-"*40)
        print("\n\t1. Whole stream courses list")
        print("\n\t2. All courses that available")
        print("\n\t3. Grade and Point list")
        print("\n\n\t0. Exit the menu\n\n")

        options[2] = input("Please select an option : ")
        if options[2] in ("0","1","2","3"):
            if options[2] == "0":
                loop[16] = False

            elif options[2] == "1":
                key_in_student_details()
                print("\n\t"+"-"*29+"\n\tStream 1 : Biological Science\n\t"+"-"*29+"\n\tFHHM1022 Effective Communication Skills\n\tFHEL1012 English for Academic Study\n\tFHMM1014 Mathematics I\n\tFHMM1024 Mathematics II\n\tFHMM1034 Mathematics III\n\tFHSC1124 Organic Chemistry\n\tFHSC1114 Physical Chemistry\n\tFHSC1214 Fundamentals of Cell Biology\n\tFHSC1134 Inorganic Chemistry\n\tFHSC1224 Introduction to Physiological Systems\n\tFHSC1234 Modern Biology\n\tFHSP1014 Physics I\n\tFHSP1024 Physics II\n\tFHCT1022 Programming Concepts\n")
                print("\n\t"+"-"*49+"\n\tStream 2 : Physical Science (Engineering Science)\n\t"+"-"*49+"\n\tFHHM1022 Effective Communication Skills\n\tFHEL1012 English for Academic Study\n\tFHMM1014 Mathematics I\n\tFHMM1024 Mathematics II\n\tFHMM1034 Mathematics III\n\tFHSC1124 Organic Chemistry\n\tFHSC1114 Physical Chemistry\n\tFHSC1014 Mechanics\n\tFHSC1024 Thermodynamics and Electromagnetism\n\tFHSC1034 Waves and Modern Physics\n\tFHSC1134 Inorganic Chemistry\n\tFHCT1022 Programming Concepts\n\tFHSB1214 Biology I\n\tFHSB1224 Biology II\n")
                print("\n\t"+"-"*51+"\n\tStream 3 : Physical Science (Technological Science)\n\t"+"-"*51+"\n\tFHHM1022 Effective Communication Skills\n\tFHEL1012 English for Academic Study\n\tFHMM1014 Mathematics I\n\tFHMM1024 Mathematics II\n\tFHMM1034 Mathematics III\n\tFHSC1124 Organic Chemistry\n\tFHSC1114 Physical Chemistry\n\tFHCT1012 Computing Technology\n\tFHCT1014 Introduction to Data Analytics\n\tFHCT1024 Programming Concepts and Design\n\tFHBM1114 Management\n\tFHSC1014 Mechanics\n\tFHSC1024 Thermodynamics and Electromagnetism\n\tFHSB1214 Biology I\n")
                print("\n\t"+"-"*37+"\n\tStream 4 : Accountancy and Management\n\t"+"-"*37+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHBM1214 Financial Accounting\n\tFHBM1224 Financial Management\n\tFHMM1314 Mathematics for Business I\n\tFHMM1324 Mathematics for Business II\n\tFHBM1024 Microeconomics and Macroeconomics\n\tFHBM1014 Principles of Economics\n")
                print("\n\t"+"-"*52+"\n\tStream 5 : Arts and Social Science (Chinese Studies)\n\t"+"-"*52+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHHM1134 Introduction to Social Psychology\n\tFHHM1114 Introduction to Sociology\n\tFHMM1214 Mathematics for Social Science\n\tXXXXXXXX Introduction to Chinese Literature\n\tXXXXXXXX Introduction to Chinese Writing\n\tXXXXXXXX Selected Texts of Modern Chinese Literature\n")
                print("\n\t"+"-"*51+"\n\tStream 6 : Arts and Social Science (Social Science)\n\t"+"-"*51+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHHM1134 Introduction to Social Psychology\n\tFHHM1114 Introduction to Sociology\n\tFHMM1214 Mathematics for Social Science\n\tFHBM1024 Microeconomics and Macroeconomics\n\tFHBM1014 Principles of Economics\n\tFHHM1124 Socialization as a Process\n")
                print("\n\t"+"-"*96+"\n\tStream 7 : Arts and Social Science (Graphic Design and Multimedia, Game Design and Architecture)\n\t"+"-"*96+"\n\tFHEL1024 Academic English\n\tFHCT1012 Computing Technology\n\tFHHM1012 Critical Thinking\n\tFHHM1022 Effective Communication Skills\n\tFHEL1134 English for Business Communication\n\tFHEL1114 English Language Proficiency\n\tFHBM1114 Management\n\tFHBM1124 Marketing\n\tFHAD1024 Analytical Drawing\n\tFHAD1014 Design Fundamentals\n\tFHAD1034 Figure Drawing\n\tFHHM1134 Introduction to Social Psychology\n\tFHHM1114 Introduction to Sociology\n\tFHMM1214 Mathematics for Social Science\n")
                
                input("Press ...Enter... to return to menu ...")

            elif options[2] == "2":
                key_in_student_details()
                print(
                    "\n\t"+"-"*15+"\n\tList of Courses\n\t"+"-"*15,
                    "\n\tFHHM1022 Effective Communication Skills\n",
                    "\tFHEL1012 English for Academic Study\n",
                    "\tFHMM1014 Mathematics I\n",
                    "\tFHMM1024 Mathematics II\n",
                    "\tFHMM1034 Mathematics III\n",
                    "\tFHSC1124 Organic Chemistry\n",
                    "\tFHSC1114 Physical Chemistry\n",
                    "\tFHSC1214 Fundamentals of Cell Biology\n",
                    "\tFHSC1134 Inorganic Chemistry\n",
                    "\tFHSC1224 Introduction to Physiological Systems\n",
                    "\tFHSC1234 Modern Biology\n",
                    "\tFHSP1014 Physics I\n",
                    "\tFHSP1024 Physics II\n",
                    "\tFHCT1022 Programming Concepts\n",
                    "\tFHSC1014 Mechanics\n",
                    "\tFHSC1024 Thermodynamics and Electromagnetism\n",
                    "\tFHSC1034 Waves and Modern Physics\n",
                    "\tFHSB1214 Biology I\n",
                    "\tFHSB1224 Biology II\n",
                    "\tFHCT1012 Computing Technology\n",
                    "\tFHCT1014 Introduction to Data Analytics\n",
                    "\tFHCT1024 Programming Concepts and Design\n",
                    "\tFHBM1114 Management\n",
                    "\tFHEL1024 Academic English\n",
                    "\tFHHM1012 Critical Thinking\n",
                    "\tFHHM1022 Effective Communication Skills\n",
                    "\tFHEL1134 English for Business Communication\n",
                    "\tFHEL1114 English Language Proficiency\n",
                    "\tFHBM1124 Marketing\n",
                    "\tFHBM1214 Financial Accounting\n",
                    "\tFHBM1224 Financial Management\n",
                    "\tFHMM1314 Mathematics for Business I\n",
                    "\tFHMM1324 Mathematics for Business II\n",
                    "\tFHBM1024 Microeconomics and Macroeconomics\n",
                    "\tFHBM1014 Principles of Economics\n",
                    "\tFHHM1134 Introduction to Social Psychology\n",
                    "\tFHHM1114 Introduction to Sociology\n",
                    "\tFHMM1214 Mathematics for Social Science\n",
                    "\tXXXXXXXX Introduction to Chinese Literature\n",
                    "\tXXXXXXXX Introduction to Chinese Writing\n",
                    "\tXXXXXXXX Selected Texts of Modern Chinese Literature\n",
                    "\tFHHM1124 Socialization as a Process\n",
                    "\tFHAD1024 Analytical Drawing\n",
                    "\tFHAD1014 Design Fundamentals\n",
                    "\tFHAD1034 Figure Drawing\n")
                
                input("Press ...Enter... to return to menu ...")

            elif options[2] == "3":
                key_in_student_details()
                print(
                    "\n\t"+"-"*17+"\n\tGrades and Points\n\t"+"-"*17,
                    "\n\tGrade | Point\n",
                    "\t------|------\n",
                    "\t A+   | 4.00\n",
                    "\t A    | 4.00\n",
                    "\t A-   | 3.67\n",
                    "\t B+   | 3.33\n",
                    "\t B    | 3.00\n",
                    "\t B-   | 2.67\n",
                    "\t C+   | 2.33\n",
                    "\t C    | 2.00\n",
                    "\t F    | 0.00\n")

                input("Press ...Enter... to return to menu ...")

        else:
            input("Invalid options ... Reinput again ...\nPress ...Enter... to continue")

"""[Variables]
"""
gp_course_hour_list = []
course_hour_list = []
cpga = [0]

def calculate_CPGA():
    gp_course_hour_list.clear()
    course_hour_list.clear()
    if data[student_id[0]]['courses'] == None:
        print()
    else:
        for courses in data[student_id[0]]['courses']:
            gp_course_hour_list.append(data[student_id[0]]['courses'][courses]['gp_course_hour'])
            course_hour_list.append(data[student_id[0]]['courses'][courses]['course_hour'])
        
        cpga[0] = sum(gp_course_hour_list) / sum(course_hour_list)
        print("Your CPGA for all subjects is %.4f"%cpga[0])

"""[Variables]
"""
valid_course_code = [""]
subject = ["",""]

def validation_course_code():

    # Science Stream
    if student_stream[0] == "1":
        if course_code[0] in ("FHHM1022","FHEL1012","FHMM1014","FHMM1024","FHMM1034","FHSC1124","FHSC1114","FHSC1214","FHSC1134","FHSC1224","FHSC1234","FHSP1014","FHSP1024","FHCT1022"):
            valid_course_code[0] = True
            if course_code[0] == "FHHM1022":
                subject[0] = "Effective Communication Skills"
            elif course_code[0] == "FHEL1012":
                subject[0] = "English for Academic Study"
            elif course_code[0] == "FHMM1014":
                subject[0] = "Mathematics I"
            elif course_code[0] == "FHMM1024":
                subject[0] = "Mathematics II"
            elif course_code[0] == "FHMM1034":
                subject[0] = "Mathematics III"
            elif course_code[0] == "FHSC1124":
                subject[0] = "Organic Chemistry"
            elif course_code[0] == "FHSC1114":
                subject[0] = "Physical Chemistry"
            elif course_code[0] == "FHSC1214":
                subject[0] = "Fundamentals of Cell Biology"
            elif course_code[0] == "FHSC1134":
                subject[0] = "Inorganic Chemistry"
            elif course_code[0] == "FHSC1224":
                subject[0] = "Introduction to Physiological Systems"
            elif course_code[0] == "FHSC1234":
                subject[0] = "Modern Biology"
            elif course_code[0] == "FHSP1014":
                subject[0] = "Physics I"
            elif course_code[0] == "FHSP1024":
                subject[0] = "Physics II"
            elif course_code[0] == "FHCT1022":
                subject[0] = "Programming Concepts"
        
        else:
            valid_course_code[0] = False

    elif student_stream[0] == "2":
        if course_code[0] in ("FHHM1022","FHEL1012","FHMM1014","FHMM1024","FHMM1034","FHSC1124","FHSC1114","FHSC1014","FHSC1024","FHSC1034","FHSC1134","FHCT1022","FHSB1214","FHSB1224","FHSB1214"):
            valid_course_code[0] = True
            if course_code[0] == "FHHM1022":
                subject[0] = "Effective Communication Skills"
            elif course_code[0] == "FHEL1012":
                subject[0] = "English for Academic Study"
            elif course_code[0] == "FHMM1014":
                subject[0] = "Mathematics I"
            elif course_code[0] == "FHMM1024":
                subject[0] = "Mathematics II"
            elif course_code[0] == "FHMM1034":
                subject[0] = "Mathematics III"
            elif course_code[0] == "FHSC1124":
                subject[0] = "Organic Chemistry"
            elif course_code[0] == "FHSC1114":
                subject[0] = "Physical Chemistry"
            elif course_code[0] == "FHSC1014":
                subject[0] = "Mechanics"
            elif course_code[0] == "FHSC1024":
                subject[0] = "Thermodynamics and Electromagnetism"
            elif course_code[0] == "FHSC1034":
                subject[0] = "Waves and Modern Physics"
            elif course_code[0] == "FHSC1134":
                subject[0] = "Inorganic Chemistry"
            elif course_code[0] == "FHCT1022":
                subject[0] = "Programming Concepts"
            elif course_code[0] == "FHSB1214":
                subject[0] = "Biology I"
            elif course_code[0] == "FHSB1224":
                subject[0] = "Biology II"

        else:
            valid_course_code[0] = False
    
    elif student_stream[0] == "3":
        if course_code[0] in ("FHHM1022","FHEL1012","FHMM1014","FHMM1024","FHMM1034","FHSC1124","FHSC1114","FHCT1012","FHCT1014","FHCT1024","FHBM1114","FHSC1014","FHSC1024"):
            valid_course_code[0] = True
            if course_code[0] == "FHHM1022":
                subject[0] = "Effective Communication Skills"
            elif course_code[0] == "FHEL1012":
                subject[0] = "English for Academic Study"
            elif course_code[0] == "FHMM1014":
                subject[0] = "Mathematics I"
            elif course_code[0] == "FHMM1024":
                subject[0] = "Mathematics II"
            elif course_code[0] == "FHMM1034":
                subject[0] = "Mathematics III"
            elif course_code[0] == "FHSC1124":
                subject[0] = "Organic Chemistry"
            elif course_code[0] == "FHSC1114":
                subject[0] = "Physical Chemistry"
            elif course_code[0] == "FHCT1012":
                subject[0] = "Computing Technology"
            elif course_code[0] == "FHCT1014":
                subject[0] = "Introduction to Data Analytics"
            elif course_code[0] == "FHCT1024":
                subject[0] = "Programming Concepts and Design"
            elif course_code[0] == "FHBM1114":
                subject[0] = "Management"
            elif course_code[0] == "FHSC1014":
                subject[0] = "Mechanics"
            elif course_code[0] == "FHSC1024":
                subject[0] = "Thermodynamics and Electromagnetism"
            elif course_code[0] == "FHSB1214":
                subject[0] = "Biology I"
        
        else:
            valid_course_code[0] = False

    #Arts Stream
    elif student_stream[0] == "4":
        if course_code[0] in ("FHEL1024","FHCT1012","FHHM1012","FHHM1022","FHEL1134","FHEL1114","FHBM1114","FHBM1124","FHBM1214","FHBM1224","FHMM1314","FHMM1324","FHBM1024","FHBM1014"):
            valid_course_code[0] = True
            if course_code[0] == "FHEL1024":
                subject[0] = "Academic English"
            elif course_code[0] == "FHCT1012":
                subject[0] = "Computing Technology"
            elif course_code[0] == "FHHM1012":
                subject[0] = "Critical Thinking"
            elif course_code[0] == "FHHM1022":
                subject[0] = "Effective Communication Skills"
            elif course_code[0] == "FHEL1134":
                subject[0] = "English for Business Communication"
            elif course_code[0] == "FHEL1114":
                subject[0] = "English Language Proficiency"
            elif course_code[0] == "FHBM1114":
                subject[0] = "Management"
            elif course_code[0] == "FHBM1124":
                subject[0] = "Marketing"
            elif course_code[0] == "FHBM1214":
                subject[0] = "Financial Accounting"
            elif course_code[0] == "FHBM1224":
                subject[0] = "Financial Management"
            elif course_code[0] == "FHMM1314":
                subject[0] = "Mathematics for Business I"
            elif course_code[0] == "FHMM1324":
                subject[0] = "Mathematics for Business II"
            elif course_code[0] == "FHBM1024":
                subject[0] = "Microeconomics and Macroeconomics"
            elif course_code[0] == "FHBM1014":
                subject[0] = "Principles of Economics"
        
        else:
            valid_course_code[0] = False

    elif student_stream[0] == "5":
        if course_code[0] in ("FHEL1024","FHCT1012","FHHM1012","FHHM1022","FHEL1134","FHEL1114","FHBM1114","FHBM1124","FHHM1134","FHHM1114","FHMM1214"):
            valid_course_code[0] = True
            if course_code[0] == "FHEL1024":
                subject[0] = "Academic English"
            elif course_code[0] == "FHCT1012":
                subject[0] = "Computing Technology"
            elif course_code[0] == "FHHM1012":
                subject[0] = "Critical Thinking"
            elif course_code[0] == "FHHM1022":
                subject[0] = "Effective Communication Skills"
            elif course_code[0] == "FHEL1134":
                subject[0] = "English for Business Communication"
            elif course_code[0] == "FHEL1114":
                subject[0] = "English Language Proficiency"
            elif course_code[0] == "FHBM1114":
                subject[0] = "Management"
            elif course_code[0] == "FHBM1124":
                subject[0] = "Marketing"
            elif course_code[0] == "FHHM1134":
                subject[0] = "Introduction to Social Psychology"
            elif course_code[0] == "FHHM1114":
                subject[0] = "Introduction to Sociology"
            elif course_code[0] == "FHMM1214":
                subject[0] = "Mathematics for Social Science"
                '''
            elif course_code[0] == "XXXXXXXX":
                subject[0] = "Introduction to Chinese Literature"
            elif course_code[0] == "XXXXXXXX":
                subject[0] = "Introduction to Chinese Writing"
            elif course_code[0] == "XXXXXXXX":
                subject[0] = "Selected Texts of Modern Chinese Literature"
                '''
        
        elif course_code[0] == "XXXXXXXX":
            valid_course_code[0] = False
            input("\tSorry to say that the following subjects haven't been registered yet ...\n\tIntroduction to Chinese Literature\n\tIntroduction to Chinese Writing\n\tSelected Texts of Modern Chinese Literature\n\tPress ...Enter... to continue ...\n\t")
        
        else:
            valid_course_code[0] = False

    elif student_stream[0] == "6":
        if course_code[0] in ("FHEL1024","FHCT1012","FHHM1012","FHHM1022","FHEL1134","FHEL1114","FHBM1114","FHBM1124","FHHM1134","FHHM1114","FHMM1214","FHBM1024","FHBM1014","FHHM1124"):
            valid_course_code[0] = True
            if course_code[0] == "FHEL1024":
                subject[0] = "Academic English"
            elif course_code[0] == "FHCT1012":
                subject[0] = "Computing Technology"
            elif course_code[0] == "FHHM1012":
                subject[0] = "Critical Thinking"
            elif course_code[0] == "FHHM1022":
                subject[0] = "Effective Communication Skills"
            elif course_code[0] == "FHEL1134":
                subject[0] = "English for Business Communication"
            elif course_code[0] == "FHEL1114":
                subject[0] = "English Language Proficiency"
            elif course_code[0] == "FHBM1114":
                subject[0] = "Management"
            elif course_code[0] == "FHBM1124":
                subject[0] = "Marketing"
            elif course_code[0] == "FHHM1134":
                subject[0] = "Introduction to Social Psychology"
            elif course_code[0] == "FHHM1114":
                subject[0] = "Introduction to Sociology"
            elif course_code[0] == "FHMM1214":
                subject[0] = "Mathematics for Social Science"
            elif course_code[0] == "FHBM1024":
                subject[0] = "Microeconomics and Macroeconomics"
            elif course_code[0] == "FHBM1014":
                subject[0] = "Principles of Economics"
            elif course_code[0] == "FHHM1124":
                subject[0] = "Socialization as a Process "

        else:
            valid_course_code[0] = False

    elif student_stream[0] == "7":
        if course_code[0] in ("FHEL1024","FHCT1012","FHHM1012","FHHM1022","FHEL1134","FHEL1114","FHBM1114","FHBM1124","FHAD1024","FHAD1014","FHAD1034","FHHM1134","FHHM1114","FHMM1214"):
            valid_course_code[0] = True
            if course_code[0] == "FHEL1024":
                subject[0] = "Academic English"
            elif course_code[0] == "FHCT1012":
                subject[0] = "Computing Technology"
            elif course_code[0] == "FHHM1012":
                subject[0] = "Critical Thinking"
            elif course_code[0] == "FHHM1022":
                subject[0] = "Effective Communication Skills"
            elif course_code[0] == "FHEL1134":
                subject[0] = "English for Business Communication"
            elif course_code[0] == "FHEL1114":
                subject[0] = "English Language Proficiency"
            elif course_code[0] == "FHBM1114":
                subject[0] = "Management"
            elif course_code[0] == "FHBM1124":
                subject[0] = "Marketing"
            elif course_code[0] == "FHAD1024":
                subject[0] = "Analytical Drawing"
            elif course_code[0] == "FHAD1014":
                subject[0] = "Design Fundamentals"
            elif course_code[0] == "FHAD1034":
                subject[0] = "Figure Drawing"
            elif course_code[0] == "FHHM1134":
                subject[0] = "Introduction to Social Psychology"
            elif course_code[0] == "FHHM1114":
                subject[0] = "Introduction to Sociology"
            elif course_code[0] == "FHMM1214":
                subject[0] = "Mathematics for Social Science"
        
        else:
            valid_course_code[0] = False

"""[Variables]
"""
valid_mark = [""]
mark = ["",""]
grade = ["",""]
point = [0,0]
numbers = [str(numbers).zfill(1) for numbers in range(0,101)]

def validation_mark():
    if mark[0] in numbers:
        valid_mark[0] = True
        mark[0] = int(mark[0])
        if 100 >= mark[0] >= 90:
            grade[0] = "A+"
            point[0] = 4.00
        elif 90 > mark[0] >= 80:
            grade[0] = "A"
            point[0] = 4.00
        elif 80 > mark[0] >= 70:
            grade[0] = "A-"
            point[0] = 3.67
        elif 70 > mark[0] >= 65:
            grade[0] = "B+"
            point[0] = 3.33
        elif 65 > mark[0] >= 60:
            grade[0] = "B"
            point[0] = 3.00
        elif 60 > mark[0] >= 55:
            grade[0] = "B-"
            point[0] = 2.67
        elif 55 > mark[0] >= 50:
            grade[0] = "C+"
            point[0] = 2.33
        elif 50 > mark[0] >= 40:
            grade[0] = "C"
            point[0] = 2.00
        elif 40 > mark[0] >= 0:
            grade[0] = "F"
            point[0] = 0.00
    else:
        valid_mark[0] = False

"""[Variables]
"""
edit_bool = ["",""]
course_code = ["",""]
course_hour = [0,0]
gp_list = [0,0,0,0,0,0,0,0,0,0,2.0,2.3333,2.6667,3.0,3.3333,3.6667,4.0,4.0,4.0,4.0,4.0]
gp = [0,0]
gp_course_hour = [0,0]

def key_in_courses():
    loop[3] = True
    while loop[3]:
        key_in_student_details()
        print_student_stream()
        print("\n")
        print_courses()
        print("\n")
        calculate_CPGA()
        print("\n")
        course_code[0] = input("Please enter your course code : (Enter 'X' to exit to menu) ")
        if course_code[0].upper() == "X":
            loop[3] = False

        else:
            validation_course_code()
            if valid_course_code[0] == True:

                if data[student_id[0]]['courses'] == None:
                        loop[7] == True
                        while loop[7]:
                            mark[0] = input("Please enter your mark : (Enter 'X' to cancel) ")
                            if mark[0].upper() == "X":
                                loop[7] = False

                            else:
                                validation_mark()
                                if valid_mark[0] == True:
                                    loop[7] = False
                                    course_hour[0] = int(course_code[0][-1])
                                    gp[0] = gp_list[mark[0] // 5]
                                    gp_course_hour[0] = gp[0] * course_hour[0]
                                    data[student_id[0]]['courses'] = {course_code[0]:{
                                        'subject': subject[0], 
                                        'mark': mark[0], 
                                        'grade': grade[0], 
                                        'point': point[0], 
                                        'course_hour': course_hour[0], 
                                        'gp': gp[0], 
                                        'gp_course_hour': gp_course_hour[0]}}

                                else: # valid_mark[0] == False
                                    input("The range of marks only between 0 - 100 , \nPress ...Enter... to continue ...")

                else:
                    if course_code[0] in data[student_id[0]]['courses'].keys():
                        edit_bool[0] = input("The course code you just entered already exists !!!\nDo you want to edit its value ? : (y/N) ")
                        if edit_bool[0].upper() not in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                            input("Seems you had entered any else keys, by default we cancelled your replacement method ...\nPress ...Enter... to continue ...")
                        elif edit_bool[0].upper() in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                            edit_bool[0] = strtobool(edit_bool[0])
                            if edit_bool[0] == True:
                                course_code[1] = course_code[0]
                                subject[1] = data[student_id[0]]['courses'][course_code[0]]['subject']
                                mark[1] = data[student_id[0]]['courses'][course_code[0]]['mark']
                                grade[1] = data[student_id[0]]['courses'][course_code[0]]['grade']
                                point[1] = data[student_id[0]]['courses'][course_code[0]]['point']
                                course_hour[1] = data[student_id[0]]['courses'][course_code[0]]['course_hour']
                                gp[1] = data[student_id[0]]['courses'][course_code[0]]['gp']
                                gp_course_hour[1] = data[student_id[0]]['courses'][course_code[0]]['gp_course_hour']

                                loop[4] = True
                                while loop[4]:
                                    key_in_student_details()
                                    print_student_stream()
                                    print("\n")
                                    print_courses()
                                    print("\n")
                                    calculate_CPGA()
                                    print("\n")
                                    course_code[0] = input("Please enter your new course code replacement for %s :\n(Enter 'X' to cancel) "%course_code[1])
                                    if course_code[0].upper() == "X":
                                        loop[4] = False

                                    elif (course_code[0] == course_code[1]) or (course_code[0] not in data[student_id[0]]['courses'].keys()):
                                        validation_course_code()
                                        if valid_course_code[0] == True:
                                            loop[5] = True
                                            while loop[5]:
                                                mark[0] = input("Please enter your mark replacement for %s :\n(Enter 'X' to cancel) "%course_code[1])
                                                if mark[0].upper() == "X":
                                                    loop[4] = False
                                                    loop[5] = False

                                                else:
                                                    validation_mark()
                                                    if valid_mark[0] == True:
                                                        loop[4] = False
                                                        loop[5] = False
                                                        course_hour[0] = int(course_code[0][-1])
                                                        gp[0] = gp_list[mark[0] // 5]
                                                        gp_course_hour[0] = gp[0] * course_hour[0]

                                                        del data[student_id[0]]['courses'][course_code[1]]
                                                        data[student_id[0]]['courses'][course_code[0]] = {
                                                            'subject': subject[0], 
                                                            'mark': mark[0], 
                                                            'grade': grade[0], 
                                                            'point': point[0], 
                                                            'course_hour': course_hour[0], 
                                                            'gp': gp[0], 
                                                            'gp_course_hour': gp_course_hour[0]}

                                                    else: # valid_mark[0] == False
                                                        input("The range of marks only between 0 - 100 , \nPress ...Enter... to continue ...")

                                        else: # valid_course_code[0] == False
                                            input("Invalid Course Code ... Please enter again ...\nPress ...Enter... to continue ...")

                                    elif course_code[0] in data[student_id[0]]['courses'].keys():
                                        input("You have enter a same subject twice ...\nPress ...Enter... to enter course code again ...")

                    elif course_code[0] not in data[student_id[0]]['courses'].keys():
                        loop[6] = True
                        while loop[6]:
                            mark[0] = input("Please enter your mark : (Enter 'X' to cancel) ")
                            if mark[0].upper() == "X":
                                loop[6] = False

                            else:
                                validation_mark()
                                if valid_mark[0] == True:
                                    loop[6] = False
                                    course_hour[0] = int(course_code[0][-1])
                                    gp[0] = gp_list[mark[0] // 5]
                                    gp_course_hour[0] = gp[0] * course_hour[0]
                                    data[student_id[0]]['courses'][course_code[0]] = {
                                        'subject': subject[0], 
                                        'mark': mark[0], 
                                        'grade': grade[0], 
                                        'point': point[0], 
                                        'course_hour': course_hour[0], 
                                        'gp': gp[0], 
                                        'gp_course_hour': gp_course_hour[0]}

                                else: # valid_mark[0] == False
                                    input("The range of marks only between 0 - 100 , \nPress ...Enter... to continue ...")

            else: # valid_course_code[0] == False
                input("Invalid Course Code ... Please enter again ...\nPress ...Enter... to continue ...")

"""[Variables]
"""    
student_id = [0]
student_name = [""]
student_stream = [""]
student_password = ["","",""]

def key_in_student_details():
    loop[1] = True
    while loop[1]:

        # If student id haven't entered before ...
        if student_id[0] == 0:
            loop[17] = True
            while loop[17]:
                clear_screen()
                print("\t"+"-"*40+"\n\t\tWelcome To CPGA Calculator\n\t\tFor UTAR University\n"+"\t"+"-"*40)

                try:
                    student_id[0] = str(int(input("Please enter your UTAR student ID : ")))
                    loop[17] = False
                except:
                    input("Student ID only accept integers ... Press ...Enter... to reenter ...")
            
            # If id exists in data
            if student_id[0] in data.keys():
                student_password[1] = data[student_id[0]]['student_password']

                if student_password[1] == None:
                    student_name[0] = data[student_id[0]]['student_name']
                    student_stream[0] = data[student_id[0]]['student_stream']

                elif student_password[1] != None:
                    loop[8] = True
                    while loop[8]:
                        student_password[0] = getpass("Please enter your password : ")
                        if student_password[0] == student_password[1]:
                            loop[8] = False
                            student_name[0] = data[student_id[0]]['student_name']
                            student_stream[0] = data[student_id[0]]['student_stream']
                        
                        else:
                            print("Incorrect password, Please enter again ...")

            # Else if id not exists in data
            elif student_id[0] not in data.keys():
                student_name[0] = input("Looks like you're new to here ,\nPlease enter your FULL NAME : ")
                
                # Check if student stream entered in the range of 1 - 7
                loop[2] = True
                while loop[2]:
                    student_stream[0] = input("Please enter your chosen stream : (Range Between 1 - 7) ")
                    if student_stream[0] in ("1","2","3","4","5","6","7"):
                        loop[2] = False
                    else:
                        input("Invalid stream ... Reinput again ...\nPress Enter to continue ...")
                        clear_screen()
                        print("\t"+"-"*40+"\n\t\tWelcome To CPGA Calculator\n\t\tFor UTAR University\n"+"\t"+"-"*40)
                        print("\tYou're now registering new student as %s"%student_name[0])
                        print("\t\tID : %s"%student_id[0])
                
                # Create a new key for new student
                student_password[1] = None
                data[student_id[0]] = {
                    'student_name' : student_name[0], 
                    'student_stream' : student_stream[0],
                    'student_password' : student_password[1], 
                    'courses' : None}
        
        # Everything variable works valid , time to print student details out ...
        else:
            loop[1] = False
            clear_screen()
            print("\t"+"-"*40+"\n\t\tWelcome To CPGA Calculator\n\t\tFor UTAR University\n"+"\t"+"-"*40)
            print("\t    You're now logged in as %s"%data[student_id[0]]['student_name'])
            print("\t\tID : %s"%student_id[0])

"""[Variables]
"""    
options = ["","",""]
new_student_id = [""]
new_student_name = [""]
new_student_stream = [""]

def edit_student_details():
    loop[13] = True
    while loop[13]:
        key_in_student_details()

        # Options
        print("\t"+"-"*40+"\n\t"+"Please choose one option from below ..."+"\n\t"+"-"*40)
        print("\n\t1. Student ID")
        print("\n\t2. Student Name")
        print("\n\t3. Student Stream")
        print("\n\t4. Account Password")
        print("\n\n\t0. Save and Exit to main menu\n\n")

        options[1] = input("Please select an option : ")
        if options[1] in ("0","1","2","3","4"):
            if options[1] == "0":
                loop[13] = False
                export_student_data()

            elif options[1] == "1":
                loop[14] = True
                while loop[14]:
                    key_in_student_details()
                    edit_bool[1] = input("\nAre you really sure you want to edit your STUDENT ID ?\nTHIS CANNOT BE UNDONE !! : (y/N) ")

                    if edit_bool[1].upper() not in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                        input("Seems you had entered any else keys ...\nPress ...Enter... to input again ...")

                    elif edit_bool[1].upper() in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                        edit_bool[1] = strtobool(edit_bool[1])
                        if edit_bool[1] == True:
                            loop[14] = False
                            loop[17] = True
                            while loop[17]:
                                try:
                                    key_in_student_details()
                                    new_student_id[0] = str(int(input("\nPlease enter your NEW UTAR student ID : ")))
                                    loop[17] = False
                                except:
                                    input("Student ID only accept integers ... Press ...Enter... to reenter ...")

                            data[new_student_id[0]] = data.pop(student_id[0])
                            student_id[0] = new_student_id[0]
                            key_in_student_details()
                            input("\nYou had successfully changed your Student ID . . .\nPress ...Enter... to continue ...")

                        elif edit_bool[1] == False:
                            loop[14] = False

            elif options[1] == "2":
                loop[14] = True
                while loop[14]:
                    key_in_student_details()
                    edit_bool[1] = input("\nAre you really sure you want to edit your STUDENT NAME ?\nTHIS CANNOT BE UNDONE !! : (y/N) ")

                    if edit_bool[1].upper() not in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                        input("Seems you had entered any else keys ...\nPress ...Enter... to input again ...")

                    elif edit_bool[1].upper() in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                        edit_bool[1] = strtobool(edit_bool[1])
                        if edit_bool[1] == True:
                            loop[14] = False
                            key_in_student_details()
                            new_student_name[0] = input("\nPlease enter your NEW UTAR student name : ")
                            data[student_id[0]]['student_name'] = new_student_name[0]
                            student_name[0] = new_student_name[0]
                            key_in_student_details()
                            input("\nYou had successfully changed your Student Name . . .\nPress ...Enter... to continue ...")

                        elif edit_bool[1] == False:
                            loop[14] = False

            elif options[1] == "3":
                loop[14] = True
                while loop[14]:
                    key_in_student_details()
                    edit_bool[1] = input("\nAre you really sure you want to edit your STUDENT STREAM ?\n"+"-"*72+"\nNOTE THAT ALL YOUR PREVIOUS ENTERED COURSES RECORD WILL ALL BE RESET !!!\n"+"-"*72+"\nTHIS CANNOT BE UNDONE !! : (y/N) ")

                    if edit_bool[1].upper() not in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                        input("Seems you had entered any else keys ...\nPress ...Enter... to input again ...")

                    elif edit_bool[1].upper() in ("Y","YES","T","TRUE","ON","1","N","NO","F","FALSE","OFF","0"):
                        edit_bool[1] = strtobool(edit_bool[1])
                        if edit_bool[1] == True:
                            loop[14] = False
                            loop[15] = True
                            while loop[15]:
                                key_in_student_details()
                                new_student_stream[0] = input("\nPlease enter your NEW UTAR student stream : (Range Between 1 - 7) ")
                                if new_student_stream[0] in ("1","2","3","4","5","6","7"):
                                    loop[15] = False
                                else:
                                    input("Invalid stream ... Reinput again ...\nPress Enter to continue ...")

                            data[student_id[0]]['student_stream'] = new_student_stream[0]
                            student_stream[0] = new_student_stream[0]
                            data[student_id[0]]['courses'] = None
                            key_in_student_details()
                            input("\nYou had successfully changed your Student Stream . . .\nPress ...Enter... to continue ...")

                        elif edit_bool[1] == False:
                            loop[14] = False

            elif options[1] == "4":
                key_in_student_details()
                if student_password[1] != None:
                    loop[9] = True
                    while loop[9]:
                        student_password[0] = getpass("\nPlease enter your previous password : ")
                        if student_password[0] == student_password[1]:
                            loop[9] = False
                            loop[10] = True
                            while loop[10]:
                                student_password[0] = getpass("\nPlease enter your new password : ")
                                student_password[2] = getpass("\nPlease reenter your new password : ")
                                if student_password[2] == student_password[0]:
                                    loop[10] = False
                                    student_password[1] = student_password[2]
                                    data[student_id[0]]['student_password'] = student_password[1]
                                    input("Your password has been successfully changed\nPress ...Enter... to continue ...")

                                else:
                                    print("The password you just entered was incorrect ! ...\nPress ...Enter... to continue ...")
                                    key_in_student_details()
                        
                        else:
                            input("Incorrect password, Please enter again ...\nPress ...Enter... to continue ...")
                            key_in_student_details()
                
                elif student_password[1] == None:
                    loop[11] = True
                    while loop[11]:
                        student_password[0] = getpass("Please enter your new password : ")
                        student_password[2] = getpass("Please reenter your new password : ")
                        if student_password[2] == student_password[0]:
                            loop[11] = False
                            student_password[1] = student_password[2]
                            data[student_id[0]]['student_password'] = student_password[1]
                            input("Your password has been successfully changed\nPress ...Enter... to continue ...")

                        else:
                            input("The password you just entered was incorrect ! ...\nPress ...Enter... to continue ...")
                            key_in_student_details()

        else:
            input("Invalid options ... Reinput again ...\nPress ...Enter... to continue")

def export_student_data():
    with open (os.path.join(sys.path[0], 'data.json'), 'w', encoding ='utf8') as final_data:
        json.dump(data, final_data, indent = 4, ensure_ascii = True)
    final_data.close()

"""[SCRIPT START HERE]
"""
# Import student data
loop[12] = True
while loop[12]:
    try:
        with open (os.path.join(sys.path[0], 'data.json'), 'r') as initial_data:
            if os.stat(os.path.join(sys.path[0], 'data.json')).st_size != 0:
                data = json.loads(initial_data.read())
                initial_data.close()
                loop[12] = False
            else:
                data = {}
                initial_data.close()
                loop[12] = False

    except FileNotFoundError:
        with open (os.path.join(sys.path[0], 'data.json'), 'w+') as empty:
            empty.close()

loop[0] = True
while loop[0]:
    key_in_student_details()
    print_student_stream()
    
    # Options
    print("\t"+"-"*40+"\n\t\t\t"+"Menu"+"\n\t"+"-"*40)
    print("\n\t1. Edit your course marks")
    print("\n\t2. Edit your account")
    print("\n\t3. Print all courses and stuff")
    print("\n\t4. Any bugs or suggestions, Please create issues on official github\n\thttps://github.com/Fubuki-the-fox-girl/Yuuki/tree/main/Python/Assignment")
    print("\n\n\t0. Exit the program\n\n")

    options[0] = input("Please select an option : ")
    if options[0] in ("0","1","2","3","4"):
        if options[0] == "0":
            loop[0] = False
            export_student_data()
            clear_screen()

        elif options[0] == "1":
            try:
                key_in_courses()
                export_student_data()
            except:
                input("Error occured ...\nPress ...Enter... back to menu ...")

        elif options[0] == "2":
            try:
                edit_student_details()
                export_student_data()
            except:
                input("Error occured ...\nPress ...Enter... back to menu ...")

        elif options[0] == "3":
            try:
                print_all()
                export_student_data()
            except:
                input("Error occured ...\nPress ...Enter... back to menu ...")

        elif options[0] == "4":
            try:
                url = 'https://github.com/Fubuki-the-fox-girl/Yuuki/tree/main/Python/Assignment'
                webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)
            except:
                input("Error occured ...\nPress ...Enter... back to menu ...")

    else:
        input("Invalid options ... Reinput again ...\nPress ...Enter... to continue")
