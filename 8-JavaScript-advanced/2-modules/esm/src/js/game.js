import character from './domain.js';

export default class Game {
  start() {
    document.querySelector('h1').innerText = 'game started';
  }
}

export class GameSavingData {};

export function readGameSaving() {};

export function writeGameSaving() {}; 
