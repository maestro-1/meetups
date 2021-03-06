import axios from "axios";
import { sendEventDetails, sendEventImage } from "../../utils/requests.js";

export default {
  state: {
    events: [],
    event: {}
  },
  mutations: {
    getEvents(state, payload) {
      state.events = payload;
    },

    setEvent(state, event) {
      state.event = event;
    },

    createEvents(state, payload) {
      state.events.push({ ...payload });
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
              id: data[key].id,
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

    getEvent({ commit, getters, state }, ide) {
      if (ide == state.event.ide) {
        return state.event;
      }

      let event = getters.singleEvents(ide);

      if (event) {
        commit("setEvent", event);
        return event;
      } else {
        return axios
          .get(`http://127.0.0.1:5000/meetup/${ide}`)
          .then(response => {
            let { event } = response.data;
            commit("setEvent", response.data);
            return event;
          });
      }
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
          commit("createEvents", response.data);
        })
        .catch(err => err.data);
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
};
