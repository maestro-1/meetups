<template>
  <v-card flat>
    <v-sheet class="overflow-hidden" style="position: relative;">
      <v-navigation-drawer v-model="state.sideNav" fixed temporary>
        <v-list nav dense>
          <v-list-item-group v-for="(menu, index) in dynamicNav" :key="index">
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
              <v-toolbar-title>
                Events
              </v-toolbar-title>

              <v-spacer></v-spacer>

              <v-toolbar-items
                v-for="(menu, index) in dynamicNav"
                :key="index"
                class="d-none d-sm-flex"
              >
                <v-btn depressed :to="'/' + menu.route">
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
import { reactive, computed } from "@vue/composition-api";

export default {
  name: "Toolbar",

  setup() {
    const state = reactive({
      sideNav: false
    });

    const dynamicNav = computed(() => {
      let menuItems = [];
      let authenticated = localStorage.getItem("user");

      if (authenticated) {
        menuItems = [
          {
            name: "View Events",
            icons: "calendar_today",
            route: "meetups"
          },
          {
            name: "Create Event",
            icons: "add_box",
            route: "meetup/create"
          },
          {
            name: "Profile",
            icons: "person",
            route: "profile"
          }
        ];
      } else {
        menuItems = [
          {
            name: "View Events",
            icons: "calendar_today",
            route: "meetups"
          },
          {
            name: "Login",
            icons: "people_alt",
            route: "login"
          },
          {
            name: "Sign Up",
            icons: "person_add",
            route: "signUp"
          }
        ];
      }
      return menuItems;
    });
    return { state, dynamicNav };
  }
};
</script>

<style></style>
