def construir_fnd(formula, proposicoes):
    n = len(proposicoes)
    tabela = []
    
    for i in range(2 ** n):
        linha = []
        for j in range(n):
            linha.append((i >> (n - j - 1)) & 1) 
        tabela.append(linha)
    
    linhas_verdadeiras = []
    for linha in tabela:
        valores = {proposicoes[k]: bool(linha[k]) for k in range(n)}
        if avalia_formula(formula, valores): 
            linhas_verdadeiras.append(linha)
    
    termos = []
    for linha in linhas_verdadeiras:
        conjuncao = []
        for k in range(n):
            if linha[k]: 
                conjuncao.append(proposicoes[k])
            else:  
                conjuncao.append(f"¬{proposicoes[k]}")
        termos.append(" ∧ ".join(conjuncao))
    
    fnd = " ∨ ".join(termos)
    
    return fnd

proposicoes = ["P", "Q"]
formula = "(P → Q) ∨ ¬P"
fnd = construir_fnd(formula, proposicoes)
print("FND:", fnd)
