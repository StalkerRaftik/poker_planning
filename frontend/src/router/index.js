import Vue from "vue";
import VueRouter from "vue-router";
import CreateRoomView from "@/views/CreateRoomView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: CreateRoomView,
  },
  {
    path: "/game/:game_id",
    name: "game",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/RoomView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
