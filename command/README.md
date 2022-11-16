# Comando
#### Patrón de Diseño de Comportamiento
*Conserva una petición de comando como un objeto.*

**Objetivos:**
- Conservar una petición de comando como un objeto, lo cuál permite parametrizar clientes con diferentes peticiones, poner en cola o registrar peticiones, y soportar operaciones que pueden deshacerse.
- Promover la "invocación de un método en un objeto" para el estado de objeto completo.
- Una devolución de llamada orientada a objetos.

El cliente que crea un comando no es el mismo cliente que lo ejecuta. Esta separación provee flexibilidad en el momento y secuencia de comandos. Materializar comandos como objetos, significa que estos pueden ser pasados, organizados, compartidos, cargados en una tabla y, de otro modo, instrumentalizados o manipulados como cualquier otro objeto.

---
**Descripción del Código:**
- Pide al comando que cargue la petición.1
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
- Declara una interfaz para ejecutar una operación.2
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
- Define una unión entre un objeto receptor y una acción. Implementa el ejecutor invocando la operación correspondiente en el receptor.3
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
- Sabiendo cómo llevar a cabo las operaciones asociadas a la realización de una petición. Cualquier clsase puede servir como un receptor.
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)