import flet as ft

from .interface_view import InterfaceView

class HouseRulesView(InterfaceView):

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.botao_Regras = ft.TextButton(text="REGRAS DA CASA", style=ft.ButtonStyle("#ffffff"))
        self.botao_tarefas = ft.TextButton(text="LISTA DE TAREFAS", style=ft.ButtonStyle("#ffffff"))
        self.texto_nome = ft.Text(value="Nome de usuário")
        self.icone_perfil = ft.IconButton(icon=ft.icons.PERSON)
        self.texto_descricao = ft.Text(value="Adicione tudo oque pretende fazer frequentemente", size=20)
        self.icone_adicionar = ft.ElevatedButton(icon=ft.icons.ADD, text="Adionar regra")

    def build(self) -> ft.Row:
        return ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,

            controls=[

                ft.Column(
                    expand=True,
                    controls=[

                        ft.Container(
                            ft.Row(
                                controls=[
                                    self.botao_Regras,
                                    self.botao_tarefas,

                                    ft.Container(
                                        ft.Row(
                                            controls=[
                                                self.texto_nome,
                                                self.icone_perfil   
                                            ]
                                        )
                                    )

                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                expand=True
                            ),
                            bgcolor="#0f452b",
                        ),

                        ft.Container(

                            ft.Column(
                                expand=True,
                                controls=[

                                    ft.Container(
                                        self.texto_descricao
                                    ),

                                    ft.Container(
                                        
                                        ft.Column(
                                            controls=[

                                            ]
                                        )
                                    ),

                                    ft.Container(
                                       
                                        ft.Row(
                                            controls=[

                                               ft.Container(
                                                   
                                                   ft.Column(
                                                       controls=[
                                                          self.icone_adicionar 
                                                       ],
                                                       expand=True,
                                                       alignment=ft.MainAxisAlignment.END
                                                   )
                                               )
                                            ],
                                            expand=True,
                                            alignment=ft.MainAxisAlignment.END
                                        ),
                                        expand=True,
                                        
                                        
                                    )
                                         
                                ]
                                 
                            ),
                            expand=True
                            
                        )
                        
                    ]
                    
                )
            ]
        )
