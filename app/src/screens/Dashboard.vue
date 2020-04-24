<template>
    <div class="dashboard" >
        <v-container class="my-5" >
            <v-layout row wrap >
                <v-flex xs12 sm12 md12 lg12 v-for="(item, index) in grupo" :key="`${index}-${item._id} ` ">
                    <v-card flat class="background text-xs-center ma-3">
                        <Menu class="menu" v-bind:group="item"></Menu>
                    </v-card>    
                    <v-card class="text-xs-center ma-3 card-title">
                        <div style="width: 100%; height: 5px;" 
                            v-bind:style="{backgroundColor: item.color}" >
                        </div>
                        
                        <v-card-text class="">
                            <p class="title primary--text"> {{ item.group }} </p>
                        </v-card-text>
                    </v-card> 
                <v-container grid-list-lg>
                    <v-layout row wrap>
                        <v-flex xs6 sm4 md3 lg3 xl2 v-for="i in item.clients" :key="`${i}-${item._id}`"> 
                            <client v-bind:group="item._id" v-bind:client="i" ></client>
                        </v-flex>
                    </v-layout>
                </v-container>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import Menu from "../components/group/Menu.vue";
import Client from '../components/Client.vue';
import { Group } from "../function/index.js";

let group = new Group();

export default {
    components: {
        Menu,
        Client
    },
    data(){
        return {
            grupo: [ 
                
            ],
            color: '#673AB7'
        }
    },
    async created(){
        this.grupo = (await group.GET_GROUP()).data
    },
    methods: {
    },
}
</script>

<style scoped>
.title{
    width: 100%;
    text-align: center;
    
}
.card-title{
    height: 75px;   
}
</style>