from django.urls import path
from . import views

urlpatterns = [
    # Rotas Objeto Perdido
    path("inserir_objeto", views.inserir_objeto, name="inserir_objeto"),
    path("atualizar_objeto", views.atualizar_objeto, name="atualizar_objeto"),
    path("deletar_objeto/<int:id_objeto>", views.deletar_objeto, name="deletar_objeto"),
    path("listar_objetos", views.listar_objetos, name="listar_objetos"),
    path("listar_objeto/<int:id_objeto>", views.listar_objeto, name="listar_objeto"),
    # Rotas Objeto Achado
    path("inserir_objetoA", views.inserir_objetoA, name="inserir_objetoA"),
    path("atualizar_objetoA", views.atualizar_objetoA, name="atualizar_objetoA"),
    path(
        "deletar_objetoA/<int:id_objetoA>",
        views.deletar_objetoA,
        name="deletar_objetoA",
    ),
    path("listar_objetosA", views.listar_objetosA, name="listar_objetosA"),
    path(
        "listar_objetoA/<int:id_objetoA>", views.listar_objetoA, name="listar_objetoA"
    ),
]
