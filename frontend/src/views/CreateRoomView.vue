<template>
  <div class="main_container">
    <div
      class="input_block"
      :class="{ 'input_block--mobile': $vuetify.breakpoint.smAndDown }"
    >
      <span class="span-topic-21 mb-2"
        >Выберите название и систему оценивания для игры</span
      >
      <div class="input_container">
        <v-text-field
          v-model="roomName"
          outlined
          label="Название комнаты"
          clearable
        ></v-text-field>
        <v-select
          :items="votingSystems"
          class="vote_system_input"
          label="Система оценивания"
          outlined
          item-text="name"
          item-value="id"
          v-model="selectedVoteSystem"
          full-width
        ></v-select>
      </div>
      <v-btn
        block
        large
        color="primary"
        :loading="requestFetching"
        :disabled="requestFetching"
        @click="createGame"
      >
        Создать комнату
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateRoomView",
  watch: {
    "$store.state.gameData.gameId": function () {
      this.$router.push(`/game/${this.$store.state.gameData.gameId}`);
    },
  },
  data() {
    return {
      roomName: "Тест",
      selectedVoteSystem: 1,
      votingSystems: [
        {
          id: 1,
          name: "Фибоначчи (0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)",
        },
        {
          id: 2,
          name: "Модифицированный Фибоначчи (0, 1/2, 1, 2, 3, 5, 8, 13, 20, 40, 100)",
        },
        {
          id: 3,
          name: "Степени числа 2 (0, 1, 2, 4, 8, 16, 32, 64)",
        },
      ],

      requestFetching: false,
    };
  },
  methods: {
    createGame() {
      this.$store.dispatch("gameWebsocket/createGame");
    },
  },
};
</script>

<style scoped lang="scss">
.main_container {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 100%;
  height: 100%;
}

.input_block {
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 50%;
  padding: 16px;
}

.input_container {
  gap: 8px;
}

.input_block--mobile {
  width: 100%;
}

.vote_system_input {
  text-overflow: ellipsis;
}
</style>
