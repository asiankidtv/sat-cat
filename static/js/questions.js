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
        
        const questionChoice = document.getElementById("answer" + answer).parentElement


        if (answer == document.getElementById("answer").innerText.trim()) {
            console.log("Correct!!")
            questionChoice.style.color = "green"
        }
        else {
            console.log("Wrong 3:")
            questionChoice.style.color = "red"
        }
    })
})