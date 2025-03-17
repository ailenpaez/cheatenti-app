**Flujo del sistema:**

📍Autenticación con Google Calendar:
El usuario autoriza el acceso a su calendario mediante las credenciales de OAuth 2.0 almacenadas en credentials.json.
El sistema obtiene los eventos del día consultando la API de Google Calendar.
Detección de eventos próximos:
Cada 5 minutos, el sistema revisa si hay eventos que ocurrirán en los próximos 15 minutos.
Si hay un evento próximo, se activa una alerta sonora (zumbido_messenger.mp3).
Manejo de alertas y repetición:
La alerta sonora se reproduce una vez.
Si el usuario no ingresa un código numérico de 4 dígitos (configurado en config.py), la alerta se repetirá hasta 3 veces con intervalos de 5 minutos.
Cancelación de alertas:
Si el usuario ingresa el código correcto, la alerta se desactiva.
Si el usuario no responde, la alerta se repite hasta 3 veces antes de detenerse.

📍Ejemplo de uso:
Un evento en Google Calendar está programado para 14:00.
A las 13:45, CheAttenti emite una alerta sonora.
Si el usuario ingresa el código de 4 dígitos, la alerta se detiene.
Si no responde, la alerta se repetirá a las 13:50 y 13:55 antes de detenerse automáticamente.
Consideraciones técnicas:

El programa está desarrollado en Python y usa la API de Google Calendar para obtener eventos.
La reproducción de sonido se maneja con sound.py.
Se ejecuta a través de main.py, que orquesta la autenticación, la obtención de eventos y la gestión de alertas.
Se recomienda no subir credentials.json a repositorios públicos por razones de seguridad.


# CheAttenti - Sistema de Alertas para Google Calendar

CheAttenti es una aplicación de escritorio desarrollada en Python que te ayuda a mantenerte al día con tus eventos en Google Calendar mediante alertas sonoras. La aplicación monitorea tu calendario y te notifica antes de que ocurran tus eventos programados, asegurando que nunca pierdas una reunión importante.

## Características

- **Integración con Google Calendar**: Accede a tus eventos programados sin necesidad de revisar constantemente tu calendario.
- **Alertas sonoras personalizables**: Reproduce un sonido de alerta cuando se aproxima un evento.
- **Sistema de verificación**: Exige un código de verificación para confirmar que has recibido la alerta.
- **Alertas repetitivas**: Si no confirmas la alerta, el sistema la repetirá hasta 3 veces.
- **Configuración personalizable**: Ajusta el tiempo de alerta, intervalos y otros parámetros según tus necesidades.

## Requisitos previos

- Python 3.7 o superior
- Una cuenta de Google con Google Calendar
- Credenciales OAuth 2.0 para la API de Google Calendar

## Instalación

1. Clona este repositorio o descarga los archivos:

```bash
git clone https://github.com/tu-usuario/cheatenti.git
cd cheatenti
```

2. Instala las dependencias necesarias:

```bash
pip install -r src/requirements.txt
```

3. Configura las credenciales de Google Calendar:
   - Ve a la [Consola de Google Cloud](https://console.cloud.google.com/)
   - Crea un nuevo proyecto
   - Activa la API de Google Calendar
   - Crea credenciales OAuth 2.0 para una aplicación de escritorio
   - Descarga el archivo JSON de credenciales y guárdalo como `credentials.json` en la raíz del proyecto

## Estructura del proyecto

```
CHEATENTI/
│
├── assets/
│   └── zumbido_messenger.mp3      # Archivo de sonido para las alertas
│
├── src/
│   ├── main.py                   # Punto de entrada principal del programa
│   ├── config.py                 # Configuración del sistema
│   ├── google_calendar.py        # Integración con Google Calendar
│   ├── alert_system.py           # Sistema de gestión de alertas
│   ├── sound.py                  # Manejo de reproducción de sonido
│   └── requirements.txt          # Lista de dependencias
│
├── credentials.json              # Credenciales de OAuth para Google Calendar (debes crearlo)
└── README.md                     # Este archivo
```

## Configuración

Puedes personalizar el comportamiento de CheAttenti modificando las variables en el archivo `src/config.py`:

```python
# Código de 4 dígitos para cancelar alertas
VERIFICATION_CODE = "1234"  

# Intervalo de verificación en minutos
CHECK_INTERVAL = 5  

# Minutos antes del evento para disparar la alerta
ALERT_THRESHOLD = 15  

# Máximo número de alertas por evento
MAX_ALERTS = 3  

# Minutos entre alertas repetidas
ALERT_INTERVAL = 5  

# ID del calendario a consultar (primary es el principal)
CALENDAR_ID = "primary"  
```

## Uso

1. Ejecuta la aplicación desde la carpeta src:

```bash
cd src
python main.py
```

2. La primera vez que ejecutes la aplicación, se abrirá un navegador web para autorizar el acceso a tu Google Calendar.

3. Una vez autorizado, CheAttenti comenzará a monitorear tu calendario y te alertará sobre eventos próximos.

4. Cuando suene una alerta:
   - Se mostrará el nombre del evento
   - Deberás ingresar el código de verificación (por defecto: 1234)
   - Si ingresas el código correcto, la alerta se cancelará
   - Si no respondes o ingresas un código incorrecto, la alerta se repetirá hasta 3 veces

## Flujo del sistema

1. **Autenticación con Google Calendar**:
   * El usuario autoriza el acceso a su calendario mediante las credenciales de OAuth 2.0.
   * El sistema obtiene los eventos del día consultando la API de Google Calendar.

2. **Detección de eventos próximos**:
   * Cada 5 minutos, el sistema revisa si hay eventos que ocurrirán en los próximos 15 minutos.
   * Si hay un evento próximo, se activa una alerta sonora.

3. **Manejo de alertas y repetición**:
   * La alerta sonora se reproduce una vez.
   * Si el usuario no ingresa el código numérico de 4 dígitos, la alerta se repetirá hasta 3 veces con intervalos de 5 minutos.

4. **Cancelación de alertas**:
   * Si el usuario ingresa el código correcto, la alerta se desactiva.
   * Si el usuario no responde, la alerta se repite hasta 3 veces antes de detenerse.

## Seguridad

**Importante**: No subas los archivos `credentials.json` o `token.json` a repositorios públicos, ya que contienen información confidencial de acceso a tu cuenta de Google.

## Solución de problemas

- **No se reproducen sonidos**: Verifica que tienes pygame instalado correctamente y que el archivo de sonido existe en la carpeta assets.
- **Error de autenticación**: Asegúrate de que el archivo credentials.json está en la ubicación correcta y es válido.
- **No se detectan eventos**: Verifica que estás usando el ID de calendario correcto y que tienes eventos programados en el rango de tiempo configurado.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para sugerir cambios o mejoras.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
