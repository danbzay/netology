import {orderByProps, destruct, obj, character} from '../app'

test('sorting is necessary', () => {
  expect(orderByProps(obj, ["name", "level"])).toEqual(
    [
      {key: "name", value: "мечник"}, // порядок взят из массива с ключами
      {key: "level", value: 2}, // порядок взят из массива с ключами
      {key: "attack", value: 80}, // порядок по алфавиту (т.к. в массиве с ключами нет значения "attack")
      {key: "defence", value: 40}, // порядок по алфавиту (т.к. в массиве с ключами нет значения "defence")
      {key: "health", value: 10} // порядок по алфавиту (т.к. в массиве с ключами нет значения "health")
    ]);
});

test('get some attacks', () => {
  expect(destruct(character)).toEqual([
    [8, 'Двойной выстрел', 'Двойной выстрел наносит двойной урон', 'http://...'],
    [9, 'Нокаутирующий удар', 'Описание недоступно', 'http://...' ]
  ]);
});
