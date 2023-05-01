import Vue from "vue";
import Vuex from "vuex";
import gameData from "@/store/modules/gameData";
import gameWebsocket from "@/store/modules/gameWebsocket";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    gameData,
    gameWebsocket,
  },
});
