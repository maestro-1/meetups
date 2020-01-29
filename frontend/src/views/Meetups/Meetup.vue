<template>
  <v-container fluid>
    <div id="beautify">
      <v-row dense class="justify-center" style="cursor: pointer;">
        <v-col :cols="state.card.flex">
          <v-card>
            <v-img
              :src="state.card.img"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
              <v-card-title>{{ state.card.title }}</v-card-title>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <div class="description">
        <v-row dense class="justify-center">
          <v-col :cols="state.card.flex">
            <v-card>
              <v-card-text class="text--primary">
                <div>Hello There</div>

                <div>How are you</div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </div>
    </div>
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
        flex: 8
      }
    });

    return { state };
  }
};
</script>

<style lang="scss" scoped>
#beautify:hover {
  width: 85%;
  transform: translate3d(-15%, 25%, 40px);
  .description {
    transform: translate3d(120%, -519%, 20px);
    width: 65%;
  }
}
</style>
