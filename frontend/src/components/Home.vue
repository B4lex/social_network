<template>
    <v-row justify="center">
    <v-card v-for="item in post" :key="item.id" max-width="800" class="mx-12 my-10">
      <v-card-actions class="mx-auto my-auto">
        <v-img :src="item.userImage" max-width="50" class="rounded-circle" height="50" width="100%"></v-img>
        <v-card-title class="font-weight-medium">{{item.username}}</v-card-title>
        <v-spacer></v-spacer>
        <v-dialog transition="dialog-top-transition" max-width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon color=black v-bind="attrs" v-on="on">
              <v-icon>more_horiz</v-icon>
            </v-btn>
          </template>
          <template>
            <v-sheet elevation="4" wight="50">
              <div class="d-grid gap-2 mx-auto">
                <v-btn block large>Update</v-btn>
                <v-btn block large color="error">Delete</v-btn>
              </div>
            </v-sheet>
          </template>
        </v-dialog>
      </v-card-actions>
    <v-img :src="item.postImage" max-height="800" contain class="grey darken-4"></v-img>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn icon color=red>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-card-text>{{item.likes.length}}</v-card-text>
    </v-card-actions>
    <v-card-text>
      <p class="display-1 text--primary">{{item.title}}</p>
    </v-card-text>
      <hr>
      <v-card-actions v-if="item.descriptions">
        <v-btn color="orange lighten-2" text>Explore</v-btn>
        <v-spacer></v-spacer>
        <v-btn icon @click="item.show = !item.show">
          <v-icon>{{ item.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-expand-transition  v-if="item.show">
        <div>
          <v-divider></v-divider>
          <v-card-text>
            {{item.descriptions}}
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
    </v-row>
</template>
<script>
import axios from 'axios'

export default {
  name: 'home',
  data () {
    axios.get('http://127.0.0.1:8000/api/images/event/').then((response) => {
      this.candidates = response.data
      console.log(response)
    })
    return {
      candidates: null,
      post: [
        {
          id: 1,
          show: false,
          username: 'admin',
          title: 'Admin',
          postImage: 'https://www.w3schools.com/w3css/img_lights.jpg',
          userImage: 'https://www.w3schools.com/w3css/img_lights.jpg',
          descriptions: '',
          likes: [
            'kostya',
            'alex',
            'jeck'
          ]
        },
        {
          id: 2,
          show: false,
          username: 'admin',
          title: 'Admin',
          postImage: 'https://www.w3schools.com/w3css/img_lights.jpg',
          userImage: 'https://www.w3schools.com/w3css/img_lights.jpg',
          descriptions: '',
          likes: [
            'kostya',
            'alex',
            'jeck'
          ]
        },
        {
          id: 3,
          show: false,
          username: 'Heroke',
          title: 'mer',
          postImage: 'https://www.w3schools.com/w3css/img_lights.jpg',
          userImage: 'https://www.w3schools.com/w3css/img_lights.jpg',
          descriptions: 'sdfsdfsdffsdfdsfsd',
          likes: [
            'kostya',
            'alex',
            'jeck'
          ]
        }
      ]
    }
  },
  method: {
    getUsers () {
      console.log('Getting data')
      axios.get('http://127.0.0.1:8000/api/event/').then((response) => {
        this.candidates = response.data
        console.log(response)
      })
    }
  }
}
</script>
