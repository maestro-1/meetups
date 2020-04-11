import Vue from "vue";
import Vuex from "vuex";

import meetup from "./Meetups";
import user from "./User";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    meetup: meetup,
    user: user
  }
});
