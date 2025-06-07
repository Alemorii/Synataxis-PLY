import ply.lex as lex
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox 

tokens = (
    'EQUIPOS', 'NOMBRE_EQUIPO', 'IDENTIDAD_EQUIPO', 'LINK',
    'ASIGNATURA', 'CARRERA', 'UNIVERSIDAD_REGIONAL', 'DIRECCION',
    'CALLE', 'CIUDAD', 'PAIS', 'ALIANZA_EQUIPO', 'INTEGRANTES',
    'NOMBRE', 'EDAD', 'CARGO', 'FOTO', 'EMAIL', 'HABILIDADES',
    'SALARIO', 'ACTIVO', 'PROYECTOS', 'ESTADO', 'RESUMEN',
    'FECHA_INICIO', 'FECHA_FIN', 'VIDEO', 'CONCLUSION', 'VERSION',
    'FIRMA_DIGITAL', 'L_LLAVES', 'R_LLAVES', 'L_CORCHETES',
    'R_CORCHETES', 'STRING', 'REAL', 'ENTERO', 'DOS_PUNTOS', 'COMA',
    'STRING_URL', 'STRING_EMAIL', 'BOOL', 'COMILLAS', 'SLASH', 'FECHA',
)

t_L_LLAVES = r'\{'
t_R_LLAVES = r'\}'
t_L_CORCHETES = r'\['
t_R_CORCHETES = r'\]'
t_DOS_PUNTOS = r':'
t_COMA = r','
t_COMILLAS = r'"'
t_SLASH = r"/"

t_EQUIPOS = r'"equipos"'
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
t_PAIS = r'"pais"'
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

t_ignore = ' \t\r\n'

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

def t_error(t):
    error_message = f"Caracter ilegal '{t.value[0]}' en línea {t.lineno}, posición {t.lexpos}"
    output_text.insert(tk.END, f"Error: {error_message}\n")
    t.lexer.skip(1)

lexer = lex.lex()

# --- Interfaz con Tkinter (Modificadas) ---

def analizar_texto_gui():
    """Obtiene el texto de la entrada, lo analiza y muestra los tokens."""
    texto_entrada = input_text.get("1.0", tk.END).strip()
    output_text.delete("1.0", tk.END)

    if not texto_entrada:
        output_text.insert(tk.END, "Por favor, introduce texto o carga un archivo para analizar.\n")
        return

    output_text.insert(tk.END, "--- Análisis Léxico Iniciado ---\n")
    lexer.input(texto_entrada)
    for tok in lexer:
        output_text.insert(tk.END, str(tok) + "\n")
    output_text.insert(tk.END, "--- Análisis Léxico Finalizado ---\n")

def cargar_archivo_gui():
    """Abre un diálogo para seleccionar un archivo, lo lee y lo muestra en la entrada."""
    file_path = filedialog.askopenfilename(
        title="Seleccionar Archivo para Cargar",
        filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")] # Filtros para tipos de archivo
    )
    if file_path: # Si el usuario seleccionó un archivo (no canceló el diálogo)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                contenido_archivo = f.read()
            input_text.delete("1.0", tk.END) # Borra cualquier texto anterior
            input_text.insert("1.0", contenido_archivo) # Inserta el contenido del archivo
            analizar_texto_gui() # Opcional: Analiza el archivo automáticamente al cargarlo
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no fue encontrado.")
        except Exception as e: # Captura cualquier otro error durante la lectura del archivo
            messagebox.showerror("Error", f"Ocurrió un error al leer el archivo: {e}")

def limpiar_campos():
    """Limpia ambos campos de texto."""
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# --- Configuración de la Ventana Principal ---

root = tk.Tk()
root.title("Analizador Léxico con Carga de Archivos")
root.geometry("700x550") #

# --- Widgets ---

label_input = tk.Label(root, text="Escriba texto a tokenizar o eliga cargar un archivo:")
label_input.pack(pady=5)

input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_text.pack(pady=5)

# Nuevo botón para cargar archivo
boton_cargar_archivo = tk.Button(root, text="Cargar Archivo", command=cargar_archivo_gui)
boton_cargar_archivo.pack(pady=5)

boton_analizar = tk.Button(root, text="Analizar Texto", command=analizar_texto_gui)
boton_analizar.pack(pady=5)

boton_limpiar = tk.Button(root, text="Limpiar Todo", command=limpiar_campos)
boton_limpiar.pack(pady=5)

label_output = tk.Label(root, text="Resultados del Análisis:")
label_output.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
output_text.pack(pady=5)

# --- Bucle Principal de Tkinter ---
root.mainloop()
