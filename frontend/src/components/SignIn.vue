<template>
    <v-layout row wrap>
      <v-flex xs12 sm6 offset-sm3 mt-3 class="text-xs-center" mt-5>
        <h1>Sign In</h1>
      </v-flex>
      <v-flex xs12 sm6 offset-sm3 mt-3>
        <p v-if="incorrectAuth"></p>
        <div v-if="incorrectAuth">
          <p class="alert alert-danger">Incorrect username or password entered</p>
        </div>
        <form v-on:submit.prevent="signin">
          <v-layout column>
            <v-flex>
              <v-text-field name="username" v-model="username" label="Username" id="username" type="username" required></v-text-field>
            </v-flex>
            <v-flex>
              <v-text-field name="password" v-model="password"  label="Password" id="password" type="password" required></v-text-field>
            </v-flex>
            <v-flex class="text-xs-center" mt-5>
              <v-btn color="primary" type="submit">Sign In</v-btn>
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
</template>

<script>
export default {
  name: 'signin',
  data () {
    return {
      username: '',
      password: '',
      incorrectAuth: false
    }
  },
  methods: {
    signin () {
      this.$store.dispatch('userSignin', {
        username: this.username,
        password: this.password
      })
        .then((response) => {
          this.$router.push({ name: 'home' })
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
    }
  }
}
</script>
