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
              <v-img :src="item.src"></v-img>
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
    const state = reactive({
      items: [
        {
          color: "#1F7087",
          src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
          title: "Supermodel",
          artist: "Foster the People"
        },
        {
          color: "#952175",
          src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
          title: "Halcyon Days",
          artist: "Ellie Goulding"
        },
        {
          color: "#953195",
          src:
            "https://tse1.mm.bing.net/th?id=OIP.OCUUMOVcgiJFen5ASCIpowHaFj&pid=Api&P=0&w=216&h=163",
          title: "Memories",
          artist: "Maroon 5"
        }
      ]
    });

    const upComingEvents = computed(() => {
      return $store.getters.availableEvents;
    });

    onMounted(() => {
      if ($store.getters.availableEvents.length != 0) {
        return;
      }
      console.log("hahaha");
      $store.dispatch("getEvents");
    });
    return { state, upComingEvents };
  }
};
</script>

<style></style>
