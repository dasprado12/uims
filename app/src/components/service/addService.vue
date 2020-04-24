<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="80%"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          text
          v-on="on"
        >
          <v-icon class="grey--text">mdi-check</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title
          class="headline green lighten-2"
          primary-title
        >
          Choose a name to display
        </v-card-title>
        <br>
        <v-card-text>    
          <v-text-field
            label="Name"
            v-model="groupName"
          ></v-text-field>
          
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="red"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="green"
            text
            @click="show()"
          >
            Create
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import MockData from "../../mock/data.js";

export default {
  props: [ "service" ],
  data() {
      return {
        services: MockData.services,
        groupName: '',
        dialog: false,
      }
  },
  methods: {
    show(){
      alert(this.groupName)
    }
  }
}
</script>

<style scoped>
.toCenter{
    text-align: center;
}

</style>