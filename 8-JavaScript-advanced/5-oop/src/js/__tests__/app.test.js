import {Character, Bowman, Swordsman, Magician, Daemon, Undead, Zombie, 
  } from '../app';

test.each([
  ['a', 'Bowman', 'incorrect name'],
  ['aaaaaaaaaaa', 'Bowman', 'incorrect name'],
  ['Ivon', 'Bowman1', 'incorrect type'],
  ])('check errors', (name, type, error) => {
  expect(() => {
    new Character(name, type);
  }).toThrow(error);
});

test('corect character', () => {
  expect(new Character('Ivan', 'Bowman')).toEqual({name: 'Ivan', 
    type: 'Bowman', health: 100, level: 1, attack: 25, defence: 25});
});

let testCharacter = new Character('Ivan', 'Bowman');

test('correct level up', () => {
  testCharacter.levelUp();
  expect(testCharacter).toEqual({name: 'Ivan', 
    type: 'Bowman', health: 100, level: 2, attack: 30, defence: 30});
});

test('no levels for dead', () => {
  testCharacter.health = 0;
  expect(() => {
    testCharacter.levelUp();
  }).toThrow('no levels for dead');
});

test('damage calculations', () => {
  testCharacter.health = 100;
  testCharacter.damage(10);
  expect(testCharacter.health).toBe(93);
});

test('no negative health', () => {
  testCharacter.health = 1;
  testCharacter.damage(10);
  expect(testCharacter.health).toBe(0);
});

const characters = [
  [Bowman, 25, 25],
  [Swordsman, 40, 10],
  [Magician, 10, 40],
  [Daemon, 10, 40],
  [Undead, 25, 25],
  [Zombie, 40,10]
];

test.each(characters)('inheritances', (charClass, attack, defence) => {
  testCharacter = new charClass('Ivan');
  expect(testCharacter).toEqual({
    name: 'Ivan', type: testCharacter.constructor.name, health: 100, 
    level: 1, attack: attack, defence: defence});
});
