import pandas as pd
import os

def generar_reporte():
    archivo = 'data/precios_historicos.csv'
    
    if not os.path.exists(archivo):
        print("❌ No hay datos para analizar. Corré el main.py primero.")
        return

    # 1. Cargamos los datos
    df = pd.read_csv(archivo)

    # 2. Filtramos solo lo de HOY (para que no mezcle con precios viejos)
    ultima_fecha = df['fecha'].max()
    df_hoy = df[df['fecha'] == ultima_fecha]

    print(f"\n==========================================")
    print(f"📊 REPORTE DE PRECIOS - {ultima_fecha}")
    print(f"==========================================\n")

    # 3. Agrupamos por producto para encontrar el mejor precio
    for producto in df_hoy['producto'].unique():
        df_prod = df_hoy[df_hoy['producto'] == producto]
        
        # Filtramos precios en 0 (errores de scraping)
        df_prod = df_prod[df_prod['precio'] > 0]

        if df_prod.empty:
            print(f"Producto: {producto} -> Sin datos válidos hoy.")
            continue

        # Buscamos el más barato y el más caro
        mas_barato = df_prod.loc[df_prod['precio'].idxmin()]
        mas_caro = df_prod.loc[df_prod['precio'].idxmax()]
        
        ahorro = mas_caro['precio'] - mas_barato['precio']
        porcentaje_ahorro = (ahorro / mas_caro['precio']) * 100

        print(f"🧴 Producto: {producto}")
        print(f"✅ La mejor opción es {mas_barato['tienda']} a ${mas_barato['precio']}")
        print(f"❌ La más cara es {mas_caro['tienda']} a ${mas_caro['precio']}")
        
        if ahorro > 0:
            print(f"💰 ¡Ahorrás ${ahorro} ({porcentaje_ahorro:.1f}%) si comprás en {mas_barato['tienda']}!")
        else:
            print(f"⚖️ Los precios están iguales en todas las tiendas.")
        print("-" * 40)

if __name__ == "__main__":
    generar_reporte()