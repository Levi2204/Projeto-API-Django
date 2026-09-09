import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ObjetoPerdido, ObjetoAchado

# --- Rotas Objeto Perdido ---


@csrf_exempt
@require_http_methods(["POST"])
def inserir_objeto(request):
    try:
        dados = json.loads(request.body)
        nome_objeto = dados.get("nome_objeto")
        cor = dados.get("cor")
        data_perdido = dados.get("data_perdido")

        if not nome_objeto or not cor or not data_perdido:
            return JsonResponse({"mensagem": "Dados incompletos"}, status=400)

        ObjetoPerdido.objects.create(
            nome_objeto=nome_objeto, cor=cor, data_perdido=data_perdido
        )
        return JsonResponse({"mensagem": "Objeto inserido com sucesso"})
    except Exception as e:
        return JsonResponse(
            {"mensagem": "Erro ao inserir o objeto", "erro": str(e)}, status=500
        )


@csrf_exempt
@require_http_methods(["PUT"])
def atualizar_objeto(request):
    try:
        dados = json.loads(request.body)
        id_objeto = dados.get("id_objeto")
        nome_objeto = dados.get("nome_objeto")
        cor = dados.get("cor")
        data_perdido = dados.get("data_perdido")

        if not id_objeto:
            return JsonResponse({"mensagem": "ID do objeto não fornecido"}, status=400)

        obj = ObjetoPerdido.objects.filter(id_objeto=id_objeto).first()
        if obj:
            obj.nome_objeto = nome_objeto
            obj.cor = cor
            obj.data_perdido = data_perdido
            obj.save()
            return JsonResponse({"mensagem": "Objeto atualizado com sucesso"})
        else:
            return JsonResponse({"mensagem": "Objeto não encontrado"}, status=404)
    except Exception as e:
        return JsonResponse(
            {"mensagem": "Erro ao atualizar o objeto", "erro": str(e)}, status=500
        )


@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_objeto(request, id_objeto):
    try:
        obj = ObjetoPerdido.objects.filter(id_objeto=id_objeto).first()
        if obj:
            obj.delete()
            return JsonResponse({"mensagem": "Objeto deletado com sucesso"})
        else:
            return JsonResponse(
                {"mensagem": "Erro ao deletar o objeto (não encontrado)"}, status=404
            )
    except Exception as e:
        return JsonResponse(
            {"mensagem": "Erro ao deletar o objeto", "erro": str(e)}, status=500
        )


@require_http_methods(["GET"])
def listar_objetos(request):
    objetos = ObjetoPerdido.objects.all().order_by("id_objeto")
    if not objetos.exists():
        return JsonResponse([], safe=False)

    dados = [
        {
            "id_objeto": obj.id_objeto,
            "nome_objeto": obj.nome_objeto,
            "cor": obj.cor,
            "data_perdido": obj.data_perdido,
        }
        for obj in objetos
    ]
    return JsonResponse(dados, safe=False)


@require_http_methods(["GET"])
def listar_objeto(request, id_objeto):
    obj = ObjetoPerdido.objects.filter(id_objeto=id_objeto).first()
    if obj:
        objeto_dict = {
            "id_objeto": obj.id_objeto,
            "nome_objeto": obj.nome_objeto,
            "cor": obj.cor,
            "data_perdido": obj.data_perdido,
        }
        return JsonResponse({"Objeto-perdido": objeto_dict})
    else:
        return JsonResponse({"mensagem": "Objeto não encontrado"}, status=404)


# --- Rotas Objeto Achado ---


@csrf_exempt
@require_http_methods(["POST"])
def inserir_objetoA(request):
    try:
        dados = json.loads(request.body)
        id_objeto = dados.get("id_objeto")
        nome_pessoa = dados.get("nome_pessoa")
        cpf = dados.get("cpf")
        contato = dados.get("contato")

        if not id_objeto or not nome_pessoa or not cpf or not contato:
            return JsonResponse(
                {"mensagem": "Todos os campos são obrigatórios"}, status=400
            )

        # Procura o objeto perdido para preencher os dados
        obj_perdido = ObjetoPerdido.objects.filter(id_objeto=id_objeto).first()
        if not obj_perdido:
            return JsonResponse(
                {"mensagem": "Objeto perdido não encontrado"}, status=404
            )

        ObjetoAchado.objects.create(
            nome_objeto_achado=obj_perdido.nome_objeto,
            cor_achado=obj_perdido.cor,
            nome_pessoa=nome_pessoa,
            cpf=cpf,
            contato=contato,
        )
        return JsonResponse({"mensagem": "Objeto achado inserido com sucesso!"})
    except Exception as e:
        return JsonResponse(
            {"mensagem": "Erro ao inserir o objeto achado", "erro": str(e)}, status=500
        )


@csrf_exempt
@require_http_methods(["PUT"])
def atualizar_objetoA(request):
    try:
        dados = json.loads(request.body)
        id_objeto = dados.get("id_objeto")
        nome_objeto_achado = dados.get("nome_objeto")
        cor_achado = dados.get("cor")
        nome_pessoa = dados.get("nome_pessoa")
        cpf = dados.get("cpf")
        contato = dados.get("contato")

        if (
            not id_objeto
            or not nome_objeto_achado
            or not cor_achado
            or not nome_pessoa
            or not cpf
            or not contato
        ):
            return JsonResponse(
                {"mensagem": "Todos os campos são obrigatórios"}, status=400
            )

        obj = ObjetoAchado.objects.filter(id_objetoA=id_objeto).first()
        if obj:
            obj.nome_objeto_achado = nome_objeto_achado
            obj.cor_achado = cor_achado
            obj.nome_pessoa = nome_pessoa
            obj.cpf = cpf
            obj.contato = contato
            obj.save()
            return JsonResponse({"mensagem": "Objeto atualizado com sucesso!"})
        else:
            return JsonResponse({"mensagem": "Objeto não encontrado"}, status=404)
    except Exception as e:
        return JsonResponse(
            {"mensagem": "Erro ao atualizar o objeto", "erro": str(e)}, status=500
        )


@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_objetoA(request, id_objetoA):
    try:
        obj = ObjetoAchado.objects.filter(id_objetoA=id_objetoA).first()
        if obj:
            obj.delete()
            return JsonResponse({"mensagem": "Objeto deletado com sucesso"}, status=200)
        else:
            return JsonResponse({"mensagem": "Objeto não encontrado"}, status=404)
    except Exception as e:
        return JsonResponse(
            {"mensagem": "Erro ao tentar deletar o objeto", "erro": str(e)}, status=500
        )


@require_http_methods(["GET"])
def listar_objetosA(request):
    objetos = ObjetoAchado.objects.all().order_by("id_objetoA")
    if not objetos.exists():
        return JsonResponse({"mensagem": "Nenhum objeto encontrado"}, status=404)

    dados = [
        {
            "id_objetoA": obj.id_objetoA,
            "nome_objeto_achado": obj.nome_objeto_achado,
            "cor_achado": obj.cor_achado,
            "nome_pessoa": obj.nome_pessoa,
            "cpf": obj.cpf,
            "contato": obj.contato,
        }
        for obj in objetos
    ]
    return JsonResponse(dados, safe=False)


@require_http_methods(["GET"])
def listar_objetoA(request, id_objetoA):
    obj = ObjetoAchado.objects.filter(id_objetoA=id_objetoA).first()
    if obj:
        objeto_dict = {
            "id_objetoA": obj.id_objetoA,
            "nome_objeto_achado": obj.nome_objeto_achado,
            "cor_achado": obj.cor_achado,
            "nome_pessoa": obj.nome_pessoa,
            "cpf": obj.cpf,
            "contato": obj.contato,
        }
        return JsonResponse({"Objeto-perdido": objeto_dict})
    else:
        return JsonResponse({"mensagem": "Objeto não encontrado"}, status=404)
