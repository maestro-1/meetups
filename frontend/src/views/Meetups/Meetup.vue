<template>
  <v-container fluid>
    <div id="beautify" @click="expand()">
      <v-row dense class="justify-center" style="cursor: pointer;">
        <v-col :cols="state.card.flex">
          <v-card>
            <v-img
              :src="
                'http://127.0.0.1:5000/static/event_image/' + meetup.imageUrl
              "
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <v-row dense class="justify-center" style="cursor: pointer;">
        <v-col :cols="state.card.flex">
          <v-expand-transition>
            <v-card>
              <div v-if="state.show">
                <v-card-title>{{ meetup.title }}</v-card-title>
                <v-card-subtitle>{{ meetup.description }}</v-card-subtitle>
                <v-card-subtitle>{{ meetup.location }}</v-card-subtitle>
                <v-card-subtitle>{{ meetup.date }}</v-card-subtitle>
              </div>
              <div v-else>
                <v-card-actions>
                  <v-card-title>{{ meetup.title }}</v-card-title>
                </v-card-actions>
              </div>
            </v-card>
          </v-expand-transition>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import { reactive, computed } from "@vue/composition-api";
export default {
  props: ["id"],

  setup(props, { root: { $store } }) {
    const state = reactive({
      card: {
        flex: 8
      },
      show: false
    });
    const meetup = computed(() => {
      return $store.getters.singleEvents(Number(props.id));
    });

    const expand = () => {
      state.show = !state.show;
    };
    return { state, meetup, expand };
  }
};
</script>

<style lang="scss" scoped>
// #beautify:hover {
//   width: 85%;
//   transform: translate3d(-15%, 25%, 40px);
//   .description {
//     transform: translate3d(120%, -519%, 20px);
//     width: 65%;
//   }
// }
</style>
