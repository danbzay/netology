import {Magician, Daemon, ArrayBufferConverter, getBuffer} from '../app'

let testMagician = new Magician(50);
let testDaemon = new Daemon(60);

test.each([
    [testMagician, 3, false, 35], 
    [testMagician, 3, true, 27], 
    [testDaemon, 4, false, 36],
    [testDaemon, 4, true, 26],
  ])('test attack', (c, x, s, a) => {
    c.distance = x;
    c.stoned = s;
    expect(c.attack).toBe(a);
  });

test('array buffer', () => {
  const testConverter = new ArrayBufferConverter();
  const buffer = getBuffer();
  testConverter.load(buffer);
  testConverter.toString();
  console.log(testConverter.string.length);
  console.log('{"data":{"user":{"id":1,"name":"Hitman","level":10}}}'.length);
  expect(testConverter.string).toBe('{"data":{"user":{"id":1,"name":"Hitman","level":10}}}');
});
