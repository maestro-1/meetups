import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { sendEventDetails, sendEventImage } from "../utils/requests.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    events: [],
    user: null,
    alerts: null
  },
  mutations: {
    getEvents(state, payload) {
      state.events = payload;
    },
    createEvents(state, payload) {
      state.events.push(payload);
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
    },

    createEvents({ commit }, payload) {
      const meetup = {
        title: payload.title,
        location: payload.location,
        description: payload.description,
        date: payload.date
      };
      const image = payload.image;
      axios
        .all(
          [sendEventImage("http://127.0.0.1:5000/meetup/create/file", image)],
          [sendEventDetails("http://127.0.0.1:5000/meetup/create", meetup)]
        )
        .then(response => {
          console.log(response);
          commit("createEvents", response.data);
        })
        .catch(err => err.data);
    }
  },
  getters: {
    availableEvents(state) {
      console.log(state.events[1]);
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
