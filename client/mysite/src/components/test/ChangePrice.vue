<template>
    <v-card class="m-2 mt-5 p-2">
        <h1>Calc</h1>
        <h2>{{ '¥' + (price * 1.08) }}</h2>
        <v-text-field class="m-2" label="Price input" hide-details="auto" v-on:input="calc();"></v-text-field>
    </v-card>
</template>
<script>
export default {

    name: "ChangePrice",
    data() {
        return {
            price: 1,
        }
    },
    methods: {
        calc() {
            this.price = event.target.value;
        }
    },
}
</script>