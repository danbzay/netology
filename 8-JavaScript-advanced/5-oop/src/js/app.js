class Character {
  constructor(name, type) {
    if (typeof name == 'string' && name.length >= 2 && name.length <= 10) {
      this.name = name;
    } else {
      throw new Error('incorrect name');
    }
    if (['Bowman', 'Swordsman', 'Magician', 'Daemon', 'Undead', 
      'Zombie'].includes(type)) {
      this.type = type;
    } else {
      throw new Error('incorrect type');
    }
    this.health = 100;
    this.level = 1;
    this.attack = {'Bowman': 25, 'Swordsman': 40, 'Magican': 10, 'Undead': 25, 
      'Zombie': 40}[type];
    this.defence = {'Bowman': 25, 'Swordsman': 10, 'Magican': 40, 'Undead': 25, 
      'Zombie': 10}[type];
  }
}


