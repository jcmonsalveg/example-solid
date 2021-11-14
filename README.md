# Ejemplo de aplicación de principios SOLID en Python

Este repositorio presenta la aplicación de principios SOLID en lenguaje de programación PYTHON. El ejercicio se diseña en el marco del curso Fundamentos de Diseño del programa Ingeniería de Software de la Corporación Universitaria Iberoamericana. Si encuentras un error en el código o en la forma de aplicación de los principios por favor házmelo saber.

## Comenzando 🚀

La aplicación se encuentra disponible de manera pública, por tal razón puedes clonarla y trabajar sobre ella, el único fin de elaborar y compartir este código es educativo. Al interior de algunos de los archivos .py se indican las fuentes de las cuales se ha tomado la información.

## Pre-requisitos 📋

Tener instalado Python en el PC, además un editor de código como Visual Studio Code.

```
Python
Visual Studio Code
Muchas ganas de aprender
```

## Instalación 🔧

No se hace necesario realizar instalación de la aplicación, basta con descargar los archivos .py y ejecutar para ver su funcionamiento.


## Single Responsability Principle ⌨️

Este primer principio nos dice que una clase debe tener una única responsabilidad en la aplicación, es decir, que cada objeto de la aplicación hace solo una cosa. No se deben mezclar, según este principio, las difernetes capas de nuestra aplicación, por ejemplo la lógica de negocio con la lógica de presentación de la información.


## Open / Closed Principle 📦

Este principio, nombrado por primera vez por Bertrand Mayer, nos dice que un componente de software debe estar abierto para su exprensión pero cerrado para su modificación. En la medida en que nuestra aplicación crece no se modifican las clases existentes, sino que se generan nuevas clases o nuevas implementaciones de las clases existentes, esto nos permite agregar nuevas funcionalidades a nuestra aplicación sin la necesidad de modificar el código existente.


## LISKOV Substitution Principle 🛠️

Este principio hace referencia al uso de las clases extendidas. Cuando se genera la herencia de una clase a la otra, no se ve afectado el comportamiento de la clase padre. 


## Interface Segregation Principle 🖇️

Ninguna de las clases de nuestra aplicación debería depender de métodos que no utiliza. Las funciones que se crean dentro de una clase van a ser muy importantes para las demás clases que implementan esta clase. 


## Dependency Inversion Principle 📖

Las clases de alto nivel no deberían depender de las clases de bajo nivel, ambas deben depender de las abstracciones. Las abstracciones en su lugar no pueden depender de los detalles.


Plantilla tomada de internet.