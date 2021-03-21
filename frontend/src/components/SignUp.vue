<template>
    <v-layout row wrap>
      <v-flex xs12 sm6 offset-sm3 mt-5>
        <h1>Sign Up</h1>
      </v-flex>
      <v-flex xs12 sm8 offset-sm2 md6 offset-md3 mt-3>
        <h3 v-if="sendEmail" class="alert alert-success" >Registration completed successfully</h3>
        <form v-on:submit.prevent="signup">
          <v-layout column>
            <v-flex>
              <v-text-field name="username" v-model="form.username" label="Username" id="confirmPassword" type="text" required></v-text-field>
              <div v-if="incorrectAuth">
                <p class="alert alert-danger" v-for="item in error.username" :key="item">{{ item }}</p>
              </div>
            </v-flex>
            <v-flex>
              <v-text-field name="first_name" v-model="form.first_name" label="First name" id="first_name" type="text" required></v-text-field>
            </v-flex>
            <v-flex>
              <v-text-field name="last_name" v-model="form.last_name" label="Last name" id="last_name" type="text" required></v-text-field>
            </v-flex>
            <v-flex>
              <v-text-field name="email" v-model="form.email" label="Email" id="email" type="email" required></v-text-field>
              <div v-if="incorrectAuth">
                <p class="alert alert-danger" v-for="item in error.email" :key="item">{{ item }}</p>
              </div>
            </v-flex>
            <v-flex>
              <v-text-field name="password" v-model="form.password" label="Password" id="password" type="password" required></v-text-field>
              <div v-if="incorrectAuth">
                <p class="alert alert-danger" v-for="item in error.password" :key="item">{{ item }}</p>
              </div>
            </v-flex>
            <v-flex>
              <v-text-field name="password2" v-model="form.password2" label="Confirm Password" id="password2" type="password" required></v-text-field>
            </v-flex>
            <v-flex class="text-xs-center" mt-5>
              <v-btn color="primary" type="submit">Sign Up</v-btn>
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
</template>

<script>
// import axios from 'axios'
import { getAPI } from '../api/axios-api'

export default {
  name: 'signup',
  data () {
    return {
      form: {
        username: '',
        password: '',
        password2: '',
        first_name: '',
        last_name: '',
        email: ''
      },
      error: {
        username: '',
        password: '',
        email: ''
      },
      incorrectSignIn: false,
      sendEmail: false
    }
  },
  methods: {
    signup (context) {
      getAPI.post('http://127.0.0.1:8000/api/signup/', this.form)
        .then(function (response) { this.form = response.data; this.sendEmail = true })
        .catch((error) => { this.error = error.response.data; this.incorrectAuth = true })
    }
  }
}
</script>
