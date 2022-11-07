<template>
    <v-card class="m-2 mt-5 p-2">
        <h1>List Add</h1>
        <ol v-html="messages"></ol>
        <v-text-field class="m-2" label="追加する表を入力してください" hide-details="auto" v-on:input="getInputTxt();"></v-text-field>
        <v-btn elevation="2" large v-on:click="listAdd();">Click</v-btn>
    </v-card>
</template>

<script>
export default {
    name: "HomeList",
    data() {
        return {
            messages: '<li>Hello vue!</li>',
        }
    },
    methods: {
        getInputTxt() {
            this.message = event.target.value;
        },
        listAdd() {
            this.messages += '<li>' + this.message + '</li>';
        },
    },
}
</script>
