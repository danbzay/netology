export class Character {
  constructor(name, otherProperties = 'default') {
    this.name = name;
    this.other properties = otherProperties;
  }
}

export class Team {
  constructor() {
    this.members = new Set();
  }

  add(member) {
    this.members.add(member)
  }

  addAll(...members) {
    for (member of members) {
      this.members.add(member);
    }
  }

  toArray() {
    return Array.from(this.members);
  }
}
