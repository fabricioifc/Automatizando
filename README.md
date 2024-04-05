# Automatizando

Este repositório contém scripts que automatizam tarefas comuns no dia a dia de um programador de visão computacional.

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

### Removendo imagens com determinada cor

Este script foi desenvolvido para remover slices de imagens tif que possuem uma quantidade de pixels pretos acima de um determinado percentual. O script foi desenvolvido para ser executado via linha de comando e possui 4 argumentos:

- `--percent`: Percentual de pixels pretos que uma slice deve ter para ser removida
- `--label_dir`: Diretório com as imagens tif
- `--color`: Cor do pixel que será considerado preto
- `--op`: Tipo de ação a ser realizada, podendo ser `move` ou `delete`

## Como executar

Para executar o script, basta rodar o comando abaixo:

```bash
python main.py --label_dir='lib/samples/' --percent=0.5 --color='(0, 0, 0)' --op='move'
```

O comando acima irá mover ou remover todas as imagens que possuem pelo menos 50% de pixels pretos.

### Extraindo frames de um vídeo

Este script foi desenvolvido para extrair frames de um vídeo e salvar em um diretório. O script foi desenvolvido para ser executado via linha de comando e possui 2 argumentos:

- `--video_path`: Caminho do vídeo
- `--output_dir`: Diretório de saída

## Como executar

Para executar o script, basta rodar o comando abaixo:

```bash
python lib/extract_frames_from_video.py --video_path='lib/samples/video.mp4'
```

O comando acima irá extrair os frames do vídeo e salvar no diretório `lib/samples/frames`.

### Convertendo anotações de polígono para Boundig Box (CVAT)

Este script foi desenvolvido para converter anotações de polígono para anotações de bounding box. O script foi desenvolvido para ser executado via linha de comando e possui 2 argumentos:

- `--xml_file`: Caminho do arquivo xml

## Como executar

Para executar o script, basta rodar o comando abaixo:

```bash
python lib/polygon_to_bb.py --xml_file='lib/annotations/annotations.xml'
```

O comando acima irá converter as anotações de polígono para anotações de bounding box.