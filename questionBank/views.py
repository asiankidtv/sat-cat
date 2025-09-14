from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from json import load
from random import randint, seed

domainKey = {
        "cas": "questionBank\English\craftAndStructure.json",
        "eoi": "questionBank\English\expressionOfIdeas.json",
        "iai": "questionBank\English\informationAndIdeas.json",
        "sec": "questionBank\English\standardEnglishConventions.json",
    }

# Create your views here.
def questionBank(request):
    return render(request, "questionBank.html")

def question(request):
    # Takes Skill type GET argument and returns a random question from the bank.

    skill = request.GET.get("type")
    chosenquestion = None


    with open(domainKey[skill], 'r', encoding="utf-8") as file:
        data = load(file)
        foundValidQuestion = False

        # Chooses a non-underline related question
        while foundValidQuestion == False:
            chosenquestion = data[randint(1, len(data))]
            if (chosenquestion["question"]["question"]).find("underlined") == -1:
                foundValidQuestion = True

        # Provides a more helpful statement if there is no stimulus    
        if chosenquestion["question"]["paragraph"] == "null":
            chosenquestion["question"]["paragraph"] = "No Stimulus for this Question :3"
    
    return render(request, "question.html", {"question": chosenquestion})


# Scrapped idea of server-side check for answers
""" 
def getAnswer(request):
    domain = request.POST("domain")
    q = request.POST("question")

    print(domain)
    print(q)

    if request.method == "POST":
        with open(domain[domain], 'r', encoding="utf-8") as file:
            data = load(file)
            for question in data:
                if question["question"]["question"] == q:
                    return HttpResponse(question["question"]["correct_answer"], RequestContext(request))
            
        return HttpResponse("NO QUESTION FOUND")
"""