export class Character {
  constructor(name, type) {
    if (typeof name == 'string' && name.length >= 2 && name.length <= 10) {
      this.name = name;
    } else {
      throw new Error('incorrect name');
    }
    if (['Bowman', 'Swordsman', 'Magician', 'Daemon', 'Undead', 'Zombie']
      .includes(type)) {
      this.type = type;
    } else {
      throw new Error('incorrect type');
    }
    this.health = 100;
    this.level = 1;
    this.attack = {'Bowman': 25, 'Swordsman': 40, 'Magician': 10, 'Undead': 25, 
      'Zombie': 40, 'Daemon': 10}[type];
    this.defence = {'Bowman': 25, 'Swordsman': 10, 'Magician': 40, 'Undead': 25, 
      'Zombie': 10, 'Daemon': 40}[type];
  }

  levelUp() {
    if (this.health > 0) {
      this.level++;
      this.attack *= 1.2;
      this.defence *= 1.2;
      this.health = 100;
    } else {
      throw new Error('no levels for dead');
    }
  }

  damage(points) {
    this.health -= points * (1 - this.defence / 100);
    if (this.health < 0) {
      this.health = 0;
    }
  }
}

export class Bowman extends Character {
  constructor(name) {
    super(name, 'Bowman');
  }
}
export class Swordsman extends Character {
  constructor(name) {
    super(name, 'Swordsman');
  }
}
export class Magician extends Character {
  constructor(name) {
    super(name, 'Magician');
  }
}
export class Undead extends Character {
  constructor(name) {
    super(name, 'Undead');
  }
}
export class Zombie extends Character {
  constructor(name) {
    super(name, 'Zombie');
  }
}
export class Daemon extends Character {
  constructor(name) {
    super(name, 'Daemon');
  }
}


//const characters = [Bowman, Swordsman, Magician, Daemon, Undead, Zombie];
//console.log(characters);
