<template>
  <div class="shift">
    <v-card elevation="24" width="1000" class="mx-auto">
      <v-carousel hide-delimiters width="400" cycle>
        <v-row class="fill-height" align="center" justify="center">
          <v-carousel-item
            v-for="(images, i) in state.images"
            :key="i"
            :src="images.src"
          >
          </v-carousel-item>
        </v-row>
      </v-carousel>
    </v-card>
  </div>
</template>

<script>
import { reactive } from "@vue/composition-api";

export default {
  name: "Carousel",

  setup() {
    const state = reactive({
      images: [
        {
          src: "https://i.ytimg.com/vi/ROyHKuB8Cfk/maxresdefault.jpg"
        },
        {
          src: "https://i.ytimg.com/vi/L7CB30eOahA/maxresdefault.jpg"
        },
        {
          src: "https://i.ytimg.com/vi/dyBB_yJZ0k0/maxresdefault.jpg"
        },
        {
          src:
            "http://sotech-optima.co.uk/wp-content/uploads/2014/04/shutterstock_114912910.jpg"
        },
        {
          src: "https://i.ytimg.com/vi/koibdzXOYvQ/maxresdefault.jpg"
        }
      ]
    });

    return { state };
  }
};
</script>

<style>
.shift {
  margin-left: 10px;
  margin-right: 10px;
}
</style>
