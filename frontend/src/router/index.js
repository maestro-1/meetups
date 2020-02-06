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
    component: Meetup
  },
  {
    path: "/meetup/create",
    name: "createMeetUps",
    component: CreateMeetups
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile
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

export default router;
