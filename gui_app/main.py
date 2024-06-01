import flet as ft

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    #page.bgcolor = ft.colors.WHITE
    
    image_list = [
        "https://via.placeholder.com/600x400?text=Image+1",
        "https://via.placeholder.com/600x400?text=Image+2",
        "https://via.placeholder.com/600x400?text=Image+3",
    ]
    
    current_image_index = 0
    
    def update_image():
        image_display.src = image_list[current_image_index]
        page.update()
        
    def handle_prev(event):
        print("Previous button clicked")
        nonlocal current_image_index
        current_image_index = (current_image_index - 1) % len(image_list)
        update_image()
    
    def handle_next(event):
        print("Next button clicked")
        nonlocal current_image_index
        current_image_index = (current_image_index + 1) % len(image_list)
        update_image()
        
    image_display = ft.Image(
        src=image_list[current_image_index],
        width=600,
        height=400,
    )
    
    prev_btn = ft.ElevatedButton(text="Previous", on_click=handle_prev)
    next_btn = ft.ElevatedButton(text="Next", on_click=handle_next)
    
    
    page.add(ft.Column(
        [
            image_display,
            ft.Row(
                    [
                        prev_btn,
                        next_btn
                    ],
            
                    alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30
    ))
    
    
    
    def button_click(event):
        output_text.value = input_field.value
        input_field.value = ""
        page.update()
        
    input_field = ft.TextField(
        width=450, label="Введите",
        hint_text="Введите текст",
        border_color=ft.colors.BLUE_600,
        text_style=ft.TextStyle(size=14, color=ft.colors.BLACK87)
    )
    
    output_text = ft.Text(
        value="",
        style="heandleMedium",
        color=ft.colors.GREEN_700)
    
    submit_btn = ft.ElevatedButton(
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        text="Нажать",
        on_click=button_click,
        style= ft.ButtonStyle(side=ft.BorderSide(color=ft.colors.RED, width=3))
    )
    
    container = ft.Container(
        content = ft.Column(
            [
                input_field,
                output_text,
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
    
    page.add(container)
    

ft.app(target=main)