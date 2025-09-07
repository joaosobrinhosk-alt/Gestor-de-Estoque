# Funções
from funcoes import inventario, linhas

# Lista
lista = []

while True:

    linhas()
    print("1: Adicionar/Remover")
    print("2: Atualizar Quantidades")
    print("3: Inventario")
    print("4: Buscar produto")
    print("5: Salvar em txt")
    print("6: Sair")
    linhas()

    try:
        escolha = int(input("Escolha alguma opção: "))
    except ValueError:
        print("❌ Digite apenas números válidos.")
        continue

    linhas()

    if escolha == 1:
        ar = str(input("Adicionar ou remover produto [A/R]: ")).upper()
        if ar == "A":
            produto = str(input("- Que produto deseja adicionar: "))
            quantidade = int(input("- Qual será a quantidade desejada: "))
            preco = float(input("- Preço do produto: "))
            
            dados = {
                "produto": produto,
                "quantidade": quantidade,
                "preço": preco,
                "total": quantidade * preco
            }
            lista.append(dados)

            linhas()

            print("✅ Produto adicionado com sucesso!")
        elif ar == "R":
            if not lista:
                print("❌ Nenhum produto para remover.")
            else:
                inventario(lista)
                try:
                    remover_produto = int(input("Pelo índice, qual produto quer remover: "))
                    if 0 <= remover_produto < len(lista):  
                        removido = lista.pop(remover_produto)
                        print(f"✅ Produto '{removido['produto']}' removido com sucesso.")
                    else:
                        print("❌ Esse índice não existe.")
                except ValueError:
                    print("❌ Entrada inválida.")
        else:
            print("❌ Opção inválida.")

    elif escolha == 2:
        if not lista:
            print("❌ Nenhum produto para atualizar.")
        else:
            inventario(lista)
            try:
                indice_quer_remover = int(input("Qual índice deseja atualizar: "))
                nova_quantidade = int(input("Atualize a quantidade: "))

                if 0 <= indice_quer_remover < len(lista):
                    lista[indice_quer_remover]["quantidade"] = nova_quantidade
                    lista[indice_quer_remover]["total"] = nova_quantidade * lista[indice_quer_remover]["preço"]
                    print("✅ Produto atualizado:", lista[indice_quer_remover])
                else:
                    print("❌ Índice inválido.")
            except ValueError:
                print("❌ Entrada inválida.")

    elif escolha == 3:
        if not lista:
            print("📭 Ainda não existe nenhum produto na lista.")    
        else:
            inventario(lista)

    elif escolha == 4:
        if not lista:
            print("❌ A lista está vazia, não há nada para buscar.")
        else:
            buscar_produto = str(input("Buscar produto: ")).lower()
            encontrado = False
            for item in lista:
                if buscar_produto in item["produto"].lower():
                    print(f"✅ Produto encontrado: {item}")
                    encontrado = True
            if not encontrado:
                print("❌ Produto não encontrado...")

    elif escolha == 5:
        if not lista:
            print("❌ Nenhum produto para salvar.")
        else:
            with open("inventario.txt", "w", encoding="utf-8") as arquivo:
                for item in lista:
                    arquivo.write(f"{item['produto']} - Qtd: {item['quantidade']} - Preço: R${item['preço']:.2f} - Total: R${item['total']:.2f}\n")
            print("💾 Inventário salvo em 'inventario.txt'.")

    elif escolha == 6:
        print("👋 Fechando sistema... até logo!")
        break

    else:
        print("❌ Opção inválida, tente novamente.")

        
