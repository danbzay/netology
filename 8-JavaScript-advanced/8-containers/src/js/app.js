export class Character {
  constructor(name, otherProperties = 'default') {
    this.name = name;
    this.otherProperties = otherProperties;
  }
}

export class Team {
  constructor() {
    this.members = new Set();
  }

  add(member) {
    if (this.members.has(member)) {
      throw new Error('already membered');
    }
    this.members.add(member)
  }

  addAll(...members) {
    for (let member of members) {
      this.members.add(member);
    }
  }

  toArray() {
    return Array.from(this.members);
  }
}

export class ErrorRepository {
  constructor() {
    this.repository = new Map([[1,'one'],[2, 'two'],[3,'three']] );
  }

  translate(code) {
    let result = this.repository.get(code);
    if (result == undefined) {
      result = 'Unknown error';
    }
    return result;
  }
}

export class Settings {
  constructor(userSettings) {
    this.possible = {
      'theme': ['dark', 'light'], 
      'music': ['trance', 'pop', 'rock', 'chillout', 'off'],
      'difficulty': ['easy', 'normal', 'hard', 'nightmare'],
    };
    this.defaultSettings = new Map(Object.entries(this.possible)
      .map(([x,y]) => [x, y[0]]));
    this.userSettings = new Map(Object.entries(userSettings));
  }
  get settings() {
    return new Map([...this.defaultSettings, ...this.userSettings]);
  }
}
