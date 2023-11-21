
# ConversorAFD
O ConversorAFD é uma ferramenta em Python desenvolvida para converter e formatar arquivos AFD (Arquivo-Fonte de Dados) de relógios pontos, adicionando cabeçalho e rodapé corretos para importação em sistemas como o Citrix Senior.

## Como Usar
O ConversorAFD foi desenvolvido na versão 3.9.8 de 64bits do Python. Que você pode baixar clicando nesse link [Python 3.9.8 x64](https://www.python.org/downloads/release/python-398/).

### Clone o Repositório:

```bash
git clone https://github.com/nxtsoul/ConversorAFD.git
cd ConversorAFD
```

Instalar bibliotecas Python:

```bash
pip install -r requirements.txt
```

Para rodar, utilize o **`cAFD.py`**:

```bash
python cAFD.py
```

Siga as instruções fornecidas na tela do app para inserir a razão social corretamente, CNPJ e número de registro do MTE do relógio ponto, além do caminho para o arquivo AFD sem cabeçalho e rodapé, clique em **Processar** e o app abrirá uma janela para salvar o arquivo no formato correto em que sistemas como Citrix Sênior possa reconhecer, claramente, caso não haja erros no processo.

### Compilar

Caso deseje utilizar em sua versão executável para Windows, o arquivo **`cAFD.spec`** está configurada para ser executada com o PyInstaller, caso deseje compilar, rode o seguinte comando na pasta do projeto.

```bash
pyinstaller cAFD.spec
```

Após o processo do pyinstaller o executável será disponibilizado na pasta `dist`.

Se tiver ideias e melhorias, chegue junto!!! 🙃🙃🙃
