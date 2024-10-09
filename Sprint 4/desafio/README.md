## Instruções 

### Etapa 1: 

1 - Fiz o download do código escrito em python chamado "carguru.py"

2 - Em seguida, criei um arquivo Dockerfile para definir como a imagem deve ser construída, detalhando o passo a passo do processo.

3 - No Dockerfile, utilizei o comando:

`from python`

`workdir /app`

`copy carguru.py .`

`cmd ["python", "carguru.py"]`

3.1 - O comando `from` para indicar que a imagem base para a construção do Docker é uma imagem do Python.

3.2 - O comando `workdir` para definir o diretório de trabalho dentro da imagem Docker.

3.3 - O comando `copy`  para copiar o arquivo "carguru.py" para o diretório atual.

3.4 - O comando `cmd` para especificar o comando que deverá ser executado quando o container for iniciado a partir da imagem. Neste caso, ele executará o interpretador Python e passará o "carguru.py" como argumento.

4 - Em seguida, ultilizei o comando `docker build -t carguru` para criar a imagem Docker com o nome "carguru"

5 - E por fim, utilizei o comando `docker run carguru`para executar o coitêiner. 

### Etapa 2: 

Sim, é possível reutilizar coitêiners. O comando `docker start <nome_ou_id_do_conteiner>` reeutiliza um coitêiner que está parado.

No desafio, ao executar o comando `docker run carguru`, o sistema informava de forma aleatória qual carro você deveria dirigir e, em seguida, encerrava o programa. Para reutilizar o contêiner sem precisar criar um novo, utilizei o comando `docker start`, o que reiniciou o contêiner e gerou uma nova saída. Para verificar as saídas anteriores e confirmar a reutilização do contêiner, utilizei o comando `docker logs`, que exibe o histórico de saídas dos contêineres.

### Etapa 3:

1 - Criação de um script Python, chamado "print_hash" cujo o objetivo era gerar e exibir o hash SHA-1 de qualquer mensagem fornecida pelo o usuário até que o programa seja encerrado. 

2- Em seguida, criei um arquivo Dockerfile para definir como a imagem deve ser construída, detalhando o passo a passo do processo.

3 - No Dockerfile, utilizei o comando:

`from python`

`workdir /app`

`copy print_hash.py .`

`cmd ["python", "print_hash.py"]`

4 - Em seguida, ultilizei o comando `docker build -t mascarar-dados` para criar a imagem Docker com o nome "mascarar-dados"

5 - E por fim, utilizei o comando `docker run -it mascarar-dados` para executar o coitêiner. 



