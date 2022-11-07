<template>
  <div id="top-card">
    <v-card class="m-2 p-2">
      <h1>{{ message.toUpperCase() }}</h1>
      <v-text-field class="m-2" label="Main input" hide-details="auto" v-on:input="showTypeMessage();"></v-text-field>
      <v-btn elevation="2" large v-on:click="doAction();">
        Click
      </v-btn>
    </v-card>
    <v-card class="m-2 mt-5 p-2">
      <h1>Calc</h1>
      <h2>{{ '¥' + (price * 1.08) }}</h2>
      <v-text-field class="m-2" label="Price input" hide-details="auto" v-on:input="calc();"></v-text-field>
    </v-card>
  </div>
</template>

<script>
export default {

  name: "HomeBase",
  data() {
    return {
      message: 'Top Page',
      price: 1,
    }
  },
  methods: {
    doAction() {
      this.message = 'Clicked';
    },
    showTypeMessage() {
      this.message = event.target.value;
    },
    calc() {
      this.price = event.target.value;
    }
  },
}
</script>
