<template>
    <v-card class="m-2 p-2">
        <h1>{{ message.toUpperCase() }}</h1>
        <v-text-field class="m-2" label="Main input" hide-details="auto" v-on:input="showTypeMessage();">
        </v-text-field>
        <v-btn elevation="2" large v-on:click="doAction();">
            Click
        </v-btn>
    </v-card>
</template>

<script>
export default {

    name: "TypeMessage",
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
    },
}
</script>