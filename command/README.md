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
- Pide al comando que cargue la petición.
![](https://github.com/kmilo717/Design-Patterns/blob/master/Images/c1.png)
- Declara una interfaz para ejecutar una operación.
![](https://github.com/kmilo717/Design-Patterns/blob/master/Images/c2.png)
- Define una unión entre un objeto receptor y una acción. Implementa el ejecutor invocando la operación correspondiente en el receptor.
![](https://github.com/kmilo717/Design-Patterns/blob/master/Images/c3.png)
- Sabiendo cómo llevar a cabo las operaciones asociadas a la realización de una petición. Cualquier clase puede servir como un receptor.
![](https://github.com/kmilo717/Design-Patterns/blob/master/Images/c4.png)