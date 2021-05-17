import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(
  firstName,
  lastName,
  fileName,
) {
  const user = {};
  const photo = {};

  try {
    const signUp = await signUpUser(firstName, lastName);
    user.status = 'fulfilled';
    user.value = signUp;
  } catch (error) {
    user.status = 'rejected';
    user.value = error.toString();
  }
  try {
    const upload = await uploadPhoto(fileName);
    photo.status = 'fulfilled';
    photo.value = upload;
  } catch (error) {
    photo.status = 'rejected';
    photo.value = error.toString();
  }
  return [user, photo];
}
