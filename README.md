Taller Independiente - Programación Distribuida

## ¿Qué es Cliente-Servidor?
El modelo cliente-servidor es una arquitectura de red donde las tareas se distribuyen entre dos roles:
El servidor es un programa o máquina que ofrece recursos o servicios (archivos, bases de datos, páginas web, etc.) y espera peticiones de manera continua.
El cliente es quien inicia la comunicación solicitando un servicio al servidor. No se comunican clientes entre sí (a diferencia de P2P), toda la comunicación pasa por el servidor.
El flujo básico es: el cliente envía una solicitud (request) → el servidor la procesa → el servidor envía una respuesta (response).
Ejemplos cotidianos: cuando abres un navegador y escribes una URL, tu navegador es el cliente y el servidor web responde con el HTML de la página. Lo mismo ocurre con apps móviles, correo electrónico (SMTP/IMAP) o bases de datos remotas.
En programación distribuida esto es fundamental porque los sistemas se construyen con múltiples clientes accediendo a uno o varios servidores, muchas veces de forma simultánea, lo que introduce desafíos de concurrencia.

## Diferencia entre Proceso e Hilo
Un proceso es un programa en ejecución que cuenta con su propio espacio de memoria, recursos del sistema operativo y contexto de ejecución completamente independiente. Cuando abres dos instancias del mismo programa, el sistema operativo crea dos procesos separados que no comparten memoria entre sí. Si uno falla, el otro no se ve afectado. La comunicación entre procesos existe pero es compleja, requiere mecanismos especiales como sockets o pipes.
Un hilo (o thread) en cambio es una unidad de ejecución que vive dentro de un proceso. Un solo proceso puede tener múltiples hilos ejecutándose al mismo tiempo, y todos ellos comparten la misma memoria y recursos del proceso que los contiene. Esto los hace mucho más ligeros y rápidos de crear que un proceso nuevo, y la comunicación entre ellos es directa al compartir memoria. La desventaja es que si un hilo tiene un error grave, puede afectar a todos los demás hilos del mismo proceso.
Una buena analogía es pensar en el proceso como una casa completa con su propia cocina, baños y habitaciones. Los hilos serían las personas viviendo dentro de esa casa: cada una hace sus propias actividades de forma independiente pero todas comparten los mismos espacios y recursos.
En el contexto de programación distribuida esto es especialmente relevante porque un servidor típicamente crea un hilo nuevo por cada cliente que se conecta, permitiendo atender a muchos clientes de forma simultánea sin que tengan que esperar uno al otro.
Ejemplo
Abrir dos instancias de Chrome
Las pestañas dentro de Chrome
Analogía: un proceso es como una casa completa con su propia cocina, baño y habitaciones. Un hilo es como una persona viviendo dentro de esa casa; puede haber varias personas (hilos) compartiendo los mismos espacios (memoria).
En programación distribuida y servidores esto importa mucho: un servidor puede crear un hilo por cada cliente que se conecta para atenderlos simultáneamente sin bloquear a los demás.

## ¿Qué hice?
- Investigué el modelo cliente-servidor y la diferencia entre procesos e hilos
- Instalé Git y configuré WSL con Ubuntu
- Creé este repositorio y subí los archivos de clase

## ¿Qué aprendí?
- El modelo cliente-servidor es la base de la mayoría de aplicaciones distribuidas, donde el cliente solicita y el servidor responde
- Un proceso tiene su propio espacio de memoria mientras que los hilos comparten el espacio del proceso padre, siendo más ligeros pero menos aislados
- Cómo usar comandos básicos de Git (init, add, commit, push)

## Dificultades
- Configuracion de token en Git en ambiente WSL
