<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="700"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          text
          v-on="on"
          v-show="allData.length == 0 ? visibleHistoric = false : visibleHistoric = true"
        >
          Historico 
        </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline blue lighten-2"
          primary-title
        >
          {{ service.name }}
        </v-card-title>

        <v-card-text>
          <lineChat 
            v-bind:service="service"
            v-bind:data="processData"
            v-bind:time="processTime"
          ></lineChat>
        </v-card-text>
        <v-card-text>
          <div v-show="monthPicker">
            <v-row>
                <v-col cols="12" sm="6" md="4">
                  <v-menu
                    ref="menu"
                    v-model="menu1"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="fromDate"
                        label="Until"
                        readonly
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="fromDate" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="menu1 = false">Cancel</v-btn>
                      <v-btn text color="primary" @click="$refs.menu1.save(fromDate)">OK</v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-menu
                    ref="menu"
                    v-model="menu2"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="untilDate"
                        label="From"
                        readonly
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="untilDate" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="menu2 = false">Cancel</v-btn>
                      <v-btn text color="primary" @click="$refs.menu2.save(untilDate)">OK</v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-btn color="green">
                    Go
                  </v-btn>
                </v-col>
                
              </v-row>
          </div>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn
            @click="monthPicker == false ? monthPicker = true : monthPicker = false"
            text
            :color="colorPicker"
          > Filter </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
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
import lineChat from "./charts/LineChart.vue"
import { Data } from "../function/index.js";

let novoData = new Data();

export default {
  components: { lineChat },
  props: [ "service" ],
  data() {
      return {
          monthPicker: false,
          colorPicker: 'red',
          visibleHistoric: false,
          dialog: false,
          allData: [],
          processData: [],
          processTime: [],
          fromDate: '',
          untilDate: '',
          date: new Date().toISOString().substr(0, 10),
          menu1: false,
          menu2: false
      }
  },
  async created(){
    this.allData = (await novoData.getData(this.service.mac, this.service.chipset, this.service.number)).data;
    this.processInfo();
  },
  methods: {
    processInfo(){
      let data = this.allData;
      for(let i = 0; i < 5; i++){
        this.processData.push(data[i]['value'])
        this.processTime.push(data[i]['time'])
      }
    }
  }
}
</script>