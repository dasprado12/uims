import Ping from 'ping.js';

export class Pingar {
    constructor(){

    }
    ping(){
        var p = new Ping()
        p.ping("https://facebossssok.com", function(err) {
        if (err) {
            return 'false'
        }else{
            return 'true'
        }
        });
    }
}