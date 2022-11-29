<template>
  <v-app id="app">
    <v-card class="mx-auto overflow-hidden" min-height="750px" width="100%">
      <HeaderHtml></HeaderHtml>
      <div class="p-3 m-2" elevation="3" outlined>
        <router-view />
      </div>
      <FooterHtml></FooterHtml>
    </v-card>
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
