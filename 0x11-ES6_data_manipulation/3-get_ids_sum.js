export default function getStudentIdsSum(getListStudents) {
  if (Array.isArray(getListStudents)) {
    return getListStudents.reduce(
      (accumulator, current) => accumulator + current.id,
      0,
    );
  }
  return 0;
}
