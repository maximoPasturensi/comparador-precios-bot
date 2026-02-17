import requests
import os # Importante para leer variables ocultas

def enviar_telegram(mensaje):
    # En lugar de poner el texto, le pedimos al sistema que lo busque
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        print("❌ Error: No se encontraron las credenciales de Telegram.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': mensaje,
        'parse_mode': 'Markdown'
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Reporte enviado a Telegram!")
        else:
            print(f"❌ Error en Telegram: {response.status_code}")
    except Exception as e:
        print(f"❌ Error de conexión con Telegram: {e}")