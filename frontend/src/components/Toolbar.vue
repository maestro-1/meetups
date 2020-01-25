<template>
  <v-card flat>
    <v-container fluid>
      <v-navigation-drawer v-model="state.sideNav"> </v-navigation-drawer>

      <v-row class="child-flex">
        <div>
          <v-toolbar>
            <v-toolbar-title>DevMeetups</v-toolbar-title>
            <v-app-bar-nav-icon
              @click="state.sideNav = !state.sideNav"
            ></v-app-bar-nav-icon>
            <v-spacer></v-spacer>

            <v-toolbar-items>
              <v-btn depressed>
                <v-icon left>mdi-magnify</v-icon>
                View Meetups
              </v-btn>
            </v-toolbar-items>

            <v-divider inset vertical></v-divider>

            <v-toolbar-items>
              <v-btn depressed>
                <v-icon left>mdi-arrow-left</v-icon>
                Another stuff
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
        </div>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import { reactive } from "@vue/composition-api";

export default {
  name: "Toolbar",

  setup() {
    const state = reactive({
      sideNav: false
    });
    return { state };
  }
};
</script>

<style></style>
