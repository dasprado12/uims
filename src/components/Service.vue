<template>
    <v-container grid-list-lg>

        <v-layout row wrap>
            <v-flex xs12 sm6 md6 lg4 v-for="i in service" :key="i.mac">
                <v-card>
                    <span v-if="i.ip">
                        existe ip
                    </span>
                    <span v-else>
                        <div style="width: 100%; height: 5px;" 
                        v-bind:style="{backgroundColor: '#6add6ade'}" >
                    </div>
                    </span>
                    
                        <v-card-title>
                            <div class="text-xs-center ma-3 mainTitle"> {{ i.name }}  {{ i }} </div>
                        </v-card-title>
                        <v-card-subtitle>
                            <div class=""> 
                                <lastUpdate v-bind:service="i"></lastUpdate>
                            </div>
                        </v-card-subtitle>
                        <v-divider></v-divider>
                        <v-card-actions>
                            <historico 
                                v-bind:service="i"
                            ></historico>
                            <command 
                                v-bind:command="i"
                                v-bind:group="group" 
                            ></command>
                            <v-spacer></v-spacer>
                            <settings 
                                v-bind:service="i"
                                v-bind:group="group"    
                            ></settings>
                        </v-card-actions>
                </v-card> 
            </v-flex>
        </v-layout> 
  
    </v-container>   
</template>

<script>
import lastUpdate from "../components/LastUpdate.vue";
import Historico from "../components/Data.vue";
import command from "../components/service/Command.vue";
import settings from "../components/service/Settings.vue";
import { Command } from "../function/index.js";

let newService = new Command();

export default {
    props: [ 'services', 'group' ],
    components: {
        lastUpdate,
        Historico,
        command,
        settings
    },
    data(){
        return {
            hover: false,
            ipColor: '#5ca1a666',
            service: '',
        }
    },
    async created(){
        this.getService();
    },
    mounted(){

    },
    methods: {
        async getService(){
            console.log(this.group)
            this.service = (await newService.getByGroup(this.group)).data 
            console.log()
        },
        checkData(){

        }
    }
}
</script>

<style scoped>
.toCenter{
    align-content: center;
    text-align: center;
}
.mainTitle{
    color: rgb(42, 42, 42);
    /* color: #6add6ade; */
    
}
</style>