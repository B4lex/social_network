<template>
<v-app>
  <div class="navbar">
    <v-app-bar>
      <v-toolbar-title>
         <h1>Social Network</h1>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn  to="/home" v-show="this.$store.state.accessToken">
          <v-icon left dark>home</v-icon>
          Home
        </v-btn>
        <v-btn to="/signup" v-show="!this.$store.state.accessToken">
          <v-icon left dark>face</v-icon>
          Sign Up
        </v-btn>
          <v-btn to="/signin" v-show="!this.$store.state.accessToken">
          <v-icon left dark>lock_open</v-icon>
          Sign In
        </v-btn>
        <v-btn to="/username" v-show="this.$store.state.accessToken">
          <v-icon left dark>account_circle</v-icon>
          Profile
        </v-btn>
        <v-btn to="/logout" v-show="this.$store.state.accessToken">
          <v-icon left dark>logout</v-icon>
          Log Out
        </v-btn>
      </v-toolbar-items >
</v-app-bar>
  </div>
  <div class="content">
    <v-main class="justify-center">
      <router-view></router-view>
    </v-main>
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
