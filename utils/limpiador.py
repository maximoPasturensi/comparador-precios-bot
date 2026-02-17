import re

def limpiar_precio(precio_str):
    if not precio_str or precio_str == "0":
        return 0
    # Limpieza: quitamos $, centavos y dejamos solo números
    limpio = precio_str.replace("$", "").strip()
    if "," in limpio:
        limpio = limpio.split(",")[0]
    limpio = re.sub(r'\D', '', limpio)
    return int(limpio)