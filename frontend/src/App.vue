<template>
  <v-app>
    <Toolbar></Toolbar>
    <router-view></router-view>
  </v-app>
</template>

<script>
import Toolbar from "@/components/Toolbar.vue";

export default {
  name: "home",
  components: {
    Toolbar
  }
};
</script>
