<template>
  <div>
    <v-dialog
      v-model="dialog"
      width="80%"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          text
          v-on="on"
        >
          <v-icon>mdi-format-list-bulleted</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title
          class="headline green lighten-2"
          primary-title
        >
          Add service - {{ group }}
        </v-card-title>
        <br>
        <v-card-text>  
        <table v-show="showManual">
          <tr>
              <th>Name</th>
              <th>Channel</th>
              <th>Mac</th>
              <th>Chipset</th>
              <th>Number</th>
              <th>Add</th>
          </tr>
          
          <tr> 
              <td class="toCenter">
                <v-text-field v-model="manualService.name"></v-text-field>
              </td>
              <td class="toCenter">
                <v-text-field v-model="manualService.channel"></v-text-field>
              </td>
              <td class="toCenter">
                <v-text-field v-model="manualService.mac"></v-text-field>
              </td>
              <td class="toCenter">
                <v-text-field v-model="manualService.chipset"></v-text-field>
              </td>
              <td class="toCenter">
                <v-text-field v-model="manualService.number"></v-text-field>
              </td>
              <td> <v-btn text @click="addService(group, manualService)"> <v-icon>mdi-check</v-icon> </v-btn> </td>
          </tr>
        </table>  
        <table v-show="!showManual">
          <tr>
              <th>Name</th>
              <th>Channel</th>
              <th>Mac</th>
              <th>Chipset</th>
              <th>Number</th>
              <th>Add</th>
          </tr>
          
          <tr v-for="item in services" :key="item.mac"> 
              <td class="toCenter">{{item.name}}</td>
              <td class="toCenter">{{item.channel}}</td>
              <td class="toCenter">{{item.mac}}</td>
              <td class="toCenter">{{item.chipset}}</td>
              <td class="toCenter">{{item.number}}</td>
              <td> <v-btn text @click="addService(group, item)"> <v-icon>mdi-check</v-icon> </v-btn> </td>
          </tr>
        </table>

        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="grey"
            text
            @click="showManual = !showManual"
          >
            Manual
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            color="red"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>

        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
// import addService from "./addService.vue";
// import MockData from "../../mock/data.js";
import { Service, Group } from "../../function/index.js";

let novoGrupo = new Group();
let novoService = new Service();

export default {
  props: [ "group" ],
  components: {  },
  data() {
      return {
        services: [],
        groupName: '',
        dialog: false,
        showManual: false,
        manualService: {
          name: '',
          channel: '',
          mac: '',
          chipset: '',
          number: ''
        }

      }
  },
  async mounted(){
    this.services = (await novoService.getServices()).data
  },
  methods: {
    getServices(){
      
    },
    addService(group, item){
      novoGrupo.addInGroup(group, item)
    },
  }
}
</script>

<style scoped>
.toCenter{
    text-align: center;
}

</style>