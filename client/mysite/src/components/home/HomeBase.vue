<template>
  <div>
    <XmasCompornent></XmasCompornent>
    <CircleAnimation></CircleAnimation>
  </div>
</template>

<script>
import XmasCompornent from '@/components/artwork/Xmas.vue';
import CircleAnimation from '@/components/artwork/CircleAnimation.vue';

/* ここに描画処理などを実装していきます */
export default {
  name: 'App',
  components: {
      XmasCompornent,
      CircleAnimation,
  },
}
</script>