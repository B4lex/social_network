<template>
<v-app>
  <div class="navbar">
    <v-app-bar>
      <span class="hidden-sm-and-up">
        <v-toolbar-side-icon @click="sidebar = !sidebar">
      </v-toolbar-side-icon>
      </span>
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
         Social Network
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn flat to="/home">
          <v-icon left dark>home</v-icon>
          Home
        </v-btn>
        <v-btn flat to="/signup">
          <v-icon left dark>face</v-icon>
          Sign Up
        </v-btn>
          <v-btn flat to="/signin">
          <v-icon left dark>lock_open</v-icon>
          Sign In
        </v-btn>
        <v-btn flat to="/username">
          <v-icon left dark>account_circle</v-icon>
          Profile
        </v-btn>
      </v-toolbar-items >
</v-app-bar>
  </div>
  <div class="content">
    <v-content class="justify-center">
      <router-view></router-view>
    </v-content>
  </div>
</v-app>
</template>

<script>

export default {
}
</script>
<style>
  .navbar {
    background-color: rebeccapurple;
  }

</style>
