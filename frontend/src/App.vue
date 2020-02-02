<template>
  <v-app>
    <Toolbar />
    <router-view></router-view>
    <div id="footer">
      <!-- <Footer /> -->
    </div>
  </v-app>
</template>

<script>
import Toolbar from "@/components/Toolbar.vue";
// import Footer from "@/components/Footer.vue";

export default {
  name: "home",
  components: {
    Toolbar
    // Footer
  }
};
</script>

<style scoped>
#footer {
  position: absolute;
  bottom: 0;
}
</style>
