import axios from 'axios'

// const API_DOMAIN =`${process.env.URL_PANIC_WEB}`

const API_DOMAIN = 'http://localhost:5001'
const DIMS_DOMAIN = 'https://uiot-dims.herokuapp.com'
// https://uiot-dims.herokuapp.com

const API_URLS = {
    'SERVICES': DIMS_DOMAIN + '/list/service',
    'DATA': DIMS_DOMAIN + '/list/data',
    'GROUP': API_DOMAIN + '/group',
    'ADD_GROUP': API_DOMAIN + '/add/group',
    'DELETE_GROUP': API_DOMAIN + '/delete/group',
    'DELETE_IN_GROUP': API_DOMAIN + '/delete/service',
    'COMMAND': API_DOMAIN + '/command',
    'CREATE_COMMAND': API_DOMAIN + '/add/command',
    'DELETE_COMMAND': API_DOMAIN + '/delete/command',
    'CHANGE_COMMAND': API_DOMAIN + '/change/command'
}

// var config = {
//     headers: {'Access-Control-Allow-Origin': '*'}
// };

export class Service {
    constructor() {
    }    

    getServices = () => axios.get(API_URLS.SERVICES+'?latest=10')

}

export class Data {
    constructor() {
    }

    getData = (mac, chipset, number) => axios.get(API_URLS.DATA+'?mac='+mac+'&chipset='+chipset+'&serviceNumber='+number)

    getLastData = (mac, chipset, number) => axios.get(API_URLS.DATA+'?mac='+mac+'&chipset='+chipset+'&serviceNumber='+number+'&latest=1')
}

export class Group {
    constructor() {
    }

    getGroup = () => axios.get(API_URLS.GROUP, { crossdomain: true })

    createGroup = (group, color) => axios.post(API_URLS.GROUP, { "group": group, "color": color, "services": [] } )

    deleteGroup = (group) => axios.post(API_URLS.DELETE_GROUP, { "group": group, "services": [] } )

    addInGroup(group, service){
        axios.post(API_URLS.ADD_GROUP, { "group": group, "services": service })
    }
    deleteInGroup(group, service){
        axios.post(API_URLS.DELETE_IN_GROUP, { "group": group, "services": service })
    }
}

export class Command {
    constructor() {
    }

    getCommand = () => axios.get(API_URLS.COMMAND)

    getByGroup = (group) => axios.get(API_URLS.COMMAND + '?group='+group)

    getOneCommand = (chipset, mac, number) => axios.get(API_URLS.COMMAND, { 'chipset': chipset, 'mac': mac, 'number': number } )

    changeCommand = (comando) => axios.post(API_URLS.CHANGE_COMMAND, comando)

    addCommand = (service, command) => axios.post(API_URLS.CREATE_COMMAND, { "services": service , "command": command })

    deleteCommand = (service, command) => axios.post(API_URLS.DELETE_COMMAND, { "services": service, "command": command })

    interact = (ip, params) => axios.get(ip + params)
}
