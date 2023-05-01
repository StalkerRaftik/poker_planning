import store from "@/store";
import Vue from "vue";

export const MESSAGES_TYPES_ENUM = {
  GAME_CREATED: "game_created",
  CONNECTED_TO_GAME: "connected_to_game",
  GAME_NOT_FOUND: "game_not_found",
  NEW_ISSUE: "new_issue",
  ISSUE_CREATED: "issue_created",
  NO_PERMISSION: "no_permission",
};

export const SEND_MESSAGES_ENUM = {
  CREATE_ISSUE: "create_issue",
};

export default class GameWebsocketConnection {
  constructor(gameId = "") {
    this.gameId = gameId;
    this.eventHandlers = {
      [MESSAGES_TYPES_ENUM.GAME_CREATED]: this.onGameCreated,
      [MESSAGES_TYPES_ENUM.CONNECTED_TO_GAME]: this.onConnectedToGame,
      [MESSAGES_TYPES_ENUM.GAME_NOT_FOUND]: this.onGameNotFound,
      [MESSAGES_TYPES_ENUM.NEW_ISSUE]: this.onNewIssue,
      [MESSAGES_TYPES_ENUM.NO_PERMISSION]: this.onNoPermission,
      [MESSAGES_TYPES_ENUM.ISSUE_CREATED]: this.onIssueCreated,
    };
  }

  async startWebSocket() {
    this.connectWebSocket();
  }

  connectWebSocket() {
    this.ws = new WebSocket(`${process.env.VUE_APP_WS_URL}/${this.gameId}/`);
    this.ws.onopen = this.wsOnOpen.bind(this);
    this.ws.onmessage = this.wsOnMessage.bind(this);
    this.ws.onclose = this.wsOnClose.bind(this);
    this.ws.onerror = this.wsOnError.bind(this);
  }

  closeWebSocket() {
    this.ws.onclose = function () {}; // disable onclose handler first
    this.ws.close();
  }

  reconnectWebSocket() {
    let retryCount = 1;
    this.connectionInterval = setInterval(async () => {
      if (this.ws.readyState === WebSocket.CONNECTING) return;
      if (this.ws.readyState === WebSocket.OPEN) {
        this.log("Соединение восстановлено");
        clearInterval(this.connectionInterval);
        this.connectionInterval = null;
        return;
      }
      if (retryCount > 10) {
        this.log(
          "Не получилось восстановить соединение, сихнронизация приостановлена"
        );
        clearInterval(this.connectionInterval);
        this.connectionInterval = null;
        return;
      }

      this.log(`Попытка восстановить соединение #${retryCount}`);
      this.connectWebSocket();
      retryCount++;
    }, 1000);
  }

  async wsOnOpen(event) {
    this.log("Соединение установлено", event);
  }

  wsOnClose(event) {
    if (this.connectionInterval) return;

    this.log("Соединение закрыто", event);
    this.reconnectWebSocket();
  }

  wsOnError(event) {
    this.log("Ошибка от вебсокета", event);
  }

  log(...args) {
    console.info(`[WebSocket]`, ...args);
  }

  sendMessage(messageData) {
    this.ws.send(JSON.stringify(messageData));
    this.log("Отправлено сообщение", messageData);
  }

  async wsOnMessage(event) {
    const eventData = JSON.parse(event.data);
    await this.wsHandleMessage(eventData);
  }

  async wsHandleMessage(eventData) {
    this.log("Получено сообщение", eventData);
    let event_type = eventData.type;

    const messageHandlerByType = this.eventHandlers[event_type].bind(this);
    messageHandlerByType(eventData);
  }

  onGameCreated(eventData) {
    store.dispatch("gameData/createGame", {
      gameId: eventData.game_id,
      hostToken: eventData.host_token,
    });
  }

  onConnectedToGame(eventData) {
    store.dispatch("gameData/connectGame", { gameId: eventData.game_id });
  }

  onGameNotFound() {
    this.log("Игра не найдена!");
    store.dispatch("gameWebsocket/setError", "Игра не найдена");
  }

  onIssueCreated() {
    this.log("Ваша задача успешно создана");
  }

  onNewIssue(eventData) {
    store.commit("gameData/ADD_ISSUE", eventData.data);
  }

  onNoPermission() {
    Vue.notify({
      title: "Задача не создана",
      text: "У вас недостаточно прав для создания задачи",
      type: "error",
    });
    this.log("Нет доступа!");
  }
}
