<template>
    <div class="test-app">
        <h1>{{ msg }}</h1>
        <router-link to="/">TOP</router-link>
    </div>
</template>

<script>
    export default {
        name: "test-app",
        data() {
            return {
                msg: 'test message',
            }
        }
    }
</script>

<style scoped>
h1, h2 {
    color: black;
    font-weight: normal;
}
</style>