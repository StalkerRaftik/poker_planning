<template>
  <v-dialog v-model="showIssuesMenu" width="500">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        fab
        class="mr-3 issues_btn"
        dark
        color="primary"
        v-bind="attrs"
        v-on="on"
      >
        <v-icon dark> mdi-format-list-bulleted-square </v-icon>
      </v-btn>
    </template>

    <v-card class="body">
      <v-btn
        v-if="!showNewIssueForm"
        class="add_button"
        tile
        color="primary"
        outlined
        @click="showNewIssueForm = true"
      >
        <v-icon left> mdi-plus </v-icon>
        Добавить новую задачу
      </v-btn>
      <v-card v-else class="issue_form">
        <v-card-title>
          <v-text-field
            v-model="issueForm.name"
            label="Название"
            outlined
            dense
          ></v-text-field>
        </v-card-title>
        <v-card-text>
          <v-textarea
            v-model="issueForm.description"
            class="issue_text"
            outlined
            label="Описание"
            dense
            auto-grow
          />
        </v-card-text>
        <v-card-actions class="actions_container">
          <v-btn text color="cancel" @click="showNewIssueForm = false">
            Отмена
          </v-btn>
          <v-btn text color="primary" @click="createNewIssue">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
      <v-card v-for="(issue, id) in issues" :key="id">
        <v-card-title>{{ issue.name }}</v-card-title>
        <v-card-text>
          <div class="text--primary">{{ issue.description }}</div>
        </v-card-text>
        <v-card-actions class="actions_container">
          <v-btn @click="deleteIssue(id)" text color="error"> Удалить </v-btn>
        </v-card-actions>
      </v-card>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "IssuesPopup",
  data() {
    return {
      showIssuesMenu: false,
      showNewIssueForm: false,
      issueForm: {
        name: "",
        description: "",
      },
    };
  },
  computed: {
    ...mapState("gameData", ["issues"]),
  },
  methods: {
    createNewIssue() {
      this.$store.dispatch("gameWebsocket/createIssue", this.issueForm);
      this.showNewIssueForm = false;
    },
    deleteIssue(id) {
      this.$store.dispatch("gameData/deleteIssue", id);
    },
  },
};
</script>

<style scoped lang="scss">
.body {
  overflow-y: scroll;
  display: flex;
  flex-direction: column;
  gap: 24px;
  height: 80vh;
  padding: 16px;
}

.actions_container {
  display: flex;
  justify-content: end;
}

.issue_form {
  .v-card__text {
    padding-bottom: 0 !important;
  }

  .issue_text {
    min-height: 100px;
  }

  .v-card__title {
    padding-bottom: 0 !important;
  }
}
</style>
