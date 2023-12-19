let dataPython;
let dataDisplay;

function retrieveData(event){
    event.preventDefault()
    let userData = {};
    form = document.querySelector("form")
    userData["nom"] = form.nom.value;
    userData["tel"] = form.tel.value;
    userData["nbPers"] = form.nbPers.value;
    userData["nbPmr"] = form.nbPmr.value;
    userData["nbBb"] = form.nbBb.value;
    userData["dateHeure"] = form.dateHeure.value;
    userData["typeCuisine"] = form.tc.value;
    dataPython = userData
    console.log(dataPython)
    eel.mainGUI()
    console.log(dataDisplay)
    return userData
}

async function affichage(){
    dataDisplay = await eel.importJSON()();
    console.log(dataDisplay);
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function(elem){
            let td = "<td>" + elem + "</td>";
            ligne+=td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function supprimerDuTab(id){
    eel.supprimerDuGUI(id);
    affichage();
}

function triSurNom(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["nom"] < reservation2["nom"]){return -1}
        if (reservation1["nom"] > reservation2["nom"]){return 1}
        return reservation1["nom"] - reservation2["nom"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function triSurTel(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["telNum"] < reservation2["telNum"]){return -1}
        if (reservation1["telNum"] > reservation2["telNum"]){return 1}
        return reservation1["telNum"] - reservation2["telNum"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function triSurTable(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["numTable"] < reservation2["numTable"]){return -1}
        if (reservation1["numTable"] > reservation2["numTable"]){return 1}
        return reservation1["numTable"] - reservation2["numTable"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function triSurDate(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["dateHeure"] < reservation2["dateHeure"]){return -1}
        if (reservation1["dateHeure"] > reservation2["dateHeure"]){return 1}
        return reservation1["dateHeure"] - reservation2["dateHeure"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function triSurClient(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["nbrClient"] < reservation2["nbrClient"]){return -1}
        if (reservation1["nbrClient"] > reservation2["nbrClient"]){return 1}
        return reservation1["nbrClient"] - reservation2["nbrClient"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}
//ajout des tris les coupaings
function triSurRes(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["idRes"] < reservation2["idRes"]){return -1}
        if (reservation1["idRes"] > reservation2["idRes"]){return 1}
        return reservation1["idRes"] - reservation2["idRes"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function triSurPMR(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["pmr"] < reservation2["pmr"]){return -1}
        if (reservation1["pmr"] > reservation2["pmr"]){return 1}
        return reservation1["pmr"] - reservation2["pmr"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function triSurBb(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["bb"] < reservation2["bb"]){return -1}
        if (reservation1["bb"] > reservation2["bb"]){return 1}
        return reservation1["bb"] - reservation2["bb"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}

function triSurCuisine(){
    let listReservations = dataDisplay["reservation_manager"]["reservations"];
    let tbody = ""
    listReservations.sort(function(reservation1,reservation2){
        if (reservation1["idCuisine"] < reservation2["idCuisine"]){return -1}
        if (reservation1["idCuisine"] > reservation2["idCuisine"]){return 1}
        return reservation1["idCuisine"] - reservation2["idCuisine"]
    })
    listReservations.forEach(function(reservation){
        keys = Object.keys(reservation);
        let ligne = "<tr>"
        values = Object.values(reservation);
        values.forEach(function (elem) {
            let td = "<td>" + elem + "</td>";
            ligne += td;
        });
        ligne += `<td id="${reservation.idRes}" onclick='supprimerDuTab(${reservation.idRes})'>` + "<button>Supprimer</button>" + "</td>"
        ligne += "</tr>"
        tbody += ligne;
        document.querySelector("tbody").innerHTML = tbody;
    })
}


function init(){
    document.querySelector("form").addEventListener("submit",retrieveData);
    document.querySelector("form").addEventListener("submit",affichage);
    affichage();
}



eel.expose(exportPython)
function exportPython(){
    return dataPython;
}

let idTabActuel = "reservation";

function _gebi(id){ return document.getElementById(id)}


document.addEventListener("DOMContentLoaded", initTabs);


function initTabs() { console.log('in initTabs')
    _gebi('aff_'+idTabActuel).style.display = "block";
    _gebi(idTabActuel).classList.add("active");
}


function changerTab(tabButton) {  console.log('in changerTab ',tabButton);
    // cache le tab actuel
    _gebi('aff_'+idTabActuel).style.display = "none";
    _gebi(idTabActuel).classList.remove("active");
    // affiche le tab demandé
    _gebi('aff_'+tabButton.id).style.display = "block";
    _gebi(tabButton.id).classList.add("active");
    // mémorise le nouveau tab actuel
    idTabActuel = tabButton.id;
    affichage();
}