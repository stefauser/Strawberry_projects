from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import servicios


#Diccionario de productos
Catalogo = {
    "pasteles": {
        "titulo": "🍰🍓 Pasteles y Tortas",
        "descripcion": "Nuestras mejores tortas",
        "items": {
            "torta_jardin": {
                "nombre": "Jardín de Fresas",
                "precio": "30$",
                "desc": "Es una torta clásica de bizcocho de vainilla, rellena y decorada con abundante crema chantilly y fresas frescas dispuestas en rosetones.",
                "foto": 'AgACAgEAAxkBAAMhaiYAARbVXRTnkwvxidOghTd460RUAAL9DGsbqWExRUwmVwV_liHjAQADAgADeAADOwQ'
            },

            "torta_selva": {
                "nombre": "Selva Negra de Fresas",
                "precio": "35$",
                "desc": "Es un pastel de varias capas de bizcocho de chocolate intenso, intercaladas con crema chantilly y fresas frescas, cubierto con un glaseado de chocolate tipo ganache y decorado con fresas naturales.",
                "foto": 'AgACAgEAAxkBAANEaiYVIfo60hc0GKp0_7hLATDuXrwAAhwMaxupYTlF34nZfl6jZQUBAAMCAAN4AAM7BA'
            },
            "romance_fresa": {
                "nombre": "Romance de fresas",
                "precio": "40$",
                "desc": "Delicado pastel cubierto con una capa lisa de crema, decorado con fresas talladas en forma de corazón en los laterales y fresas enteras en la parte superior.",
                "foto": 'AgACAgEAAxkBAANJaiYW9tvCieU7CguAQKBU_xsHgm4AAh0MaxupYTlFVpFGccC67ucBAAMCAAN5AAM7BA'
            },
            "primaveral_fresas": {
                "nombre": "Elegancia primaveral de fresa",
                "precio": "50$",
                "desc": "Es un pastel de estilo fraisier, caracterizado por capas de bizcocho esponjoso intercaladas con crema mousseline y fresas frescas dispuestas en los laterales, decorado con un acabado espolvoreado y detalles florales.",
                "foto": 'AgACAgEAAxkBAANLaiYY_0Nl0LSYRf0Tu9cAAbfaA3bBAAIeDGsbqWE5Rc991tJ9P1oXAQADAgADeAADOwQ'
            },
            "corazon_nata": {
                "nombre": "Corazón de fresa y nata",
                "precio": "30$",
                "desc": "Es un tierno pastel con forma de corazón, elaborado con bizcocho suave, relleno de crema nata y decorado con fresas frescas cortadas en los bordes y en la parte superior. ",
                "foto": 'AgACAgEAAxkBAANNaiYZsP9CEKS64UPM9j2JQnHBkJkAAh8MaxupYTlFbNP9DRox6KYBAAMCAAN4AAM7BA'
            },
            "goteo_fresa": {
                "nombre": "Dulce Goteo de Fresa",
                "precio": "30$",
                "desc": "Es un pastel cubierto con crema de fresa y decorado con un efecto de goteo rosado, coronado con rosetones de nata y fresas frescas.",
                "foto": 'AgACAgEAAxkBAANPaiYaMHCWt1yOZN3MO_mJWLe1smQAAiAMaxupYTlFAtZCCkNH8RcBAAMCAAN4AAM7BA'
            },
        }
    },
    "tartaletas": {
        "titulo": "🥧🍓 Tartaletas de Fresa",
        "descripcion": "Nuestras mejores Tartaletas",
        "items": {
            "gigante_fresa": {
                "nombre": "Tartaleta gigante de fresas",
                "precio": "25$",
                "desc": "Se trata de una tartaleta artesanal de gran tamaño con una base de masa quebrada crujiente, rellena de crema chantilly y decorada con fresas frescas dispuestas en secciones radiales.",
                "foto": 'AgACAgEAAxkBAANVaibOzXidgM5p4gTnHrfw7F7vUj8AAlQMaxupYTlFSC4Pg_EL8tsBAAMCAAN4AAM7BA'
            },
            "pie_fresa":{
                "nombre": "Pie de fresa",
                "precio": "20$",
                "desc": "Pie de fresa clásico elaborado con una masa quebrada crujiente en formato de rejilla, relleno de fresas frescas y espolvoreado con azúcar.",
                "foto": 'AgACAgEAAxkBAANZaibPZm05R7sfVnbzpP2dGBrNLIwAAlUMaxupYTlF0ILvRzeLDtEBAAMCAAN5AAM7BA'
            },
            "tarta_fria": {
                "nombre": "Tarta fría de fresas y nata",
                "precio": "30$",
                "desc": "Esta tarta es una delicada tarta fría de fresas y nata, que presenta una base crujiente, un centro relleno de fresas frescas y está decorada con rosetones de crema montada alrededor de los bordes.",
                "foto": 'AgACAgEAAxkBAANbaibPxlFHOBgxFoiYw7cqjN10QTUAAlcMaxupYTlFpqQbjW_VUQABAQADAgADeAADOwQ'
            },
            "mini_tartas": {
                "nombre": "Mini tarta de fresa",
                "precio": "5$",
                "desc": "Estas pequeñas porciones individuales consisten en una base de masa quebrada crujiente rellena con crema pastelera y coronada con fresas frescas. ",
                "foto": 'AgACAgEAAxkBAANdaibQHAMnlxhYMG3QSss_4JEKZ9QAAlgMaxupYTlFa4nUBRon8pMBAAMCAAN4AAM7BA'
            },
            "delicia_nata":  {
                "nombre": "Delicia de Fresas",
                "precio": "30$",
                "desc": "Es una clásica tarta de base de masa quebrada con relleno cremoso, cubierta con fresas frescas, rosetones de crema chantilly y un toque de menta fresca.",
                "foto": 'AgACAgEAAxkBAANfaibQuXDA3zz6Twm_mzpAi1J9mvAAAloMaxupYTlFi-y8pyvZlcYBAAMCAAN4AAM7BA'
            },
            "corona_fresa":  {
                "nombre": "Corona de fresas y arándanos con crema",
                "precio": "30$",
                "desc": "Es una tarta artesanal elaborada con una base de masa quebrada crujiente, rellena de crema chantilly y decorada con una selección de fresas frescas y arándanos, rematada con un toque de hojas de menta.",
                "foto": 'AgACAgEAAxkBAANhaibRBGEwRVNCQRjxq38bpkpX7OkAAlsMaxupYTlFTCWQ3LfUhT0BAAMCAAN4AAM7BA'
            },
        }
    },
    "cupcakes": {
        "titulo": "🧁🍓 Cupcakes Decorados",
        "descripcion": "Cupcakes 12 unidades",
        "items": {
            "capricho_fresa": {
                "nombre": "Capricho de fresa",
                "precio": "15$",
                "desc": "Cupcakes de vainilla con un copete elegante de crema montada y decorados con una fresa entera.",
                "foto": 'AgACAgEAAxkBAANvaibViVYv9aahdQggnaukuVvCY_EAAmEMaxupYTlFfNuY7YX_KjcBAAMCAAN4AAM7BA'
            },
            "choco_fresa":  {
                "nombre": "Delicia Choco-Fresa",
                "precio": "18$",
                "desc": "Son cupcakes de chocolate con un copete de crema, decorados con hilos de chocolate fundido y una fresa fresca.",
                "foto": 'AgACAgEAAxkBAANyaibWBYx-AcshUX0Sjlb0hMikERIAAmIMaxupYTlFWsmuxFmK8wIBAAMCAAN5AAM7BA'
            },
            "explosion_fresa": {
                "nombre": "Explosión de Fresa",
                "precio": "15$",
                "desc": "Son cupcakes decorados con crema de fresa, un drizzle y una fresa fresca completa coronando cada unidad.",
                "foto": 'AgACAgEAAxkBAAN0aibWUGxqq0XUJnkDOsPg95ByQ7AAAmMMaxupYTlFY5ULWRsJ_b0BAAMCAAN4AAM7BA'
            },
            "fresa_jardin": {
                "nombre": "Fresa de Jardín",
                "precio": "20$",
                "desc": "Cupcakes de masa suave con un copete de crema chantilly, decorados en el centro con una porción de fresas picadas.",
                "foto": 'AgACAgEAAxkBAAN2aibWhJaCAeuBDGNWNxSewTO0tC0AAmQMaxupYTlFkuhNv76UMXoBAAMCAAN5AAM7BA'
            },
            "bocadito_terciopelo": {
                "nombre": "Bocaditos de terciopelo",
                "precio": "25$",
                "desc": "Son cupcakes de red velvet cubiertos con una cremosa cobertura blanca y decorados con una fresa fresca.",
                "foto": 'AgACAgEAAxkBAAN4aibXI5KuCgPLC_GcLEXWIaFO6qsAAmUMaxupYTlFZZUSfvkZeWIBAAMCAAN4AAM7BA'
            },
            "delicia_duo": {
                "nombre": "Delicia Dúo de Chocolate y Fresa",
                "precio": "25$",
                "desc": "Cupcakes de chocolate con una cobertura bicolor crema de fresa y ganache de chocolate, decorados con chispas de chocolate y una fresa fresca.",
                "foto": 'AgACAgEAAxkBAAN6aibXWyPn55Vgwauho6wsNtIwAAE1AAJnDGsbqWE5ReB-PSISlJ3LAQADAgADeAADOwQ'
            },
        }
    },
    "galletas": {
        "titulo": "🍪🍓 Galletas Rellenas",
        "descripcion": "Deliciosas y crujientes galletas, 10 unidades",
        "items": {
            "relampago_fresa": {
                "nombre": "Relámpagos de fresa",
                "precio": "15$",
                "desc": "Se trata de éclairs elaborados con masa choux, rellenos de crema chantilly y decorados artísticamente con fresas cortadas en forma de corazón",
                "foto": 'AgACAgEAAxkBAAN8aibXk3Y4UvpyMq0j9fHexztDL1oAAmgMaxupYTlFggo1r0vM0JoBAAMCAAN4AAM7BA'
            },
            "anillos_fresa": {
                "nombre": "Anillos fresa y crema",
                "precio": "15$",
                "desc": "Delicados anillos de masa tipo choux, rellenos con crema pastelera y fresas frescas, espolvoreados con azúcar glass.",
                "foto": 'AgACAgEAAxkBAAN-aibX6xeIcXI-0GmLRwhWKzrD7EQAAmkMaxupYTlF5-QeI5nkXz8BAAMCAAN4AAM7BA'
            },
            "barritas_fresa": {
                "nombre": "Barritas de fresa",
                "precio": "20$",
                "desc": "Pastelitos en forma de corazón, rellenos de crema y coronados con una fresa fresca, espolvoreados con azúcar glass.",
                "foto": 'AgACAgEAAxkBAAOAaibYKIp69jtM6-n3PX7hY1Ee5c0AAmsMaxupYTlF2gJTtkL4-gwBAAMCAAN5AAM7BA'
            },
            "magdalena_fresa": {
                "nombre": "Magdalenas de corazón con fresa",
                "precio": "12$",
                "desc": "Son pequeñas piezas de repostería con forma de corazón, horneadas con un relleno central de mermelada de fresa.",
                "foto":'AgACAgEAAxkBAAOCaibYibhEbAR8Pgifr49Zt3XwL_sAAmwMaxupYTlFBeaD9c3fg8wBAAMCAAN4AAM7BA'
            },
            "bocadito_fresa": {
                "nombre": "Bocaditos de fresa y crema",
                "precio": "20$",
                "desc": "Son pequeñas masas hojaldradas, rellenas con de crema y decoradas con fresas frescas y un toque de hierbas aromáticas.",
                "foto": 'AgACAgEAAxkBAAOEaibYxYzwuNPwnCa0BwM8SFYNr74AAm4MaxupYTlFLzIaV0axe8gBAAMCAAN5AAM7BA'
            },
            "galletas_fresa": {
                "nombre": "Sándwiches de galleta de fresa",
                "precio": "25$",
                "desc": "Estos bocaditos consisten en dos galletas de mantequilla en forma de corazón, unidas por un relleno de crema y coronadas con una fresa, con un espolvoreado final de azúcar glass.",
                "foto": 'AgACAgEAAxkBAAOGaibY-rqezYuFvUpBwKRVNqK441AAAm8MaxupYTlFS2XYeAQjAWIBAAMCAAN4AAM7BA'
            },
        }
    },
    "otros": {
        "titulo": "🍨🍓 Otros Postres",
        "descripcion": "Variedad de postres",
        "items": {
            "granola_fresa": {
                "nombre": "Parfait de Fresa y Granola",
                "precio": "5$",
                "desc": "Parfait de Fresa y Granola presentado en copa individual, que incluye capas alternas de fresas frescas, crema batida y una textura crujiente de granola.",
                "foto": 'AgACAgEAAxkBAAOIaibZous1Tqct1SlYMPP6QRDADDAAAnEMaxupYTlFbnlp0Sr8COwBAAMCAAN4AAM7BA'
            },
            "arte_florar":  {
                "nombre": "Arte Floral de Fresas ",
                "precio": "5$",
                "desc": "Las fresas han sido cortadas en láminas y dispuestas cuidadosamente para formar la apariencia de una rosa, decorado con hojas de menta fresca y pequeñas flores decorativas.",
                "foto": 'AgACAgEAAxkBAAOKaibZy2EENze3Rzz2jNBGsU2urB8AAnIMaxupYTlFhIO4517KaQwBAAMCAAN4AAM7BA'
            },
            "bizcocho_fresa": {
                "nombre": "Bizcocho de Fresa Glaseado",
                "precio": "6$",
                "desc": "Es una porción individual de pastel que consta de capas de bizcocho suave, un relleno cremoso, una cobertura glaseada y está coronado con fresas frescas y un jarabe de fresa.",
                "foto": 'AgACAgEAAxkBAAOMaibaDpDsHAjd43e3-6lpNt93tWQAAnMMaxupYTlFmqFN7p4iHeUBAAMCAAN4AAM7BA'
            },
            "soñado_fresa": {
                "nombre": "Choco-Fresa Soñado",
                "precio": "8$",
                "desc": "Esta porción individual consiste en capas de un intenso bizcocho de chocolate, alternadas con un relleno cremoso de chocolate y trozos de fresas frescas, cubierto con una capa de ganache de chocolate y decorado con virutas de chocolate y fresas naturales.",
                "foto": 'AgACAgEAAxkBAAOOaibaUn3iRm4R-FHWsIwT63bow0YAAnQMaxupYTlFSWdhOpIRJDYBAAMCAAN4AAM7BA'
            },
            "bocados_fresa": {
                "nombre": "Bocados de Amor",
                "precio": "1$",
                "desc": "Fresas frescas bañadas en chocolate y decoradas con líneas de contraste o granillos en forma de corazón.",
                "foto": 'AgACAgEAAxkBAAOQaibakTe61e0VZrRlVw9DwYz-d1cAAnYMaxupYTlFnDlavWzBMxIBAAMCAAN5AAM7BA'
            },
            "brownie_fresa": {
                "nombre": "Delicias de Fresa, Brownie y Crema",
                "precio": "5$",
                "desc": "Son postres en vaso que combinan capas de brownie, fresas frescas y crema, coronados con una fresa natural.",
                "foto": 'AgACAgEAAxkBAAOSaibawAHEoe_-uixPLNviR8mzvWcAAncMaxupYTlF-aMabEkITywBAAMCAAN4AAM7BA'
            },
        }
    }
}


def menu_categorias():
    markup = InlineKeyboardMarkup(row_width=1)
    for key, info in Catalogo.items():
        btn = InlineKeyboardButton(info["titulo"], callback_data=f"lista_{key}")
        markup.add(btn)
        
    markup.add(InlineKeyboardButton("⬅️ Volver al Inicio", callback_data='volver_inicio'))
    texto = "*🍓 Menú de productos 🍓*\n\nSelecciona una categoría:"
    return texto, markup


def generar_lista_productos(categoria):
    if categoria == "servicios":
        # Aquí se accede al diccionario dentro del archivo servicios.py
        datos = servicios.Servicios["servicios"] 
    else:
        # Aquí se accede al catálogo normal
        datos = Catalogo[categoria]
   
    markup = InlineKeyboardMarkup(row_width=1)
    
    for id_prod, info in datos["items"].items():
        texto_boton = info["nombre"] if isinstance(info, dict) else info
    
        markup.add(InlineKeyboardButton(texto_boton, callback_data=f"detalle_{categoria}_{id_prod}"))
    
    markup.add(InlineKeyboardButton("⬅️ Volver a Categorías", callback_data='ver_menu'))
    
    texto = f"🍓 *{datos['titulo']}*\n\n{datos['descripcion']}"
    return texto, markup