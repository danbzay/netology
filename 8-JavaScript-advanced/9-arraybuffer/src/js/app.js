class Character {
  constructor() {
    this.distance0 = 0;
    this.attack0 = 0;
    this.stoned0 = false;
  }

  set distance(x) {
    this.distance0 = x;
  }

  get attack() {
    let result = Math.round((1 - 0.1*this.distance0) * this.attack0);
    if (this.stoned0 == true) {
      return Math.round(result - Math.log2(this.distance0) * 5);
    } else {
      return result;
    }
  }

  set stoned(isStoned){
    this.stoned0 = isStoned;
  }
}

export class Magician extends Character {
  constructor(attack0) {
    super()
    this.attack0 = attack0;
  }
}

export class Daemon extends Character {
  constructor(attack0) {
    super()
    this.attack0 = attack0;
  }
}

export class ArrayBufferConverter {
  constructor() {
    this.string = '';
  }

  load(buffer) {
    this.buffer = buffer;
    this.bufferView = new Uint16Array(buffer);
  }

  toString() {
    this.string += String.fromCharCode(...this.bufferView);
  }
}

export function getBuffer() {
  const data = '{"data":{"user":{"id":1,"name":"Hitman","level":10}}}';
  return (input => {
    const buffer = new ArrayBuffer(data.length * 2);
    const bufferView = new Uint16Array(buffer);
    for (let i = 0; i < input.length; i++) {
      bufferView[i] = input.charCodeAt(i);
    }
    return buffer;
  })(data);
}
