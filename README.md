# DynamicDoc Library
https://github.com/SamuelSGSouza/Dynamic-Docs
DynamicDoc é uma biblioteca Python que permite a manipulação dinâmica de documentos `.docx`, processando blocos condicionais e loops de maneira semelhante a templates. Esta biblioteca utiliza variáveis e expressões lógicas no documento, substituindo as tags encontradas com os valores fornecidos pelo usuário. No repositório deste projeto, você encontrará um exemplo de uso da biblioteca, bem como um arquivo de exemplo para testes.

## Ferramentas Atuais

- **Substituição de variáveis**: Substitui as variáveis presentes no documento com os valores fornecidos.
- **Blocos condicionais**: Processa blocos `if`, ou remover parágrafos de acordo com a condição.
- **Suporte a formatação**: Formatação de variáveis substituídas com opções como negrito e itálico.

## Ferramentas Futuras 

- **Blocos de loop**: Suporte a blocos `for`, permitindo iterações sobre listas será adicionado em futuras versões.
- **Condicionais aninhados**: Suporte a condicionais adicionais como `elif` e `else` serão adicionadas em futuras versões.

## Instalação

Para instalar as dependências da biblioteca, rode:

```bash
pip install DynamicDocs==0.1.0
```

## Exemplo de Uso

```python
from dynamicdoc import DynamicDoc

doc = DynamicDoc("template.docx",nome = "João", idade = 20, maioridade = True)
doc.save("output.docx")
```

## Documentação

### Variáveis

Variáveis são definidas no documento com a seguinte sintaxe:

```
>>nome_da_variavel<<
```
As variáveis são substituídas pelos valores fornecidos no construtor da classe `DynamicDoc`. No exemplo acima, a variável `nome` será substituída por `João`.
As variáveis sofrerão uma safe_evaluation, ou seja, não é possível executar comandos maliciosos.

### Ferramentas de Formatação

Atualmente, variáveis podem ser editadas com negrito e itálico. A sintaxe é a seguinte:

```
>>ENDERECO<<(N,I)
```

Onde `N` é negrito e `I` é itálico. No exemplo acima, a variável `ENDERECO` será substituída com a formatação de negrito e itálico.

### Blocos Condicionais

Blocos condicionais sempre terão uma abertura e um fechamento. A sintaxe é a seguinte:

```
>>if NOMES<<
    *seu texto*
>>endif<<
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




