import ply.lex as lex
tokens = (
   'EQUIPOS',
   'NOMBRE_EQUIPO',
   'IDENTIDAD_EQUIPO',
   'LINK', 
   'ASIGNATURA',
   'CARRERA',
   'UNIVERSIDAD_REGIONAL',
   'DIRECCION',
   'CALLE',
   'CIUDAD',
   'PAIS',
   'ALIANZA_EQUIPO',
   'INTEGRANTES',
   'NOMBRE',
   'EDAD',
   'CARGO',
   'FOTO',
   'EMAIL',
   'HABILIDADES',
   'SALARIO',
   'ACTIVO',
   'PROYECTOS',
   'ESTADO',
   'RESUMEN',
   'FECHA_INICIO',
   'FECHA_FIN',
   'VIDEO',
   'CONCLUSION',
   'VERSION',
   'FIRMA_DIGITAL',
   'L_LLAVES',
   'R_LLAVES',
   'L_CORCHETES',
   'R_CORCHETES',
   'STRING',  # para strings genéricos
   'REAL', 
   'ENTERO',
   'DOS_PUNTOS',
   'COMA',
   'STRING_URL', #COMPUESTO
   'STRING_EMAIL',#COMPUESTO
   'BOOL',#COMPUESTO
)
t_ignore = ' \t'
#Expresiones de simbolos 
t_L_LLAVES = r'\{'
t_R_LLAVES = r'\}'
t_L_CORCHETES = r'\['
t_R_CORCHETES = r'\]'
t_DOS_PUNTOS = r':'
t_COMA = r','
#Expresiones regulares simples
t_EQUIPOS = r'equipos'# tendria que ser r'"equipos:"'?
t_INTEGRANTES = r'integrantes'
t_PROYECTOS = r'proyectos'
t_NOMBRE_EQUIPO = r'"nombre_equipo'
t_CALLE = r'calle'


#Expresiones regulares compuestas 
def t_STRING(t):
   r'"[a-zA-Z][a-zA-Z,.\s\_\'-:]+"'
   t.value = t.value[1:-1]
   return t
   
def t_BOOL(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t


data = input("ingrese la data")

#funcion de errore necesaria 
def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

#construye el lexer
lexer = lex.lex()
lexer.input(data)

for tok in lexer:
   print(tok)



