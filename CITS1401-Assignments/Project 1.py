# file: Project 1.py
# By Jacob Posel



import sys
#1 opening file and testing whether it exists
def open_file(filename):
    import os
    if os.path.isfile(filename)== True:
        infile = open(filename, 'r')
        return infile
        
      
    if os.path.isfile(filename) != True:
        sys.exit('The file does not exist, start again')


   
#2 creating units list
def get_units(unitfile):
    x = [] 
    for line in unitfile:
        unit,mark = line.strip().split(',') #split lines 
        unitmarklist = [str(unit),float(mark)] #create list with unit name and mark
        x.append(tuple(unitmarklist)) #append list into a larger tuple with all unit names and marks
    return(x)
    
 
#3 creating list of student grades, whilst testing file has correct number of grades
def get_student_records(students_file, unit_count):
    final_list = []
    for line in students_file:
        templist = []
        elements = line.strip().split(',')
        if len(elements) != unit_count+1: #test correct number of units
            print("Unit count incorrect for", elements[0])
        else:
            for x in elements: #puts student names and grades into a list, if student did not complete unit, gives value 'none'
                if x.isdigit():
                    templist.append(float(x)) 
                elif x == '':
                    templist.append(None)
                else:
                    templist.append(x)
                    final_list.append(templist)
        
    return (final_list)
  
#4 normalise student marks by dividing them by max mark in unit
def normalise(students_list, units_list):
    length = len(students_list)
    for i in range(0,len(students_list)):
        for x in range(0,len(students_list[i])-1):
            normaliser = (units_list[0+x])[1] #finds max mark
            if (students_list[i+0])[1+x] != None: #finds student mark if it does not equal none
                (students_list[i+0])[1+x] = (students_list[i+0])[1+x] / normaliser #normalises mark
    return(students_list)


 
#5 add together normalised marks and calculated mean mark
def compute_mean_pc(students_pclist):
    mean_pclist = []
    length = len(students_pclist)
    for  i in range(0, length):
        average = 0
        tally = 0
        total = 0
        length1 = len(students_pclist[i])
        for x in range(0, length1-1):
            if students_pclist[i][1+x] == None:
                pass
            else:
                tally = tally + 1 #adds up number of marks
                total = total + students_pclist[i][1+x] #finds sum of marks
        if tally == 0:
            pass
        else:
            average = total/tally #finds an average by dividing sum of marks by number of marks
            mean_pclist.append([average, (students_pclist[i])[0]])
    return(mean_pclist)


#6 print out final mean mark with student names, formats marks to 3 decimal places      
def print_final_list(mean_pclist):
    length = len(mean_pclist)
    for i in range(0, length):
        t = (mean_pclist[0+i])[0]
        t = "{0:.3f}".format(t)
        print((mean_pclist[0+i])[1],t)

    
    
    
def main():
    unit = str(input('What is the name of the file with unit names and their maximum marks: '))
    unitfile = open_file(unit)
    student = str(input('What is the name of the file with student names and their grades: '))
    students_file = open_file(student)
    unit_count = len(unitfile.readlines())
    unitfile = open_file(unit)
    units_list  = get_units(unitfile)
    students_list = get_student_records(students_file, unit_count)
    students_pclist = normalise(students_list, units_list)
    mean_pclist = compute_mean_pc(students_pclist)
    print_final_list(mean_pclist)
    
main()
    
 


     
        
        
    
    
    
    
           
           
           
           
           

            
   
    
        
        
        
        
        
 
 
 
 
   
        


    
    
    
   
   
   
   

 
                
                
                     
             
            
         
        
        
                     
                
    
  

  
    
    
    
    
    
   
    
    

    
    
    
    
    
    



  
   
   


   
    
    


