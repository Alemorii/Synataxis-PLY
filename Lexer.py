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
   'COMILLAS',
)
t_ignore = ' \t'
#Expresiones de simbolos 
t_L_LLAVES = r'\{'
t_R_LLAVES = r'\}'
t_L_CORCHETES = r'\['
t_R_CORCHETES = r'\]'
t_DOS_PUNTOS = r':'
t_COMA = r','
t_COMILLAS = r'"'

#Expresiones regulares simples
t_EQUIPOS = r'"equipos"'# tendria que ser r'"equipos:"'?
t_INTEGRANTES = r'"integrantes"'
t_PROYECTOS = r'"proyectos"'
t_NOMBRE_EQUIPO = r'"nombre_equipo"'
t_IDENTIDAD_EQUIPO = r'"identidad_equipo"'
t_LINK = r'"link"'
t_ASIGNATURA = r'"asignatura"'
t_CARRERA = r'"carrera"'
t_UNIVERSIDAD_REGIONAL = r'"universidad_regional"'
t_DIRECCION = r'"direccion"'
t_CALLE = r'"calle"'
t_CIUDAD = r'"ciudad"'
t_PAIS=r'"pais"'
t_ALIANZA_EQUIPO = r'"alianza_equipo"'
t_NOMBRE = r'"nombre"'
t_EDAD = r'"edad"'
t_CARGO = r'"cargo"'
t_FOTO = r'"foto"'
t_EMAIL = r'"email"'
t_HABILIDADES = r'"habilidades"'
t_SALARIO = r'"salario"'
t_ACTIVO = r'"activo"'
t_ESTADO = r'"estado"'
t_RESUMEN = r'"resumen"'
t_FECHA_INICIO = r'"fecha_inicio"'
t_FECHA_FIN = r'"fecha_fin"'
t_VIDEO = r'"video"'
t_CONCLUSION = r'"conclusion"'
t_VERSION = r'"version"'
t_FIRMA_DIGITAL = r'"firma_digital"'


#Expresiones regulares compuestas 
def t_STRING(t):
   r'[a-zA-Z][a-zA-Z,.\s\_\'-:]+'
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



