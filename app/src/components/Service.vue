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
                    class="primary--text"
                >
                    Interact
                </v-btn>
            </template>
                <v-layout fluid justify-center>
                    <v-flex xs12 sm12 md12 lg12 >
                        <v-card class="background">
                            <v-card-title class="base">
                                {{ client.name }}
                                <v-spacer></v-spacer>
                                <span class="primary--text ip"> IP: {{ client.ip }} </span>
                            </v-card-title>
                            <v-divider></v-divider>
                            <v-card-text>
                                <v-container grid-list-lg>
                                    <v-layout row wrap>
                                        <v-flex xs12 sm6 md4 lg4 v-for="service in services" :key="service.number">
                                            <v-card class="card">
                                                <v-card-title class="primary--text">
                                                    <v-badge
                                                        color="grey"
                                                        :content="service.number"
                                                    >
                                                        {{ service.name }}
                                                    </v-badge>
                                                </v-card-title>
                                                <v-card-subtitle class="subtitle ">
                                                    Last Update:
                                                </v-card-subtitle>
                                                <v-card-text class="body-card">
                                                    <div class="card-information">
                                                        <last-update v-bind:service="service"></last-update>
                                                    </div>
                                                </v-card-text>
                                                <v-card-actions>
                                                    <historic v-bind:service="service"></historic>
                                                    <v-spacer></v-spacer>
                                                    <v-btn 
                                                        text small class="primary--text"
                                                        :class="{active:interval}" @mousedown="start" @mouseup="stop"
                                                    > Actions </v-btn>
                                                </v-card-actions>
                                            </v-card>
                                        </v-flex>
                                    </v-layout>
                                </v-container>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer/>
                                <v-btn text></v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                </v-layout>
        </v-dialog>
    </div>
</template>

<script>
import historic from "./Data.vue"
import LastUpdate from "../components/data/LastUpdate.vue"
import { Service } from "../function/index.js"

let get_service = new Service()
// let data = new Data();

export default {
    props: [ 'client' ],
    components: {
        historic,
        LastUpdate
    },
    data(){
        return {
            lastUpdate: 'sem dados',
            interval:false,
            count: 0,
            dialog: false,
            statusColor: '#6add6ade',
            hover: false,
            ipColor: '#5ca1a666',
            services: []
        }
    },
    async mounted(){
        this.services = (await get_service.GET_SERVICE(this.client.mac, this.client.chipset)).data
        // setInterval( () => {
        //     this.lastUpdate = data.GET_DATA(this.service.mac, this.service.chipset. this.service.number)
        // },5000 )
    },
    methods: {
        start(){
            if(!this.interval){
                this.interval = setInterval( () => {
                    this.count++
                    if(this.count == 1){
                        alert('oi')
                    }
                }, 500)
            }  
        },
        stop(){
            clearInterval(this.interval)
            this.interval = false
            if(this.count == 0){
                alert('faça alguma coisa')
            }
            this.count = 0
        },
    }
}
</script>

<style scoped>
.subtitle{
    padding-top: 10px;
    padding-bottom: 1px;
    font-size: 12px;
}

.ip{
    font-size: 15px;
}

.card-information{
    padding-left: 10px;
    line-height: 50px;
    font-size: 16px;
    font-family: 'Electrolize', sans-serif;
    border-radius: 5px;
    background-color: rgba(175, 180, 206, 0.246);
    margin-bottom: -20px;
}

.body-card{
    padding-bottom: 30px;
}

</style>