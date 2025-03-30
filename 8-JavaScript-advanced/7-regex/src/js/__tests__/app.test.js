import {Validator, reducePhoneNumber} from '../app'
const v = new Validator();
test.each([
    ['0zgft', false],
    ['zgft0', false],
    ['z1234gft', false],
    ['z', true],
    ['z12g45ft', true],
  ])('validating', (name, result) => {
    expect(v.validateUserName(name)).toBe(result);
});

test('testing error', () => {
    expect( () => {
      reducePhoneNumber('n123jcnu45678901234567mbeer');
    }).toThrow('So many numbers to call');
});
  
test.each([
    ['8(913) 123 45 67', '+79131234567'],
    ['86 913 123 4567', '+869131234567'],
    ['+7(913) 123 4567', '+79131234567'],
    ['12345', '+12345'],
    ['(913)- 12-3sdfs 45 67', '+79131234567'],
  ])('some normal numbers', (number, reducedNumber) => {
    expect(reducePhoneNumber(number)).toBe(reducedNumber);
});
