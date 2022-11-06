import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TestApp from '@/components/TestApp'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test',
      name: 'TestApp',
      component: TestApp
    },
  ]
})

new Vue({
  router, //追加
  render: h => h(App)
}).$mount('#app')