import Vue from "vue";
import VueRouter from "vue-router";
import Dashboard from "../screens/Dashboard.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: Dashboard
  }
];

const router = new VueRouter({
  routes
});

export default router;
