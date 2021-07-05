def arithmetic_arranger(problems, *result):
  arranged_problems = "";
  firstnum = [];
  signs = [];
  secondnum = [];
  if(len(problems) > 5):
    return "Error: Too many problems."

  #splitting the problems into first number sign and second number checking if they are correct
  for i in problems:
    [num1, sign, num2] = i.split(" ")
    if(len(num1) > 4 or len(num2) > 4):
      return "Error: Numbers cannot be more than four digits."
    elif(sign != "+" and sign != "-"):
      return "Error: Operator must be '+' or '-'."
    elif(not num1.isdigit() or not num2.isdigit()):
      return "Error: Numbers must only contain digits."
    else:
      #arranged_problems = arranged_problems + " "*3 + num1 + " "*3
      firstnum.append(num1);
      signs.append(sign)
      secondnum.append(num2);

  #dealing with the spacing for the first numbers
  for i in range(len(signs)):
    if(len(secondnum[i]) >= len(firstnum[i])):    
      dis = len(secondnum[i]) + 2 - len(firstnum[i])
      arranged_problems = arranged_problems + " "*dis + firstnum[i] + " "*4
    elif(len(secondnum[i]) < len(firstnum[i])):
      dis = len(secondnum[i]) + 2 + (len(firstnum[i]) - len(secondnum[i])) - len(firstnum[i])
      arranged_problems = arranged_problems + " "*2 + firstnum[i] + " "*4      

  #dealing with the white space for the first initial number
  if(len(secondnum[0]) > len(firstnum[0])):    
    dis = len(secondnum[0]) + 2 - len(firstnum[0])
    arranged_problems = " "*dis +arranged_problems.strip() + "\n"
  elif(len(secondnum[0]) < len(firstnum[0])):
    dis = len(secondnum[0]) + 2 + (len(firstnum[0]) - len(secondnum[0])) - len(firstnum[0])
    arranged_problems = " "*dis +arranged_problems.strip() + "\n"

  #dealing with the white space for the signs and second numbers
  for i in range(len(signs)):
    if(len(firstnum[i]) > len(secondnum[i])):
      dis = len(firstnum[i]) - len(secondnum[i])+1;
      arranged_problems = arranged_problems + signs[i] + " "*dis + secondnum[i] + "    "
    elif(len(firstnum[i]) <= len(secondnum[i])):
      dis = len(secondnum[i]) - len(firstnum[i]) -1;
      arranged_problems = arranged_problems + signs[i] + " " + secondnum[i] + "    "

  #stripping the back and adding the new line
  arranged_problems = arranged_problems.rstrip() + "\n"
  
  #dealing with the length and spacing for the final bar at the bottom.
  for i in range(len(signs)):
    if(len(firstnum[i]) >= len(secondnum[i])):
      dis=len(firstnum[i])+2
      arranged_problems = arranged_problems + "-"*dis + " "*4
    else:
      dis=len(secondnum[i])+2
      arranged_problems = arranged_problems + "-"*dis + " "*4
  
  #final stripping of the function if True not added.
  arranged_problems = arranged_problems.rstrip()

  #dealing with True added.
  if(result):
    arranged_problems = arranged_problems + "\n"
    for i in range(len(signs)):
      if(signs[i] == "+"): #Positive Sign
        total = int(firstnum[i]) + int(secondnum[i]);

        #Dealing with the spacing in front and behind the answer 
        if(len(firstnum[i]) >= len(secondnum[i])):
          dis=len(firstnum[i]) - len(str(total)) + 2
          arranged_problems =  arranged_problems + " "*dis + str(total) + " "*4
        else:
          dis=len(secondnum[i]) - len(str(total)) + 2
          arranged_problems =  arranged_problems + " "*dis +  str(total) + " "*4

      else: #Negative Sign
        total = int(firstnum[i]) - int(secondnum[i]);

        #Dealing with the spacing in front and behind the answer 
        if(len(firstnum[i]) >= len(secondnum[i])):
          dis=len(firstnum[i]) - len(str(total)) + 2
          arranged_problems =  arranged_problems + " "*dis + str(total) + " "*4
        else:
          dis=len(secondnum[i]) - len(str(total)) + 2
          arranged_problems =  arranged_problems + " "*dis +  str(total) + " "*4

    #Final strip for the answer string.
    arranged_problems = arranged_problems.rstrip()
    print(arranged_problems)
    return arranged_problems
  else:
    return arranged_problems