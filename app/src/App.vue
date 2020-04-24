<template>
  <v-app class="grey lighten-4">
    <ToolBar/>
      <v-content class="mx-4 mb-4">

          <router-view></router-view>
          
      </v-content>
  </v-app>
</template>

<script>
import ToolBar from "./views/Toolbar.vue";

export default {
  components: {
    ToolBar,
    
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Electrolize&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');

.brackgroundColor{
  background-color: rgb(19, 50, 151);
}
</style>
