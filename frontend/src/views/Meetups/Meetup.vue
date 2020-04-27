<template>
  <v-container fluid>
    <v-card class="mx-auto my-12" max-width="1000">
      <v-card-title class="d-flex justify-center align-baseline">
        <h1>{{ event.title }}</h1>
      </v-card-title>

      <v-container fluid>
        <v-img
          height="500"
          :src="'http://127.0.0.1:5000' + event.imageUrl"
        ></v-img>
      </v-container>

      <v-card-text>
        <div class="my-4 subtitle-1">
          {{ event.location }}
        </div>

        <div>{{ event.description }}</div>
      </v-card-text>

      <v-divider class="mx-4"></v-divider>

      <v-card-text>
        <v-chip-group
          v-model="selection"
          active-class="deep-purple accent-4 white--text"
          column
        >
          <v-chip>{{ date.day }}</v-chip>
          <v-chip>{{ date.time }}</v-chip>
        </v-chip-group>
      </v-card-text>

      <v-card-actions>
        <v-btn color="deep-purple lighten-2" text>
          register
        </v-btn>
        <v-btn color="deep-purple lighten-2" text>
          unregister
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { computed } from "@vue/composition-api";
export default {
  props: {
    event: {
      type: Object,
      required: true
    }
  },

  setup(props) {
    const date = computed(() => {
      let [day, time] = props.event.date.split(" ");
      time = time.slice(0, 5);
      return { day, time };
    });
    return { date };
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
