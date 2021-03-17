import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '@/components/Home'
import signin from '@/components/SignIn'
import signup from '@/components/SignUp'
import account from '@/components/Account'

Vue.use(VueRouter)

const routes = [
  { path: '/home', component: home },
  { path: '/signin', component: signin },
  { path: '/signup', component: signup },
  { path: '/username', component: account }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
