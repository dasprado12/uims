<template>
  <nav>
    <v-app-bar app>
      <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"> </v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-light"> UIoT </span>
        <span> Board </span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <add-group></add-group>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app class="grey darken-1" >
      <v-list>
        <v-list>
          <v-list-item v-for="item in links" :key="item.text" :to="item.route">
            <v-list-item-title class="white--text">
              {{ item.text }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-list>
    </v-navigation-drawer>

  </nav>

</template>

<script>
import addGroup from "../components/toolbar/addGroup.vue";

export default {
  components: {  
    addGroup
},
  data() {
    return {
      drawer: false,
      links: [
      { icon: 'far fa-chart-bar', text: 'Dashboard', route: '/' },
      { icon: 'dashboard', text: 'Rules', route: '/rules' },
      { icon: 'fas fa-circle-notch fa-spin', text: 'Statistic', route: '/statistic'},
      { icon: 'fas fa-sliders-h', text: 'Settings', route: '/settings'},
    ],
    }
  }
}
</script>

<style scoped>
.description-project-text{
  size: 5px;
  color: rgb(255, 255, 255);
  margin-left: 15px;
}
.colorUIoT{
  color: rgb(71, 71, 71);
}
.colorBoard{
  color: rgb(128, 128, 128);
}
</style>