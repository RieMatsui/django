<template>
    <div class="acount">
        <h1>{{ msg }}</h1>
        userAccount
    </div>
</template>

<script>
    export default {
        name: "UserAccount",
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