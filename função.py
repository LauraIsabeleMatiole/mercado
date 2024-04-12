def login()
  usuario = input('digite seu usuario: ')        

  senha = input('digite sua senha: ')

if (usuario == usuariologado['usuario1'] and senha == senhalogado['senha1']) or (usuario == usuariologado['usuario2'] and senha == senhalogado['senha2']):
    usuariologado = usuario
    senhalogado = senha
    dinheiro = float(input("Digite a quantidade de dinheiro disponivel:"))
    print(" -------- Caixa inicializado -------- ")
else:
    print("⚠ Seu usuário ou senha estão errados")