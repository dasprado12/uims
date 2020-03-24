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
          class="headline green lighten-2"
          primary-title
        >
          Create group
        </v-card-title>

        <v-card-text>
          <v-row>
           <v-col cols="12" sm="12" md="12">
              <v-text-field
                label="Name"
                v-model="groupName"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="12" md="12">
              <v-color-picker v-model="colorPicker" class="ma-2" hide-canvas hide-inputs></v-color-picker>
              {{ colorPicker }}
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

let novoGrupo = new Group();

export default {
  props: [ "service" ],
  data() {
      return {
        colorPicker: '#0053FFE8',
        groupName: '',
        dialog: false,
      }
  },
  methods: {
    createGroup(){
      novoGrupo.createGroup(this.groupName, this.colorPicker)
      this.dialog = false                                                                                                                                                                                           
    }
  }
}
</script>