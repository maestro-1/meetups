import Axios from "axios";

export const sendEventDetails = (url, data) => {
  Axios.post(url, data);
};

export const sendEventImage = (url, formData) => {
  Axios.post(url, formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });
};
