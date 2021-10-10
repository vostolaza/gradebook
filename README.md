## 📋 Requerimientos y ⚙️ Configuración

Las librerías de Python utilizadas están listadas en el archivo requirements.txt en la raíz del proyecto y pueden ser instaladas ejecutando el siguiente comando:

````bash
pip install -r requirements.txt
````

### Dot env

Variables que dependen del ambiente de ejecución se deben ingresar en el archivo `.env`. Puede guiarse de el archivo `.env.sample` para el armado de este. Debe ingresar el correo y contraseña de la cuenta de Google utilizada para iniciar sesión en CodingRooms y la ruta del binario o ejecutable del Chrome Driver.

## Ejecución ▶️

Antes de ejecutar el proyecto, se debe ingresar la URL del gradebook en la linea 12 del archivo `gradebook.py`. 