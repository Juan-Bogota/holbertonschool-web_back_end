export default function updateStudentGradeByCity(
  getListStudents,
  city,
  newGrades,
) {
  if (typeof city !== 'string') throw new Error('City must be an string');
  if (
    !Array.isArray(newGrades)
    && newGrades.every((el) => typeof el !== 'object')
  ) throw new Error('newGrades is not an Array of Objects');
  if (Array.isArray(getListStudents)) {
    const filterStudent = getListStudents.filter((el) => el.location === city);
    return filterStudent.map((el) => {
      const [data] = newGrades.filter((item) => item.studentId === el.id);
      console.log('data is', data);
      return {
        ...el,
        grade: data ? data.grade : 'N/A',
      };
    });
  }
  throw new Error('getListStudents is not an Array');
}
