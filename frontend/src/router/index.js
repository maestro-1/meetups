import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Meetup from "@/views/Meetups/Meetup.vue";
import Meetups from "@/views/Meetups/Meetups.vue";
import CreateMeetups from "@/views/Meetups/CreateMeetup.vue";
import Profile from "@/views/Users/Profile.vue";
import Signin from "@/views/Users/Signin.vue";
import Signup from "@/views/Users/Signup.vue";
import { store } from "../store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/about",
    name: "about",
    component: About
  },
  {
    path: "/meetups",
    name: "meetups",
    component: Meetups
  },
  {
    path: "/meetups/:id",
    name: "meetup",
    props: true,
    component: Meetup,
    beforeEnter(to, from, next) {
      store
        .dispatch("getEvent", to.params.id)
        .then(event => {
          to.params.event = event;
          next();
        })
        .catch(error => {
          if (error.response && error.response.status == 404) {
            console.log(error);
            //   next({ name: '404', params: { resource: 'event' } })
            // } else {
            //   next({ name: 'network-issue' })
          }
        });
    }
  },
  {
    path: "/meetup/create",
    name: "createMeetUps",
    component: CreateMeetups,
    meta: { requiresAuth: true }
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile,
    meta: { requiresAuth: true }
  },
  {
    path: "/login",
    name: "login",
    component: Signin
  },
  {
    path: "/signup",
    name: "signUp",
    component: Signup
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((To, From, next) => {
  let logging = localStorage.getItem("user");
  if (To.matched.some(record => record.meta.requiresAuth)) {
    if (!logging) {
      next("/");
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
