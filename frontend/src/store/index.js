import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    events: [],
    user: null,
    errors: null
  },
  mutations: {
    getEvents(state, payload) {
      state.events = payload;
    }
  },
  actions: {
    getEvents({ commit }) {
      axios
        .get("http://127.0.0.1:5000/meetups")
        .then(response => {
          let events = response.data;
          return events;
          // return events.sort((eventA, eventB) => eventA.date - eventB.date);
        })
        .then(data => {
          let meetups = [];
          for (let key in data) {
            meetups.push({
              id: Number(key) + 1,
              title: data[key].title,
              description: data[key].description,
              location: data[key].location,
              imageUrl: data[key].imageUrl,
              date: data[key].date
            });
          }
          commit("getEvents", meetups);
        })
        .catch(err => err.message);
    }
  },
  getters: {
    availableEvents(state) {
      return state.events;
    },
    singleEvents(state) {
      return eventId => {
        return state.events.find(event => {
          return event.id == eventId;
        });
      };
    }
  }
});
