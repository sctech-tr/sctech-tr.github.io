var errcount = 0;
var warncount = 0;
var infocount = 0;

function error() {
    errcount++;
    console.error(errcount);
}

function warn() {
    warncount++;
    console.warn(warncount);
}

function info() {    
    infocount++;
    console.log(infocount);
}