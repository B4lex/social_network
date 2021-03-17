<template>
  <v-container class="header account">
    <v-row>
      <v-col cols="12" md="4">
        <v-row justify="center">
          <v-avatar size="10em" class="pa-2 rounded-circle">
              <img :src=post.userImage alt="John">
          </v-avatar>
        </v-row>
      </v-col>
      <v-col cols="12" md="8">
          <div>
              <h4>{{post.username}}</h4>
          </div>
          <v-row>
            <v-col cols="12" md="4">
              <span>
                <h3>{{post.images.length}}</h3>
                <p>images</p>
              </span>            </v-col>
            <v-col cols="12" md="4">
              <span>
                <h3>{{post.subscriptions}}</h3>
                <p>subscriptions</p>
              </span>
            </v-col>
            <v-col cols="12" md="4">
              <span>
                <h3>{{post.followers}}</h3>
                <p>followers</p>
              </span>
            </v-col>
            <div>
              <h5>email: {{post.email}}</h5>
            </div>
          </v-row>
      </v-col>
    </v-row>
    <div class="content">
      <v-row class="pa-16">
        <hr>
        <v-col v-for="image in post.images" :key="image" class="d-flex child-flex" cols="4">
          <v-img :src=image aspect-ratio="1" class="grey lighten-2">
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>
<script>
export default {
  name: 'account',
  data () {
    return {
      post: {
        id: 1,
        username: 'kostya12362',
        email: 'rota199804@gmail.com',
        userImage: 'https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/global-review/2019/ey-staff-at-event.jpg',
        subscriptions: 300,
        followers: 120,
        images: [
          'https://picsum.photos/500/300?image=10',
          'https://picsum.photos/500/300?image=11',
          'https://picsum.photos/500/300?image=12',
          'https://picsum.photos/500/300?image=13',
          'https://picsum.photos/500/300?image=14',
          'https://picsum.photos/500/300?image=15',
          'https://picsum.photos/500/300?image=16',
          'https://picsum.photos/500/300?image=17',
          'https://picsum.photos/500/300?image=18',
          'https://picsum.photos/500/300?image=19'
        ]
      }
    }
  }
}
</script>
<style>
.header {
  width: 60%;
  padding: 40px;
}
</style>
