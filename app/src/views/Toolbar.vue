<template>
  <nav>
    <v-app-bar app flat class="base">
      <v-app-bar-nav-icon class="" @click="drawer = !drawer"> </v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase grey--text--{darken}">
        <span class="font-weight-light"> UIoT </span>
        <span> Board </span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <add-group></add-group>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app class="" >
      
        <v-list-item>
          <v-list-item-avatar>
          <v-img src="../assets/12036880.png"></v-img>
        </v-list-item-avatar>
          <v-list-item-content>

            <v-list-item-title class="title grey--text ">
              Dashboard
            </v-list-item-title>
            <v-list-item-subtitle class="grey--text font-weight-thinoverline">
              <span class="subtitle">Universal Internet of Things </span>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item v-for="item in links" :key="item.text" :to="item.route">
          <v-list-item-icon>
            <v-icon> {{ item.icon }} </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <span class="primary--text"> {{ item.text }} </span>
          </v-list-item-content>
        </v-list-item>
      <template v-slot:append>
        <div class="toCenter pa-5">
        <!-- <v-icon> mdi-weather-sunny </v-icon> -->
        <v-switch
          v-model="$vuetify.theme.dark"
          hide-details
          inset
          label="Theme Dark"
        />
        <!-- <v-icon> mdi-weather-night </v-icon> -->
        </div>
      </template>


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
      color: '#6f71bc',
      drawer: false,
      links: [
        { icon: 'mdi-view-dashboard', text: 'Dashboard', route: '/' },
        { icon: 'mdi-ruler', text: 'Rules', route: '/rules' },
        { icon: 'mdi-chart-bar', text: 'Statistic', route: '/statistic'},
        { icon: 'mdi-information', text: 'Settings', route: '/settings'},
      ],
    }
  }
}
</script>

<style scoped>
.subtitle{
  font-size: 13px;
}
.fundo{
  background-color: #6f71bc;
  height: 10x;
  line-height: 10px;
}
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
.menu-title{
  padding-bottom: 10px;
}
.toCenter{
  align-content: center;
}
</style>fundo