# Preguntas

1. **Identifica una ejecución exitosa y una fallida. ¿Qué commit o cambio produjo cada una y qué step determinó el resultado?**

   La ejecución exitosa se evidencia en el workflow #6 asociado al commit 00f9662, donde el step Ejecutar pruebas finalizó exitosamente.

   La ejecución fallida fue producida en el workflow #7 asociada al commit 4912649, por el cambio en el código assert clasificar_stock(7, 20) == "NORMAL" para que fallara intencionadamente. El step que determinó este fallo fue Ejecutar pruebas

2. **¿Por qué ejecutar pytest localmente no reemplaza ejecutar pytest en GitHub Actions?**

   Ejecutar pytest localmente no reemplaza a GitHub Actions porque Actions utiliza un runner limpio que requiere descargar el repositorio e instalar dependencias desde cero. Esto evita falsos positivos causados por configuraciones locales, dependencias no declaradas o archivos que no fueron enviados al repositorio.

3. **¿Qué riesgo tendría hacer merge a main sin esperar los checks del Pull Request?**

   El riesgo radica en integrar un cambio que rompa el código que antes funcionaba. Esperar los checks del evento pull_request asegura que las verificaciones automáticas pasaron antes del merge.

4. **En tu ejecución fallida, copia solo la línea esencial del error y explica qué te permitió diagnosticar.**

   La línea esencial es

   *FAILED tests/test_inventario.py::test_stock_critico - AssertionError: assert 'CRITICO' == 'NORMAL'.*

   Esto permitió diagnosticar que la función evaluó los valores y retornó CRITICO, lo cual no coincidió con la aserción intencionalmente incorrecta que esperaba NORMAL.

5. **¿Qué diferencia existe entre un step que usa `uses:` y uno que utiliza `run:`?**

   Uses: Indica el uso de un componente reutilizable o acción como descargar el repositorio o configurar Python

   Run: ejecuta comandos directos del sistema dentro del runner.

6. **¿Qué información aporta `${{ github.actor }}` en `run-name` y por qué puede ser útil en un proyecto en equipo?**

   Esta variable registra y muestra qué usuario o contribuidor del repositorio disparó la ejecución del workflow. Esto puede ser útil para saber qué persona ejecutó cada workflow e identificar, en caso de error, qué usuario lo cometió

7. **Si tu workflow pasa pero la aplicación completa falla localmente con Docker, ¿significa que Actions “no sirve”? Explica qué está verificando y qué no.**

   Que el workflow pase pero la aplicación falle localmente no invalida Actions, ya que el CI está configurado para verificar rápidamente la calidad mínima del código, como la sintaxis y las pruebas unitarias. El workflow no levanta toda la infraestructura ni ejecuta simulaciones completas en cada commit.

8. **Propón tres checks para tu variante de RapidGo. Para cada uno explica qué error concreto evitaría.**

   a. **Validación del contrato JSON:** comprobar que los eventos de experiencia del cliente contengan los campos obligatorios, como event_id, order_id, rating, reason, channel y timestamp, con los tipos de datos correctos. Evitaría que eventos incompletos o mal estructurados lleguen a Kafka y provoquen errores durante el procesamiento con Spark.

   b. **Pruebas de KPIs y alertas:** ejecutar pruebas automatizadas que verifiquen el cálculo de la calificación media, la identificación de motivos frecuentes de insatisfacción y la activación de las alertas cuando se cumplan los umbrales definidos. Evitaría errores en las métricas o que el sistema no detecte una caída de satisfacción o una concentración de reclamos.

   c. **Validación de Docker Compose:** comprobar que el docker compose tenga una configuración válida y que los servicios definidos cumplan con la estructura esperada. Evitaría errores de sintaxis o configuración que impidan iniciar los componentes necesarios para ejecutar el pipeline

9. **¿Cuál de esos checks debería implementarse primero y por qué?**

   La validación del contrato JSON, porque los eventos son la entrada del pipeline y todos los componentes posteriores dependen de que los datos tengan una estructura consistente, el hecho de detectar campos faltantes, tipos incorrectos o calificaciones fuera del rango permitido desde el inicio reduce los errores en Kafka y Spark, facilita las pruebas posteriores y permite validar automáticamente cada cambio mediante GitHub Actions.

10. **¿Qué prueba sería demasiado costosa o frágil para ejecutar en cada push y cómo la validarías entonces?**

    Una prueba de integración completa del pipeline, que levante Kafka, Spark, el Data Lake y Airflow mediante Docker y simule un flujo de eventos de principio a fin, podría ser demasiado costosa para ejecutarse en cada push, debido al tiempo de inicio de los servicios, el consumo de recursos y los posibles fallos asociados al entorno.

    La mejor opcion seria validarla a traves de ejecuciones programadas o antes de publicar un release, utilizando un entorno controlado y un conjunto de eventos de prueba. En cada push se mantendrian los checks rápidos, como la validación del JSON, las pruebas unitarias de los KPIs y las alertas, y la validación de la configuración de Docker Compose; de esta manera, se obtiene retroalimentación rápida durante el desarrollo sin dejar de comprobar periódicamente el funcionamiento integral del sistema.
