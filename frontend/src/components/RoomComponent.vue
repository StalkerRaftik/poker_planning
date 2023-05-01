<template>
  <div class="main_container">
    <div class="header">
      <div class="header_block left">
        <span class="room_name">Название комнаты</span>
      </div>
      <div class="header_block center">
        <v-text-field
          readonly
          label="Ссылка для приглашения"
          value="bit.ly/office2016txt"
          outlined
          dense
          append-icon="mdi-content-copy"
        ></v-text-field>
      </div>
      <div class="header_block right"></div>
    </div>
    <div class="body">
      <div style="flex: 0 1 10%"></div>
      <div class="center_block" style="flex: 0 1 80%">
        <div class="text-h4 current_issue_top_text">(1/10) Оцените задачу:</div>
        <v-card style="max-width: 600px">
          <v-card-text>
            <p class="text-h4 text--primary">{{ activeIssue.name }}</p>
            <div class="text--primary">
              {{ activeIssue.description }}
            </div>
          </v-card-text>
        </v-card>
      </div>
      <div class="actions_container" style="flex: 0 1 10%">
        <IssuesPopup />
      </div>
    </div>
    <div class="footer">
      <div></div>
      <div class="cards_container">
        <v-card
          v-for="choice in choices"
          :key="choice"
          class="pick_card"
          elevation="2"
          >{{ choice }}</v-card
        >
      </div>
      <div></div>
    </div>
  </div>
</template>

<script>
import IssuesPopup from "@/components/IssuesPopup";
import { mapState } from "vuex";

export default {
  name: "RoomComponent",
  components: { IssuesPopup },
  data() {
    return {
      choices: [1, 2, 3, 4, 5, 6],
    };
  },
  computed: {
    ...mapState("gameData", ["activeIssue"]),
  },
};
</script>

<style scoped lang="scss">
.main_container {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 16px;
}

.header {
  display: flex;
  justify-content: space-between;
}

.header_block {
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
}

.room_name {
  font-weight: 500;
  font-size: 21px;
}

.body {
  display: flex;
  justify-content: space-between;
  gap: 8px;
}

.actions_container {
  display: flex;
  align-items: center;
  justify-content: end;
}

.issues_btn {
  border-radius: 15%;
  max-width: 40px;
  max-height: 40px;
}

.center_block {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 32px;
  margin-bottom: 50px;
}

.current_issue_top_text {
  font-weight: 300;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-basis: 0;
}

.cards_container {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.pick_card {
  width: 50px;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;

  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;

  font-size: 24px;
  font-weight: 600;

  transition: 0.1s;
}

.pick_card:hover {
  background-color: #cd9cff56;
  border: 1px solid rgba(205, 156, 255, 0.38);
  color: #9d3afffd;
}
</style>
