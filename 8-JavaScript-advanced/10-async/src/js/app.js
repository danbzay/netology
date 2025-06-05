import read from './reader';
import json from './parser';

export class GameSavingLoader {
  static load() {
   return read().then((data) => json(data));
  }
}

export class GameSavingLoaderAwait {
  static async load() {
    let data, result;
    try {
      data = await read();
    } catch(error) {
      return error;
    }
    try {
      result = await json(data);
    } catch(error) {
      return error;
    }
    return result;
  }
}
