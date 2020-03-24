<template>
  <v-app class="grey lighten-4">
    <ToolBar/>
      <v-content class="mx-4 mb-4">
          <router-view></router-view>
      </v-content>
    <!-- <teste-footer></teste-footer> -->
  </v-app>
</template>

<script>
import ToolBar from "./views/Toolbar.vue";
// import testeFooter from "./views/Footer.vue";

export default {
  components: {
    ToolBar,
    
  }
}
</script>

<style>
.brackgroundColor{
  background-color: rgb(19, 50, 151);
}
</style>
