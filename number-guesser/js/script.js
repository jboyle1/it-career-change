let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below: 001 Gernerate a number from 1 to 10. This is the
// secret target number.

function generateTarget() {
    return Math.floor(Math.random() * Math.floor(9));
}

// 002 create a function called 'compareGuesses()' to determine which player
// wins based on which guess is closest to the target. If both players are tied,
// the human user should win. Return true if the human player wins, and false if
// the computer player wins.
function compareGuesses(humanGuessInput, target, computerGuess) {
    if (Math.abs(humanGuessInput - target) <= Math.abs(computerGuess - target)) {
        return true;
    }
    if (Math.abs(humanGuessInput - target) >= Math.abs(computerGuess - target)) {
        return false;
    }
}

// 003 This function will be used to correctly increase the winner’s score after
// each round.

function updateScore(winner) {
    if (winner == 'human') {
        return humanScore++
    }
    if (winner == "computer") {
        return computerScore++
    } else {}
}

// This function will be used to update the round number after each round.

function advanceRound() {
    return currentRoundNumber++
}
