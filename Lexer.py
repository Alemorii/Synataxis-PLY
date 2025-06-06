import ply.lex as lex
import sys
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
   'STRING_URL', #COMPUESTO-listo
   'STRING_EMAIL',#COMPUESTO-listo
   'BOOL',#COMPUESTO
   'COMILLAS',
   'SLASH',
   'FECHA', #listo
)

#Expresiones de simbolos 
t_L_LLAVES = r'\{'
t_R_LLAVES = r'\}'
t_L_CORCHETES = r'\['
t_R_CORCHETES = r'\]'
t_DOS_PUNTOS = r':'
t_COMA = r','
t_COMILLAS = r'"'
t_SLASH= r"/"

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

t_ignore = ' \t'
#Expresiones regulares compuestas 
def t_FECHA(t):
   r'(19[0-9][0-9]|20[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
   return t

def t_REAL(t):
   r'-?\d+\.\d+'
   t.value = float(t.value)
   return t

def t_ENTERO(t):
   r'-?\d+'
   t.value = int(t.value)
   return t
   
def t_BOOL(t):
   r'true|false'
   t.value = True if t.value == 'true' else False
   return t

def t_STRING_URL(t):
   r'http[s]?://[a-zA-Z0-9.-]+(:[0-9]+)?(/[a-zA-Z0-9._/#:-]*)*'
   return t

def t_STRING_EMAIL(t):
   r'"[a-zA-Z0-9._+-]+@[a-zA-Z0-9._+-]+\.[a-zA-Z]{2,4}"'
   return t


def t_STRING(t):
   r'[a-zA-Z.\s\_\'-]+ |[a-zA-Z]'
   return t


#funcion de errore necesaria 
def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

#construye el lexer
lexer = lex.lex()

def procesar_archivo(file_name): #lee archivo y muestra tokens
   try:
      with open(file_name, 'r', encoding ='utf-8')as f:
         data = f.read()
      
      lexer.input(data)

      print(f"\n--- Analizando archivo: {file_name} ---")
      for tok in lexer:
         print(tok)
      print("Análisis léxico completo.")
   except FileNotFoundError:
      print("error, archivo no encontrado")

program = True
if __name__ == "__main__":
   while program == True:
      print("\n -- Bienvenidx al analizador lexico--")
      print("1. Procesar archivo actual'ejemplo.txt'")
      print("2. Procesar otro archivo")
      print("3. procesar tokens de texto")
      print("4. Salir")
      print('-'* 40)

      choice = input("Elige una opcion (1,2,3,4) :")

      match choice:
         case "1":
            procesar_archivo('ejemplo.txt')
         case "2":
            file_name = input("introduzca el nombre del archivo :" )
            procesar_archivo(file_name)
         case "3":
            data = input("ingrese texto a tokenizar :\n ") 
            lexer.input(data)
            for tok in lexer:
               print(tok) 
            print("analisis lexico completo") 
         case "4": 
            sys.exit() 



