import {Character, Team, ErrorRepository, Settings} from '../app';

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

const testER = new ErrorRepository;

test.each([[1, 'one'], [5, 'Unknown error']])('test error repository', 
  (c, e ) => {
    expect(testER.translate(c)).toBe(e);
});

const testSettings = new Settings({'theme':'light'});

test('testing settings', () => {
  expect(Array.from(testSettings.settings.entries())).toEqual([
    ['theme', 'light'], ['music', 'trance'], ['difficulty', 'easy']]);
});
