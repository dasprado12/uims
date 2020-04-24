<template>
    <div>
        <v-card class="card">
            <span>
                <div style="width: 100%; height: 5px;" 
                    v-bind:style="{backgroundColor: client_info.network_color}" />
            </span>
            <v-card-title>
                <div class="primary--text text-xs-center ma-3"> 
                    {{ client.name }}
                </div>
            </v-card-title>
            <v-card-text v-show="isShow" class="text-xs-center ">
                <div class="card-information">
                     
                    <span class="ma-3"> Status:  <span v-bind:style="{color: client_info.status_color}"> {{ client_info.status }}  </span> </span><br>
                    <span class="ma-3"> Network: <span :class="{ 
                        'on': client_info.network == 'On',
                        'fail': client_info.network == 'Fail',
                        'try': client_info.network == 'Ping...'
                        }"> {{ client_info.network }} </span> </span>
                </div>
            </v-card-text>
            <v-card-text v-show="!isShow" class="text-xs-center ">
                <div class="card-content" @click="alerta()">
                    <span class="ma-3"> channel:  {{ client.channel }} </span><br>
                    <span class="ma-3"> chipset:  {{ client.chipset }} </span><br>
                    <span class="ma-3"> mac: {{ client.mac }} </span><br>
                    <span class="ma-3"> IP: {{ client.ip }} </span>
                </div>
            </v-card-text>
            <v-card-text>
                <div class=""> 
                    
                </div>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions v-show="!show_delete"> 
                <Service v-bind:client="client"></Service>
                <!-- <v-btn text disabled v-show="!isWorking"> Searching.. </v-btn> -->
                <v-spacer></v-spacer>
                <v-btn class="primary--text" text @click="isShow = !isShow"> Config </v-btn>
            </v-card-actions>
            <v-card-actions class="red" v-show="show_delete">
                <v-btn class="delete" @click="deleteClient(client)" text> client </v-btn>
            </v-card-actions>
        </v-card>
    </div> 
</template>

<script>
import Service from "./Service.vue";
import { Network, Group } from "../function/index.js";
// import Ping from 'ping.js'

let ping = new Network();  
let group = new Group();

export default {    
    props: [ 'group', 'client' ],
    components: {
        Service
    },
    data(){
        return {
            isShow: true,
            isWorking: false,
            show_delete: false,
            client_info: {
                network_color: "#d81818",
                status_color: '',
                status: 'Unreacheable',
                network: 'Fail'
            },
            color_info: {
                working: "#33b113",
                ping: "#d88e18",
                not_working: "#d81818"
            },
        }    
    },
    async created(){
    },
    async mounted(){
        this.ping() 
        setInterval( () => {
                this.ping()
        }, 30000 );
    },
    methods: {
        alerta(){
            this.show_delete = !this.show_delete
        },
        async ping() {
            this.isWorking = false
            this.client_info.network = "Ping..."
            this.client_info.network_color = this.color_info.ping
            let result = (await ping.PING(this.client.ip)).data
            this.client_info.network = result.response
            if(result == 'On'){
                this.client_info.network = "On"
                this.client_info.network_color = this.color_info.working
                this.isWorking = true
            }if(result == 'Fail'){
                this.client_info.network = "Fail"
                this.client_info.network_color = this.color_info.not_working
                this.isWorking = false
            }
        },
        deleteClient(client){
            group.DELETE_CLIENT(this.group, client)
            console.log(this.group)
            console.log(client)
        }
    }
}
</script>

<style scoped>
.toCenter{
    align-content: center;
    text-align: center;
}
.main_title{
    font-size: 21px;
    color: rgb(80, 80, 80);
}
.exampleColor{
    color: #e91414da;
}

.card-information{
    line-height: 32px;
    font-size: 16px;
    font-family: 'Electrolize', sans-serif;
    border-radius: 5px;
    background-color: rgba(175, 180, 206, 0.246);
    margin-bottom: -20px;
}

.card-status{
    color: #d86e18;
}

.card-content{
    width: 100%;
    line-height: 32px;
    font-size: 16px;
    font-family: 'Electrolize', sans-serif;
    border-radius: 5px;
    background-color: rgba(211, 209, 118, 0.692);
    margin-top: -20px;
    margin-bottom: -20px;
}

.on{
    color: green;
}

.try{
    color: #d89e18;
}

.fail{
    color: #d81818;
}
</style>