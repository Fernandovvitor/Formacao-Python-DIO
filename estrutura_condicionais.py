def verificar_habilitacao():
    print("=== Sistema de Verificação de Condutores ===")
    
    try:
        idade = int(input("Digite a sua idade: "))
        
        if idade >= 18:
            print("✅ Você já tem idade para tirar a sua carteira de motorista!")
        elif idade == 17:
            print("⏳ Quase lá! Falta apenas 1 ano para você poder iniciar o processo.")
        else:
            falta = 18 - idade
            print(f"🚫 Você ainda não pode dirigir. Faltam {falta} anos para você ter idade legal.")
            
    except ValueError:
        print("❌ Erro: Por favor, digite um número inteiro válido para a idade.")

# Executa a função
verificar_habilitacao()