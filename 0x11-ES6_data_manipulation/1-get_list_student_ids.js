export default function getListStudentIds(getListStudents) {
  if (Array.isArray(getListStudents)) {
    return getListStudents.map((el) => el.id);
  }
  return [];
}
