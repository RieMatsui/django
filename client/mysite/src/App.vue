<template>
  <v-app id="app">
    <v-card class="mx-auto overflow-hidden" min-height="750px" width="100%">
    <HeaderHtml></HeaderHtml>
    <v-card class="p-3 m-2" elevation="3" outlined>
      <router-view/>
    </v-card>
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
