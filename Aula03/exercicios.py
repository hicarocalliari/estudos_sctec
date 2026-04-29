### 01
nome = "mARIA da silVA sOUZA"
print ( nome.title())

### 02

senha_digitada = "Python2024"
senha_armazenada = "python2024"

if ( senha_armazenada.upper() == senha_digitada.upper()):
    print ("Senhas Iguais, acesso autorizado")
else:
    print ("Senha incorreta !")

### 03

mensagem = "ERRO CRÍTICO NO SERVIDOR"
mensagem = mensagem.swapcase()
print (mensagem)

### 04

email = "usuario@empresa.com."

if "@" in email and email.endswith((".com",".com.br")):
    print (f"Email Correto")
else:
    print (f"Email incorreto !")

### 05

log = "ERROR: conexão recusada. Tentativa 1 ErROR. Tentativa 2 ERROR."
log = log.upper()
print (f"A quantidade de vezes que apareceu erro foi de: {log.count("ERROR")}")

### 06

caminho = "/home/usuario/documentos/relatorio_final.pdf"
print (caminho[caminho.rfind("/") + 1:])

### 07

cpf = "123.456.789-00"
print ( cpf.replace(".","").replace("-",""))

### 08
nome = "   João Silva   "
print (nome.lstrip().rstrip())

### 9

numero_pedido = "4521"

print (numero_pedido.zfill(8))