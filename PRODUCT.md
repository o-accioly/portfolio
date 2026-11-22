# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Definida pelo autor: **Django + Tailwind CSS**. O resto foi delegado ("siga o caminho que achar melhor"):
Django 6 servindo templates, Tailwind v4 pela CLI standalone (`django-tailwind-cli`, sem Node no projeto),
JavaScript em módulos ES sem bundler, i18n nativo do Django, WhiteNoise para estáticos. Repositório público
no GitHub.

## Users

Dois públicos com o mesmo peso (confirmado em 2026-11-21):

- **Quem contrata para vaga.** Recrutador técnico, líder de engenharia ou fundador avaliando um
  Forward Deployed Engineer / engenheiro full-stack sênior, inclusive fora do Brasil. Chega por um link no
  LinkedIn ou no currículo, tem pouco tempo e quer evidência: produto real no ar, tamanho do que foi
  entregue, quem fez o quê.
- **Quem contrata para projeto.** Dono de negócio ou gestor, muitas vezes não técnico, que precisa de
  alguém que entenda a operação, construa o sistema e coloque em produção. Quer ver o que já funciona
  para outro negócio parecido e como falar com o autor.

## Product Purpose

Portfólio pessoal de **Gabriel Accioly**, engenheiro de software do Rio de Janeiro. Mostra os produtos que
ele construiu e opera, e prova a capacidade central: levar um problema de negócio do zero até a produção,
sozinho, incluindo descoberta, arquitetura, código, integrações, hospedagem e suporte. Sucesso é o
visitante sair sabendo o que Gabriel já colocou no ar e entrar em contato.

## Positioning

Engenheiro que trabalha **dentro da operação do cliente** (perfil Forward Deployed Engineer): senta com o
dono da loja, o médico ou o time de dados, entende o trabalho e entrega software rodando em produção. O
que um portfólio vizinho não copia: os produtos estão no ar com usuários reais, vários deles concebidos,
construídos, hospedados e mantidos pela mesma pessoa, e o próprio repositório deste site é público.

## Operating Context

- O visitante chega de um link (LinkedIn, currículo, GitHub, mensagem) e abre no celular ou no notebook.
- Os projetos citados são sites reais; cada um tem link para o produto no ar.
- O repositório é público: o código do portfólio também é amostra de trabalho, junto com o `CLAUDE.md` e
  as regras de desenvolvimento com agentes.

## Capabilities and Constraints

- **Projetos mostrados:** Diapasão (diapasao.com), KayaDoc
  (kayadoc.com.br), Kaya Mind (kayamind.com), Kaya Dashboard (dashboard.kayamind.com), KayaEducation
  (kayaeducation.com.br), Desbravador, Sabo,
  ZipZap, Duetto Musical (duettomusical.com.br), Optimum Capital (optimumcapital.com.br) e Standup. Cada
  um abre uma camada de detalhe com prints em mockups de dispositivos. O ZipZap mostra o painel real com
  dados sintéticos (notebook e celular), o KayaEducation mostra a área do aluno e o painel de uma marca de teste com a trilha de demonstração, o Desbravador mostra o projeto de demonstração embutido nos cinco
  tamanhos e o Diapasão tem as gravações do painel na loja demo Casa do Som. O Sabo e o Standup não têm
  página pública: o monitor mostra cada um rodando localmente. No Sabo, o agente responde de verdade sobre
  uma base de mercado fictícia (marcas, importadores e volumes inventados; o banco real nunca aparece). O Kaya
  Dashboard mostra o ambiente de uma marca fictícia e o console da equipe (sem relatório do Power BI
  carregado); no celular fica só a tela pública de login, porque o layout logado quebra em 390 px. No
  Standup, a empresa fictícia "Estúdio Aurora" aparece em monitor, notebook e celular; o tablet fica
  desativado porque o layout do produto quebra em 820 px.
- **Mockups em vários formatos:** monitor ultrawide, monitor comum, notebook, tablet e celular, para
  mostrar responsividade e a navegação de cada produto.
- **Páginas (desde 2026-11-21, a pedido do autor: "separa mais as páginas"):** Início, Projetos
  (`/projects/`), uma página por projeto, Sobre (`/about/`) e Tecnologias (`/stack/`), nos três idiomas. A
  faixa de contato fecha todas as páginas.
- **Busca e IA:** o autor quer ser achado por "Gabriel Accioly", "oAccioly" e "oAccioly Faz", e quer os
  projetos achados pelo nome. Todo texto vem do servidor; cada página tem título e descrição próprios,
  canonical, `hreflang`, Open Graph com imagem e JSON-LD que liga a pessoa, a empresa e o site pelo mesmo
  `@id`. `robots.txt` libera buscadores e assistentes de IA; `/llms.txt` e `/llms-full.txt` resumem o site
  em inglês para modelos de linguagem.
- **Idioma automático:** português (origem), inglês e espanhol, escolhido pelo idioma do navegador, com
  troca manual.
- **Tema automático:** claro ou escuro conforme o sistema do visitante, com troca manual.
- **Prints:** só páginas públicas são capturadas por script (`scripts/capture.py`). Telas atrás de login
  entram depois, escolhidas pelo autor, e nunca com dado de cliente real.
- **Segunda rodada, combinada com o autor:** capturar as telas internas dos produtos privados, com login
  ou rodando localmente e populando dados de demonstração realistas.
- **Sabo:** é o agente analista de mercado da Kaya (repositório `agent-kayaboard`, na conta
  `oaccioly-kaya`); não é o assistente do Diapasão, que tem o mesmo nome.
- **Fita crepe:** o autor quer textura real e vai enviar uma foto ou scan; até lá a fita é uma cor chapada.
- **Em aberto:** e-mail ou outro contato público além de LinkedIn e GitHub; o endereço exato do site no
  domínio da oAccioly Faz; o papel do autor em kayamind.com; ano de início do KayaDoc, do Kaya Dashboard
  e do Sabo.

## Brand Commitments

- Nome: Gabriel Accioly. LinkedIn `linkedin.com/in/oaccioly`, GitHub `github.com/o-accioly`.
- Marca e hospedagem: **oAccioly Faz** (OACCIOLY FAZ LTDA, CNPJ 65.469.093/0001-43, Pouso Alegre, MG), a
  empresa do autor, em cujo domínio o site fica. O nome da empresa e o nome do autor aparecem juntos e
  animados: a placa do cabeçalho alterna entre os dois e o rodapé assina "oAccioly faz".
- Pedido do autor: nada simples ou genérico; movimento, 3D e motion graphics como linguagem do site;
  qualidade no nível do site do Diapasão.
- Voz: direta, adulta, concreta. Fala de resultado e mostra a tela real.

## Evidence on Hand

Do LinkedIn do autor (lido em 2026-11-21) e dos repositórios locais:

- Programa desde 2017 (freelance desde janeiro de 2017), mais de 8 anos.
- **Diapasão** (fundador, desde jun/2025): SaaS de varejo multi-tenant com 2 lojas e 20 usuários; estoque,
  PDV, loja virtual, CRM e nota fiscal; IA no catálogo, nas notas de entrada e no atendimento; assistente
  Sabo; WhatsApp, pagamentos, fiscal, Mercado Livre e frete; PostgreSQL com Row-Level Security.
- **Kaya Mind** (desde jun/2022, tempo integral): KayaDoc com cerca de 4.000 usuários cadastrados,
  pagamentos Pagar.me e assinatura digital A1/A3; KayaEducation (LMS white-label); ambientes de análise
  multi-tenant com a API oficial do Power BI; cerca de 20 extratores de dados por mês no início.
- **Duetto Musical** (desde mar/2025): loja em Django, automação de atendimento com n8n e Chatwoot,
  integração com Dolibarr.
- **ZipZap:** motor de conexão e entrega para WhatsApp, multi-tenant (Symfony, FrankenPHP, RabbitMQ,
  runtimes em Node e Go).
- **B2W Energia Solar** (2021 a 2026): Volt-x, automação de financiamento solar entre vários bancos.
- **Formação:** Tecnólogo em Ciência de Dados, Cruzeiro do Sul Virtual (2020 a 2022).
- Prints públicos em `static/shots/`.

Não existe e não se inventa: depoimentos, logos de clientes, números de receita, métricas de performance.

## Product Principles

1. **O produto real é a prova.** Toda afirmação aponta para uma tela, um link ou um número que existe.
2. **Do problema à produção.** Cada projeto conta o caminho inteiro: qual era o problema, o que foi
   construído, onde roda.
3. **Dois leitores, uma página.** O técnico acha a arquitetura; o dono de negócio acha o resultado. Nenhum
   dos dois precisa atravessar o texto do outro.
4. **Nada que exponha cliente.** Dado real de terceiros não aparece em print, texto ou código.

## Accessibility & Inclusion

WCAG AA em contraste e foco. `prefers-reduced-motion` respeitado: o site é de movimento, então toda cena
tem um estado parado completo. Conteúdo legível e navegável sem JavaScript. Celular primeiro.
