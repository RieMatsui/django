import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import vuetify from './plugins/vuetify'
import 'vuetify/dist/vuetify.min.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueRouter from 'vue-router'
import UserAccount from '@/components/UserAccount'
import HomeBase from '@/components/home/HomeBase'
import TestBase from '@/components/test/TestBase'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.devtools = true;

Vue.use(Vuetify)

const opts = {}

export default new Vuetify(opts)

Vue.use(VueRouter)

// BootstrapVueをプロジェクト全体で利用できるようにする
Vue.use(BootstrapVue)

// BootstrapVueアイコンコンポーネントプラグインの使用
Vue.use(IconsPlugin)

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
    {
      path: '/test',
      name: 'TestBase',
      component: TestBase,
    },
  ]
})

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')