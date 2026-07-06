import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from dotenv import load_dotenv

load_dotenv()

import productos
import servicios
import contacto

TOKEN = os.getenv('TOKEN')
TELEFONO = os.getenv('MI_TELEFONO')
INSTAGRAM = os.getenv('MI_INSTAGRAM')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'menu'])
def inicio(message):
    markup= InlineKeyboardMarkup()

    btn_productos = InlineKeyboardButton("🍓 Menú de Postres", callback_data="ver_menu")
    btn_servicios = InlineKeyboardButton("📦 Nuestros Servicios", callback_data="servicios")
    btn_contacto = InlineKeyboardButton(" 📞 Contacto y Ubicación", callback_data="contacto")
    
    markup.row(btn_productos)
    markup.row(btn_servicios)
    markup.row(btn_contacto)
    
    texto = (
        f"🍓 **PASTELERÍA FRESA DULCE, TU MEJOR OPCIÓN.** 🍓\n"
        f"¡Hola, bienvenido fresalover! Selecciona una opción del menú para comenzar:"
    )
    
    bot.send_message(message.chat.id, texto, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def manejador_principal(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    
    bot.answer_callback_query(call.id)

    if call.data == "volver_inicio":
        bot.delete_message(cid, mid)
        inicio(call.message)


#Productos - Servicios
    elif call.data.startswith("detalle_"):
        partes = call.data.split('_')
        categoria = partes[1]
        id_item = "_".join(partes[2:])
        
        try:
            if categoria == "servicios":
                item = servicios.Servicios["servicios"]["items"][id_item]
                texto_detalle = f"🍓 *{item['nombre']}*\n\n{item['desc']}"
                callback_volver = "servicios"
                bot.edit_message_text(texto_detalle, cid, mid, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Volver", callback_data=callback_volver)), parse_mode="Markdown")
            else:
                prod = productos.Catalogo[categoria]["items"][id_item]
                texto_detalle = f"*{prod['nombre']}*\nPrecio: {prod['precio']}\n\n{prod['desc']}"
                markup = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Volver a la lista", callback_data=f"lista_{categoria}"))
                
                if 'foto' in prod:
                    bot.edit_message_media(chat_id=cid, message_id=mid, media=telebot.types.InputMediaPhoto(prod['foto'], caption=texto_detalle, parse_mode="Markdown"), reply_markup=markup)
                else:
                    bot.edit_message_text(texto_detalle, cid, mid, reply_markup=markup, parse_mode="Markdown")
        except Exception as e:
            print(f"Error en detalle: {e}")

     
#Navegar por menu principal

    #Categorias
    elif call.data == "ver_menu":
        texto, menu = productos.menu_categorias()
        bot.edit_message_text(texto, cid, mid, reply_markup=menu, parse_mode="Markdown")

    #Lista de productos
    elif call.data.startswith("lista_"):
        categoria = call.data.split('_')[1]
        texto, menu = productos.generar_lista_productos(categoria)
        bot.delete_message(cid, mid)
        bot.send_message(cid, texto, reply_markup=menu, parse_mode="Markdown")

    #Servicios
    elif call.data == "servicios":
        datos = servicios.Servicios["servicios"]
        markup = InlineKeyboardMarkup(row_width=1)
        for id_item, info in datos["items"].items():
            markup.add(InlineKeyboardButton(info["nombre"], callback_data=f"detalle_servicios_{id_item}"))
        markup.add(InlineKeyboardButton("⬅️ Volver al Inicio", callback_data="volver_inicio"))
        bot.edit_message_text(f"🍓 *{datos['titulo']}*\n\n{datos['descripcion']}", cid, mid, reply_markup=markup, parse_mode="Markdown")

    #Contacto
    elif call.data == "contacto":
        texto, menu = contacto.menu_contacto()
        bot.edit_message_text(texto, cid, mid, reply_markup=menu, parse_mode="Markdown")

bot.infinity_polling()