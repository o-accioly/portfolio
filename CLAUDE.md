# Portfólio — instruções do projeto

Site pessoal de Gabriel Accioly: Django 6 servindo templates, Tailwind v4 pela CLI standalone
(`django-tailwind-cli`), JavaScript em módulos ES sem bundler. **Sem banco de dados e sem Node.** Repositório
público: tudo aqui é amostra de trabalho.

Aqui fica só o que vale em quase toda sessão. O produto está em `PRODUCT.md`, o sistema visual em `DESIGN.md`
e o processo de tela em `.claude/rules/frontend.md` (carrega ao tocar template, CSS ou JS).

## Regras que valem sempre

1. **Nada que exponha cliente.** O repositório é público. Print só de página pública ou de ambiente de
   demonstração; nenhum dado real de terceiros em imagem, texto, teste ou commit. Na dúvida, não entra.
2. **Fato com fonte.** Número, data, cargo e tecnologia vêm do LinkedIn do autor, do README do projeto ou do
   site no ar. Não invente depoimento, cliente, métrica ou tecnologia que o projeto não usa. Fato novo que
   não dá para conferir vira pergunta ao autor.
3. **Três idiomas, uma estrutura.** O texto nasce em `portfolio/content/pt_br.py` e é espelhado em `en.py` e
   `es.py`, chave por chave. Mudou um, mude os três: `test_content.py` reprova estrutura diferente e
   placeholder perdido. Não há gettext no projeto (o ambiente não tem `msgfmt`); a detecção de idioma e os
   prefixos de URL continuam sendo do Django.
4. **Fatos em `catalog.py`, prosa em `content/`.** `catalog.py` não guarda frase; `content/` não guarda
   slug, URL nem ano.
5. **Número em CSS se monta no Python.** O template localiza float (`12,5` em pt-BR) e quebra o estilo em
   silêncio. Valor de `style=""` chega pronto como string (`Shot.pan_css`, `left`, `width`).
6. **Segredo fora do repositório.** Configuração por variável de ambiente (`.env.example`); `.env` não é
   versionado.

## Idioma do código

Código, identificadores, comentários e docstrings em inglês. Texto visível nasce em pt-BR. Documentação
(`README.md`, este arquivo, `PRODUCT.md`, `DESIGN.md`) em português.

## Rodar e testar

- Servidor com CSS em watch: `.venv/bin/python manage.py tailwind runserver`.
- Só compilar o CSS: `.venv/bin/python manage.py tailwind build` (o arquivo gerado `static/css/app.css` não
  é versionado).
- Testes: `.venv/bin/python manage.py test portfolio`. Lint e formato: `.venv/bin/ruff check .` e
  `.venv/bin/ruff format .`.
- Prints: `scripts/capture.py` (ver README). Capturas de revisão de tela: `scripts/review_shots.py`, que
  grava em `.impeccable/review/` (fora do git).

## Checklist por tarefa

1. Texto novo nos três idiomas, com o teste passando.
2. Tela tocada: olhar o resultado renderizado em 1440 px e 390 px, tema claro e escuro, antes de dizer que
   terminou (`rules/frontend.md`).
3. `ruff` e testes verdes.
4. Commit e push só quando o autor pedir.

## Onde está o detalhe

- **Design:** skill `impeccable`, com `PRODUCT.md`, `DESIGN.md` e o contrato de direção em
  `.impeccable/surfaces/`.
- **Estrutura do código:** tabela no `README.md`.
