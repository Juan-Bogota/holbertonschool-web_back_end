const validateNumber = (number, name) => {
  if (typeof number !== 'number') throw new Error(`${name} is not a number`);
  return true;
};

export default function createInt8TypedArray(length, position, value) {
  validateNumber(length, 'length');
  validateNumber(position, 'position');
  validateNumber(value, 'value');
  try {
    const buffer = new ArrayBuffer(length);
    const view = new DataView(buffer, 0);
    view.setInt8(position, value);
    return view;
  } catch (err) {
    throw new Error('Position outside range');
  }
}
