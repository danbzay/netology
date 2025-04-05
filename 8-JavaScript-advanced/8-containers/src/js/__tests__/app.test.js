import {Character, Team} from '../app';

const ivan = new Character('Ivan');
const pyotr = new Character('Pyotr');
const vasiliy = new Character('Vasiliy');
const characters = [ivan, pyotr, vasiliy];

const testTeam = new Team();

test('test add', ()=> {
  testTeam.add(ivan);
  expect(testTeam.toArray()).toEqual([ivan]);
});

test('test add error', () => {
  expect( () => {
    testTeam.add(ivan);
  }).toThrowError('already membered');
 });

test('test add all', () => {
  testTeam.addAll(ivan, ... characters);
  expect(testTeam.toArray()).toEqual(characters);
});
