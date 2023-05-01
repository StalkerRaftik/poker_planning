<template>
  <v-app>
    <v-main>
      <router-view />
      <notifications class="notification" />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
};
</script>

<style scoped lang="scss">
.notification {
  margin-right: 8px;
  margin-top: 8px;
}
</style>
