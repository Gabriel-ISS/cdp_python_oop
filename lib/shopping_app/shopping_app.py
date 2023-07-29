from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Mother board", 28980, seller)
    Item("Power supply unit", 8980, seller)
    Item("PC case", 8727, seller)
    Item("3.5inch HDD", 10980, seller)
    Item("2.5inch SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU Cooler", 13400, seller)
    Item("Graphic board", 23800, seller)

print("🤖 Dime tu nombre")
customer = Customer(input())

print("🏧 Introduce el importe para recargar tu monedero")
customer.wallet.deposit(int(input()))

print("🛍️ Empezar a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor ingrese el numero de producto")
    number = int(input())

    print("⛏ Ingrese la cantidad a comprar")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Cantidad a pagar: {customer.cart.total_amount()}")

    print("😭 Quieres finalizar la compra？(si/no)")
    end_shopping = input() == "si"

print("💸 Confirmar compra? (si/no)")
if input() == "si":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈結果┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ {customer.name} es propietario de:")
customer.show_items()
print(f"😱👛 El balance de {customer.name} es: {customer.wallet.balance}")

print(f"📦 {seller.name} tiene disponible:")
seller.show_items()
print(f"😻👛 El balance de {seller.name} es: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Monto total: {customer.cart.total_amount()}")

print("🎉 Finalizado")
