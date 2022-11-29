<template>
    <v-card class="mt-5 p-4">
        <div>
            <h1 class="m-3">GASP Sample</h1>
            <div class="circle"></div>
        </div>
    </v-card>
</template>

<script>
    import {gsap, Elastic} from "gsap";

    export default {
        name: 'cercleMove',
        mounted() {
            const animation = gsap.to(".circle", {
                backgroundColor: "blue",
                x: 500,
                ease: Elastic.easeOut,
                duration: 5,
            })
            animation;
        }

    }
</script>

<style>
    .circle {
        background-color: aqua;
        width: 200px;
        height: 200px;
        border-radius: 50%;
        text-align: left;
    }
</style>