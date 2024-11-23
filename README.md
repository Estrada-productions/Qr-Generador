### Steven Estrada.
#####  Ingeniero en Sistemas.


## **Generador de Códigos QR con Python**
Este proyecto consiste en una aplicación de escritorio que permite generar códigos QR personalizados a partir de un texto o URL proporcionado por el usuario. La aplicación está construida usando Tkinter para la interfaz gráfica y qrcode para la generación de los códigos QR. Se ha implementado el patrón de diseño Modelo-Vista-Controlador (MVC) para organizar el código de manera estructurada.
# Tecnologías Usadas
•	Python 3.x
•	Tkinter: Librería estándar para la interfaz gráfica de usuario (GUI).
•	CustomTkinter: Una extensión de Tkinter que mejora la apariencia y proporciona un diseño más moderno.
•	qrcode: Librería para la creación de códigos QR.
# Descripción del Proyecto
La aplicación permite a los usuarios generar códigos QR a partir de un texto o URL ingresado. El proceso está dividido en tres secciones principales siguiendo el patrón de diseño Modelo-Vista-Controlador (MVC):
###### •	Modelo: •	Modelo: Genera el código QR a partir de los datos proporcionados.
###### •	Vista•	Vista: Interfaz gráfica de usuario que muestra las opciones disponibles y presenta la interfaz interactiva.
###### •	Controlador:•	Controlador: Controla la lógica de la interacción entre el modelo y la vista.
El diseño de la interfaz gráfica es llamativo, utilizando **CustomTkinter** para modernizar la apariencia de la aplicación. La ventana emergente que solicita la URL o texto para el código QR tiene un fondo de color brillante para atraer la atención del usuario.
## Instalación
Para ejecutar este proyecto, necesitarás tener Python instalado en tu PC. Si no lo tienes, puedes descargarlo desde aquí.
#### Requisitos
1.	Instalar Python 3.x.
2.	Instalar las dependencias del proyecto mediante pip.
En la terminal, navega al directorio donde has guardado el proyecto y ejecuta:
bash
Copiar código
```
pip install -r requirements.txt
```
Crear el archivo requirements.txt
Puedes crear el archivo requirements.txt con las siguientes dependencias:
Copiar código
qrcode
customtkinter
### Alternativa de instalación manual:
Si no deseas usar el archivo requirements.txt, puedes instalar manualmente las dependencias:
bash
Copiar código
```
pip install qrcode
```
```
pip install customtkinter
```
## **Ejecución**
Una vez que las dependencias estén instaladas, puedes ejecutar el proyecto directamente desde la terminal:
bash
Copiar código
python main.py
Esto abrirá la ventana principal de la aplicación donde podrás generar los códigos QR.
## **Flujo de Ejecución**
**1.**	Abrir la ventana principal: Al iniciar la aplicación, se muestra una ventana con un botón que dice "Crear Código QR".

**2**.	Introducir texto o URL: Al hacer clic en el botón, se abre una ventana emergente donde puedes introducir un texto o una URL que desees convertir en un código QR.

**3.**	Generar el código QR: Después de introducir el texto, el código QR se genera y se guarda como una imagen en el archivo codigo_qr.png en el directorio del proyecto.

**4.**	Visualización del mensaje de éxito: Una vez generado el QR, se muestra un mensaje de éxito en una ventana emergente.
## **Explicación del Código**
## **1**. Modelo (GeneradorQrModelo)
El modelo se encarga de la lógica de la generación del código QR. Utiliza la librería qrcode para crear el código QR a partir del texto o URL proporcionado. Además, guarda la imagen generada en formato PNG.
## **2**. Vista (GeneradorQrVista)
La vista contiene la interfaz gráfica de usuario (GUI) construida con Tkinter y CustomTkinter. Incluye:
•	Un botón para generar el código QR.
•	Una ventana emergente personalizada para ingresar el texto o URL.
•	Mensajes informativos y de error.
## **3**. Controlador (GeneradorQrControlador)
El controlador maneja la lógica entre la vista y el modelo. Se encarga de gestionar la interacción del usuario, como la apertura de la ventana emergente para ingresar el texto, la generación del código QR y la visualización de los resultados.
## **4**. Ventana Emergente Personalizada (VentanaEmergente)**4**. Ventana Emergente Personalizada (VentanaEmergente)
Esta ventana es creada utilizando CTkToplevel, que permite tener un diseño completamente personalizable. La ventana tiene un fondo llamativo y un campo de texto para que el usuario ingrese la URL o texto que desea convertir en un código QR.
### **Contribuciones**
Si deseas contribuir al proyecto, por favor, sigue estos pasos:
**1.	**Haz un fork del repositorio.
**2.	**Crea una nueva rama (git checkout -b feature-nueva).
**3.	**Realiza tus cambios y haz un commit (git commit -am 'Añadir nueva característica').
**4.	**Envía un push a tu rama (git push origin feature-nueva).
**5.**	Abre un Pull Request para revisar tus cambios.
**
## EXPLICACION DEL DIAGRAMA UML.**
Explicación del Diagrama:
### **1.**	Clases principales:
o	GeneradorQrModelo: Se encarga de la generación del código QR a partir de un texto o URL.
o	GeneradorQrVista: Se encarga de la interfaz gráfica, mostrando botones, campos de texto y mensajes de información al usuario.
o	GeneradorQrControlador: Actúa como intermediario entre el modelo y la vista. Gestiona las interacciones del usuario y coordina la creación del código QR.
### **2.	**Relaciones:**2.	**Relaciones:
o	GeneradorQrControlador tiene asociaciones tanto con GeneradorQrModelo como con GeneradorQrVista, ya que coordina la generación del código QR (modelo) y actualiza la interfaz gráfica (vista).
o	GeneradorQrVista se encarga de la interfaz, pero depende del controlador para manejar la lógica.
### **3.	**Atributos y Métodos:**3.	**Atributos y Métodos:
o	Modelo: Contiene la lógica para generar el QR y la configuración de parámetros.
o	Vista: Contiene los elementos visuales de la interfaz, como botones y cuadros de texto, y también maneja la interacción con el usuario.
o	Controlador: Conecta el modelo con la vista, gestionando las interacciones del usuario.

### Enlace al Diagrama UML:
https://miro.com/app/board/uXjVLBX_XHQ=/?share_link_id=272499467586 


###FIN/END
