import ply.yacc as yacc 
from lexer import tokens, lexer

start = 'json'

resultado = None

def p_json(p):
    '''json: L_LLAVES EQUIPOS DOS_PUNTOS lista_equipos COMA 
        VERSION DOS_PUNTOS nullable_string COMA 
        FIRMA_DIGITAL DOS_PUNTOS nullable_string 
        R_llaves'''
    global resultado
    p[0] = {
        "equipos": p[4],
        "version": p[7],
        "firma_digital": p[10]
    }
    resultado = p[0]

def p_lista_equipos(p):
    '''lista_equipos : L_CORCHETES equipo R_CORCHETES
                    | L_CORCHETES equipo R_CORCHETES COMA lista_equipos'''
    if len(p) == 4:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[5]

def p_equipo(p):
    '''equipo : L_LLAVES
            NOMBRE_EQUIPO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
            IDENTIDAD_EQUIPO DOS_PUNTOS COMILLAS STRING_URL COMILLAS COMA
            DIRECCION DOS_PUNTOS direccion COMA
            LINK DOS_PUNTOS COMILLAS STRING_URL COMILLAS COMA
            CARRERA DOS_PUNTOS COMILLAS STRING COMILLAS COMA
            ASIGNATURA DOS_PUNTOS COMILLAS STRING COMILLAS COMA
            UNIVERSIDAD_REGIONAL DOS_PUNTOS COMILLAS STRING COMILLAS COMA
            ALIANZA_EQUIPO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
            INTEGRANTES DOS_PUNTOS lista_integrantes COMA
            PROYECTOS DOS_PUNTOS lista_proyectos
            R_LLAVES'''
    p[0] = {
        "nombre_equipo": p[5],
        "identidad_equipo": p[10],
        "direccion": p[13],
        "link": p[18],
        "carrera": p[23],
        "asignatura": p[28],
        "universidad_regional": p[33],
        "alianza_equipo": p[38],
        "integrantes": p[41],
        "proyectos": p[44]
    }

def p_direccion(p):
    '''direccion : L_LLAVES campos_direccion R_LLAVES'''
    p[0] = p[2]

def p_campos_direccion_uno(p):
    '''campos_direccion : campo_direccion'''
    p[0] = [p[1]]  # crea lista con un solo campo
    

def p_campos_direccion_varios(p):
    '''campos_direccion : campo_direccion COMA campos_direccion'''
    p[0] = [p[1]] + p[3]  # concatena listas

def p_campo_direccion_calle(p):
    'campo_direccion : CALLE DOS_PUNTOS COMILLAS STRING COMILLAS'
    p[0] = ('calle', p[4])  # retorna tupla

def p_campo_direccion_ciudad(p):
    'campo_direccion : CIUDAD DOS_PUNTOS COMILLAS STRING COMILLAS'
    p[0] = ('ciudad', p[4])

def p_campo_direccion_pais(p):
    'campo_direccion : PAIS DOS_PUNTOS COMILLAS STRING COMILLAS'
    p[0] = ('pais', p[4])

def p_lista_integrantes_uno(p):
    '''lista_integrantes : L_CORCHETES integrante R_CORCHETES'''
    p[0] = [p[2]]  # lista con un solo integrante

def p_lista_integrantes_varios(p):
    '''lista_integrantes : L_CORCHETES integrante COMA lista_integrantes R_CORCHETES'''
    p[0] = [p[2]] + p[4]  # concatena el integrante con el resto de la lista

def p_integrante(p):
    '''integrante : L_LLAVES
                        NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                        EDAD DOS_PUNTOS NUMBER COMA
                        CARGO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                        FOTO DOS_PUNTOS COMILLAS STRING_URL COMILLAS COMA
                        EMAIL DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                        HABILIDADES DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                        SALARIO DOS_PUNTOS NUMBER COMA
                        ACTIVO DOS_PUNTOS BOOLEAN
                sR_LLAVES'''
    p[0] = (
        p[5],   # nombre
        p[10],  # edad
        p[14],  # cargo
        p[19],  # foto
        p[24],  # email
        p[29],  # habilidades
        p[34],  # salario
        p[38]   # activo
    )

def p_lista_proyectos_uno(p):
    '''lista_proyectos : L_CORCHETES proyecto R_CORCHETES'''
    p[0] = [p[2]]  # lista con un solo proyecto

def p_lista_proyectos_varios(p):
    '''lista_proyectos : L_CORCHETES proyecto COMA lista_proyectos R_CORCHETES'''
    p[0] = [p[2]] + p[4]  # concatena el proyecto con el resto de la lista

def p_proyecto(p):
    '''proyecto : L_LLAVES
                    NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    ESTADO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    RESUMEN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    TAREAS DOS_PUNTOS lista_tareas COMA
                    FECHA_INICIO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    FECHA_FIN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    VIDEO DOS_PUNTOS COMILLAS STRING_URL COMILLAS COMA
                    CONCLUSION DOS_PUNTOS COMILLAS STRING COMILLAS
                R_LLAVES'''
    p[0] = (
        p[5],   # nombre
        p[10],  # estado
        p[15],  # resumen
        p[20],  # lista_tareas (ya como lista)
        p[25],  # fecha_inicio
        p[30],  # fecha_fin
        p[35],  # video
        p[40]   # conclusion
    )

def p_lista_tareas(p):
    '''lista_tareas : L_CORCHETES tareas R_CORCHETES'''
    p[0] = p[2]  # lista de tareas


def p_tareas_uno(p):
    '''tareas : tarea'''
    p[0] = [p[1]]  # lista con una sola tarea

def p_tareas_varios(p):
    '''tareas : tarea COMA tareas'''
    p[0] = [p[1]] + p[3]  # concatena tarea con el resto de la lista

def p_tarea_nombre_estado_resumen(p):
    '''tarea : L_LLAVES
                    NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    ESTADO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    RESUMEN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    FECHA_INICIO DOS_PUNTOS nullable_date COMA
                    FECHA_FIN DOS_PUNTOS nullable_date
            R_LLAVES'''
    p[0] = (p[5], p[10], p[15], p[20], p[23])


def p_tarea_nombre_resumen_estado(p):
    '''tarea : L_LLAVES
                    NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    RESUMEN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    ESTADO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    FECHA_INICIO DOS_PUNTOS nullable_date COMA
                    FECHA_FIN DOS_PUNTOS nullable_date
            R_LLAVES'''
    p[0] = (p[5], p[15], p[10], p[20], p[23])


def p_tarea_estado_nombre_resumen(p):
    '''tarea : L_LLAVES
                    ESTADO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    RESUMEN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    FECHA_INICIO DOS_PUNTOS nullable_date COMA
                    FECHA_FIN DOS_PUNTOS nullable_date
            R_LLAVES'''
    p[0] = (p[10], p[5], p[15], p[20], p[23])

def p_tarea_estado_resumen_nombre(p):
    '''tarea : L_LLAVES
                    ESTADO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    RESUMEN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    FECHA_INICIO DOS_PUNTOS nullable_date COMA
                    FECHA_FIN DOS_PUNTOS nullable_date
            R_LLAVES'''
    p[0] = (p[15], p[5], p[10], p[20], p[23])

def p_tarea_resumen_nombre_estado(p):
    '''tarea : L_LLAVES
                    RESUMEN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    ESTADO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    FECHA_INICIO DOS_PUNTOS nullable_date COMA
                    FECHA_FIN DOS_PUNTOS nullable_date
            R_LLAVES'''
    p[0] = (p[10], p[15], p[5], p[20], p[23])

def p_tarea_resumen_estado_nombre(p):
    '''tarea : L_LLAVES
                    RESUMEN DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    ESTADO DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    NOMBRE DOS_PUNTOS COMILLAS STRING COMILLAS COMA
                    FECHA_INICIO DOS_PUNTOS nullable_date COMA
                    FECHA_FIN DOS_PUNTOS nullable_date
            R_LLAVES'''
    p[0] = (p[15], p[10], p[5], p[20], p[23])
