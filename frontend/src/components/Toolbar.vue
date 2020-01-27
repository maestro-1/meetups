<template>
  <v-card flat>
    <v-sheet class="overflow-hidden" style="position: relative;">
      <v-navigation-drawer v-model="state.sideNav" fixed temporary>
        <v-list nav dense>
          <v-list-item-group
            v-for="(menu, index) in state.menuItems"
            :key="index"
          >
            <div>
              <p>
                <v-icon left>{{ menu.icons }}</v-icon>
                {{ menu.name }}
              </p>
            </div>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>

      <v-container fluid>
        <v-row class="child-flex">
          <div>
            <v-toolbar>
              <v-app-bar-nav-icon
                @click.stop="state.sideNav = !state.sideNav"
                class="d-sm-none "
              ></v-app-bar-nav-icon>
              <v-toolbar-title>Events</v-toolbar-title>

              <v-spacer></v-spacer>

              <v-toolbar-items
                v-for="(menu, index) in state.menuItems"
                :key="index"
                class="d-none d-sm-flex"
              >
                <v-btn depressed>
                  <v-icon left>{{ menu.icons }}</v-icon>
                  {{ menu.name }}
                </v-btn>
                <v-divider inset vertical></v-divider>
              </v-toolbar-items>
            </v-toolbar>
          </div>
        </v-row>
      </v-container>
    </v-sheet>
  </v-card>
</template>

<script>
import { reactive } from "@vue/composition-api";

export default {
  name: "Toolbar",

  setup() {
    const state = reactive({
      sideNav: false,
      menuItems: [
        {
          name: "View Events",
          icons: "calendar_today"
        },
        {
          name: "Create Event",
          icons: "add_box"
        },
        {
          name: "Profile",
          icons: "person"
        },
        {
          name: "Login",
          icons: "people_alt"
        },
        {
          name: "Sign Up",
          icons: "person_add"
        }
      ]
    });
    return { state };
  }
};
</script>

<style></style>
