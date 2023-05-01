<template>
  <div class="loader_container">
    <LoaderComponent style="width: 100px; height: 100px" />
  </div>
</template>

<script>
import LoaderComponent from "@/components/LoaderComponent";
export default {
  name: "JoinRoomComponent",
  components: { LoaderComponent },
  mounted() {
    this.$store.dispatch(
      "gameWebsocket/connectGame",
      this.$route.params.game_id
    );
  },
};
</script>

<style scoped>
.loader_container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
