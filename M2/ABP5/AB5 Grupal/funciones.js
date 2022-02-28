function required(){
    var vacia = document.forms["form1"]["text1"].value;
    if (vacia == ""){
        alert("Please input a Value");
        return false;
    }
    else {
        alert('Code has accepted : you can try another');
        return true; 
    }
}


function requeridos()
{
var empt = document.forms["form1"]["text1"].value;
if (empt == "")
{
alert("Por favor complete sus datos antes de enviar");
return false;
}
else 
{
alert('Datos recibidos');
return true; 
}
}
