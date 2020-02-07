<template>
  <v-container>
    <v-layout row>
      <v-flex xs12 sm6 offset-xs3>
        <h3>Create a new Event</h3>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12>
        <form>
          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-text-field
                name="title"
                label="Title"
                id="title"
                v-model="state.event.title"
                required
              ></v-text-field>
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-text-field
                name="location"
                label="Location"
                id="location"
                v-model="state.event.location"
                required
              ></v-text-field>
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <input type="file" id="files" ref="files" />
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <img :src="state.event.imageUrl" height="100" />
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-textarea
                name="description"
                label="Description"
                id="description"
                v-model="state.event.description"
                required
              ></v-textarea>
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex xs12 sm6 offset-xs3>
              <v-row>
                <v-col cols="12" lg="6">
                  <v-menu
                    v-model="state.menu1"
                    :close-on-content-click="false"
                    max-width="290"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        :value="datetime"
                        clearable
                        label="Event date"
                        readonly
                        v-on="on"
                        @click:clear="state.event.date = null"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="state.event.date"
                      @change="state.menu1 = false"
                    ></v-date-picker>
                  </v-menu>
                </v-col>

                <template>
                  <v-row>
                    <v-col cols="11" sm="5">
                      <v-menu
                        ref="menu"
                        v-model="state.menu2"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="state.time"
                        transition="scale-transition"
                        offset-y
                        max-width="290px"
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on }">
                          <v-text-field
                            v-model="state.time"
                            label="Event time"
                            prepend-icon="access_time"
                            readonly
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-time-picker
                          v-if="state.menu2"
                          v-model="state.time"
                          full-width
                          @click:minute="$refs.menu.save(state.time)"
                        ></v-time-picker>
                      </v-menu>
                    </v-col>
                  </v-row>
                </template>
              </v-row>
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex xs12 sm6 offset-xs3>
              <v-btn class="primary" :disabled="!validForm" @click="createEvent"
                >Create Event</v-btn
              >
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import moment from "moment";
import { reactive, computed } from "@vue/composition-api";
export default {
  props: [],

  setup(props, { root: $store, $router }) {
    const state = reactive({
      event: {
        title: " ",
        location: " ",
        imageUrl: " ",
        description: " ",
        date: new Date().toISOString().substr(0, 10)
      },
      menu1: false,
      time: null,
      menu2: false
    });

    const datetime = computed(() =>
      state.event.date
        ? moment(state.event.date).format("dddd, MMMM Do YYYY")
        : ""
    );

    const validForm = computed(() => {
      return (
        state.event.title !== " " &&
        state.event.location !== " " &&
        // state.event.imageUrl !== " " &&
        state.event.description !== " "
      );
    });

    const createEvent = () => {
      const newEvent = {
        title: state.event.title,
        location: state.event.location,
        description: state.event.description,
        imageUrl: state.event.imageUrl,
        date: (() => state.event.date + "," + state.time)()
      };
      $store.dispatch("createEvents", newEvent);
      $router.push({ name: "meetups" });
    };

    return { state, datetime, createEvent, validForm };
  }
};
</script>

<style></style>
