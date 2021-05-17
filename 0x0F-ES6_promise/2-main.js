import handleResponseFromAPI from "./2-then";

const promise = Promise.reject("mi error");
handleResponseFromAPI(promise);
