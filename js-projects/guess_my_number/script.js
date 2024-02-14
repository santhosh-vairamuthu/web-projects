let number = Math.floor(Math.random() * (20 - 1) + 1);
let score = 20;
let highScore = 0;

const addMessage = function(message){
    document.querySelector('.message').textContent = message;
};

document.querySelector('.reset').addEventListener('click', function(){
    number = Math.floor(Math.random() * (20 - 1) + 1);
    score = 20;
    document.querySelector('body').style.backgroundColor = '#fff';
    document.querySelector('.guess').value = '';
    document.querySelector('.number').textContent = '?';
    score=20;
    document.querySelector('.score').textContent = 20;
    addMessage('Start Guessing...');
});

document.querySelector('.check').addEventListener('click',function(){
    const guess = Number(document.querySelector('.guess').value);
    if(!guess){
        addMessage('Empty box ...')
    }else if(guess === number){
        addMessage("Correct Guess 🥳 !");
        if(score > highScore){
            highScore = score;
        }
        document.querySelector('.highscore').textContent = highScore;
        document.querySelector('.number').textContent = number;
        document.querySelector('body').style.backgroundColor = '#08fa75';
    }else{
        addMessage(guess > number ? 'Too High 😟' : 'Too Low 😟')
        score-=2;
        document.querySelector('.score').textContent = score;
    }
});