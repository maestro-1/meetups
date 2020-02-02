<template>
  <div class="home">
    <v-card class="mx-auto mt-8" max-width="1000" flat>
      <Carousel></Carousel>
      <v-card-actions>
        <div class="my-2 mt-10 mb-6">
          <v-btn color="info" to="/meetup/create" dark
            >Register New Event</v-btn
          >
        </div>
      </v-card-actions>
      <h3>{{ state.reply }}</h3>
      <!-- <v-expand-transition>
        <div v-if="show">
        </div>
      </v-expand-transition> -->
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
import Carousel from "@/components/Carousel.vue";
import { onMounted, reactive } from "@vue/composition-api";

export default {
  components: {
    Carousel
  },
  setup() {
    const state = reactive({
      reply: " "
    });

    onMounted(() => {
      axios
        .get("http://127.0.0.1:5000/")
        .then(response => {
          return (state.reply = response.data);
        })
        .catch(err => err.message);
    });
    return { state };
  }
};
</script>
