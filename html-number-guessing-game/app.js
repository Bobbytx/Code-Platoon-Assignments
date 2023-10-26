let computerGuess = Math.floor(Math.random()*100)

let numberGen = (event) => {
    computerGuess = Math.floor(Math.random()*100)
    let messageOutput = document.getElementById("message")
    messageOutput.innerHTML = "Guess a number again"
}

let randomNumber = (event) => {
    event.preventDefault()
    let userinput = document.getElementById("inputId").value
    let messageOutput = document.getElementById("message")
    console.log(computerGuess)
    console.log(userinput)

    if (userinput == computerGuess) {
        console.log(true)
        messageOutput.innerHTML = "You guessed correct!"
    }
    else if(userinput < computerGuess) {
        console.log('Too Low')
        messageOutput.innerHTML = "Too Low!"
    }
    else if(userinput > computerGuess) {
        console.log('Too High')
        messageOutput.innerHTML = "Too High!"
    }
    
}


