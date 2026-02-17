# 🛒 Smart Price Tracker & Deal Detector Bot

Bot automatizado de Scraping diseñado para monitorear precios de productos de cuidado personal en tiempo real, comparar valores históricos y notificar ofertas automáticamente vía Telegram.

## 📱 Vista previa del Bot
A continuación se muestra un ejemplo del reporte diario enviado a Telegram, incluyendo la detección automática de ofertas:

<p align="center">
  <img src="/Users/maximopasturensi/Desktop/Proyecto_Precios/screenshots/WhatsApp Image 2026-02-17 at 17.04.18.jpeg" width="300" title="Reporte de Telegram">
</p>

## 🚀 Características Principales
* **Scraping Multitienda:** Soporte para Farmacity, Pigmento, Simplicity y GetTheLook.
* **Detección de Ofertas:** Compara el precio del día contra un historial local (`CSV`) y calcula el porcentaje de ahorro.
* **Automatización Total:** Ejecución diaria programada mediante **GitHub Actions** (CI/CD).
* **Notificaciones Instantáneas:** Alertas inteligentes por Telegram con formato enriquecido.
* **Arquitectura Robusta:** Uso de Selenium en modo *headless* para ejecución en servidores en la nube.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.9
* **Librerías:** Selenium, Pandas, Requests.
* **Infraestructura:** GitHub Actions (Automatización y base de datos liviana).
* **Notificaciones:** Telegram Bot API.

## 🤖 Cómo funciona el Pipeline
1. **Trigger:** GitHub Actions inicia el flujo cada mañana (Cron job).
2. **Extracción:** Los scrapers navegan las URLs configuradas y limpian los datos.
3. **Análisis:** El sistema lee el historial, detecta si el precio bajó y actualiza la base de datos.
4. **Alerta:** Si hay una rebaja, envía un mensaje detallado al usuario.

## 💻 Implementación Técnica
El núcleo del sistema utiliza una lógica de comparación de precios basada en archivos CSV para la persistencia de datos:

'''
    # 2. Guardar historial y Generar Reporte con Ofertas
    if resultados:
        guardar_datos_inteligente(resultados)
        
        resumen = "🔔 *REPORTE DE PRECIOS* 🔔\n\n"
        resumen += f"📅 Fecha: {fecha_hoy}\n"
        resumen += "--------------------------\n\n"
        
        for res in resultados:
            tienda = res['tienda']
            producto = res['producto']
            precio = res['precio']
            
            # Buscamos si el precio bajó respecto al historial
            oferta = procesar_precio_y_buscar_oferta(tienda, producto, precio)
            
            if oferta:
                resumen += f"🔥 *¡OFERTA EN {tienda}!* 📉\n"
                resumen += f"🧴 {producto}: *${precio}*\n"
                resumen += f"⚠️ _(Bajó {oferta['porcentaje']}% - Antes ${oferta['anterior']})_\n\n"
            else:
                p_texto = f"${precio}" if precio > 0 else "No encontrado ❌"
                resumen += f"🔹 *{tienda}* - {producto}: {p_texto}\n"
        
        resumen += "\n✅ _Pipeline finalizado con éxito_"
        enviar_telegram(resumen)    
'''
---
*Proyecto desarrollado por Máximo Pasturensi como parte de un flujo de automatización profesional.*
