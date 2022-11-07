<template>
  <v-app id="app">
    <v-card class="mx-auto overflow-hidden" height="400" width="100%">
    <HeaderHtml></HeaderHtml>
    <router-view/>
    </v-card>
    <FooterHtml></FooterHtml>
  </v-app>
</template>
<script>
import HeaderHtml from './components/common/HeaderHtml';
import FooterHtml from './components/common/FooterHtml';

export default {
  name: 'App',
  components: {
    HeaderHtml,
    FooterHtml,
  },

  data: () => ({

  }),
};
</script>
