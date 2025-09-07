def inventario(lista):
    print("\n📦 INVENTÁRIO 📦")
    print("Índice | Produto         | Quantidade | Preço     | Total")
    print("-" * 55)
    for c in range(len(lista)):
        print(f"{c+1:<6} | {lista[c]['produto']:<14} | {lista[c]['quantidade']:<10} | R$ {lista[c]['preço']:<7.2f} | R$ {lista[c]['total']:<7.2f}")
    print()

def linhas():
    print("-=" * 30)