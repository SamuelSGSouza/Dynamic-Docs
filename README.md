# DynamicDoc Library

DynamicDoc é uma biblioteca Python que permite a manipulação dinâmica de documentos `.docx`, processando blocos condicionais e loops de maneira semelhante a templates. Esta biblioteca utiliza variáveis e expressões lógicas no documento, substituindo as tags encontradas com os valores fornecidos pelo usuário.

## Features

- **Substituição de variáveis**: Substitui as variáveis presentes no documento com os valores fornecidos.
- **Blocos condicionais**: Processa blocos `if`, `elif`, `else` no documento para incluir ou remover parágrafos de acordo com a condição.
- **Blocos de loop**: Suporte a blocos `for`, permitindo iterações sobre listas.
- **Suporte a formatação**: Formatação de variáveis substituídas com opções como negrito e itálico.

## Instalação

Para instalar as dependências da biblioteca, rode:

```bash
pip install python-docx