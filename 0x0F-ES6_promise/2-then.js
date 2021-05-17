export default function handleResponseFromAPI(promise) {
  promise
    .then((success) => {
      console.log("Got a response from the API");
      return { status: 200, body: success };
    })
    .catch((err) => {
      console.log("Got a response from the API");
      new Error();
    });
}
