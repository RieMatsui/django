import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import App from './App.vue'
import VueRouter from 'vue-router'
import UserAccount from '@/components/UserAccount'
import HomeBase from '@/components/HomeBase'
import vuetify from './plugins/vuetify'


Vue.use(Vuetify)

const opts = {}

export default new Vuetify(opts)

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomeBase',
      component: HomeBase
    },
    {
      path: '/acount',
      name: 'UserAccount',
      component: UserAccount
    },
  ]
})

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')