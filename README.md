# Portfólio de Gabriel Accioly

Site pessoal em **Django 6 + Tailwind CSS v4**, sem banco de dados e sem Node no projeto. Mostra os produtos
em que trabalho num monitor 3D que assume cinco formatos de tela, e as tecnologias de cada um numa matriz
de roteamento.

*Personal portfolio built with Django and Tailwind CSS: a studio mixing console where each product is a
track and a single 3D device morphs between ultrawide, desktop, laptop, tablet and phone.*

## O que tem aqui

- **Monitor 3D em CSS puro.** Um único corpo vira monitor ultrawide, monitor, notebook, tablet e celular
  interpolando largura, altura e raio (`theme/app.css`, bloco `.dv`). A tela é um `<img>` real, nítido e
  com texto alternativo. O print rola até o fim e o monitor "navega" para a próxima página do mesmo site.
- **Faixas com medidores.** Cada produto é um canal da mesa: escadas de LED mostram quantas tecnologias
  dele estão em cada grupo, e o fader abre o projeto.
- **Matriz de habilidades.** Cada linha é uma tecnologia e cada coluna um produto. Isolar um produto apaga
  o que está fora da mixagem dele e coloca o produto no monitor.
- **Idioma automático.** `/` redireciona para `/pt-br/`, `/en/` ou `/es/` conforme o `Accept-Language` do
  navegador (`LocaleMiddleware` + `i18n_patterns`). Quem não pede nenhum dos três recebe inglês.
- **Tema automático.** Claro ou escuro pelo sistema, com `light-dark()` nos tokens; o interruptor "Luz do
  estúdio" permite fixar a escolha.
- **Sem JavaScript, continua funcionando.** O conteúdo todo vem do servidor; os scripts são módulos ES sem
  bundler e só acrescentam interação. Com `prefers-reduced-motion`, cada cena já nasce no estado final.

## Rodar

```bash
python3 -m venv .venv
```

```bash
.venv/bin/pip install -r requirements.txt
```

```bash
cp .env.example .env
```

```bash
.venv/bin/python manage.py tailwind runserver
```

O último comando baixa a CLI do Tailwind na primeira vez, recompila o CSS a cada mudança e sobe o servidor em
`http://localhost:8000`.

## Testar

```bash
.venv/bin/python manage.py test portfolio
```

Os testes cobrem a detecção de idioma, as páginas nos três idiomas e a igualdade de estrutura entre os
arquivos de texto.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `config/` | Settings únicos, configurados por variáveis de ambiente (`.env.example`) |
| `portfolio/catalog.py` | Fatos sem idioma: projetos, tecnologias, dispositivos, linha do tempo |
| `portfolio/content/` | Texto em português (origem), inglês e espanhol, com a mesma estrutura |
| `portfolio/shots.py` | Leitura do manifesto dos prints e cálculo da rolagem dentro do dispositivo |
| `portfolio/templates/` | Home, página de projeto e o monitor |
| `theme/app.css` | Tokens, tipografia e as peças da mesa (entrada do Tailwind) |
| `static/js/` | Módulos ES: monitor, matriz, luz, revelações e o tom de 440 Hz |
| `static/shots/` | Prints dos produtos e `manifest.json` |
| `scripts/capture.py` | Captura as páginas públicas em cinco tamanhos de tela |

## Prints

Só páginas públicas são capturadas:

```bash
.venv/bin/pip install pillow playwright
```

```bash
.venv/bin/python scripts/capture.py
```

O script usa o Chromium do Playwright ou, se ele não estiver instalado, o Chrome do sistema. Para acrescentar
um site ou uma página interna, edite `SITES` no script (a primeira página, `home`, é a capa; as outras são
para onde o monitor navega). O que já existe em disco não é refeito sem `--force`.

**Telas internas** (atrás de login) entram à mão, sempre de um ambiente com dados de demonstração: nenhum
dado de cliente entra neste repositório. Há dois jeitos:

- **Na galeria "Por dentro"** da página do projeto: salve `static/shots/<projeto>/inside-<dispositivo>-<nome>.webp`.
  Se houver um `.webm` ou `.mp4` com o mesmo nome, a gravação toca no lugar da imagem (é assim que o Diapasão
  mostra o painel da loja demo Casa do Som). A legenda vem de `inside` no texto do projeto.
- **No monitor 3D**, como páginas do produto: salve `<dispositivo>-home.webp` (primeira tela) e
  `<dispositivo>-<página>-full.webp`, como as capturas públicas, e marque `demo_screens=True` no projeto em
  `portfolio/catalog.py` (é assim que o ZipZap mostra o painel). Tamanhos de tela sem captura ficam
  desativados no seletor.

Depois, regenere o manifesto.

```bash
.venv/bin/python scripts/capture.py --manifest
```

## Publicar

A imagem Docker compila o CSS, coleta os estáticos com hash e sobe o Gunicorn na porta 8000:

```bash
docker build -t portfolio .
```

```bash
docker run --rm -p 8000:8000 -e DJANGO_SECRET_KEY=troque-isto -e DJANGO_ALLOWED_HOSTS=localhost -e DJANGO_SECURE_SSL_REDIRECT=0 portfolio
```

Em produção, defina `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS` e `SITE_URL`.
`CONTACT_EMAIL` e `REPO_URL` são opcionais.

O site no ar, em [oacciolyfaz.com](https://oacciolyfaz.com), roda no Dokploy como Docker Compose
(`docker-compose.yml`), puxando este repositório. As variáveis ficam na aba Environment do Dokploy; os
domínios `oacciolyfaz.com` e `www.oacciolyfaz.com` ficam na aba Domains, e o `www` usa o middleware
`portfolio-www-to-root@docker`, declarado no compose, para redirecionar à raiz. Depois de um push, o
deploy é disparado no Dokploy.

## Desenvolvimento com agentes

O projeto é mantido com Claude Code. [CLAUDE.md](CLAUDE.md) traz o que vale em toda sessão,
[PRODUCT.md](PRODUCT.md) descreve o produto e [DESIGN.md](DESIGN.md) o sistema visual; as regras de tela ficam
em `.claude/rules/`.

## Quem assina

O site é de Gabriel Accioly e fica no domínio da empresa dele, a **oAccioly Faz** (OACCIOLY FAZ LTDA, CNPJ
65.469.093/0001-43).

## Fontes

Anybody, Hanken Grotesk e Mynerve, servidas do próprio projeto, sob a SIL Open Font License.
