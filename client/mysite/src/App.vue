<template>
  <div id="app">
    <HeaderHtml/>
    <router-view/>
    <FooterHtml/>
  </div>
</template>

<script>
import HeaderHtml from "./components/common/HeaderHtml.vue";
import FooterHtml from "./components/common/FooterHtml.vue";

export default {
  name: 'App',
  components: {
    HeaderHtml,
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
