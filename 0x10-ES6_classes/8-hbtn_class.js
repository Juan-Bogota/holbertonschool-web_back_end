export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](data) {
    if (data === 'string') return this._location;
    if (data === 'number') return this._size;
    throw new Error("the type isn't Number or String");
  }
}
