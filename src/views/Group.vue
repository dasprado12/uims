<template>
    <div class="team">
        <v-container class="my-5">
            <v-layout row wrap>
                <v-flex xs12 sm12 md12 lg12 v-for="(item, index) in grupo" :key="index">
                    <v-card flat class="text-xs-center ma-3">
                        <Menu v-bind:group="item.group"></Menu>
                    </v-card>    
                    <v-card class="text-xs-center ma-3 card-title">
                        <div style="width: 100%; height: 5px;" 
                            v-bind:style="{backgroundColor: item.color}" >
                        </div>
                        
                        <v-card-text>
                            <p class="title"> {{ item.group }} </p>
                        </v-card-text>
                    </v-card>
                        <service 
                        v-bind:services="item.services"
                        v-bind:group="item.group" />
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import service from "../components/Service.vue";
import Menu from "../components/group/Menu.vue";
// import MockData from "../mock/data.js";
import { Group } from "../function/index.js";

let novoGrupo = new Group();

export default {
    components: {
        service,
        Menu
    },
    data(){
        return {
            grupo: null,
            color: '#673AB7'
        }
    },
    async created(){
        this.getGroups()
    },
    methods: {
        async getGroups(){
            this.grupo = (await novoGrupo.getGroup()).data
        },
        barStyle(color){
            return {
                "width": "100%",
                "height": "5px",
                "background-color": color
            }
        }
    },
}
</script>

<style scoped>
.title{
    text-align: center;
}

.card-title{
    height: 75px;
}

.low{
    background-color: #0051ff9f;
}

</style>