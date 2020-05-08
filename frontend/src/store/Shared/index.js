export default {
  state: {
    alert: null
  },
  mutations: {
    setAlert(state, alert) {
      state.alert = alert;
    },
    clearAlert(state) {
      state.alert = null;
    }
  },
  actions: {
    clearAlert({ commit }) {
      commit("clearAlert");
    }
  },
  getters: {
    alert(state) {
      return state.alert;
    }
  }
};
