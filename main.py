import json
import pandas as pd
from datetime import datetime
import os

from utils.limpiador import limpiar_precio
from scrapers.farmacity import FarmacityScraper
from scrapers.pigmento import PigmentoScraper
from scrapers.simplicity import SimplicityScraper
from scrapers.getthelook import GetTheLookScraper
from reportero import generar_reporte

def guardar_datos_inteligente(nuevos_datos):
    path_archivo = 'data/precios_historicos.csv'
    os.makedirs('data', exist_ok=True)
    df_nuevo = pd.DataFrame(nuevos_datos)
    if os.path.exists(path_archivo):
        df_viejo = pd.read_csv(path_archivo)
        df_final = pd.concat([df_viejo, df_nuevo], ignore_index=True)
    else:
        df_final = df_nuevo
    df_final = df_final.drop_duplicates(subset=['fecha', 'producto', 'tienda'], keep='last')
    df_final.to_csv(path_archivo, index=False, encoding='utf-8')

if __name__ == "__main__":
    with open('config/productos.json', 'r') as f:
        config = json.load(f)

    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    resultados = []

    # Inicializamos los bots (headless=False para ver qué pasa con Pigmento)
    bots = {
        "Farmacity": FarmacityScraper(headless=True),
        "Pigmento": PigmentoScraper(headless=True),
        "Simplicity": SimplicityScraper(headless=True),
        "GetTheLook": GetTheLookScraper(headless=True)
    }

    for prod_id, urls in config.items():
        for tienda, bot in bots.items():
            url = urls.get(tienda)
            if url:
                print(f"🕵️ Buscando en {tienda}...")
                precio_raw = bot.obtener_precio(url)
                precio_final = limpiar_precio(precio_raw)
                resultados.append({
                    'fecha': fecha_hoy,
                    'producto': prod_id,
                    'tienda': tienda,
                    'precio': precio_final
                })

    for bot in bots.values():
        bot.cerrar_driver()

    guardar_datos_inteligente(resultados)
    generar_reporte()
    
from utils.notificador import enviar_telegram

if resultados:
    resumen = "🚀 *¡Reporte de Precios Listo!* 🚀\n\n"
    resumen += f"📅 Fecha: {fecha_hoy}\n"
    resumen += "--------------------------\n"
    
    for res in resultados:
        # Si el precio es 0, ponemos un aviso
        p = f"${res['precio']}" if res['precio'] > 0 else "No encontrado ❌"
        resumen += f"🧴 *{res['tienda']}*: {p}\n"
    
    resumen += "\n✅ _Pipeline finalizado con éxito_"
    enviar_telegram(resumen)