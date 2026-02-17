import pandas as pd
import os
from datetime import datetime

def procesar_precio_y_buscar_oferta(tienda, producto, precio_actual):
    archivo = 'data/precios_historicos.csv'
    oferta_detectada = None
    
    # 1. Leer el historial si existe
    if os.path.exists(archivo) and os.path.getsize(archivo) > 0:
        df = pd.read_csv(archivo)
        
        # 2. Buscar el último precio registrado de este producto en esta tienda
        filtro = (df['tienda'] == tienda) & (df['producto'] == producto)
        registros_previos = df[filtro]
        
        if not registros_previos.empty:
            ultimo_precio = registros_previos.iloc[-1]['precio']
            
            # 3. Comparar: ¿Bajó el precio?
            if precio_actual < ultimo_precio:
                ahorro = ultimo_precio - precio_actual
                porcentaje = (ahorro / ultimo_precio) * 100
                oferta_detectada = {
                    'anterior': ultimo_precio,
                    'ahorro': ahorro,
                    'porcentaje': round(porcentaje, 1)
                }
    
    # 4. Guardar el nuevo precio en el CSV
    nuevo_registro = {
        'fecha': datetime.now().strftime('%Y-%m-%d'),
        'tienda': tienda,
        'producto': producto,
        'precio': precio_actual
    }
    
    # Append al CSV
    df_nuevo = pd.DataFrame([nuevo_registro])
    df_nuevo.to_csv(archivo, mode='a', index=False, header=not os.path.exists(archivo))
    
    return oferta_detectada