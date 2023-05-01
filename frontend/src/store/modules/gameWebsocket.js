import GameWebsocketConnection, { SEND_MESSAGES_ENUM } from "@/websocket";
import store from "../index";

export default {
  namespaced: true,
  state: {
    ws: null,
    isHost: false,
    gameId: null,
    error: null,
  },
  getters: {},
  mutations: {
    SET_WS(state, ws) {
      state.ws = ws;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    async createGame(ctx) {
      const ws = new GameWebsocketConnection();
      await ws.startWebSocket();
      ctx.commit("SET_WS", ws);
      return ws;
    },
    async connectGame(ctx, gameId) {
      const ws = new GameWebsocketConnection(gameId);
      await ws.startWebSocket();
      ctx.commit("SET_WS", ws);
    },
    setError(ctx, errorText) {
      ctx.commit("SET_ERROR", errorText);
    },
    async createIssue(ctx, issueData) {
      await ctx.dispatch("sendMessage", {
        type: SEND_MESSAGES_ENUM.CREATE_ISSUE,
        data: issueData,
      });
    },
    async sendMessage(ctx, messageData) {
      const token = store.state.gameData.hostToken;
      if (token) {
        messageData.token = token;
      }
      ctx.state.ws.sendMessage(messageData);
    },
  },
};
