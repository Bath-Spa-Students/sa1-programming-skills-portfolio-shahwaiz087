#steps
#1 Create an application that requires the user to answer the question, "What is the capital of France?"then you wait for their response
#2 If the user types the correct response ("Paris"), the application need to show that the message entered is correct
#3 It would print incorrectly if the response was incorrect

#presenting the variable query
Answer = input("What is the capital of France?:")
if Answer =="Paris" : #choosing the response to the query
    print("the answer is correct :) ") #It is accurate if the response is in Paris
else:
    print("the answer is wrong :( .") #If it is anything other than Paris, the response is incorrect and ought to be written