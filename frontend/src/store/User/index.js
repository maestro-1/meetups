import axios from "axios";

export default {
  state: {
    user: null,
    loading: false,
    error: null
  },
  mutations: {
    SignUpUser(state, payload) {
      state.alerts = payload;
    },
    Error(state, error) {
      state.error = error;
    },
    LogUserIn(state, userData) {
      state.user = userData;
      localStorage.setItem("user", JSON.stringify(userData));
      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${userData.token}`;
    },
    logUserOut() {
      localStorage.removeItem("user");
      location.reload();
    }
  },
  actions: {
    SignUpUser({ commit }, payload) {
      const user = {
        full_name: payload.fullname,
        password: payload.password,
        contact: payload.contact,
        email: payload.email
      };
      axios
        .post("http://127.0.0.1:5000/signup", user)
        .then(response => {
          commit("SignUpUser", response.data);
        })
        .catch(err => {
          commit("Error", err);
        });
    },
    LogUserIn({ commit }, payload) {
      const userDetails = {
        email: payload.email,
        password: payload.password
      };
      axios
        .post("http://127.0.0.1:5000/login", userDetails)
        .then(response => {
          commit("LogUserIn", response.data);
        })
        .catch(err => {
          commit("Error", err);
        });
    }
  },
  getters: {}
};
