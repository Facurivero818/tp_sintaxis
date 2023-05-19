/*MENU*/
const menu = `
1 - Mostrar Lenguaje.
2 - Analizar Cadena Completa.
3 - Analizar Cadena Paso a Paso.
4 - Cadena Ejemplo.
5 - Salir  
`
let flag = true;

while (flag){

    let  opcion = prompt(menu);
    switch(opcion){
        case '1': 
            console.clear()
            console.log("L = {a\u207F"+"b\u00B2\u207F | n > 0}")
            break;
        case '2': 
            console.clear()
            analizar_cadena()
            break;
        case '3': 
            console.clear()
            analizar_cadena_pap()
            break;
        case '4': 
            console.clear()
            ejemplo()
            break;
        case '5':
            flag = false;
            break;
        default:
            console.log("Opcion incorrecta, vuelva a elegir");
    }
}


function analizar_cadena(){
    let palabra = prompt("Ingrese una palabra: ");
    let cont = 0;
    for (let letra of palabra){ 
        if (letra === "a"){
            cont += 1; 
        }
        else break;
    }
    let caracterA = 'a';
    let caracterB = 'b';
    let cadena=caracterA.repeat(cont)+caracterB.repeat(2*cont);
    if ((cadena === palabra) && (palabra.length!=0))
        return console.log("La palabra ingresada pertenece al Lenguaje ")
     else 
        return console.log("La palabra ingresada no pertenece al Lenguaje")
}

function ejemplo(){
    let caracterA = 'a';
    let caracterB = 'b';
    let maximo = 100;
    let minimo  = 1;
    let numeroAleatorio = Math.floor(Math.random() * (maximo - minimo + 1)) + minimo;
    let cadena=caracterA.repeat(numeroAleatorio)+caracterB.repeat(2*numeroAleatorio);
    return console.log(cadena) 
}

function analizar_cadena_pap(){
    let palabra = "";
    let cant_a = 0;
    let cant_b = 0;
    while (true){
        let caracter = prompt("ingrese un caracter: ");
        if (caracter == ""){
            if (2*cant_a == cant_b)
                return console.log(`palabra: ${palabra}`);
            else 
                return console.log("false1");}
        else if (caracter.length > 1){
            console.log("Debe ingresar un solo caracter");
            continue;
        } else if (caracter !="a" && caracter !="b")
            return console.log("False2");
        else{
            if (caracter == "a" && (palabra.indexOf('b')==-1 )){
                cant_a += 1;
                palabra += caracter;
            } else if ((caracter == "b") && (cant_b/2 < cant_a) && (cant_a > 0)){ 
                cant_b +=1;
                palabra += caracter;
            }else return console.log("false3")
            }
    }

}
