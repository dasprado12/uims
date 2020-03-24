<template>
  <div class="text-left">
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn text v-on="on" >
            <v-icon> mdi-menu </v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item>
            <v-list-item-title><list-service v-bind:group="group"></list-service></v-list-item-title>
            <v-list-item-title><delete-group v-bind:group="group"></delete-group></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
import listService from "../service/listService.vue";
import deleteGroup from "./deleteGroup.vue";

export default {
    props: [ "group" ],
    components: {
        listService,
        deleteGroup
    }
}
</script>