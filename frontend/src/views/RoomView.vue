<template>
  <div class="room_view">
    <div v-if="error" class="room_error">
      <span class="room_error_text">{{ error }}</span>
      <router-link to="/" style="text-decoration: none">
        <v-btn
          @click="removeError"
          x-large
          color="primary"
          outlined
          width="300"
          height="80"
        >
          На главную
        </v-btn>
      </router-link>
    </div>
    <JoinRoomComponent v-if="!gameId" />
    <RoomComponent v-else />
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium at
    consequatur corporis dignissimos earum est et harum ipsum laboriosam, minima
    molestiae nobis odio pariatur quidem repudiandae sequi soluta vel veritatis.
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa debitis
    deserunt distinctio dolore ea eos excepturi illum impedit magni molestiae,
    natus nesciunt officia quam, ratione recusandae repudiandae sapiente vel
    voluptatum!
  </div>
</template>

<script>
import { mapState } from "vuex";
import RoomComponent from "@/components/RoomComponent";
import JoinRoomComponent from "@/components/JoinRoomComponent";

export default {
  name: "RoomView",
  components: { JoinRoomComponent, RoomComponent },
  data() {
    return {};
  },
  computed: {
    ...mapState("gameData", ["gameId"]),
    ...mapState("gameWebsocket", ["error"]),
  },
  mounted() {},
  methods: {
    removeError() {
      this.$store.dispatch("gameWebsocket/setError", null);
    },
  },
};
</script>

<style scoped lang="scss">
.room_view {
  width: 100%;
  height: 100%;
}

.room_error {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 64px;
  justify-content: center;
  align-items: center;
}

.room_error_text {
  font-weight: 300;
  font-size: 24px;
}
</style>
