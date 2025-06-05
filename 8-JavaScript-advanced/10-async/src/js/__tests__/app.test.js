import { GameSavingLoader, GameSavingLoaderAwait} from '../app';

test('checking then', () => { 
  return GameSavingLoader.load().then(saving => {
    expect(saving).toBe('{"id":9,"created":1546300800,' + 
      '"userInfo":{"id":1,"name":"Hitman","level":10,"points":2000}}');
  });
});

test('checking await', async () => { 
  let testSaving  = await GameSavingLoaderAwait.load();
  expect(testSaving).toBe('{"id":9,"created":1546300800,' + 
      '"userInfo":{"id":1,"name":"Hitman","level":10,"points":2000}}');
});

jest.mock('../reader');
const read = new Error('error reading');
test('errors when read await', async () => {
  await expect(GameSavingLoaderAwait.load()).reject
  .toMatch(new Error('ierror reading'));
});
