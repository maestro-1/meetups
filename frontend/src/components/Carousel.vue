<template>
  <v-carousel hide-delimiters>
    <v-carousel-item
      v-for="(images, i) in state.images"
      :key="i"
      :src="images.src"
    >
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import { reactive } from "@vue/composition-api";

export default {
  name: "Carousel",

  setup() {
    const state = reactive({
      images: [
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
        }
      ]
    });

    return { state };
  }
};
</script>

<style></style>
