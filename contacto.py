import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def menu_contacto():
    numero = os.getenv('MI_NUMERO')
    instagram_url = os.getenv('MI_INSTAGRAM')

    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("📲 WhatsApp Atención", url=f"https://wa.me/{numero}"))
    markup.add(InlineKeyboardButton("💻 Visita nuestro Instagram", url=instagram_url))
    markup.add(InlineKeyboardButton("📍 Ver en Google Maps", url="https://maps.app.goo.gl/enlace_real"))
    markup.add(InlineKeyboardButton("⬅️ Volver al Inicio", callback_data='volver_inicio'))
    
    texto = (
        "🍓 **PASTELERÍA FRESA DULCE** 🍓\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🚗 **Dirección:** Av. Victoria, Calle Caracas, La Victoria - Edo. Aragua.\n\n"
        "⏰ **Horario:** Lun-Vie: 7:00 AM - 8:00 PM | Sáb: 7:00 AM - 8:00 PM | Dom: 8:00 AM - 6:00 PM\n\n"
        "Pulsa abajo para escribirnos por WhatsApp o ver nuestra ubicación:"
    )
    
    return texto, markup