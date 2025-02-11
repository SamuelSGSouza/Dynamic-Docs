# DynamicDoc Library
https://github.com/SamuelSGSouza/Dynamic-Docs
DynamicDoc é uma biblioteca Python que permite a manipulação dinâmica de documentos `.docx`, processando blocos condicionais e loops de maneira baseada no jinja2. Esta biblioteca utiliza variáveis e expressões lógicas no documento, substituindo as tags encontradas com os valores fornecidos pelo usuário. No repositório deste projeto, você encontrará um exemplo de uso da biblioteca, bem como um arquivo de exemplo para testes.

## Ferramentas Atuais

- **Substituição de variáveis**: Substitui as variáveis presentes no documento com os valores fornecidos.
- **Blocos condicionais**: Processa blocos `if`, ou remover parágrafos de acordo com a condição.

## Ferramentas Futuras 

- **Blocos de loop**: Suporte a blocos `for`, permitindo iterações sobre listas será adicionado em futuras versões.
- **Condicionais aninhados**: Suporte a condicionais aninhadas como if's dentro de if's será adicionado em futuras versões

## Instalação

Para instalar as dependências da biblioteca, rode:

```bash
pip install DynamicDoc==1.0.2
```

## Exemplo de Uso

```python
from DynamicDoc.dynamicdoc import DynamicDoc

doc = DynamicDoc("template.docx",nome = "João", idade = 20, maioridade = True)
doc.save_document("output.docx")
```

Caso deseje os bytes do documento, basta utilizar a seguinte sintaxe:

```python
from DynamicDoc.dynamicdoc import DynamicDoc

doc = DynamicDoc("template.docx",nome = "João", idade = 20, maioridade = True)
document_bytes = doc.get_document()
```


## Documentação

### Variáveis

Variáveis são definidas no documento com a seguinte sintaxe:

```
>#nome_da_variavel#<
```
As variáveis são substituídas pelos valores fornecidos no construtor da classe `DynamicDoc`. No exemplo acima, a variável `nome` será substituída por `João`.
As variáveis sofrerão uma safe_evaluation, ou seja, não é possível executar comandos maliciosos.


### Blocos Condicionais

Blocos condicionais sempre terão uma abertura e um fechamento. A sintaxe é a seguinte:

```
>#if NOMES#<
    *seu texto*
>#endif#<
```

No exemplo acima, o bloco será processado se a variável `NOMES` for verdadeira. Caso contrário, o bloco será removido do documento.

### Inline IF's

Caso deseje, você também pode inserir uma verificação condicional dentro do seu texto para que 
a verificação condicional funcione internamente no parágrafo. As informações do parágrafo irão compartilhar estilizações do documento original.

```

Lorem Ipsum is >#if dummy#< simply dummy >#endif#<text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

```

No exemplo acima, o bloco será processado se a variável `NOMES` for verdadeira. Caso contrário, o bloco será removido do documento.

## Contribuição

Para contribuir com a biblioteca, siga os passos abaixo:

1. Faça um fork do repositório
2. Crie uma branch com a feature que deseja adicionar (`git checkout -b feature/nova-feature`)
3. Commit as mudanças (`git commit -am 'Adicionando nova feature'`)
4. Faça um push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
```



