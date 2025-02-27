import flet as ft

from .interface_view import InterfaceView

class LoginUserView(InterfaceView):

    def __init__(self, page: ft.Page) -> None:
        self.lista_animacao = ft.Image(src=r"src/views/assets/logo_projeto_regras.png", width=200, height=200)
        self.texto_login = ft.Text(value="Login de usuário", size=20, font_family= "Nimbus Mono PS", text_align=ft.TextAlign.CENTER)
        self.entrada_nome = ft.TextField(hint_text="Insira o nome de usuário", width=300, text_align=ft.TextAlign.CENTER, border_color="#50c77a")
        self.entrada_senha = ft.TextField(hint_text="Insira sua senha",password=True, width=300, text_align=ft.TextAlign.CENTER, border_color="#50c77a")
        self.botao_entrar = ft.Button(text="Entrar", width=150, color="#101413", bgcolor="#50c77a")
        self.botao_esqueceu_senha = ft.TextButton(text="Esqueci minha senha", style=ft.ButtonStyle("#50c77a"))
        self.botao_criar_conta = ft.TextButton(text="Criar uma conta nova", style=ft.ButtonStyle("#50c77a"), on_click=lambda e: login_for_create_cont_constructor(page))


    def build(self) -> ft.Row:
        return ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[
                        ft.Container(
                            ft.Column(
                                controls=[
                                    self.lista_animacao,
                                    self.texto_login   
                                ],
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER
                            )
                        ),
                        
                        ft.Container(
                            ft.Column(
                                expand=True,
                                spacing=15,
                                controls=[
                                    self.entrada_nome,
                                    self.entrada_senha
                                ]
                            ),                 
                        ),

                        ft.Container(
                            ft.Row(
                                spacing=10,
                                controls=[
                                    self.botao_entrar,
                                    self.botao_esqueceu_senha    
                                ]
                            )           
                        ),

                        ft.Container(
                            ft.Row(
                                controls=[
                                    self.botao_criar_conta 
                                ]
                            ),
                            height=200               
                        )
                    ]
                )
            ],        
        )

from src.main.constructor.login_user_constructor import login_for_create_cont_constructor