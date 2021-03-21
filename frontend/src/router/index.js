import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '@/components/Home'
import signin from '@/components/SignIn'
import signup from '@/components/SignUp'
import account from '@/components/Account'
import logout from '../views/LogOut'

Vue.use(VueRouter)

const routes = [
  { path: '/home', component: home, name: 'home', meta: { requiresLogin: true } },
  { path: '/signin', component: signin, name: 'signin' },
  { path: '/signup', component: signup, name: 'signup' },
  { path: '/logout', component: logout, name: 'logout', meta: { requiresLogin: true } },
  { path: '/username', component: account, name: 'username', meta: { requiresLogin: true } }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
