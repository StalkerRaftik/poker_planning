import Vue from "vue";

export default {
  namespaced: true,
  state: {
    isHost: false,
    gameId: null,
    hostToken: null,
    issues: {},
    activeIssue: {
      id: 1,
      name: "Тестовая задача",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda autem blanditiis cupiditate deserunt doloremque dolores dolorum odio quas quasi sequi sint suscipit tempora, unde, vel voluptatem. At culpa provident rem!",
    },
  },
  getters: {},
  mutations: {
    ADD_ISSUE(state, issueData) {
      console.log(issueData);
      Vue.set(
        state.issues,
        issueData.id,
        JSON.parse(JSON.stringify(issueData))
      );
    },
    DELETE_ISSUE(state, id) {
      Vue.set(state.issues, id, null);
      delete state.issues[id];
    },
    SET_GAME_ID(state, id) {
      state.gameId = id;
    },
    SET_IS_HOST(state, isHost) {
      state.isHost = isHost;
    },
    SET_HOST_TOKEN(state, hostToken) {
      state.hostToken = hostToken;
    },
  },
  actions: {
    createGame(ctx, { gameId, hostToken }) {
      ctx.commit("SET_GAME_ID", gameId);
      console.log(hostToken);
      ctx.dispatch("setHostData", hostToken);
    },
    connectGame(ctx, { gameId, hostPassword }) {
      ctx.commit("SET_GAME_ID", gameId);
      if (hostPassword) {
        ctx.dispatch("setHost", hostPassword);
      }
    },
    setHostData(ctx, hostToken) {
      ctx.commit("SET_HOST_TOKEN", hostToken);
      ctx.commit("SET_IS_HOST", true);
    },
    deleteIssue(ctx, id) {
      ctx.commit("DELETE_ISSUE", id);
    },
  },
};
