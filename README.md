# aps-quinto
Repositório Base da APS do quinto semestre. 

# Links úteis para o uso do Github
Como adicionar arquivos à um repositório
https://docs.github.com/pt/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line

Clonando um repositório (Após uma mudança feita por outra pessoa)
https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

# Básico
1. Caso tenha alguma atualização que alguém fez, pegar os arquivos novos
        git pull https://github.com/DanielH556/aps-quinto.git
2. Após o comando pull, fazer as mudanças necessárias nos arquivos
        Por exemplo, um arquivo que você tem vai receber linhas novas ou retirar linhas anteriores. 
        Use o comando
          git fetch https://github.com/DanielH556/aps-quinto.git
        Seguido de
          git merge origin/master
3. Checar se os arquivos estão nos conformes (mudanças feitas, etc)
4. Ao finalizar seu trabalho, enviar os arquivos (dar commit) para o repositório no github (seguir o passo a passo do link).

# Como rodar o FTP
1. Executar o arquivo "ftpserver.py" junto com o arquivo "server.py"
2. Envio do arquivo -> escolher o arquivo após clicar no botão " + "
        Quando aparecer a mensagem "Arquivo enviado" no chat, o envio do arquivo ao servidor ftp está completo.
3. Recepção do arquivo -> Para receber o arquivo, digite "receber_arquivo" no chat. Esta é a mensagem chave pra executar a função de recebimento de arquivo

**Observações:** O arquivo gerado na pasta "server_data" do cliente que enviou o arquivo é uma réplica do original. Já no cliente que recebe, o arquivo é baixado na pasta geral (ainda não consegui mexer nisso, estava muito eufórico pra poder arrumar isso). Mas a ideia primordial do programa está pronta de certa forma.
        Os testes foram feitos apenas com arquivos .mp3, ainda é necessário testar com arquivos .mp4 (embora eu acredite que funcione da mesma forma - mas vai saber (。﹏。*))

### Quaisquer dúvidas, entrar em contato comigo (Daniel)