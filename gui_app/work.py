import flet as ft

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Сумма закупок"
    
    def update_app_bar():
        app_bar.actions.clear()
        app_bar.actions.append(ft.Text(f"Баланс: {balance.value} ", size=18, color=ft.colors.WHITE))
        page.update()
    
    def button_click(event):
        balance.value = input_field.value
        print(balance.value)
        input_field.value = ""
        page.remove(input_container)
        page.add(app_bar)
        page.add(shop_container)
        page.update()
        update_app_bar()
        
    balance = ft.Text(
        value=0,
        size=20,
        color=ft.colors.GREEN_700)
            
    input_field = ft.TextField(
        width=450, label="Введите сумму баланса",
        hint_text="Введите сумму баланса",
        border_color=ft.colors.BLUE_600,
        text_style=ft.TextStyle(size=14, color=ft.colors.BLACK87)
    )
    
    submit_btn = ft.ElevatedButton(
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        text="Пополнить баланс",
        on_click=button_click,
    )
    
    input_container = ft.Container(
        content = ft.Column(
            [
                input_field,
                submit_btn,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=40,
    )
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.add(input_container)
    
    products = [
        {"name": "Продукт 1", "price": 100, "count": 1},
        {"name": "Продукт 2", "price": 200, "count": 2},
        {"name": "Продукт 3", "price": 300, "count": 3},
    ]
    
    def create_product_card(name, price, count):
        def buy_product(event):
            total_price = price * count
            current_balance = float(balance.value)
            if current_balance >= total_price:
                balance.value = str(current_balance - total_price)
                update_app_bar()
                ft.toast(f"Purchased {name} for {total_price}")
            else:
                ft.toast(f"Not enough balance to purchase {name}")

        return ft.Card(
            content=ft.Column(
                [
                    ft.Text(value=name, size=20, color=ft.colors.BLACK),
                    ft.Text(value=f"Цена: {price}", size=16, color=ft.colors.BLACK),
                    ft.Text(value=f"Кол-во: {count}", size=16, color=ft.colors.BLACK),
                    ft.ElevatedButton(text="Купить", on_click=buy_product)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            width=300,
            height=250,
        )
    
    
    app_bar = ft.AppBar(
        title=ft.Text("Store", size=20, color=ft.colors.WHITE),
        actions=[
            ft.Text(f"Balance: {balance.value} ", size=18, color=ft.colors.WHITE)
        ],
        bgcolor=ft.colors.BLACK,
    )
    
    product_cards = [create_product_card(p["name"], p["price"], p["count"]) for p in products]
    
    shop_container = ft.Container(
        content = ft.Row(
            product_cards,
            alignment=ft.MainAxisAlignment.CENTER,

        ),
        padding=40,
    )
    

    page.add()


ft.app(target=main)



# Реализуйте подсчет суммы закупок.У вас в приложения в виде списка отображаются продукты,
# цена и их количество. Пользователь вводит количество баланса на своем счету и выбирает продукты и их количество.
# Дайте понять если ему хватит финансов на закупки или нет  