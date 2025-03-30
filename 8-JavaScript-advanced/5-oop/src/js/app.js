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
    this.attack = 0;
    this.defence = 0;
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
    this.attack = 25;
    this.defence = 25;
  }
}
export class Swordsman extends Character {
  constructor(name) {
    super(name, 'Swordsman');
    this.attack = 40;
    this.defence = 10;
  }
}
export class Magician extends Character {
  constructor(name) {
    super(name, 'Magician');
    this.attack = 10;
    this.defence = 40;
  }
}
export class Undead extends Character {
  constructor(name) {
    super(name, 'Undead');
    this.attack = 25;
    this.defence = 25;
  }
}
export class Zombie extends Character {
  constructor(name) {
    super(name, 'Zombie');
    this.attack = 40;
    this.defence = 10;
  }
}
export class Daemon extends Character {
  constructor(name) {
    super(name, 'Daemon');
    this.attack = 10;
    this.defence = 40;
  }
}



//const characters = [Bowman, Swordsman, Magician, Daemon, Undead, Zombie];
//console.log(characters);
