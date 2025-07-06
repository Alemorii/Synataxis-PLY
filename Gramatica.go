Σ --> <json> 
//se deriva sigma en el no terminal <json> 
 
<json> --> { 
  "equipos": <lista_equipos>, 
  "version": <nullable_string>, 
  "firma_digital": <nullable_string> 
} 
// <json> genera la base del documento donde se encuentran n equipos 
la versión y firma digital que pueden ser nullos 
 
<lista_equipos> --> [<equipo>] | [<equipo>, <lista_equipos>] 
//el no terminal <lista_equipos> genera la n > 0 de quipos  
mediante el no termal <equipo> en el caso de ser un solo equipo o no 
terminal <equipo> terminal, y la recursión de <lista_equipos> 
 
<equipo> --> { 
  "nombre_equipo": string, 
  "identidad_equipo": <stringURL>, 
  "link": <stringURL>, 
  "asignatura": string, 
  "carrera": string, 
  "universidad_regional": string, 
  "direccion": <direccion>, 
  "alianza_equipo": string, 
  "integrantes": <lista_integrantes>, 
  "proyectos": <lista_proyectos> 
} 
//<equipo> genera un equipo dando la posibilidad de tener p proyectos y 
i integrantes 
 
<direccion> --> { 
  "calle": string, 
  "ciudad": string, 
  "pais": string 
} 
 
<direccion> --> { 
  "calle": string, 
  "pais": string, 
  "ciudad": string 
} 
 
<direccion> --> { 
  "ciudad": string, 
  "calle": string, 
  "pais": string 
} 
 
<direccion> --> { 
  "ciudad": string, 
  "pais": string, 
  "calle": string 
}
<direccion> --> { 
  "calle": string, 
  "ciudad": string, 
  "pais": string 
} 
 
<direccion> --> { 
  "calle": string, 
  "pais": string 
  "ciudad": string, 
} 

<direccion> --> { 
  "pais": string, 
  "calle": string, 
  "ciudad": string 
}

<direccion> --> { 
  "pais": string, 
  "ciudad": string, 
  "calle": string 
}
 
<direccion> --> {} 
// se general las distintas combinaciones que son posibles de tener en 
la dirección en el equipo 
  
<lista_integrantes> --> [<integrante>] | [<integrante>, <lista_inte
grantes>] 
//<lista_integrantes> genera i > 0 integrantes 
se deriva en <integrante> para i = 1 y se llama recursivamente en  
<integrante>, <lista_integrantes> para i > 1 
 
<integrante> --> { 
  "nombre": string, 
  "edad": <nullable_integer>, 
  "cargo": string, 
  "foto": string, 
  "email": string, 
  "habilidades": string, 
  "salario": float, 
  "activo": bool 
} 
//<integrante> se deriva en los datos que representan a 1 estudiante, 
en donde su edad puede estar asignado o no 
 
<lista_proyectos> --> [<proyecto>] | [<proyecto>, <lista_proyectos>] 
// <lista_proyectos> genera p > 0 proyectos, donde para generar uno 
solo se deriva en <proyecto> y para p > 1 se deriva recursivamente des
pués de generar 1 proyecto 
 
<proyecto> --> { 
  "nombre": string, 
  "estado": string, 
  "resumen": string, 
  "tareas": <lista_tareas>, 
  "fecha_inicio": date, 
  "fecha_fin": date, 
  "video": <stringURL> //ESTO HAY QUE CAMBIAR!!!!
  "conclusion": string 
} 
//<proyecto> genera los datos que tiene que tener 1 proyecto, es cada 
uno pueden existir varias tareas 
 
<lista_tareas> --> [<tareas>]  
<tareas>--> <tarea> | <tarea>,<tareas>
//<lista_tareas> se deriva en <tareas> 
//<tareas> se deriva un t > 0 tareas 
 
<tarea> --> { 
  "nombre": string, 
  "estado": string, 
  "resumen": string, 
  "fecha_inicio": <nullable_date>, 
  "fecha_fin": <nullable_date> 
} 
 
 
 
<tarea> --> { 
  "nombre": string, 
  "resumen": string, 
  "estado": string, 
  "fecha_inicio": <nullable_date>, 
  "fecha_fin": <nullable_date> 
} 
 
<tarea> --> { 
  "estado": string, 
  "nombre": string, 
  "resumen": string, 
  "fecha_inicio": <nullable_date>, 
  "fecha_fin": <nullable_date> 
} 
 
<tarea> --> { 
  "estado": string, 
  "resumen": string, 
  "nombre": string, 
  "fecha_inicio": <nullable_date>, 
  "fecha_fin": <nullable_date> 
} 
 
<tarea> --> { 
  "resumen": string, 
  "nombre": string, 
  "estado": string, 
  "fecha_inicio": <nullable_date>, 
  "fecha_fin": <nullable_date> 
} 
 
<tarea> --> { 
  "resumen": string, 
  "estado": string, 
  "nombre": string, 
  "fecha_inicio": <nullable_date>, 
  "fecha_fin": <nullable_date> 
} 
//se realizan las posibles combinaciones en la que se pueden dispo
ner  los datos de <tarea>. Genera los datos necesarios para cada tarea, 
donde la fecha de inicio y de fin pueden estar definidos o no 
 
<nullable_string> --> string | null
//<nullable_string> se deriva en un string terminal o puede ser vacío 
 
<nullable_integer> --> integer | null 
//<nullable_integer> se deriva en un intero terminal o puede ser vacío 
 
<nullable_date> --> date | null 
//<nullable_date> se deriva en un date terminal (una fecha) o puede ser 
vacío 
 
<stringURL> -->"http://"<nombre_dominio><puerta><ruta> | 
"https://"<nombre_dominio><puerta><ruta> 
//<stringURL> genera un string url  
 
<nombre_dominio>-->string 
//<nombre_dominio> se deriva en un string terminal que define el nombre 
de dominio del URL 
 
<puerta>-->integer | null 
//<nullable_string> se deriva en un entero terminal o puede ser vacío. 
Define la puerta de la URL 
 
<ruta>--> /<char_ruta>| /<char_ruta><ruta> 
//<ruta> genera la ruta de la URL  
 
<char_ruta>--> <char>| <char> <char_ruta> 
//<char_ruta> genera la cantidad necesaria de caracteres que tiene la 
ruta 
 
<char>--> <letra> | <digito> | "-" | "_" | "." | "/" | "#" | ":"| 
//<char> se deriva en un una letra ,dígito o otro símbolo permitido 
para la URL 
 
<stringEmail>--> <email> @ <email> . <extension> 
//<stringEmail> se deriva en el formato que tiene que tener un Email 
válido 
 
<email>--> <char_email> | <char_email> <email> 
//<email> genera la cantidad de caracteres que tiene que puede tener el 
email a generar 
 
 
 
<extension> --> <letra> <letra> 
              | <letra> <letra> <letra> 
              | <letra> <letra> <letra> <letra> 
//<extension> se puede derivar en 2 a 4 letras terminales ,según lo es
pecificado en los requerimientos, por medio de <letra>  
 
 
<char_email> --> <letra> | <digito>  | "_"  | "."  | "+"  | "-" 
// el no terminal <char_email> puede derivar en terminales de algunos 
símbolos o en los no terminales que generan letras y números  
 
<letra> --> "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | 
"k" | "l" | "m"| "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | 
"x" | "y" | "z" 
| "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | 
"K" | "L" | "M" 
| "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | 
"X" | "Y" | "Z" 
//terminales letra del alfabeto sin la letra “ñ” 
<digito> --> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" 
// terminales dígitos numéricos de 0 a 
