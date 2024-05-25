import logging

# Configuración del logger
logger = logging.getLogger('LOG')
logger.setLevel(logging.DEBUG)

# Crear el archivo creacion-procesos.log
file_handler = logging.FileHandler('Crear_Modificar.log')
file_handler.setLevel(logging.DEBUG)

# Formatear los mensajes
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)