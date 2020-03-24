import Vue from "vue";
import VueRouter from "vue-router";
import Group from "../views/Group.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "group",
    component: Group
  }
];

const router = new VueRouter({
  routes
});

export default router;
