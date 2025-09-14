let form
document.addEventListener("DOMContentLoaded", function() {
    form = document.getElementById("questionForm")
    form.addEventListener("submit", function(e) {
        e.preventDefault()
        var data = new FormData(form)
        let answer

        for (var pair of data.entries()) {
            if (pair[0] == "listGroupRadio") {
                answer = pair[1]
            }
            else {
                console.log("An error occured or an invalid input was submitted")
            }
        }

        if (answer == document.getElementById("answer").innerText.trim()) {
            console.log("Correct!!")
            // Change CSS of answerchoice to greem
        }
        else {
            console.log("Wrong 3:")
            // Change CSS of answer choice to red
        }
    })
})

/*
    TODO: 
    - Get input sent through form
    - Check if input and answer match
    - If they do, change CSS of answer choice to Green
    - If not, change CSS of answer choice to red
*/