import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './api/store'
import vuetify from './plugins/vuetify'
import '@mdi/font/css/materialdesignicons.css'
import Vuetify from 'vuetify'

Vue.config.productionTip = false

Vue.use(Vuetify, {
  iconfont: 'mdi'
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'signin' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
