import Axios from "axios";

export const sendEventDetails = (url, data) => {
  Axios.post(url, data);
};

export const sendEventImage = (url, file) => {
  let formData = new FormData();
  formData.append("imageUrl", file);
  Axios.post(url, formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });
};
