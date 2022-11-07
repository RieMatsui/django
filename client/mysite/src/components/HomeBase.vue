<template>
  <div id="top-card">
    <h1>{{ message }}</h1>
    <v-text-field class="m-2" label="Main input" hide-details="auto" v-on:input="showTypeMessage();"></v-text-field>
    <v-btn elevation="2" large v-on:click="doAction();">
      Click
    </v-btn>
  </div>
</template>

<script>

export default {
  name: "HomeBase",
  data() {
    return {
      message: 'Top Page',
    }
  },
  methods: {
    doAction() {
      this.message = 'Clicked';
    },
    showTypeMessage() {
      this.message = event.target.value;
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
