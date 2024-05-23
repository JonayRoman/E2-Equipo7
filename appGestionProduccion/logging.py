import logging

# Configuración del logger de creacion de proyectos
logger = logging.getLogger('creacion_proceso')
logger.setLevel(logging.DEBUG)

# Crear el archivo creacion-procesos.log
file_handler = logging.FileHandler('Crear_Modificar.log')
file_handler.setLevel(logging.DEBUG)

# CFormatear los mensajes
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)