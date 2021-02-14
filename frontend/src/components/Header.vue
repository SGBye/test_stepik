<template>
    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="py-0 fill-height">
        <router-link to="/" class="header-title">Настройки "Scorick"</router-link>
        <v-spacer></v-spacer>
      </v-container>
    </v-app-bar>
</template>

<script>
export default {
name: "Header"
}
</script>


<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&display=swap');

  .header-title {
    cursor: pointer;
    color: black;
    font-family: 'Tenor Sans', sans-serif;
    font-size: 33px;
    font-weight: bold;
    text-decoration: none;
  }
</style>
