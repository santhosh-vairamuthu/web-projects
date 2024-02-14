'use strict';


const diceRoll = document.querySelector('.btn--roll');
const diceControl = document.querySelector(".dice");
const btnHold = document.querySelector('.btn--hold');
const btnNew = document.querySelector('.btn--new');
const player0 = document.querySelector('.player--0');
const player1 = document.querySelector('.player--1');
const player0Current = document.querySelector('#current--0');
const player1Current = document.querySelector('#current--1');
const player0Score = document.querySelector('#score--0');
const player1Score = document.querySelector('#score--1');



let playStatus = true;
let activePlayer = 0;
let current = 0;
let score = [0, 0];

const switchPlayer = function(){
    activePlayer = (activePlayer == 0) ? 1 : 0;
    player0.classList.toggle('player--active');
    player1.classList.toggle('player--active');
    current = 0;
    player0Current.textContent = 0;
    player1Current.textContent = 0;
}

const winnerAnnounce = function(){
    document.querySelector(`.player--${activePlayer}`).classList.add('player--winner');
    playStatus = false;
}

btnNew.addEventListener('click', function(){
    score[0] = 0;
    score[1] = 0;
    current = 0;
    activePlayer = 0;
    player0Current.textContent = 0;
    player1Current.textContent = 0;
    player0Score.textContent = 0;
    player1Score.textContent = 0;
    player0.classList.remove('player--winner');
    player1.classList.remove('player--winner');
    player1.classList.remove('player--active');
    player0.classList.add('player--active');

});

btnHold.addEventListener('click', function(){
    if(playStatus){
        score[activePlayer] += current;
        document.querySelector(`#score--${activePlayer}`).textContent = score[activePlayer];
        if(score[activePlayer] >= 100){
            winnerAnnounce()
        }else{
            switchPlayer();
        }
    }
});

diceRoll.addEventListener('click', function(){
    if(playStatus){
        const rand = Math.floor(Math.random() * (7 - 1) + 1);
        diceControl.src = `dice-${rand}.png`;
        if(rand !== 1){
            current+=rand;
            if(score[activePlayer] + current >= 100){
                document.querySelector(`#current--${activePlayer}`).textContent = current;
                winnerAnnounce();
            }else{
                document.querySelector(`#current--${activePlayer}`).textContent = current;
            }
        }else{
            switchPlayer();
        }
    }
});