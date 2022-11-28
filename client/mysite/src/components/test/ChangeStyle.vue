<template>
    <v-card class="m-2 mt-5 p-2">
        <h1 v-bind:class="classes">{{ message }}</h1>
        <h2 v-bind:style="styles">{{ message }}</h2>
        <v-btn elevation="2" large v-on:click="changeStyle();">Click</v-btn>
    </v-card>
</template>
<script>
let classObj = {
    success_bule: true,
    warning_red: false,
};
export default {
    name: "HomeChangeStyle",
    data() {
        return {
            message: "Change Style",
            styles: {
                margin: '10px',
                padding: '10px',
                fontSize: '30px',
                backgroundColor: '#eee6ff',
                border: '3px solid #5c00d2',
            },
            classes: classObj,
        }
    },
    methods: {
        changeStyle() {
            classObj.success_bule = !classObj.success_bule;
            classObj.warning_red = !classObj.warning_red;
        }
    }
}
</script>
<style>
.warning_red {
    font-size: 25px;
    font-weight: 600;
    font-style: normal;
    color: #e54304;
    background-color: #FFFFFF;
}

.success_bule {
    font-size: 25px;
    font-weight: 600;
    font-style: italic;
    color: #5c00d2;
    background-color: #FFFFFF;
}
</style>

