export class Validator {
  validateUserName(name) {
    return name.length == 1 ? /[a-zA-Z]/.test(name) : 
      /^[a-zA-Z]((?!\d{4,})\w)*[a-zA-Z]$/.test(name);
  }
}

export function reducePhoneNumber(number) {
  let result = number.replace(/[^\d]/g, '');
  if (result.length == 10) {
    return '+7' + result;
  }
  if (result.length == 11) {
    if (result.substring(0,1) == '8') {
      return '+7' + result.substring(1,12);
    } else {
      return '+' + result;
    }
  }
  if (result.length > 15 ) {
    throw new Error('So many numbers to call');
  } else {
    return '+' + result;
  }
}
