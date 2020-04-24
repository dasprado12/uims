<template>
    <div class="lastUpdate">
        <v-div class="mainTitle">
            {{ service.parameter }}: <span             
            :class="{ 
                'low': lastData == 'sem dados', 
                'medium': lastData == 'carregando', 
                'high': lastData != 'sem dados' & lastData != 'carregando' 
                }"> {{ lastData }} </span> {{ service.unit }}
        </v-div>
    </div>
</template>

 <script>
import { Data } from "../../function/index.js"

let new_data = new Data();

export default {
    name: "lastUpdate",
    props: [ "service" ],
    data(){
        return {
            lastData: 'sem dados',
        }
    },
    async mounted(){
        setInterval(() => {
            this.getLastData();
        }, 5000)    
    },
    methods: {
        async getLastData(){
            this.lastData = 'carregando'
            let data = (await new_data.GET_LAST_DATA(this.service.mac, this.service.chipset, this.service.number)).data;
            let lastData = data[0]['value'][0]
            if(this.service.paremter == null){
                this.service.parameter = "value"
            }
            if(lastData.length == 0){
                lastData == 'sem dados'
            }else{
                this.lastData = lastData
            }
        }     

    }
}
</script>

<style scoped>
.low{
    color:rgb(192, 13, 13);
}
.medium{
    color: rgb(153, 144, 25);
}
.high{
    color: rgb(6, 116, 24);
}
.mainTitle{
    font-size: 18px;
}
</style>