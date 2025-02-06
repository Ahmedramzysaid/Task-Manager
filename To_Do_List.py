#  start 


# dictionary  ---- > Your Tasks 
Tasks = {
    
   # "Task 1" : "I read roses from the Quran" ,
    #  "Task 2": "complete my course" ,
    #"Task 3" : "solve problems about STLs" ,
}


while (True) :
        # collection --- > commands . 
    Commands = {
    "Add": "Add a new task",
    "Remove": "Remove a task",
    "View": "View all tasks",
    "Exist": "Exit the program"
    }
    
    print("choose your command" ) ;
    print (Commands) ;

     
    # number tasks  
    number_Task = Tasks.__len__()+1 ;
    
    
    # select your command
    command =  input("Entre your command : ") ;    
    command = command.capitalize() ;  # if users entre word wrong 
    
    if (command ==  'View'):  # print all tasks 
        if (Tasks.__len__() == 0 ):
            print("No There any task")
        else :
            print(Tasks) ;
        
        
        
    elif(command == 'Add') : # to add New task 

        Tasks[f"Task {++number_Task}"] =input("Entre your task : ")
        print("Task is added")
        print(Tasks)
        
# remove any to task   . you completed
      
    elif(command == "Remove") :  
        
# if exist task in the dictionary Tasks or not 
         if (Tasks.__len__()== 0) :
             print("No There any task")
         else :
           task_to_remove = input("Entre the task want to remove : ")
           if task_to_remove not in Tasks :
               print("There task not exist .")
           else:
               del Tasks[task_to_remove]
           print(Tasks)
           
           

           
# if he want to exist  from  program
    elif (command == "Exist"):
        print("Exist the program .")
        break ;
    
# if he write command not exist in the commands
    else :
        print ("Invalid  the command / option ")
    
# notes
# I use function ------> __len__() 
# to return  size  ------ > dictionary  (Tasks) 


  
  
                               # End 