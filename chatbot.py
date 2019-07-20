#program to build a responsive bot
#created by:sahil agarwal
#date:13 march,2019

#import json to parse the input file .json so that we can make a more automatic system
import json
import itertools
import numpy as np

#stage variable to divide the given json format into stages as explained in the response file
#var_in is a variable to store the response submitted by the user
stage=[]
var_in={}
connected_variable=True
#load the json file into a variable data so that as to parse it
#also the directory of the python script and the json file should be similar
data=json.load(open("assignment_1_input_2.json"))
query=data["questions"]

#this loop will return a list of dictionaries with each dictionary representing a particular stage
for i in range(len(query)):
    if len(query[i])==1:
        substage=[]
        substage.append(query[i])
        stage.append(substage)
    elif len(query[i])>=1 :
        substage=[]
        temp=iter(query[i].items())
        substage.append(dict(itertools.islice(temp,(len(query[i])-1))))
        substage.append(dict(iter(temp)))
        stage.append(substage)

#slicing the stage variable to ensure the quality parsing of the file
stage1=stage[0:7]
stage2=stage[7:]

#main function dealing with the responsive input output
var=0
while var<(len(stage1)):                                  
    for index in stage1[var]:                       #index will contain each dictionary in the stage[i] of list
        for key,txt in index.items():               #extracting the key and value from the dictionary
            if key!="var" and key!="conditions":
                print(txt)
            elif key=="var":
                var_in[txt]=input()
            if txt=="age" and var_in[txt].isdigit()==True:
                var=var+1
            elif txt=="age" and var_in[txt].isdigit()==False:
                pass

    var+=1            
    
if txt=="Congratulations! Registration Successful.": 
        connected_variable=True                         #on successful registration,connected_variable is assigned a true value



#this set of code deals with theafter events of registration        
print()
matrix=[]
flag=0
if connected_variable==True:
    full_name= var_in["first_name"] + ' ' + var_in["last_name"]
    for var in range(len(stage2)):
        for index in stage2[var]:
            for key,txt in index.items():
                if key=="instruction":
                    if flag==0:
                        print(txt % full_name)
                        flag+=1
                    elif flag==1:
                        print(txt)
                    else:
                        continue
                elif key=="text":
                    print(txt)
                    temp=(input())
                    matrix.append(list(temp.split(" ")))
                    
                elif key=="var":
                    var_in[txt]=txt            
#prints the transpose of he input matrix
print(np.array(matrix).T)                    
                    
                    
                



        
           
               
