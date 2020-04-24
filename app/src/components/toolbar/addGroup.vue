<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          text
          v-on="on"
        >
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title
          v-bind:style="{backgroundColor: group.color }"
          primary-title
        >
          Create group
        </v-card-title>

        <v-card-text>
          <v-row>
           <v-col cols="12" sm="12" md="12">
              <v-text-field
                label="Name"
                v-model="group.group"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="toCenter">
            <v-col cols="12" sm="12" md="12">
              <v-color-picker width="100%" v-model="group.color" class="ma-2" hide-canvas hide-inputs></v-color-picker>
              
            </v-col>
          </v-row>
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
            @click="createGroup()"
          >
            Create
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
  props: [ "service" ],
  data() {
      return {
        group: {
          color: '#0053FFaa',
          group: '',
        },
        dialog: false,
      }
  },
  methods: {
    createGroup(){
      group.CREATE_GROUP(this.group)
      console.log(this.group)
      this.dialog = false                                                                                                                                                                                           
    }
  }
}
</script>

<style scoped>
.toCenter{
  align-content: center;
  text-align: center;
}
</style>