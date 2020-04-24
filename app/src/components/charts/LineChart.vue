<template>
    <div id="app">
        <vue-apex-charts width="100%" type="line" :options="options" :series="series"></vue-apex-charts>
        
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'


export default {
    props: [ 'data', 'time' ],
    components: {
        VueApexCharts
    },
    data(){
        return {
            options: {
                chart: {
                id: 'vuechart-example'
                },
                xaxis: {
                categories: this.time
                }
            },
            series: [{
                name: 'series-1',
                data: this.data
            }]
        }
    }
}
</script>