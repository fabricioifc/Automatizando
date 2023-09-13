# Rotina para Copiar Imagens

Este é uma simples rotina para percorrer uma pasta com imagens TIFF RGB e copiar as imagens que possuem pelo menos 50% de pixels pretos para outra pasta "output".

## Como usar

Como o python instalado, faça:

1. Criando o ambiente virtual

```python
python -m venv .venv
```

2. Ativando o ambiente virtual

```python
# No Windows
.venv\Scripts\activate

# No Linux
source .venv/bin/activate
```

3. Instalando as dependências

```python
pip install -r requirements.txt
```

4. Executando o script

```python
python main.py --label_dir='/home/fabricio/Mauren/EXTRACTION/SLICES/'
```

## Parâmetros

- `--label_dir`: Diretório com as imagens TIFF RGB
- `--color`: Cor do pixel que será considerado para copiar ou não a imagem. Padrão: (0, 0, 0)

## Resultado

As imagens que possuem menos que 50% de pixels pretos serão copiadas para a pasta "output" e as demais serão ignoradas.

## Observações

- O script foi testado apenas com imagens TIFF RGB.