import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import { store } from "./store";
import vuetify from "./plugins/vuetify";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import "@mdi/font/css/materialdesignicons.css";
import VueCompositionApi from "@vue/composition-api";
import Axios from "axios";
import AlertCmp from "../src/components/Alert.vue";

Vue.use(VueCompositionApi);
Vue.use(vuetify);
Vue.config.productionTip = false;

Vue.component("app-alert", AlertCmp);

new Vue({
  router,
  store,
  vuetify,
  created() {
    const user = localStorage.getItem("user");
    if (user) {
      const userData = JSON.parse(user);
      this.$store.commit("LogUserIn", userData);
    }
    Axios.interceptors.response.use(
      response => response,
      error => {
        if (error.response.data === 401) {
          this.$store.commit("logUserOut");
        }
        return Promise.reject(error);
      }
    );
  },
  render: h => h(App)
}).$mount("#app");
