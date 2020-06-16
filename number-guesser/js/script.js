let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

// 001 Gernerate a number from 1 to 10. This is the secret target number.

const generateTarget = () => {
    return Math.floor(Math.random() * 10);
}

console.log(generateTarget());

const compareGuesses = (userGuess, computerGuess, targetGuess) => {

    const userDifference = getAbsoluteDistance(userGuess, targetGuess);
    const computerDifference = getAbsoluteDistance(computerGuess, targetGuess);
    alertMessage(userGuess);

    return computerDifference >= userDifference;
}

