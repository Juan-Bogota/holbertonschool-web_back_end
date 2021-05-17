export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const idx of newArray) {
    const value = idx;
    newArray[newArray.indexOf(idx)] = appendString + value;
  }

  return newArray;
}
