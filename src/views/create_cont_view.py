import flet as ft

from .interface_view import InterfaceView

class CreateContView(InterfaceView):

    def __init__(self, page: ft.Page) -> None:
        self.texto = ft.Text(value="Vamos criar uma nova conta", size=20, font_family= "Nimbus Mono PS", text_align=ft.TextAlign.CENTER)
        self.entarda_nome = ft.TextField(hint_text="Nome de usuário", width=300, text_align=ft.TextAlign.CENTER, border_color="#50c77a")
        self.entrada_senha = ft.TextField(hint_text="Crie uma senha", width=300, text_align=ft.TextAlign.CENTER, border_color="#50c77a")
        self.confirmacao_senha = ft.TextField(hint_text="Confirme a senha", width=300, text_align=ft.TextAlign.CENTER, border_color="#50c77a")
        self.entrada_email = ft.TextField(hint_text="Vincule um Email a conta", width=300, text_align=ft.TextAlign.CENTER, border_color="#50c77a")
        self.botao_criar_conta = ft.Button(text="Criar conta", width=150, color="#101413", bgcolor="#50c77a")
        self.botao_voltar_loggin = ft.TextButton(text="Voltar", style=ft.ButtonStyle("#50c77a"), on_click=lambda e: create_cont_for_login(page))

    def build(self) -> ft.Row:
        return ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[

                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    controls=[

                        ft.Container(
                            ft.Column(
                                controls=[
                                   self.texto 
                                ],
                                height=100
                            )                          
                        ),

                        ft.Container(
                            ft.Column(
                                controls=[
                                    self.entarda_nome,
                                    self.entrada_senha,
                                    self.confirmacao_senha,
                                    self.entrada_email,
                                ]
                            )
                            
                        ),

                        ft.Container(
                            ft.Row(
                                controls=[
                                    self.botao_criar_conta,
                                    self.botao_voltar_loggin    
                                ],
                                height=50
                            )
                            
                        )


                    ]
                )
            ]
        )
    
from src.main.constructor.create_cont_constructor import create_cont_for_login