import config

# Imprime los valores de configuración para verificar
print(f"Código de verificación: {config.VERIFICATION_CODE}")
print(f"Intervalo de verificación: {config.CHECK_INTERVAL} minutos")
print(f"Umbral de alerta: {config.ALERT_THRESHOLD} minutos")
print(f"Máximo de alertas: {config.MAX_ALERTS}")