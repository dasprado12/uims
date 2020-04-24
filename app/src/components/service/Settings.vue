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
          <!-- <v-icon> mdi-settings </v-icon> -->
          config
        </v-btn>
      </template>
      <v-card>
        <v-card-title
          class="headline grey darkeen-2"
          primary-title
        >
          Settings [ {{ group }} > {{ service.name }} ]
        </v-card-title>
        <br>
        <v-card-text> 
        <div v-show="!visibleDelete">
        <v-card-title>
            Service
        </v-card-title>   
        <v-row>
            <v-col cols="2" sm="4" md="3">
            <v-text-field
                label="Chipset"
                v-model="service.chipset"
                disabled
            ></v-text-field>
            </v-col>
            <v-col cols="12" sm="4" md="3">
            <v-text-field
                label="Mac"
                v-model="service.mac"
                disabled
            ></v-text-field>
            </v-col>
            <v-col cols="12" sm="4" md="3">
            <v-text-field
                label="Number"
                v-model="service.number"
                disabled
            ></v-text-field>
            </v-col>
            <v-col cols="12" sm="4" md="3">
            <v-text-field
                label="Name"
                v-model="service.name"
                disabled
            ></v-text-field>
            </v-col>
            <v-col cols="12" sm="2" md="3">
            <v-text-field
                label="Parameter"
                v-model="service.parameter"
                disabled
            ></v-text-field>
            </v-col>
            <v-col cols="12" sm="2" md="3">
            <v-text-field
                label="Unit"
                v-model="service.unit"
                disabled
            ></v-text-field>
            </v-col>
            <v-col cols="12" sm="4" md="3">
            <v-text-field
                label="IP"
                v-model="service.ip"
            ></v-text-field>
            </v-col>
            <v-col cols="12" sm="1" md="1">
              <v-btn @click="editService()">
                enviar
              </v-btn>
            </v-col>
        </v-row>
        <v-divider></v-divider>
        </div>
        <v-row>
          <v-col v-show="visibleDelete" cols="12" sm="12" md="12" class="toCenter">
              <v-btn color="red--text" @click="deleteService()">
                  Delete Service
              </v-btn>
            </v-col>
        </v-row>
      

        
        <div v-show="visibleCommand">
        <v-card-title>
            Add command
        </v-card-title>
            <v-row>
              <v-col cols="12" sm="4" md="4">
                <v-text-field
                    label="ip"
                    v-model="ip"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4" md="4">
                <v-text-field
                    label="params"
                    v-model="params"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4" md="4">
                <v-text-field
                    label="Button Name"
                    v-model="btnName"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="12" class="toCenter">
                <v-btn color="green--text" @click="createCommand()">
                    Create Command
                </v-btn>
              </v-col>
            </v-row>
          </div>
        
        <v-divider></v-divider>
        <v-card-title>
            All Commands
        </v-card-title>
            <v-row>
              <table>
                  <tr>
                    <th>Name</th>
                    <th>IP</th>
                    <th>Params</th>
                    <th>Remove</th>
                </tr>
                <tr v-for="item in commands" :key="item.mac"> 
                    <td class="toCenter">{{item.name}}</td>
                    <td class="toCenter">{{item.ip}}</td>
                    <td class="toCenter">{{item.params}}</td>
                    <td class="tocenter"><v-btn text @click="deleteCommand(service, item)"> <v-icon>mdi-close</v-icon> </v-btn></td>
                </tr>
              </table>
              
              
            </v-row>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="red"
            text
            @click="visibleDelete = !visibleDelete"
          >
            Delete Service
          </v-btn>
          <v-btn
            color="green"
            text
            @click="visibleCommand = !visibleCommand"
          >
            Add command
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
import { Group, Command } from "../../function/index.js";

let novoGrupo = new Group();
let novoComando = new Command();

export default {
  props: [ "service", 'group' ],
  data() {
      return {
        visibleDelete: false,
        visibleCommand: false,
        btnName: '',
        groupName: '',
        dialog: false,
        commands: [],
        ip: '',
        params: '',
      }
  },
  async created(){
    this.getCommand();
  },
  methods: {
    async getCommand(){
      let service = this.service
      this.commands = (await novoComando.getOneCommand(service.chipset, service.mac, service.number)).data[0]['command']
    },
    deleteService(){
      novoGrupo.deleteInGroup(this.group, this.service)
    },
    createCommand(){
      let comando = { 
        "ip": this.ip,
        "params": this.params,
        "name": this.btnName
      }
      fetch(novoComando.addCommand(this.service, comando))
      .then(this.getCommand())
      
    },
    deleteCommand(service, command){
      novoComando.deleteCommand(service, command)
      this.getCommand()
    },
    editService(){
      novoComando.changeCommand(this.service)
    }
  }
}
</script>

<style scoped>
.toCenter{
  text-align: center;
}
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
  background-color: #dddddd;
}
</style>