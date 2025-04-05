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

class ErrorRepository {
  constructor() {
    this.repository = new Map();
  }

  translate(code) {
    return this.repository[code];
  }

}
