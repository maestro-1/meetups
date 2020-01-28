<template>
  <v-container fluid class="beautify" cursor pointer>
    <v-row dense class="justify-center">
      <v-col :cols="state.card.flex">
        <v-card>
          <v-img
            :src="state.card.img"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="600px"
          >
          </v-img>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { reactive } from "@vue/composition-api";
export default {
  setup() {
    const state = reactive({
      card: {
        title: "foster",
        img: "https://cdn.vuetifyjs.com/images/cards/girl.jpg",
        flex: 9
      }
    });
    return { state };
  }
};
</script>

<style scoped>
.beautify:hover {
  translate: 10;
}
</style>
