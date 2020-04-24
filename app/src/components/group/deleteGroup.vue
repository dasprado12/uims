<template>
  <div>
    <v-dialog
      v-model="dialog"
      width="30%"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          text
          v-on="on"
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title
          class="headline red lighten-2"
          primary-title
        >
          Delete group
        </v-card-title>
        <br>
        <v-card-text>    
            Do you want delete {{ group.group }}
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
            @click="excludeGroup()"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { Group } from "../../function/index.js";

let group = new Group();

export default {
  props: [ "group" ],
  data() {
      return {
        groupName: '',
        dialog: false,
      }
  },
  methods: {
    excludeGroup(){
        group.DELETE_GROUP(this.group._id)
        this.dialog = false
    }
  }
}
</script>

<style scoped>
.toCenter{
    text-align: center;
}

</style>