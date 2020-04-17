<template>
  <v-container>
    <v-row dense class="justify-center">
      <v-col v-for="(item, i) in upComingEvents" :key="i" cols="10">
        <v-card :color="item.color" :to="'/meetups/' + item.id">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="item.title"></v-card-title>

              <v-card-subtitle v-text="item.description"></v-card-subtitle>
              <v-card-subtitle v-text="item.location"></v-card-subtitle>
            </div>

            <v-avatar class="ma-3" size="180" tile width="180">
              <img :src="'http://127.0.0.1:5000' + item.imageUrl" />
            </v-avatar>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { reactive, onMounted, computed } from "@vue/composition-api";

export default {
  setup(props, { root: { $store } }) {
    const state = reactive({});

    const upComingEvents = computed(() => {
      return $store.getters.availableEvents;
    });

    onMounted(() => {
      $store.dispatch("getEvents");
    });
    return { state, upComingEvents };
  }
};
</script>

<style></style>
