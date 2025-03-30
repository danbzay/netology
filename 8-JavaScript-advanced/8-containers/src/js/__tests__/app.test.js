import {Character, Team} from '../app';

const ivan = new Character('Ivan');
const pyotr = new Character('Pyotr');
const vasiliy = new Character('Vasiliy');
const characters = [ivan, pyotr, vasiliy];

const testTeam = new Team();

test('test add', () => {
  expect(testTeam.add(ivan).toHaveProperty('members', Equal , [{name='Ivan', otherProperties = 'default'}]]
  [[characters, ivan], characters]

