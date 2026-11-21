---
paths:
  - "**/*.html"
  - "theme/**"
  - "static/js/**"
---

# Regra — Telas: a Sala de Mixagem

A skill `impeccable` é a ferramenta de design do projeto. O mundo visual está decidido e documentado em
`DESIGN.md`: uma mesa de estúdio. Seção ou componente novo **herda** esse mundo; trocar cor, fonte ou motivo
do sistema só a pedido do autor.

## O vocabulário da mesa

- **Painel** (`--face`, `--face-up`, `--face-down`) dividido por **sulcos** (`groove`), nunca por cartão
  com sombra.
- **Poço** (`.well`) escuro nos dois temas: é onde ficam os dispositivos.
- **Fita crepe** (`.tape`, `.tape-strip`) com letra de caneta (`hand`): só para nome de projeto e para a
  fita da assinatura no rodapé.
- **Legenda** (`legend`): caixa alta estendida, para rótulo de painel. Não vira subtítulo em cima de título.
- **Lâmpada** (`.lamp`), **célula** (`.mx-cell`) e **medidor** (`.meter`, escada de LED por barramento
  nas faixas): o apagado também é desenhado.
- **Fader** (`.fader`): só na faixa de projeto, como a ação de abrir.
- **Seletor de monitor** (`.nest`): os cinco tamanhos de tela como contornos aninhados em escala real; o
  atual em linha cheia, os outros tracejados.
- **Patch bay** (`.patch`): o processo, um conector por etapa, uma etapa em cena por vez.
- **Assinatura** (`.wordmark`, `.nameplate-flip`): "oAccioly Faz" e o nome do autor andam juntos.
- **Tecla** (`.key`, `.key-primary`, `.key-well`, `.key-small`): toda ação que não é uma peça da própria
  mesa (nome na fita, contorno do seletor, conector do patch bay e a faixa inteira já são os controles).
- **Cor de tampa** por barramento (`data-bus`): vermelho, amarelo, creme, azul, verde, laranja. Cor nova
  não entra para enfeitar.

## Convenções

- Tailwind para layout e espaçamento; peça da mesa repetida vira classe em `theme/app.css`.
- Cor sempre por token (`var(--…)` ou utilitário `text-ink`, `bg-well`…), nunca hex no template.
- Tema por `light-dark()` nos tokens; não escreva variante `dark:` para cor que já tem token.
- Ícone só pela tag `{% icon %}` (`portfolio/templatetags/console.py`), um traço, uma família.
- JavaScript só acrescenta: a página renderiza e navega sem ele. Estado em atributo (`aria-pressed`,
  `data-*`), movimento no CSS.
- Movimento novo entra dentro de `@media (prefers-reduced-motion: no-preference)` e parte de um estado já
  visível. Animação contínua precisa de pausa.
- Unidade `cqw` dentro de `.rig` e `.dv-screen`: o dispositivo escala com o contêiner, não com a janela.

## Antes de dizer que terminou

1. `manage.py tailwind build` e `scripts/review_shots.py` com o servidor no ar.
2. Olhar 1440 px e 390 px, claro e escuro: sem rolagem horizontal, fita inteira na primeira tela do
   desktop (o script imprime onde ela termina), nada sobreposto, cinco formatos do monitor em ordem.
   O hook do ambiente bloqueia `Read` de imagem grande: use o visualizador (`review` no
   `.claude/launch.json`, `view.html?img=…&s=…&y=…`) ou fatias JPEG pequenas.
3. Clicar cada controle tocado e conferir o console.
4. `impeccable detect --json` nos arquivos alterados; achado mecânico se corrige na hora.
