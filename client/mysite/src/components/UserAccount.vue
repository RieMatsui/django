<template>
    <div class="acount">
        <ol v-html="message"></ol>
    </div>
</template>

<script>
export default {
    data() {
        return { message : '<li>User Acount</li>'}
    }
}
</script>

<style scoped>
h1, h2 {
    color: black;
    font-weight: normal;
}
</style>