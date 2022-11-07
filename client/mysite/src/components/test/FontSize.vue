<template>
    <v-card class="m-2 mt-5 p-2">
        <h1 v-bind:style="style">{{ message }}</h1>
        <v-text-field class="m-2" label="フォントサイズを入力" hide-details="auto" v-on:change="onChange();" value="20"></v-text-field>
    </v-card>
</template>
<script>
export default {
    data() {
        return {
            message: 'Change Size!',
            style:'font-size:20px; color:#0000e4;',
        }
    },
    methods: {
        onChange() {
            this.style = 'font-size:' +  event.target.value + 'px; color:#0000e4;';
        }
    },
}
</script>