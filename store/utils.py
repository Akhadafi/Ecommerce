import json

from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES["cart"])
    except:
        cart = {}

    print("Cart:", cart)
    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0}
    cartItems = order["get_cart_items"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=1)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_items"] += cart[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageURL": product.imageURL,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)

            if product.digital == False:
                order["shipping"] = True
        except:
            pass
    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "shipping": False,
    }
    return {"cartItems": cartItems, "order": order, "items": items}
