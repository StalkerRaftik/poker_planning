// import axios from "axios";
//
// export const clientSettings = {
//   baseURL: process.env.VUE_APP_BASE_URL,
//   headers: {},
// };
// if (localStorage.authToken) {
//   clientSettings.headers["Authorization"] = `Token ${localStorage.authToken}`;
// }
//
// export let client = axios.create(clientSettings);
//
// export function newClient(extraSettings) {
//   client = axios.create({
//     ...clientSettings,
//     ...extraSettings,
//   });
//   return client;
// }
