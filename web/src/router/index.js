import Vue from 'vue'
import VueRouter from "vue-router";
import Main from "@/views/Main/Main.vue";
import Message from "@/views/Message/Message.vue";
import Feature from "@/views/Feature/Feature.vue";
import Publish from "@/views/PersonalCenter/Publish.vue";
import Login from "@/views/Auth/Login.vue";
import Register from "@/views/Auth/Register.vue";
import Profile from "@/views/PersonalCenter/Profile.vue"
import HelloWorld from "@/views/HelloWorld";

Vue.use(VueRouter)
const routes = [
  {
    path: "/hello",
    name: "HelloWorld",
    component: HelloWorld
  },
  {
    path: "/",
    name: "Main",
    component: Main,
    redirect: '/feature',
    children: [
      {
        path: "/login",
        name: "Login",
        component: Login,
      },
      {
        path: "/register",
        name: "Register",
        component: Register,
      },
      {
        path: "/feature",
        name: "Feature",
        component: Feature,
      },
      {
        path: "/publish",
        name: "Publish",
        component: Publish,
      },
      {
        path: "/message/:mid",
        name: "Message",
        component: Message,
      },
      {
        path: "/profile",
        name: "Profile",
        component: Profile,
      },
    ]
  },
];

const router = new VueRouter({
  routes,
  mode: 'history'
});

export default router;
