<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="700"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          text small class="primary--text"
          v-on="on"
        >
          Historic
        </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline blue lighten-2"
          primary-title
        >
          {{ service.name }}
        </v-card-title>


        <!-- <v-divider></v-divider>

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
        </v-card-actions> -->
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
// import lineChat from "./charts/LineChart.vue"
// import { Data } from "../function/index.js";

// let novoData = new Data();

export default {
  // components: { lineChat },
  name: 'historic',
  props: [ "service" ],
  data() {
      return {
          dialog: false,
          // monthPicker: false,
          // colorPicker: 'red',
          // visibleHistoric: false,
          // allData: [],
          // processData: [],
          // processTime: [],
          // fromDate: '',
          // untilDate: '',
          // date: new Date().toISOString().substr(0, 10),
          // menu1: false,
          // menu2: false
      }
  },
  async created(){
    // this.allData = (await novoData.getData(this.service.mac, this.service.chipset, this.service.number)).data;
    // console.log(this.allData[0])
    // this.processInfo();
  },
  methods: {
    processInfo(){
      // let data = this.allData;
      // for(let i = 0; i < 5; i++){
      //   this.processData.push(data[i]['value'])
      //   this.processTime.push(data[i]['time'])
      // }
    }
  }
}
</script>