import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = (firstName, lastName, fileName) => {
  const status = [];
  return signUpUser(firstName, lastName)
    .then((res) => {
      status.push({ status: 'fulfilled', value: res });
      uploadPhoto(fileName)
        .then((res) => {
          status.push({ status: 'fulfilled', value: res });
        })
        .catch((err) => {
          status.push({ status: 'reject', value: err });
        });
      return status;
    })
    .catch((err) => {
      status.push({ status: 'reject', value: err });
    });
};

export default handleProfileSignup;
