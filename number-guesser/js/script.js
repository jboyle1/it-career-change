let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

// 001 Gernerate a number from 1 to 10. This is the secret target number.

const generateTarget = () => {
    return Math.floor(Math.random() * 10);
}


// console.log(generateTarget());

// 002 create a function called 'compareGuesses()' to determine which player wins based on which guess is closest to the target. If both players are tied, the human user should win. Return true if the human player wins, and false if the computer player wins.
const compareGuesses = (userGuess, computerGuess, targetGuess) => {

    const userDifference = getAbsoluteDistance(userGuess, targetGuess);
    const computerDifference = getAbsoluteDistance(computerGuess, targetGuess);
    alertMessage(userGuess);

    return computerDifference >= userDifference;
}

// 003 This function will be used to correctly increase the winner’s score after each round.

const updateScore = winner =>{

	if (winner === 'human'){

		humanScore++;

	}else if(winner === 'computer'){

		computerScore++;
	}

}