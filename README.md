# Projeto Final - Coder Turma 54375 Python

Projeto que visa a construção de um pipeline de dados que consiste em importar 3 bases de dados extraídas de um site com dados API, criar um alerta de sucesso ou falha na importação dessas bases, tratar cada uma individualmente, salvando seus dados para disponibilização e criar a documentação do projeto realizado.


### 📋 Pré-requisitos

Você precisa ter instalado:
* [PYTHON](https://www.python.org/downloads/release/python-3122/)
* Um editor de código-fonte da sua preferência (VSCode por exemplo)


## ⚙️ Executando

O projeto utiliza 3 URL's para analise, limpeza e tratamento dos dados:

1. [Feriados Nacionais](https://brasilapi.com.br/api/feriados/v1/2024) - lista dos feriados nacionais e suas datas no ano de 2024.
2. [PIX](https://brasilapi.com.br/api/pix/v1/participants) - lista cadastral das instituições que utilizam o PIX no Brasil.
3. [Corretoras de Investimento](https://brasilapi.com.br/api/cvm/corretoras/v1) - lista cadastral das instituições credenciadas para operar investimentos no Brasil.

#### Importação das API's
A importação das API's ocorrem via uma 'def' que tem por objetivo verificar o status da conexão da URL informada, e, em caso de sucesso, já salva o arquivo '.json' no uma variável informada no momento de rodar a 'def'. Na falha da conexão, ela não retorna nenhum dado. Em ambos casos um alerta é emitido, indicando o resultado da conexão. 

```
url_exemplo = 'https://www.exemplo.com.br/api'
df_exemplo = df_result_req(url_exemplo)
```

### 🔩 Analise da execução

#### Primeira API 
A primeira API utilizada é a de [Feriados Nacionais](https://brasilapi.com.br/api/feriados/v1/2024) para o ano de 2024. 

1. O DataFrame original contém 3 colunas 'date, name e type'.
2. Foi excluída a coluna 'type', visto que o DF se refere a feriados nacionais, e a coluna informava o tipo de feriado ('national' na informação).
3. Foram renomeadas as colunas
   - 'date' para 'Data';
   - 'name' para 'Feriado Nacional'.
4. A coluna 'Data' foi atualizada para formato 'datetime'.
5. Foi definida a coluna 'Feriado Nacional' como index.

O novo DataFrame com a base tratada foi inserida em uma nova variável, preservando os dados originais.

#### Segunda API 
A segunda API utilizada é a de Cadastro das Instituições que aderiram ao [PIX](https://brasilapi.com.br/api/pix/v1/participants) atualizada até a data da extração. 

1. O DataFrame original contém 6 colunas 'ispb, nome, nome_reduzido, modalidade_participacao, tipo_participacao e inicio_operacao'.
2. Foram renomeadas as colunas:
   - 'nome' para 'Razão Social';
   - 'nome_reduzido' para 'Nome';
   - 'ispb' para 'ISPB';
   - 'modalidade_participacao' para 'Modalidade';
   - 'tipo_participacao' para 'Tipo';
   - 'inicio_operacao' para 'Inicio da Operação'.
3. A coluna 'Inicio da Operação' foi atualizada para formato 'datetime'.
4. Foi definida a coluna 'ISPB' como index, por ser o Identificador de Sistema de Pagamentos Brasileiro (código único da instituição).

O novo DataFrame com a base tratada foi inserida em uma nova variável, preservando os dados originais.

#### Terceira API 
A terceira API utilizada é a de Cadastro das [Corretoras de Investimento](https://brasilapi.com.br/api/cvm/corretoras/v1) atualizada até a data da extração. 

1. O DataFrame original contém 19 colunas 'cnpj,type,nome_social,nome_comercial,status,email,telefone,cep,pais,uf,municipio,bairro,complemento,logradouro,data_patrimonio_liquido,valor_patrimonio_liquido,codigo_cvm,data_inicio_situacao,data_registro'.
2. Foram excluídas as colunas 'type' por conter o mesmo dado em todas ('Corretoras') e 'data_patrimonio_liquido' por ser um dado irrelevante e com datas sem atualização.
3. Foram renomeadas as colunas:
   - 'nome_social' para 'Razão Social';
   - 'nome_comercial' para 'Nome Comercial';
   - 'cnpj' para 'CNPJ';
   - 'status' para 'Status';
   - 'email' para 'E-Mail';
   - 'telefone' para 'Telefone';
   - 'cep' para 'CEP';
   - 'pais' para 'País';
   - 'uf' para 'UF';
   - 'municipio' para 'Município';
   - 'bairro' para 'Bairro';
   - 'logradouro' para 'Endereço';
   - 'complemento' para 'Complemento';
   - 'valor_patrimonio_liquido' para 'Valor PL';
   - 'codigo_cvm' para 'Cod. CVM';
   - 'data_registro' para 'Data Registro';
   - 'data_inicio_situacao' para 'Data Mudança Status'.
4. As colunas 'Data Registro' e 'Data Mudança Status' foram atualizadas para formato 'datetime'.
5. A coluna 'Valor PL' foi atualizada para o formato 'numeric'
6. Foi definida a coluna 'Cod. CVM' como index, por ser o código da instituição na Comissão de Valores Mobiliários.
7. A ordem das colunas foi alterada para: 'CNPJ','Razão Social','Nome Comercial','Data Registro','Valor PL','Telefone','E-Mail','Endereço','Complemento','Bairro','Município','UF','País','CEP','Status','Data Mudança Status'.
8. Os dados nulos das colunas 'Telefone', 'E-Mail','Nome Comercial' foram substituidos pela info 'Não Informado'.
9. Os dados nulos das colunas 'Endereço', 'Bairro', 'Município', 'UF', 'País', 'CEP', 'Complemento' foram substituidos pela info '-'.
10. Os dados nulos da coluna 'Valor PL' foram substituidos pela info '0,00'.

O novo DataFrame com a base tratada foi inserida em uma nova variável, preservando os dados originais.

## 🛠️ Construído com:

* [Visual Studio Code](https://code.visualstudio.com/)


## 📌 Versão

Nós usamos [GitHub](https://github.com/) para controle de versão. Para as versões disponíveis, observe [Git do Projeto](https://github.com/victorcanda22/ExercicioCoder). 

## ✒️ Autores

* **Victor Canda** - *Trabalho Inicial* - [Git do Victor](https://github.com/victorcanda22/)
* **Victor Canda** - *Documentação* - [Git do Victor](https://github.com/victorcanda22/)