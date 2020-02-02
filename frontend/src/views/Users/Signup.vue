<template>
  <v-container class="cnt">
    <v-layout row class="mt-12">
      <v-flex xs12 sm6 offset-xs3>
        <h3>Sign up</h3>
      </v-flex>
    </v-layout>

    <v-layout row>
      <v-flex xs12>
        <form>
          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-text-field
                name="full_name"
                label="Full name"
                id="full_name"
                v-model="state.user.fullname"
                required
              ></v-text-field>
            </v-flex>
          </v-layout>

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
                name="contact"
                label="phone number"
                id="phone_number"
                v-model="state.user.contact"
                required
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
              <v-text-field
                name="confirm_password"
                label="confirm password"
                id="confirm_password"
                v-model="state.user.confirmPassword"
                :rules="[compare]"
                required
                type="password"
              ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 xs6 offset-xs3>
              <v-btn class="primary">Sign up</v-btn>
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { reactive, computed } from "@vue/composition-api";

export default {
  setup() {
    const state = reactive({
      user: {
        fullname: "",
        contact: "",
        emai: "",
        emailRules: [
          v => !!v || "E-mail is required",
          v => /.+@.+\..+/.test(v) || "E-mail not valid"
        ],
        password: "",
        confirmPassword: ""
      }
    });

    const compare = computed(() => {
      return state.user.password !== state.user.confirmPassword
        ? "passwords do not match"
        : true;
    });

    const validForm = computed(() => {
      return "";
    });

    return { state, compare, validForm };
  }
};
</script>

<style>
.cnt {
  margin-top: 7%;
}
</style>
