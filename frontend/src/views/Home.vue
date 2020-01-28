<template>
  <div class="home">
    <h2>{{ state.reply }}</h2>
    <Carousel></Carousel>
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
