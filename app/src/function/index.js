import axios from 'axios'

// const API_DOMAIN =`${process.env.URL_PANIC_WEB}`

const API_DOMAIN = 'http://localhost:5000'
const DIMS_DOMAIN = 'https://uiot-dims.herokuapp.com'
// https://uiot-dims.herokuapp.com

const API_URLS = {
    'DIMS_CLIENT':   DIMS_DOMAIN + '/list/client',
    'DIMS_SERVICES': DIMS_DOMAIN + '/list/service',
    'DIMS_DATA':     DIMS_DOMAIN + '/list/data',
    
    'PING':     API_DOMAIN + '/ping',
    'GROUP':    API_DOMAIN + '/group',
    'CLIENT':   API_DOMAIN + '/group/client/',
    'SERVICE':  API_DOMAIN + '/service'  
}

export class Network {
    constructor(){

    }

    STATUS = (ip) => axios.get( ip+'/DEVICE=STATUS')

    PING = (ip) => axios.get(API_URLS.PING+'?ip='+ip)
}

export class Client {
    constructor(){

    }

    GET_CLIENT = () => axios.get(API_URLS.DIMS_CLIENT + '?latest=10')

    
}

export class Service {
    constructor(){

    }

    GET_SERVICE = (mac, chipset) => axios.get(API_URLS.SERVICE + `/${mac}/${chipset}`)
}

export class Data {
    constructor() {
    }

    GET_DATA = (mac, chipset, number) => axios.get(API_URLS.DATA+'?mac='+mac+'&chipset='+chipset+'&serviceNumber='+number)

    GET_LAST_DATA = (mac, chipset, number) => axios.get(API_URLS.DIMS_DATA+'?mac='+mac+'&chipset='+chipset+'&serviceNumber='+number+'&latest=1')
}

export class Group {
    constructor() {
    }

    GET_GROUP = () => axios.get(API_URLS.GROUP, { crossdomain: true })

    CREATE_GROUP = (group) => axios.post(API_URLS.GROUP, group )

    DELETE_GROUP = (id) => axios.delete(API_URLS.GROUP +'/'+ id )

    ADD_CLIENT = (id, client) => axios.post(API_URLS.CLIENT + id, client)

    DELETE_CLIENT = (id, client) => axios.post(API_URLS.CLIENT + `delete/${id}`, client)
}

export class Command {
    constructor() {
    }

    getCommand = () => axios.get(API_URLS.COMMAND)

    getByGroup = (group) => axios.get(API_URLS.COMMAND + '?group='+group)

    getOneCommand = (chipset, mac, number) => axios.get(API_URLS.COMMAND + '?chipset=' + chipset, '&mac=' + mac, '&number=' + number )

    changeCommand = (comando) => axios.post(API_URLS.CHANGE_COMMAND, comando)

    addCommand = (service, command) => axios.post(API_URLS.CREATE_COMMAND, { "services": service , "command": command })

    deleteCommand = (service, command) => axios.post(API_URLS.DELETE_COMMAND, { "services": service, "command": command })

    interact = (ip, params) => axios.get(ip + params)
}

export class Action {
    constructor() {

    }
    testDevice(ip){
        axios.get(ip)
        .then( function(response) {
            console.log(response.data)
        })
    }
}
