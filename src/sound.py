import pygame
import time

class SoundPlayer:
    def __init__(self):
        # Inicializa el mezclador de pygame
        pygame.mixer.init()
        
    def play_alert(self, sound_file):
        """Reproduce un archivo de sonido de alerta."""
        try:
            # Carga el archivo de sonido
            pygame.mixer.music.load(sound_file)
            # Reproduce el sonido
            pygame.mixer.music.play()
            
            # Espera hasta que termine la reproducción
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
                
            return True
        except Exception as e:
            print(f"Error al reproducir el sonido: {e}")
            return False
            
    def stop_alert(self):
        """Detiene la reproducción del sonido actual."""
        pygame.mixer.music.stop()