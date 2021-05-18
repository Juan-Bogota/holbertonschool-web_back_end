export default function getStudentsByLocation(getListStudents, city) {
  if (Array.isArray(getListStudents)) {
    return getListStudents.filter((el) => el.location === city);
  }
  return [];
}
