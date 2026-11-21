---
version: 1
slug: "portfolio-templates-portfolio-home-html"
primary_target: "portfolio/templates/portfolio/home.html"
related_targets: ["portfolio/templates/portfolio/project_detail.html"]
---

# Surface brief: site do portfólio (home + detalhe de projeto)

Scope: `/` (home) e `/projects/<slug>/`. Visitor mode: Experience.

Audience and job: quem contrata para vaga (FDE / full-stack sênior) e quem contrata para projeto, com o mesmo peso. Os dois precisam ver, em segundos, produtos reais no ar e achar como falar com o autor.

Proof: prints públicos reais em `static/shots/`, links para os produtos, fatos do LinkedIn. Sem depoimentos, logos de cliente ou métricas inventadas.

Constraints: Django + Tailwind v4, sem bundler; pt-BR, en, es automáticos; tema claro/escuro pelo sistema; dispositivos 3D em cinco formatos; cada cena com estado parado completo para `prefers-reduced-motion`.

Memorable moment: isolar um projeto na mesa e ver, ao mesmo tempo, os canais das habilidades acenderem e o monitor trocar de produto e de tamanho de tela.

Unresolved: e-mail público, domínio, prints das telas internas, o que exatamente foi feito em kayamind.com.

## Direction contract

THESIS: O portfólio é a mesa de um estúdio onde uma pessoa toca todos os instrumentos. Recusa o arranjo padrão de portfólio de dev: nome gigante no alto e grade de cartões de projeto.

OWN-WORLD: Painel esmaltado azul-acinzentado (claro com a luz acesa, petróleo com a luz baixa), dividido por sulcos gravados em faixas e canais. Legendas serigrafadas em caixa alta estendida. Fita crepe branca atravessando a mesa com os nomes dos projetos escritos a caneta. Medidores de LED em escada, com células apagadas desenhadas. Tampas de fader e lâmpadas em vermelho, amarelo, azul e verde, uma cor por barramento. Poço escuro do monitor, onde ficam os dispositivos.

STORY: O visitante entende que os produtos são reais e estão no ar, acredita que a mesma pessoa leva do problema à produção, e abre um projeto ou entra em contato.

FIRST VIEWPORT: Faixa fina no alto com a placa do nome (que vira "oAccioly Faz" e volta), navegação, idioma e interruptor de luz. A frase principal atravessa o poço numa linha só, em display estendido. Abaixo, à esquerda, o texto de apresentação, a ação principal (abrir o projeto em cena) e, no pé da coluna, o seletor de monitor: os cinco tamanhos de tela como contornos aninhados em escala real, cada um uma tecla, o atual em linha cheia e os outros tracejados. À direita, ocupando três quartos da largura, o dispositivo 3D com o print real do projeto selecionado rolando. Fechando a tela, a fita crepe de ponta a ponta com os nomes dos projetos escritos a caneta: tocar num nome troca o produto no monitor. (Adaptação registrada em 2026-11-21: a frase passou a correr por cima do poço inteiro e o seletor foi para o pé da coluna esquerda, para o monitor ficar maior. No celular a ordem é frase, texto, ação, monitor, seletor, fita.)

FORM: Sala de controle com mesa de mixagem analógica; posição 4 da lista ordenada; seed:7b532a8f2b7a711b. Elevações herdadas das cartas recusadas: tamanhos de tela aninhados (cheio/tracejado); o apagado também é desenhado; uma leitura monumental por cena; densidade com fio fino no detalhe; toda seleção aparece no canal e no monitor.

Signature interaction: solo de projeto. Motion grammar: o monitor muda de formato por interpolação de largura, altura e raio; medidores sobem em degraus; a página do projeto abre com o monitor viajando entre as duas telas.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
