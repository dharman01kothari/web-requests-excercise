# get_data.py
import requests
import json

if __name__=="__main__":
    print("\nREQUESTING SOME DATA FROM THE INTERNET...\n\n")
    
    #-------------Part 1------------------
    request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
    
    response = requests.get(request_url)
    response_data = json.loads(response.text)
    
    print('For part 1')
    print(response_data['name'])
    print('\n**********************************\n\n')

    #-------------Part 2------------------

    request2_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"

    resp = requests.get(request2_url)
    resp_data = json.loads(resp.text)

    i = 0
    print('For part 2')
    
    while i != len(resp_data):
        print('Name:',resp_data[i]['name'],' ','ID:',resp_data[i]['id'])
        i = i + 1

    print('\n**********************************\n\n')

    #-------------Part 3------------------

    request3_url='https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json'

    student = requests.get(request3_url)
    student_data = json.loads(student.text)

    x = 0
    scores=[]
    
    print('For part 3')

    while x != len(student_data['students']):
       scores.append(student_data['students'][x]['finalGrade'])
       x = x + 1

    print('For the scores in the webpage:')
    print("Min Score is:",min(scores))
    print("Max Score is:",max(scores))
    Mean = sum(scores)/len(scores)
    print("Average Score is:", Mean)
    print('\n*******************************\n\n')

