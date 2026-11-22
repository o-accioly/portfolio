---
name: Sala de Mixagem
description: O portfólio de Gabriel Accioly desenhado como a mesa de um estúdio onde uma pessoa toca todos os instrumentos.
colors:
  face: "light-dark(#bfccd4, #0d2a30)"
  face-up: "light-dark(#d3dde3, #143840)"
  face-down: "light-dark(#a9b9c3, #081d22)"
  ink: "light-dark(#0e1a22, #ece6d7)"
  ink-soft: "light-dark(#2b3f4c, #a7bcc0)"
  groove-a: "light-dark(rgb(14 26 34 / 0.34), rgb(0 0 0 / 0.7))"
  groove-b: "light-dark(rgb(255 255 255 / 0.62), rgb(255 255 255 / 0.07))"
  well: "light-dark(#0b2026, #051316)"
  well-up: "light-dark(#143039, #0c2227)"
  well-ink: "#ece6d7"
  well-soft: "#a3b8bd"
  well-groove: "rgb(255 255 255 / 0.1)"
  tape: "light-dark(#f5f1e7, #e6e1d3)"
  tape-edge: "light-dark(#e3dccb, #cfc8b6)"
  marker: "#15171a"
  cap-red: "#cf3a2b"
  cap-yellow: "#efb22e"
  cap-cream: "#f1ede3"
  cap-blue: "#2f73bd"
  cap-green: "#2f9e63"
  cap-orange: "#e07a2c"
  dv-bezel: "#0a0c0f"
  dv-edge: "#474f58"
  dv-back: "#2a3037"
  dv-deck: "#3a424b"
typography:
  display-1:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "clamp(2.125rem, calc((min(100vw - 2 * var(--gutter), 96rem) - 1.5rem) / (var(--chars, 23) * 0.76)), 5.5rem)"
    fontWeight: 800
    lineHeight: 0.94
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 122"
  display-2:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "clamp(1.875rem, 1.1rem + 2.7vw, 3.375rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.015em"
    fontVariation: "'wdth' 122"
  display-3:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "clamp(1.125rem, 1rem + 0.5vw, 1.375rem)"
    fontWeight: 700
    lineHeight: 1.15
    fontVariation: "'wdth' 116"
  lead:
    fontFamily: "Hanken Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Hanken Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  legend:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.1em"
    fontVariation: "'wdth' 118"
  key:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 650
    lineHeight: 1.1
    letterSpacing: "0.08em"
    fontVariation: "'wdth' 116"
  hand:
    fontFamily: "Mynerve, Segoe Print, cursive"
    fontSize: "clamp(1.2rem, 0.75rem + 0.65vw, 1.6rem)"
    fontWeight: 400
    lineHeight: 1
rounded:
  cell: "1px"
  cap: "2px"
  plate: "3px"
  key: "5px"
  frame: "6px"
  lamp: "50%"
spacing:
  gutter: "clamp(1rem, 4vw, 3.5rem)"
  band: "clamp(3.5rem, 8vw, 7rem)"
  band-inner: "96rem"
  bridge: "3.5rem"
  key-min: "2.75rem"
components:
  key:
    backgroundColor: "{colors.face-up}"
    textColor: "{colors.ink}"
    typography: "{typography.key}"
    rounded: "{rounded.key}"
    padding: "0.55rem 1rem"
    height: "2.75rem"
  key-primary:
    backgroundColor: "{colors.cap-red}"
    textColor: "#fff"
    typography: "{typography.key}"
    rounded: "{rounded.key}"
    padding: "0.55rem 1rem"
    height: "2.75rem"
  key-well:
    backgroundColor: "{colors.well-up}"
    textColor: "{colors.well-ink}"
    typography: "{typography.key}"
    rounded: "{rounded.key}"
    padding: "0.55rem 1rem"
    height: "2.75rem"
  key-small:
    backgroundColor: "{colors.face-up}"
    textColor: "{colors.ink}"
    rounded: "{rounded.key}"
    padding: "0.35rem 0.7rem"
    height: "2.25rem"
  nameplate:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.face}"
    rounded: "{rounded.plate}"
    padding: "0.4rem 0.7rem"
  tape:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.marker}"
    typography: "{typography.hand}"
    padding: "0.3em 0.75em 0.36em"
  tape-strip:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.marker}"
    typography: "{typography.hand}"
    padding: "0.5rem calc(var(--gutter) + 1rem)"
  well:
    backgroundColor: "{colors.well}"
    textColor: "{colors.well-ink}"
  nest-size:
    backgroundColor: "{colors.well}"
    textColor: "{colors.well-soft}"
    rounded: "{rounded.plate}"
  lamp:
    backgroundColor: "{colors.cap-red}"
    rounded: "{rounded.lamp}"
    size: "0.5rem"
  fader-cap:
    backgroundColor: "{colors.cap-red}"
    rounded: "{rounded.cap}"
    width: "1.75rem"
    height: "1.125rem"
  rack-unit:
    backgroundColor: "{colors.face-up}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "0.75rem 1rem"
---

# Design System: Sala de Mixagem

## Overview

**Creative North Star: "A Sala de Mixagem"**

O site é a mesa de um estúdio onde uma pessoa toca todos os instrumentos. Cada produto é uma faixa da mesa, cada habilidade é um canal que acende, e o produto em cena aparece num monitor que muda de formato. A página é um painel esmaltado azul-acinzentado: com a luz acesa ele é claro, com a luz baixa ele vira petróleo. O painel é dividido por sulcos gravados, as legendas são serigrafadas em caixa alta estendida, e uma fita crepe atravessa a mesa com os nomes dos projetos escritos a caneta.

A densidade é a de um equipamento: fio fino, peças pequenas e exatas, e uma leitura grande por cena (a frase do monitor, o título de cada faixa de página). Tudo que indica estado é desenhado também apagado, de modo que a mesa parada já está completa. A seleção nunca fica num lugar só: escolher um projeto muda a fita, o monitor, o texto da tecla principal e, no solo, a matriz de canais.

O que este mundo recusa, por decisão do projeto: nome gigante no alto seguido de grade de cartões de projeto. Aqui projeto é faixa de mesa, separada por sulco.

**Key Characteristics:**
- Painel esmaltado em dois estados de luz (`light-dark()` nos tokens, `data-theme` como escolha manual).
- Poço escuro nos dois temas, onde ficam os dispositivos e o processo.
- Sulco gravado (corte escuro com lábio claro) no lugar de cartão e sombra.
- Seis cores de tampa, uma por barramento; o vermelho também é a cor de ação.
- Três vozes de letra: display estendido (Anybody), texto (Hanken Grotesk), caneta (Mynerve).
- Um corpo 3D que vira cinco dispositivos mudando só os números.
- JavaScript só acrescenta; cada cena tem estado parado completo.

## Colors

Um painel frio azul-acinzentado com tinta quase preta, um poço petróleo com tinta creme, fita creme, e seis cores de tampa saturadas usadas em peças pequenas.

### Primary
- **Vermelho de tampa** (`cap-red`): a cor de ação. Tecla principal, tampa do fader, sublinhado da navegação, traço de caneta sob o nome em cena, agulha de reprodução da trajetória, e a faixa inteira de contato (texto branco). Também é o barramento `lang`.

### Secondary
- **Amarelo de sinal** (`cap-yellow`): o que está ligado agora. Contorno cheio do tamanho atual no seletor de monitor, sinal que corre no cabo do patch bay, linha de carregamento da tela, cor da seleção de texto, verbo da assinatura no rodapé. Também é o barramento `data`.

### Tertiary
- **Tampas de barramento** (`cap-cream` para `ui`, `cap-blue` para `ai`, `cap-green` para `infra`, `cap-orange` para `integ`): aparecem em lâmpadas, células da matriz, escadas de medidor e regiões da trajetória, sempre pela variável `--cap` herdada de `data-bus`.

### Neutral
- **Painel** (`face`): fundo da página e do cabeçalho. `face-up` é o plano levantado (teclas, faixas alternadas, unidade de rack, faixa sob o cursor); `face-down` é o rebaixo (trilho do fader, fundo da célula apagada do medidor, trilha da trajetória).
- **Tinta** (`ink`, `ink-soft`): texto sobre o painel. `ink-soft` é para apoio: leads, legendas secundárias, datas.
- **Sulco** (`groove-a` corte escuro, `groove-b` lábio claro): toda divisão do painel. Sempre os dois juntos.
- **Poço** (`well`, `well-up`): fundo escuro do monitor, do patch bay, do rodapé e da navegação entre projetos. `well-ink` e `well-soft` são a tinta lá dentro e não mudam com o tema; `well-groove` é o fio dentro do poço.
- **Fita e caneta** (`tape`, `tape-edge`, `marker`): a fita crepe é um preenchimento chapado, sem textura, com uma borda um tom abaixo; a caneta é quase preta nos dois temas.
- **Corpo de dispositivo** (`dv-bezel`, `dv-edge`, `dv-back`, `dv-deck`): moldura, espessura, costas e base do monitor 3D e dos aparelhos das faixas. Não são cor de interface.

### Named Rules
**A Regra do Barramento.** Cor de tampa só entra carregando um barramento (`data-bus` define `--cap`) ou como ação (vermelho) e sinal (amarelo). Cor nova não entra para enfeitar.

**A Regra do Poço.** O poço é escuro com a luz acesa e com a luz baixa. Dentro dele use `well-ink`, `well-soft`, `well-groove` e a tecla `key-well`; nunca `ink` nem `face`.

**A Regra do Token.** Cor de interface vem de token (`var(--…)` ou utilitário `text-ink`, `bg-well`). Tema se resolve em `light-dark()` no token, não em variante `dark:`.

## Typography

**Display Font:** Anybody variável, peso 100 a 900 e largura 50% a 150% (com Arial Narrow, sans-serif)
**Body Font:** Hanken Grotesk variável (com ui-sans-serif, system-ui, sans-serif)
**Label/Mono Font:** não há mono; a legenda é a própria Anybody estendida em caixa alta. A caneta é Mynerve (com Segoe Print, cursive).

**Character:** A Anybody estendida e pesada faz a serigrafia e os títulos de um equipamento; a Hanken Grotesk lê bem em texto corrido; a Mynerve é a única letra com mão, e por isso só escreve em fita ou nome de projeto.

### Hierarchy
- **Display 1** (800, largura 122%, tamanho calculado do comprimento da frase até 5.5rem, 0.94): a frase do monitor. Uma por página. `--chars` recebe o número de caracteres para a frase caber numa linha no desktop em qualquer idioma.
- **Display 2** (800, largura 122%, clamp de 1.875rem a 3.375rem, 1): título de cada faixa de página e da etapa em cena no patch bay.
- **Display 3** (700, largura 116%, clamp de 1.125rem a 1.375rem, 1.15): nome de trilha na trajetória, rótulo de unidade de rack, subtítulos da página de projeto.
- **Lead** (400, clamp de 1.0625rem a 1.1875rem, 1.55, no máximo 62ch): o parágrafo que acompanha um título.
- **Body** (400, 1rem, 1.55): texto corrido. Rótulos de linha da matriz e partes do rack usam peso 500 em 0.875rem a 0.9375rem.
- **Legend** (600, largura 118%, 0.6875rem, 0.1em, caixa alta): rótulo de painel. Navegação, leitura do monitor, papel e data na faixa, cabeçalho de grupo da matriz, nome de etapa no conector, termos da ficha técnica.
- **Key** (650, largura 116%, 0.75rem, 0.08em, caixa alta; 0.6875rem na tecla pequena): texto de tecla.
- **Hand** (Mynerve 400, linha 1; 1.2rem a 1.6rem na fita, 1.625rem na etiqueta da faixa, até 6rem no título da página de projeto): nome de projeto escrito a caneta.

A assinatura do rodapé é um caso à parte: Anybody 850 com largura 150%, de 2.5rem a 6rem. Números que se alinham usam `tabular` (algarismos tabulares e alinhados).

### Named Rules
**A Regra da Legenda.** A legenda rotula um painel, um controle ou um dado. Ela não vira subtítulo em cima de título.

**A Regra da Caneta.** Mynerve só escreve nome de projeto (na fita, na etiqueta, na tela sem print) e a palavra da fita da assinatura. Nenhum outro texto é manuscrito.

**A Regra da Largura.** A hierarquia da Anybody se faz com peso e largura (`font-stretch` de 116% a 150%), não com outra família.

## Layout

A página é uma pilha de faixas de largura total (`band`: respiro vertical de 3.5rem a 7rem, margem lateral `--gutter` de 1rem a 3.5rem), cada uma com miolo centrado de até 96rem (`band-inner`). As faixas alternam `face`, `face-up` e poço, e a divisão entre elas é sulco ou troca de plano. O cabeçalho (ponte) é fixo no alto, com 3.5rem de altura.

Primeira tela da home: a frase atravessa o poço numa linha só; abaixo, uma coluna estreita à esquerda (texto, ações e, no pé, o seletor de monitor) e o monitor ocupando três quartos (`0.5fr / 1.5fr`); fechando, a fita de ponta a ponta, que sangra 1rem além da margem e avança sobre a faixa seguinte. A partir de 64rem a largura do monitor é calculada pela altura da janela para que monitor, controles e fita caibam numa tela; a coluna esquerda ocupa `0.72fr` para o nome do autor caber numa linha.

Dentro de `.rig` e `.dv-screen` as medidas são em `cqw`: o dispositivo escala com o contêiner, não com a janela.

Pontos de quebra observados: 40rem (placa e teclas do cabeçalho compactas), 48rem (monitor mais alto, faixas em uma coluna, trajetória empilhada, rack sem perspectiva), 64rem (primeira tela em duas colunas, painel do patch em duas colunas), 75rem (faixas passam de duas para quatro colunas), 90rem (seis colunas estreitas; a etiqueta de fita da faixa escala com a largura da própria faixa, em `cqi`), 80rem (navegação sobe para a primeira linha do cabeçalho; abaixo disso ela é uma segunda linha rolável). No celular a ordem da primeira tela é frase, texto, ação, monitor, seletor, fita.

Alvo de toque: 2.75rem de altura mínima em tecla, nome na fita e link de navegação; 2.25rem na tecla pequena.

## Elevation & Depth

O painel é plano e gravado. A profundidade vem de três fontes: o sulco (um corte de 1px em `groove-a` com um lábio de 1px em `groove-b`), a troca de plano tonal (`face-down`, `face`, `face-up`, poço) e o 3D real dos dispositivos. Sombra projetada só existe em objeto físico solto sobre a mesa: tecla, fita, tampa de fader, aparelho, rack.

### Shadow Vocabulary
- **Sulco** (`border-top: 1px solid var(--groove-a); box-shadow: inset 0 1px 0 var(--groove-b)`): toda divisão do painel.
- **Tecla em repouso** (`box-shadow: 0 2px 3px -1px var(--groove-a), inset 0 1px 0 var(--groove-b)`): tecla levantada.
- **Tecla pressionada** (`transform: translateY(1px); box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.28)`): `:active`, `aria-pressed="true"`, `aria-current="true"`.
- **Tecla no poço** (`box-shadow: 0 2px 4px -1px rgb(0 0 0 / 0.6), inset 0 1px 0 rgb(255 255 255 / 0.08)`).
- **Fita** (`box-shadow: 0 1px 2px rgb(0 0 0 / 0.28)` na etiqueta; `0 3px 8px -2px rgb(0 0 0 / 0.45)` na tira).
- **Lâmpada acesa** (`box-shadow: 0 0 6px 1px color-mix(in oklab, var(--cap) 60%, transparent)`): o único brilho do sistema.
- **Tampa do fader** (`box-shadow: 0 2px 4px -1px rgb(0 0 0 / 0.5), inset 0 0 0 1px rgb(0 0 0 / 0.3)`).
- **Aparelho da faixa** (`box-shadow: 0 14px 22px -12px rgb(0 0 0 / 0.55), 0 2px 0 var(--dv-edge)`).
- **Rack** (`box-shadow: 30px 30px 50px -30px rgb(0 0 0 / 0.5)` no quadro; unidade aberta sobe `translateZ(28px)` com `0 16px 22px -8px rgb(0 0 0 / 0.55)`).
- **Chão do monitor** (gradiente radial preto a 60% com `blur(1.4cqw)`): a sombra de contato do dispositivo 3D.

### Named Rules
**A Regra do Sulco.** Painel se divide com sulco ou com troca de plano, nunca com cartão sombreado.

**A Regra do Objeto Solto.** Só projeta sombra o que estaria solto sobre a mesa. Texto, faixa e painel não têm sombra.

## Shapes

Cantos de equipamento: quase retos. Célula de medidor com 1px, tampa e trilho de fader com 2px, placa do nome, contornos do seletor, células da matriz e unidades de rack com 3px, tecla com 5px, quadro do rack com 6px. Círculo só em lâmpada, conector do patch bay e parafuso do rack. Os raios maiores pertencem aos corpos de dispositivo, calculados em `cqw` por formato.

A fita é um retângulo sem raio, sempre levemente torta (tira a -0.45°, etiquetas entre -1.2° e 1.1° pela variável `--tape-turn`). Contorno tracejado significa "disponível, não em cena"; contorno cheio significa "em cena". O foco visível é um contorno de 2px na cor do texto, afastado 3px.

## Components

### Buttons
Tudo que se aperta é tecla: curta, serigrafada, com curso de 1px.
- **Shape:** canto de 5px, borda de 1px em `groove-a`, altura mínima de 2.75rem, texto no estilo `key`.
- **Primary (`key-primary`):** fundo `cap-red`, texto branco. A ação principal da cena (abrir o projeto em cena, ver no ar).
- **Padrão (`key`):** fundo `face-up`, tinta `ink`. Sobre o painel e sobre a faixa vermelha de contato.
- **No poço (`key-well`):** fundo `well-up`, tinta `well-ink`, borda `well-groove`.
- **Pequena (`key-small`):** 2.25rem de altura, texto em 0.6875rem. Idioma, luz, solo, pausa do monitor.
- **Hover / Focus:** o fundo escurece misturando 14% a 20% da tinta (`color-mix` em oklab); pressionada desce 1px e troca a sombra por um rebaixo interno, em 140ms com `--ease-out`.
- **Com lâmpada:** uma tecla de estado leva uma `.lamp` antes do texto; `aria-pressed` ou `aria-current` na tecla acende a lâmpada.

### Lâmpada, célula e medidor
- **Lâmpada (`.lamp`):** círculo de 0.5rem. Apagada: 18% da cor da tampa com aro a 55%. Acesa: cor cheia com brilho.
- **Célula (`.mx-cell`):** quadrado de 0.8125rem na matriz de canais. No solo, as células do projeto escolhido crescem 1.3 vezes e ganham brilho; as outras colunas recuam para 30% da cor; as linhas fora da mixagem ficam com rótulo a 42%.
- **Medidor (`.meter`):** escada de células de 0.8rem por 0.3rem, uma escada por barramento, acesa de baixo para cima conforme quantas tecnologias do produto estão naquele barramento. Sobe em degraus de 110ms.

### Fita
- **Tira (`.tape-strip`):** atravessa a primeira tela de ponta a ponta com os nomes dos projetos (`.tape-name`). O nome em cena recebe um traço de caneta vermelho, desenhado da esquerda para a direita em 420ms; sob o cursor o traço aparece pela metade.
- **Etiqueta (`.tape`):** pedaço de fita com o nome do projeto na faixa e no título da página de projeto, e a palavra final da assinatura no rodapé.

### Faixa de projeto
- **Corner Style:** sem raio; a faixa é uma coluna do painel.
- **Background:** transparente sobre `face`; `face-up` sob o cursor ou com foco.
- **Shadow Strategy:** nenhuma; sulco à direita e embaixo.
- **Internal Padding:** 1.5rem 1.15rem 1.4rem.
- **Conteúdo, em ordem:** aparelho com o print real, etiqueta de fita com o nome, frase do produto, legenda de papel e data, ponte de medidores, fader.
- **Fader (`.fader`):** só existe aqui e é a ação de abrir. A tampa vermelha corre o trilho até o fim em 520ms quando a faixa recebe cursor ou foco, e o aparelho gira em 3D.

### Navigation
- **Ponte (`.bridge`):** cabeçalho fixo, painel a 92% com desfoque de fundo de 10px, fechado por sulco. À esquerda a placa do nome; à direita teclas pequenas de idioma (com lâmpada) e a tecla de luz.
- **Placa (`.nameplate`):** fundo `ink`, texto `face`, canto de 3px. Alterna entre o nome do autor e "oAccioly Faz" três vezes e para.
- **Link (`.nav-link`):** legenda em `ink`; sob cursor ou foco, um fio de 2px em `cap-red` cresce da esquerda em 260ms.
- **Transporte:** no fim da página de projeto, uma faixa de poço com duas teclas `key-well`, projeto anterior e próximo.

### Poço e monitor
- **Poço (`.well`):** fundo `well` com um gradiente radial suave em `well-up`. Recebe o monitor, o patch bay, o rodapé e o transporte.
- **Monitor (`.rig`, `.dv`):** um corpo 3D com espessura real que assume cinco formatos (ultrawide, desktop, notebook, tablet, celular) interpolando largura, altura, raio, moldura e inclinação em 900ms (`--morph`). Mostra o print real rolando devagar; quando o produto não tem página pública, mostra o nome a caneta e uma lista de estados com lâmpadas, marcada como ilustração. Entre a home e a página de projeto, o monitor viaja por transição de visualização (600ms).
- **Leitura e pausa:** sob o monitor, uma legenda com o projeto e o formato em cena, e uma tecla pequena que pausa o movimento.

### Seletor de monitor
`.nest`: os cinco tamanhos de tela como contornos aninhados em escala real, ancorados no canto inferior esquerdo, cada um uma tecla com a largura em pixels no canto. O atual tem contorno cheio de 2px em `cap-yellow` e fundo com 16% de amarelo; os outros têm contorno tracejado de 1px, que fica cheio sob o cursor.

### Patch bay
`.patch`: o processo. Um conector circular por etapa sobre um cabo; o sinal amarelo corre o cabo até a etapa escolhida em 620ms e o conector em cena cresce 1.25 vezes. Uma etapa em cena por vez. Sem JavaScript, todas as etapas ficam listadas.

### Trajetória, rack e ficha
- **Trajetória (`.lanes`):** uma trilha por experiência, com régua de anos em fios de sulco, região na cor do barramento e agulha vermelha; a região em andamento esmaece na ponta direita.
- **Rack (`.rack`):** as camadas de um projeto como unidades `details` num quadro de poço em leve perspectiva; a unidade aberta avança e acende as lâmpadas das suas partes.
- **Ficha (`.facts`):** lista de termo e valor separada por sulcos, termo em legenda.

### Primeira tela: quem está na mesa
Abaixo da frase, a coluna esquerda abre com o `h1` da página: o nome do autor em Anybody 800 com largura
112% (de 2.125rem a 2.5rem, numa linha só no desktop) e o traço de caneta vermelho por baixo, o mesmo que a
fita desenha sob o nome em cena. Logo depois, o papel em Hanken 600, o texto de apoio em `well-soft` e as
duas audiências (`.hero-buses`): uma linha por público, separada por fio de poço, com lâmpada acesa na cor do
barramento (amarelo para vaga, laranja para projeto) e a legenda à esquerda. Em telas de desktop baixas (até
54rem de altura) o texto de apoio sai para a fita continuar na primeira tela. A leitura sob o monitor diz o
projeto, o tipo, o endereço no ar e o formato.

### Barramentos de serviço
`.services`: uma linha por barramento, separada por sulco, em três colunas no desktop: legenda com lâmpada,
título em `display-3` com o texto, e "No ar em" com etiquetas de fita (`.tape-link`) dos projetos onde aquilo
roda. Na página de Tecnologias a mesma linha traz o porquê e as tecnologias como etiquetas gravadas
(`.service-skills`: 0.8125rem, aro em `groove-a`, fundo rebaixado).

### Par de telas
`.pair`: o print grande num notebook (tampa com base e entalhe) ou num monitor (pescoço e pé), e o celular
encostado na frente, no canto inferior direito. Tudo em `cqw`, com sombra de objeto solto. A tela é o print
inteiro, preso pelo topo; sob o cursor ou com foco, a página rola até o fim no tempo do próprio print. Aparece
na página de Projetos (uma por produto) e na galeria "As telas." da página de projeto, que mostra cada
página capturada com legenda e link para a página inteira.

### Páginas internas
Projetos, Sobre e Tecnologias abrem com trilha (`.crumbs`: legenda, barra como separador, página atual em
`ink-soft`) e o título em `display-1` numa linha. Na página de Projetos cada produto é uma `.entry` de largura
total que alterna `face` e `face-up` e troca o lado do par de telas. Perguntas frequentes (`.faq`) são
`details` separados por sulco, com o mesmo chevron do rack. O link de navegação da página atual mantém o fio
vermelho aceso (`aria-current="page"`). O rodapé lista as páginas e todos os projetos.

### Assinatura
`.wordmark` no rodapé: "oAccioly" em Anybody com largura 150%, o verbo em `cap-yellow` e, numa etiqueta de fita, o que a empresa faz. As letras alargam uma depois da outra, como faders subindo. Junto com a placa do cabeçalho, é onde o nome da empresa e o nome do autor aparecem juntos.

### Ícones
Uma família desenhada, só pela tag `{% icon %}`: grade de 24, traço de 1.75, pontas redondas, cor do texto.

## Do's and Don'ts

### Do:
- **Do** desenhar o estado apagado de tudo que acende: lâmpada, célula, degrau de medidor, contorno tracejado do seletor.
- **Do** mostrar a seleção em mais de um lugar: fita, monitor, tecla principal e, no solo, a matriz.
- **Do** dividir o painel com sulco (`groove`, `groove-b`) ou com troca de plano (`face`, `face-up`, poço).
- **Do** usar `key`, `key-primary`, `key-well` e `key-small` para todo botão e link de ação que não seja uma peça própria da mesa (nome na fita, contorno do seletor, conector do patch bay, faixa de projeto), com 2.75rem de altura mínima.
- **Do** dar a cada cena um estado parado completo: movimento novo entra em `@media (prefers-reduced-motion: no-preference)` e parte de um estado já visível.
- **Do** usar `--ease-out` (`cubic-bezier(0.16, 1, 0.3, 1)`) para resposta e `--ease-in-out` para percurso; medidor sobe em degraus.
- **Do** medir em `cqw` dentro de `.rig` e `.dv-screen`.
- **Do** manter a página navegável sem JavaScript: estado em atributo (`aria-pressed`, `data-*`), movimento no CSS.

### Don't:
- **Don't** abrir a página com nome gigante no alto e grade de cartões de projeto.
- **Don't** separar conteúdo com cartão sombreado; a mesa tem sulco.
- **Don't** clarear o poço no tema claro nem usar `ink` ou `face` dentro dele.
- **Don't** acrescentar cor de tampa sem barramento, nem usar tampa como decoração.
- **Don't** escrever a caneta outra coisa que não nome de projeto ou a fita da assinatura.
- **Don't** pôr legenda como subtítulo em cima de título.
- **Don't** usar o fader fora da faixa de projeto.
- **Don't** escrever cor em hex no template nem variante `dark:` para cor que já tem token.
- **Don't** deixar animação contínua sem pausa.
