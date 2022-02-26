// Cree la función JavaScript mostrarFecha(), la que debe desplegar la fecha y hora
// actuales en formato “Hoy es [DIA SEMANA] [DIA] de [MES] de [AÑO], y son las [HORA]
// horas, [MINUTOS] minutos con [SEGUNDOS] segundos”. El campo [DIA SEMANA] debe
// ser de texto correspondiente al día de la semana.


const months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
const days = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"];

const d = new Date();



function mostrarFecha(){
    document.getElementById("diasemana").innerHTML=d.getDate();
    
    let day = days[d.getDay()];
    document.getElementById("dia").innerHTML = day;

    let month = months[d.getMonth()];
    document.getElementById("mes").innerHTML = month;
    
    document.getElementById("ano").innerHTML=d.getFullYear();
    
    document.getElementById("hora").innerHTML=d.getHours();
    
    document.getElementById("minutos").innerHTML=d.getMinutes();
    
    while (true) {
        document.getElementById("segundos").innerHTML=d.getSeconds();
    }
    
    
}