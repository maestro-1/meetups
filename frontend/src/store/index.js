import Vue from "vue";
import Vuex from "vuex";

import Meetup from "./Meetups";
import User from "./User";
import Alert from "./Shared";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    Meetup,
    User,
    Alert
  }
});
