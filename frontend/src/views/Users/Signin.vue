<template>
  <v-container class="cnt">
    <v-layout row class="mt-12">
      <v-flex xs12 sm6 offset-xs3>
        <h3>Login</h3>
      </v-flex>
    </v-layout>

    <v-layout row>
      <v-flex xs12>
        <form>
          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-text-field
                name="email"
                label="Email"
                id="email"
                v-model="state.user.email"
                :rules="state.user.emailRules"
                required
                type="email"
              ></v-text-field>
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-text-field
                name="paswword"
                label="password"
                id="password"
                v-model="state.user.password"
                required
                type="password"
              ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-btn class="primary">Login</v-btn>
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { reactive } from "@vue/composition-api";

export default {
  setup() {
    const state = reactive({
      user: {
        emai: "",
        emailRules: [
          v => !!v || "E-mail is required",
          v => /.+@.+\..+/.test(v) || "E-mail not valid"
        ],
        password: ""
      }
    });
    return { state };
  }
};
</script>

<style></style>
