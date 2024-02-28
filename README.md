# Projeto Final - Coder Turma 54375 Python

Projeto que visa importar e tratar 3 bases de dados extraídas de um site com dados API.


### 📋 Pré-requisitos

Você precisa ter instalado:
* [PYTHON](https://www.python.org/downloads/release/python-3122/)
* Um editor de código-fonte da sua preferência (VSCode por exemplo)


## ⚙️ Executando

O projeto utiliza 3 URL's para analise, limpeza e tratamento dos dados.

Para testar a primeira etapa com uma nova URL que não sejam as já determinadas, é necessário informa-la na primeira etapa numa "variável_x", e depois criar um "df_x" utilizando a def "df_result_req" para criação desse df.

```
url_exemplo = "www.urlexemplo.com.br"
df_exemplo = df_result_req(url_exemplo)
```

### 🔩 Analise da execução

#### Primeira API 
A primeira API utilizada é a de [Feriados Nacionais](https://brasilapi.com.br/api/feriados/v1/2024) para o ano de 2024. 

O DataFrame original contém 3 colunas 'date, name e type'.
Na limpeza e tratamento dos dados:
    - Foi excluída a coluna 'type', visto que o DF se refere a feriados nacionais, e a coluna informava o tipo de feriado ('national' na informação).
    - Foram renomeadas as colunas
        * 'date' para 'Data';
        * 'name' para 'Feriado Nacional'.
    - A coluna 'Data' foi atualizada para formato 'datetime'.
    - Foi definida a coluna 'Feriado Nacional' como index.
O novo DataFrame com a base tratada foi inserida em uma nova variável, preservando os dados originais.

#### Segunda API 
A segunda API utilizada é a de Cadastro das Instituições que aderiram ao [PIX](https://brasilapi.com.br/api/pix/v1/participants) atualizada até a data da extração. 

O DataFrame original contém 6 colunas 'ispb, nome, nome_reduzido, modalidade_participacao, tipo_participacao e inicio_operacao'.

Na limpeza e tratamento dos dados:

    - Foram renomeadas as colunas

        * 'nome' para 'Razão Social';
        
        * 'nome_reduzido' para 'Nome';
        * 'ispb' para 'ISPB';
        * 'modalidade_participacao' para 'Modalidade';
        * 'tipo_participacao' para 'Tipo';
        * 'inicio_operacao' para 'Inicio da Operação'.
    - A coluna 'Inicio da Operação' foi atualizada para formato 'datetime'.
    - Foi definida a coluna 'ISPB' como index, por ser o Identificador de Sistema de Pagamentos Brasileiro (código único da instituição).
O novo DataFrame com a base tratada foi inserida em uma nova variável, preservando os dados originais.

## 🛠️ Construído com:

* [Visual Studio Code](https://code.visualstudio.com/)


## 📌 Versão

Nós usamos [GitHub](https://github.com/) para controle de versão. Para as versões disponíveis, observe [Git do Projeto](https://github.com/victorcanda22/ExercicioCoder). 

## ✒️ Autores

* **Victor Canda** - *Trabalho Inicial* - [Git do Victor](https://github.com/victorcanda22/)
* **Victor Canda** - *Documentação* - [Git do Victor](https://github.com/victorcanda22/)