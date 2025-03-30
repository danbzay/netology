export const obj = {name: 'мечник', health: 10, level: 2, attack: 80, defence: 40}
export const character = {
  name: 'Лучник',
  type: 'Bowman',
  health: 50,
  level: 3,
  attack: 40,
  defence: 10,
  special: [
    {
      id: 8,
      name: 'Двойной выстрел',
      icon: 'http://...',
      description: 'Двойной выстрел наносит двойной урон'
    },
    {
      id: 9,
      name: 'Нокаутирующий удар',
      icon: 'http://...'
      // <- обратите внимание, описание "засекречено"
    }
  ]
}


export function orderByProps(obj, keys) {
  return Object.entries(obj).map((x) => ({key:x[0], value:x[1]}))
    .sort((a,b) => a.key > b.key ? 1 : -1)
    .sort((a,b) => 
    (keys.indexOf(a.key) == -1 ? keys.length : keys.indexOf(a.key))
    - (keys.indexOf(b.key) == -1 ? keys.length : keys.indexOf(b.key)));
}

//console.log(orderByProps(obj, ["name", "level"]));

export function destruct(character) {
  const {special} = character;
  const result = [];
  for (const attack of special) {
    const {id, name, description='Описание недоступно', icon} = attack;
    result.push([id, name, description, icon]);
  }
  return result;
}
//console.log(destruct(character));
