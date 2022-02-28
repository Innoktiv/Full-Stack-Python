// Cree la función JavaScript mostrarFecha(), la que debe desplegar la fecha y hora
// actuales en formato “Hoy es [DIA SEMANA] [DIA] de [MES] de [AÑO], y son las [HORA]
// horas, [MINUTOS] minutos con [SEGUNDOS] segundos”. El campo [DIA SEMANA] debe
// ser de texto correspondiente al día de la semana.

const months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
const days = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"];

const d = new Date();

function mostrarFecha(){
    document.getElementById("diasemana").innerHTML=d.getDate();       
}

function mostrarDia() {
    let day = days[d.getDay()];
    document.getElementById("dia").innerHTML = day;
}
function mostrarMes() {
    let month = months[d.getMonth()];
    document.getElementById("mes").innerHTML = month;
    
}
function mostrarYear(){
    document.getElementById("ano").innerHTML=d.getFullYear();
}
function mostrarHora(){
    document.getElementById("hora").innerHTML=d.getHours();
}
function mostrarMinutos() {
    document.getElementById("minutos").innerHTML=d.getMinutes();
}

function mostrarSegundos() {
    document.getElementById("segundos").innerHTML=d.getSeconds();
    
}



// Calcular fechas
// Un dia en millisegundos
var one_day = 1000 * 60 * 60 * 24
  
// Dia actual en 2 variables
var present_date = new Date();
  
// JavaScript entiende los meses de 0-11
var final_ano = new Date(present_date.getFullYear(), 11, 31)
  
// Calcula el resultado en milisegundos y convertir en dias
var Result = Math.round(final_ano.getTime() - present_date.getTime()) / (one_day);
  
// Saca decimales 
var Final_Result = Result.toFixed(0);

//Mostrar resultado
document.getElementById("resultado").innerHTML = Final_Result;