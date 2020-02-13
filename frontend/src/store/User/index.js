import axios from "axios";

export default {
  state: {
    user: null
  },
  mutations: {
    SignUpUser(state, payload) {
      state.alerts = payload;
    },
    SignUpError(state, payload) {
      state.error = payload;
    },
    LogUserIn(state, payload) {
      state.user = payload;
      console.log(state.user);
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
          commit("SignUpUser", response);
        })
        .catch(err => {
          console.log(err);
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
        .catch(err => console.log(err));
    }
  },
  getters: {}
};
