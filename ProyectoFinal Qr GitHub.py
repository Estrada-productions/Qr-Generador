import tkinter as tk
from tkinter import simpledialog, messagebox
import customtkinter as ctk
import qrcode

# Generación de QR
#Creamos la clase
class GeneradorQrModelo:
    def __init__(self):
        self.qrcode = qrcode.QRCode(
            version=1,  # Nivel de detalle del QR
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Corrección de errores
            box_size=10,  # Tamaño de cada cuadro
            border=4  # Bordes alrededor del QR
        )

    def generar_qr(self, texto, file_name="sample.png", fg="black", bg="white"):
        """Genera el código QR y lo guarda como una imagen."""
        try:
            self.qrcode.clear()
            self.qrcode.add_data(texto)
            self.qrcode.make(fit=True)
            qr_image = self.qrcode.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            return True, "¡QR generado correctamente!"
        except Exception as e:
            return False, f"No se pudo generar el QR: {e}"



# Vista Interfaz de Usuario
class GeneradorQrVista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.button = None
        self.controlador = None

        # Configurar la ventana principal con CustomTkinter
        self.ventana.geometry("400x300")
        self.ventana.title("Generador de Código QR")
        self.ventana.configure(bg='#212121')  # Fondo oscuro

        # Cambiar el tema de CustomTkinter 
        ctk.set_appearance_mode("Dark")  # Usamos modo oscuro 
        ctk.set_default_color_theme("dark-blue")  # Tema de colores oscuros

        # Creamos un frame para contener los widgets
        self.frame = ctk.CTkFrame(self.ventana, corner_radius=15, fg_color="#424242")  # Fondo gris oscuro
        self.frame.pack(padx=20, pady=20, expand=True)

        # Etiqueta de título
        self.titulo = ctk.CTkLabel(self.frame, text="Generador de Códigos QR", font=("Helvetica", 20, "bold"), text_color="white")
        self.titulo.pack(pady=(0, 20))

        # Botón para generar el QR
        self.button = ctk.CTkButton(
            self.frame,
            text="Crear Código QR",
            font=("Helvetica", 14),
            command=self.on_crear_qr,
            fg_color="#00C853",  # Color verde brillante
            hover_color="#1DE9B6",  # Color de hover (más brillante)
            width=200,  # Ancho personalizado para que se vea bien
            height=40  # Altura personalizada para un botón más grande
        )
        self.button.pack(pady=20)

        # Agregar un Label para indicaciones
        self.instrucciones = ctk.CTkLabel(self.frame, text="Introduce un texto o enlace para generar un QR.", font=("Helvetica", 12), text_color="white")
        self.instrucciones.pack()

    def set_controlador(self, controlador):
        "Asigna el controlador a la vista"
        self.controlador = controlador

    def on_crear_qr(self):
        "Maneja la acción de crear un QR"
        self.controlador.crear_qr()

    def mostrar_mensaje(self, titulo, mensaje):
        "Muestra un mensaje de información o error"
        messagebox.showinfo(title=titulo, message=mensaje)

    def mostrar_error(self, mensaje):
        "Muestra un mensaje de error"
        messagebox.showerror(title="Error", message=mensaje)

    def mostrar_advertencia(self, mensaje):
        "Muestra un mensaje de advertencia"
        messagebox.showwarning(title="Advertencia", message=mensaje)

# Controlador  de Interacción

class GeneradorQrControlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.vista.set_controlador(self)

    def crear_qr(self):
        "Gestiona la creación del QR desde la vista"
        # Pedimos al usuario ingresar el texto para el código QR
        usuario_input = simpledialog.askstring(
            title="Entrada",
            prompt="Introduce el texto o algún link para generar el QR:",
            parent=self.vista.ventana
        
       
        )

        if usuario_input:
            # Llamamos al modelo para generar el código QR
            success, mensaje = self.modelo.generar_qr(usuario_input, file_name='codigo_qr.png', fg='black', bg='white')
            if success:
                self.vista.mostrar_mensaje("QR Generado", mensaje)
            else:
                self.vista.mostrar_error(mensaje)
        else:
            self.vista.mostrar_advertencia("¡No se ingresó texto!")

# Configuración de la Aplicación
# Creamos la ventana principal
root = ctk.CTk()

# Crear instancias del Modelo, Vista y Controlador
modelo = GeneradorQrModelo()
vista = GeneradorQrVista(root)
controlador = GeneradorQrControlador(vista, modelo)

# Bucle principal de la interfaz gráfica
root.mainloop()