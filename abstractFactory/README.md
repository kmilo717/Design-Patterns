# Fábrica Abstracta
#### Patrón de Diseño Creacional
*Crea una instancia de varias familias de clases*

**Objetivos:**
- Proveer una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.
- Una jerarquía que conserva muchas posibles "plataformas" y la construcción de un grupo de "productos".
- El operador `new` considerado nocivo.

La Fábrica Abstracta define un método de fábrica por producto. Cada método de fábrica conserva el operador `new` y las clases de productos concretas y específicas de la plataforma. Luego, cada "plataforma" es modelada con una clase derivada de una fábrica.

---
**Descripción del Código:**
- Declara una interfaz para operaciones que crea objetos de productos abstractos.
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
- Implementa las operaciones para crear objetos de productos concretos.
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
- Declara una interfaz para un tipo de objeto de producto.
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
- Define un objeto de producto a ser creado por la correspondiente fábrica concreta.
Implementar la interfaz *abstractProduct*.
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)