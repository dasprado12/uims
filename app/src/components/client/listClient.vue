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
          All available clients
          <v-spacer></v-spacer>
          {{ group.group }}
        </v-card-title>
        <br>
        <v-card-text>    
          <table>
            <tr>
                <th>Name</th>
                <th>Channel</th>
                <th>Mac</th>
                <th>Chipset</th>
                <th>Add</th>
            </tr>
            <tr v-for="item in clients" :key="item.mac"> 
                <td class="toCenter">{{item.name}}</td>
                <td class="toCenter">{{item.channel}}</td>
                <td class="toCenter">{{item.mac}}</td>
                <td class="toCenter">{{item.chipset}}</td>
                <td> <v-btn text @click="bind_client(item)"> <v-icon>mdi-check</v-icon> </v-btn> </td> 
            </tr>
          </table>
          <v-dialog
            width="10%"
            v-model="ip_dialog"
          >
            <v-card>
              <v-card-title class="headline grey lighten-2"> 
                Add IP               
              </v-card-title><br>
              <v-card-text>
                <v-text-field solo label="IP" v-model="new_client.ip"></v-text-field>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text color="green" @click="send_client(new_client)">
                  Create
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
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

        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { Client, Group } from "../../function/index.js";

let client = new Client();
let group = new Group();

export default {
  props: [ "group" ],
  components: {  },
  data() {
      return {
        selectClient: true,
        clients: null,
        dialog: false,
        ip_dialog: false,
        new_client: {
          channel: '',
          chipset: '',
          location: '',
          mac: '',
          name: '',
          processor: '',
          serial: '',
          time: '',
          ip: ''
        }

      }
  },
  async mounted(){
    this.clients = (await client.GET_CLIENT()).data
  },
  methods: {
    bind_client(client){
      this.new_client = Object.assign({}, client)
      this.ip_dialog = true
    },
    send_client(client){
      group.ADD_CLIENT(this.group._id, client)
      console.log(this.group._id)
      console.log(client)
    }
  }
}
</script>

<style scoped>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #acacac;
}

</style>