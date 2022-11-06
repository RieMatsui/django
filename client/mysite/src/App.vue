<template>
  <div id="app">
    <HeaderHtml/>
    <router-view/>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App" message="Hello"/>
    <FooterHtml/>
  </div>
</template>

<script>
import HeaderHtml from "./components/common/HeaderHtml.vue";
import FooterHtml from "./components/common/FooterHtml.vue";
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HeaderHtml,
    HelloWorld,
    FooterHtml,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
