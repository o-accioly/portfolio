"""Portuguese copy: the source language. `en.py` and `es.py` mirror this structure key by key
(`portfolio/tests/test_content.py` fails when they drift)."""

CONTENT = {
    "meta": {
        "title": "Gabriel Accioly (oAccioly) · Engenheiro de software, do problema à produção",
        "description": "Gabriel Accioly (oAccioly), engenheiro de software full-stack com perfil Forward Deployed. "
        "Produtos no ar, como Diapasão, KayaDoc e ZipZap, de ponta a ponta.",
        "job_title": "Engenheiro de software full-stack",
        "og_locale": "pt_BR",
        "about_title": "Sobre Gabriel Accioly (oAccioly) · Engenheiro de software no Rio de Janeiro",
        "about_description": "Gabriel Accioly: engenheiro de software desde 2017, fundador do Diapasão, "
        "desenvolvedor na Kaya Mind e dono da oAccioly Faz. Trajetória, formação e método.",
        "projects_title": "Projetos de Gabriel Accioly · SaaS, IA, dados e integrações no ar",
        "projects_description": "Produtos que Gabriel Accioly construiu e opera: Diapasão, KayaDoc, Kaya Dashboard, "
        "KayaEducation, Sabo, ZipZap, Desbravador e mais, com telas reais.",
        "stack_title": "Tecnologias de Gabriel Accioly · Python, Django, PostgreSQL, IA e Docker",
        "stack_description": "Tecnologias que Gabriel Accioly usa e onde estão no ar: Python, Django, PostgreSQL, "
        "HTMX, agentes de IA, Docker, WhatsApp, pagamentos e nota fiscal.",
        "project_title": "{name}: {kind} · Projeto de Gabriel Accioly",
    },
    "nav": {
        "skip": "Pular para o conteúdo",
        "label": "Seções",
        "projects": "Projetos",
        "skills": "Habilidades",
        "process": "Processo",
        "journey": "Trajetória",
        "contact": "Contato",
        "language": "Idioma",
        "home": "Início",
        "about": "Sobre",
        "stack": "Tecnologias",
        "breadcrumb": "Você está em",
    },
    "theme": {"label": "Luz do estúdio", "auto": "Automática", "light": "Acesa", "dark": "Baixa"},
    "hero": {
        "title": "Do problema à produção.",
        "name": "Gabriel Accioly",
        "role": "Engenheiro de software full-stack, com perfil Forward Deployed.",
        "lead": "Entro na operação, construo o sistema e coloco no ar: descoberta, arquitetura, código, "
        "integrações, hospedagem e suporte. Faço o caminho inteiro desde 2017.",
        "audiences": [
            {
                "label": "Vaga",
                "text": "Forward Deployed Engineer ou full-stack sênior, para times que precisam de produto em "
                "produção.",
            },
            {
                "label": "Projeto",
                "text": "Sistema sob medida para o seu negócio, do diagnóstico ao suporte depois do lançamento.",
            },
        ],
        "open": "Abrir {name}",
        "contact": "Falar comigo",
        "about": "Sobre mim",
        "monitor": "Monitor",
        "tape": "Projetos no monitor",
        "on_stage": "Em cena",
        "no_page": "sem página pública",
    },
    "devices": {
        "label": "Tamanho de tela",
        "ultrawide": "Ultrawide",
        "desktop": "Monitor",
        "laptop": "Notebook",
        "tablet": "Tablet",
        "phone": "Celular",
    },
    "projects": {
        "title": "Cada produto, uma faixa.",
        "lead": "Cada faixa é um produto em que trabalho. Abra uma para ver as telas em cada tamanho e as "
        "camadas do sistema.",
        "open": "Abrir projeto",
        "live": "Ver no ar",
        "repo": "Ver repositório",
        "since": "desde {year}",
        "illustration": "Ilustração. Este produto não tem página pública.",
        "all": "Todos os projetos, em detalhe",
        "page_title": "Projetos.",
        "page_lead": "{count} produtos, cada um com o problema, o que construí, onde roda e as telas reais. Os que "
        "estão no ar têm link; os privados aparecem rodando com dados de demonstração.",
        "stack": "Tecnologias",
        "screens_count": "{count} telas capturadas",
        "highlights": {
            "diapasao": [
                "Estoque, PDV, loja virtual, CRM e nota fiscal num sistema só",
                "IA no cadastro, nas notas de entrada e no primeiro atendimento pelo WhatsApp",
                "Assistente Sabo que consulta e age, com confirmação antes de operação sensível",
                "Cada loja isolada por Row-Level Security, com teste de isolamento no CI",
                "2 lojas e 20 usuários em produção",
            ],
            "kayadoc": [
                "Experiências separadas para médicos, pacientes e marcas",
                "Pagamentos pela Pagar.me",
                "Assinatura digital com certificado A1 e A3",
                "PWA com passkeys, segundo fator e login pelo Google",
                "Cerca de 4.000 usuários cadastrados",
            ],
            "kayamind": [
                "Desenvolvimento dos produtos desde 2022, em tempo integral e remoto",
                "KayaDoc, KayaEducation, Kaya Dashboard e Sabo",
                "Cerca de 20 extratores de dados por mês no início",
                "Método de extração ensinado ao time, que passou a construir os próprios",
            ],
            "kaya-dashboard": [
                "Um ambiente de análise para cada marca",
                "Relatórios incorporados pela API oficial do Power BI",
                "Cada marca vê só os próprios números",
                "Console da equipe para gerir marcas e painéis",
            ],
            "kayaeducation": [
                "LMS white-label: cada marca com a própria identidade",
                "Cursos organizados em trilhas de aprendizagem",
                "Área do aluno e painel da marca",
                "Django, HTMX e Tailwind",
            ],
            "desbravador": [
                "Extrator criado numa conversa com um agente Claude, num terminal dentro do navegador",
                "Execução determinística em Playwright, sem modelo de linguagem no caminho crítico",
                "Qualidade medida a cada execução",
                "Até 3 tentativas de correção automática antes de chamar uma pessoa",
                "Configuração versionada, com canário antes de promover",
            ],
            "sabo": [
                "Perguntas de mercado em português, com números rastreáveis até a consulta",
                "Ferramentas de banco somente de leitura",
                "Resposta ao vivo, anexos e conversa por voz",
                "Roda no Claude Agent SDK ou na Responses API da OpenAI",
                "Cota e custo medidos por pessoa; versão 1.0 em outubro de 2026",
            ],
            "zipzap": [
                "Cinco estados de entrega, cada um com a sua evidência",
                "API que responde 202 e entrega o resultado por webhook assinado",
                "Runtimes em Node (Baileys) e Go (whatsmeow) atrás do mesmo contrato",
                "Contas passam para outro worker sem novo QR",
                "Usado pelo Diapasão",
            ],
            "duetto": [
                "Loja virtual em Django",
                "Atendimento automatizado com n8n e Chatwoot",
                "Estoque atualizado e SEO de produto enriquecido",
                "Integração com o Dolibarr para a gestão",
                "Onde nasceu o Diapasão",
            ],
            "optimum": [
                "Site e plataforma em Django com Wagtail",
                "A equipe publica documentos e artigos sem depender de desenvolvedor",
                "Blog, área de documentos e calculadora para o investidor",
                "Celery e Redis para as tarefas em segundo plano",
            ],
            "standup": [
                "Atas, dailies e reuniões operacionais",
                "Pautas, decisões e as tarefas que saem de cada reunião",
                "Edição colaborativa em tempo real com Hocuspocus e Yjs",
                "Next.js na interface, Django REST Framework na API",
            ],
        },
        "pages": {
            "diapasao": {
                "home": "Página inicial do Diapasão",
                "crm": "CRM",
                "loja": "Loja virtual",
                "assistente": "Assistente de IA",
            },
            "kayadoc": {"home": "Página inicial", "funcionalidades": "Funcionalidades", "planos": "Planos"},
            "kayamind": {"home": "Página inicial", "relatorios": "Relatórios"},
            "kaya-dashboard": {
                "home": "Ambiente de uma marca fictícia",
                "console": "Console da equipe",
                "paineis": "Painéis da marca",
                "eventos": "Eventos de uso",
                "entrar": "Tela de login",
            },
            "kayaeducation": {
                "home": "Área do aluno",
                "aula": "Aula",
                "conteudo": "Conteúdo do curso",
                "engajamento": "Engajamento",
                "entrar": "Tela de login",
                "painel": "Painel da marca",
                "trilha": "Trilha de aprendizagem",
            },
            "desbravador": {
                "home": "Visão geral",
                "painel": "Painel do projeto",
                "extrator": "Extrator",
                "execucoes": "Execuções",
                "dados": "Dados extraídos",
            },
            "sabo": {"home": "Chat com o agente", "consultas": "Modo avançado, com o SQL", "custo": "Uso e custo"},
            "zipzap": {
                "home": "Visão geral do painel",
                "conversas": "Conversas",
                "instancia": "Número conectado",
                "webhooks": "Webhooks",
            },
            "duetto": {"home": "Página inicial da loja", "categoria": "Categoria de mesas de som"},
            "optimum": {"home": "Página inicial", "quem-somos": "Quem somos", "calculadora": "Calculadora"},
            "standup": {
                "home": "Início",
                "operacional": "Reunião operacional",
                "daily": "Daily",
                "ata": "Ata",
            },
        },
        "items": {
            "diapasao": {
                "kind": "SaaS de varejo",
                "tagline": "A loja inteira num sistema só: estoque, PDV, loja virtual, CRM e nota fiscal.",
                "role": "Fundador e engenheiro",
                "problem": "Loja com catálogo grande vive de integrar ERP com e-commerce, e a "
                "sincronia quebra sempre no mesmo lugar: cadastro duplicado, estoque "
                "divergente, atendimento lento. O primeiro sistema nasceu dentro de "
                "uma loja de instrumentos; quando outras lojas pediram o mesmo, "
                "refiz tudo para servir qualquer varejo.",
                "built": "Uma plataforma em Django que junta estoque, PDV, loja virtual, CRM e "
                "nota fiscal. A IA melhora o cadastro (descrição, ficha técnica, "
                "imagem), categoriza as notas de entrada e responde o primeiro contato "
                "no WhatsApp. O Sabo, assistente ligado aos dados da loja, consulta e "
                "age, e pede confirmação antes de qualquer operação sensível.",
                "runs": "Cada loja é um tenant isolado por Row-Level Security no PostgreSQL, "
                "com teste de isolamento como etapa obrigatória do CI. Roda em bare "
                "metal com Docker; hoje atende 2 lojas e 20 usuários.",
                "facts": [
                    ["Papel", "Fundador e engenheiro"],
                    ["Período", "Desde junho de 2025"],
                    ["Em uso", "2 lojas, 20 usuários"],
                    ["Isolamento", "Row-Level Security por loja"],
                    ["Onde roda", "Bare metal, Docker"],
                ],
                "layers": {
                    "interface": "Quatro superfícies para quatro públicos: o site, a "
                    "loja com a marca do lojista, o painel de trabalho e o "
                    "console da plataforma.",
                    "app": "Apps Django finos por responsabilidade. Toda tela nasce com "
                    "a permissão do papel e a trava do plano.",
                    "data": "Um schema só; o banco garante que uma loja nunca lê a linha da outra.",
                    "ai": "IA com ação: o assistente executa no sistema, sempre com "
                    "confirmação nas operações que mexem em dinheiro ou estoque.",
                    "integrations": "O que a loja já usa, ligado num lugar só, para ninguém digitar duas vezes.",
                    "infra": "Deploy por contêiner em servidor próprio, com o CI rodando em runner da casa.",
                },
                "screen": [],
                "inside": {
                    "atendimento": "Atendimento no WhatsApp com o robô",
                    "pdv": "Venda no balcão (PDV)",
                    "produtos": "Cadastro de produto e estoque",
                    "crm": "CRM em kanban",
                    "fatura": "Fatura e nota fiscal",
                    "mercadolivre": "Anúncios no Mercado Livre",
                },
            },
            "kayadoc": {
                "kind": "Plataforma de bem-estar",
                "tagline": "Médicos, pacientes e marcas na mesma plataforma, com pagamento e assinatura digital.",
                "role": "Arquitetura e desenvolvimento · Kaya Mind",
                "problem": "Três públicos com necessidades diferentes precisavam conviver no "
                "mesmo produto: o médico que prescreve e assina, o paciente que "
                "acompanha e paga, a marca que participa. Cada um com a sua "
                "experiência e sem enxergar o dado do outro.",
                "built": "Plataforma multi-tenant em Django com experiências dedicadas para "
                "médicos, pacientes e marcas. Pagamentos pela Pagar.me e assinatura "
                "digital com certificado A1 e A3 (VIDaaS, BirdID, Syn e pyHanko). "
                "Funciona como PWA, com passkeys, autenticação em dois fatores e login "
                "pelo Google.",
                "runs": "Cerca de 4.000 usuários cadastrados. Roda em Docker sobre Linux, com "
                "deploy pelo Easypanel, CI/CD e avisos operacionais por n8n, Teams e "
                "ntfy.",
                "facts": [
                    ["Papel", "Arquitetura e desenvolvimento"],
                    ["Empresa", "Kaya Mind, desde 2022"],
                    ["Usuários", "Cerca de 4.000 cadastrados"],
                    ["Pagamentos", "Pagar.me"],
                    ["Assinatura", "Certificado A1 e A3"],
                ],
                "layers": {
                    "interface": "Uma experiência para cada público, instalável no celular.",
                    "app": "Autenticação forte desde o cadastro: passkey, segundo fator e SSO.",
                    "data": "Banco relacional, cache e filas para o que não pode travar a tela.",
                    "integrations": "Pagamento e assinatura com validade jurídica, dentro do fluxo.",
                    "infra": "Contêineres em Linux com deploy automatizado.",
                },
                "screen": [],
                "inside": {},
            },
            "kayamind": {
                "kind": "Dados do mercado de cannabis",
                "tagline": "A empresa onde respondo pelo desenvolvimento dos produtos desde 2022.",
                "role": "Cientista de dados e desenvolvedor Django",
                "problem": "Uma startup de inteligência de mercado precisa de dado novo toda "
                "semana e de produto no ar ao mesmo tempo. Com time enxuto, a mesma "
                "pessoa cuida da extração, da arquitetura, do código e do deploy de "
                "vários projetos em paralelo.",
                "built": "Os produtos da Kaya: o KayaDoc, o KayaEducation (um LMS white-label "
                "com trilhas de aprendizagem) e os ambientes de análise por marca. No "
                "início, cerca de 20 extratores de dados por mês; depois ensinei o "
                "método ao time, que passou a construir os próprios, e fiquei com as "
                "extrações mais difíceis.",
                "runs": "Trabalho em tempo integral e remoto. Integrações e avisos "
                "automatizados com n8n, Microsoft Teams e ntfy; entrega acelerada por "
                "agentes (Claude Code e Codex), com CI/CD, testes e revisão de "
                "segurança.",
                "facts": [
                    ["Papel", "Cientista de dados e desenvolvedor Django"],
                    ["Período", "Desde junho de 2022"],
                    ["Regime", "Tempo integral, remoto"],
                    ["Extratores", "Cerca de 20 por mês no início"],
                ],
                "layers": {
                    "app": "Três produtos Django mantidos em paralelo.",
                    "data": "Coleta, limpeza e carga dos dados que alimentam as análises.",
                    "integrations": "Automação entre os sistemas e o time.",
                    "infra": "Contêineres em Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "kaya-dashboard": {
                "kind": "Análise por marca",
                "tagline": "Cada marca entra e vê só os próprios gráficos, servidos pela API oficial do Power BI.",
                "role": "Arquitetura e desenvolvimento · Kaya Mind",
                "problem": "As marcas clientes precisavam consultar os próprios números "
                "sem receber planilha e sem enxergar o concorrente.",
                "built": "Ambientes de análise multi-tenant em Django. Os relatórios são "
                "incorporados pela API oficial do Power BI, e cada marca recebe "
                "os gráficos e os insights dela.",
                "runs": "Acesso por login em dashboard.kayamind.com. Roda em Docker sobre "
                "Linux, com deploy pelo Easypanel.",
                "facts": [
                    ["Papel", "Arquitetura e desenvolvimento"],
                    ["Empresa", "Kaya Mind, desde 2022"],
                    ["Gráficos", "API oficial do Power BI"],
                    ["Modelo", "Um ambiente por marca"],
                ],
                "layers": {
                    "interface": "Um ambiente para cada marca.",
                    "app": "O Django decide quem vê qual relatório.",
                    "data": "Relatórios incorporados pela API oficial.",
                    "infra": "Contêineres em Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "kayaeducation": {
                "kind": "LMS white-label",
                "tagline": "Plataforma de cursos com trilhas de aprendizagem e um ambiente próprio para cada marca.",
                "role": "Arquitetura e desenvolvimento · Kaya Mind",
                "problem": "Cada marca queria oferecer cursos com a própria identidade, "
                "sem montar uma plataforma de ensino do zero.",
                "built": "Um LMS white-label em Django: trilhas de aprendizagem e "
                "ambientes educacionais que cada marca personaliza.",
                "runs": "No ar em kayaeducation.com.br, com acesso por login. Roda em Docker sobre Linux.",
                "facts": [
                    ["Papel", "Arquitetura e desenvolvimento"],
                    ["Empresa", "Kaya Mind, desde 2022"],
                    ["Modelo", "White-label, um ambiente por marca"],
                    ["Conteúdo", "Trilhas de aprendizagem"],
                ],
                "layers": {
                    "interface": "Um ambiente de ensino com a identidade de cada marca.",
                    "app": "Cursos organizados em trilhas.",
                    "data": "Banco relacional e cache.",
                    "infra": "Contêineres em Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "desbravador": {
                "kind": "Extração web com agente de IA",
                "tagline": "Extratores de dados criados numa conversa com um agente e "
                "executados sem IA no caminho crítico.",
                "role": "Autor",
                "problem": "Extrator de dados quebra sempre que o site de origem muda, e "
                "escrever cada um à mão não escala.",
                "built": "Uma plataforma onde o extrator nasce de uma conversa com um agente "
                "Claude, num terminal dentro do navegador: o agente sonda o site e "
                "gera uma configuração determinística. A execução roda em "
                "Playwright, sem modelo de linguagem, barata e previsível. A "
                "qualidade é medida a cada execução; quando cai, o sistema tenta se "
                "corrigir até três vezes antes de chamar uma pessoa.",
                "runs": "Django com Channels para o terminal por WebSocket, Postgres com "
                "JSONB, Celery e Redis para o agendamento e um pool de navegadores "
                "em contêineres. Configuração é dado, nunca código: nada gerado por "
                "modelo é executado em produção. Tudo é versionado e passa por "
                "canário antes de ser promovido.",
                "facts": [
                    ["Papel", "Autor"],
                    ["Período", "Desde maio de 2026"],
                    ["Execução", "Determinística, sem LLM"],
                    ["Correção", "Até 3 tentativas automáticas"],
                    ["Código", "Repositório privado"],
                ],
                "layers": {
                    "interface": "Painel de extratores, execuções e bloqueios, com um terminal embutido.",
                    "app": "Projetos com membros e papéis.",
                    "ai": "O agente cria e conserta; nunca roda em produção.",
                    "runtime": "Um executor fixo e testado consome a configuração.",
                    "data": "Estado central, agendamento e dados extraídos com idempotência.",
                    "infra": "Navegadores de longa duração em contêineres.",
                },
                "screen": [
                    "Descoberta com agente",
                    "Execução determinística",
                    "Checagem de qualidade",
                    "Correção automática",
                    "Versão e canário",
                ],
                "inside": {},
            },
            "sabo": {
                "kind": "Agente analista de mercado",
                "tagline": "Perguntas de mercado em português, respondidas com números rastreáveis até a consulta.",
                "role": "Arquitetura e desenvolvimento · Kaya Mind",
                "problem": "Gestor de marca precisa de número de mercado para decidir preço, "
                "lançamento e território, e não pode esperar um analista montar cada "
                "resposta.",
                "built": "Um agente que responde sobre o mercado de cannabis medicinal a partir dos "
                "dados de importação e de dispensação em farmácias. Ele consulta o banco "
                "por ferramentas somente de leitura, explica o resultado e só pergunta de "
                "volta quando a dúvida é real. O chat escreve a resposta enquanto ela é "
                "gerada, aceita imagem, PDF, planilha e áudio, e tem conversa por voz. A "
                "equipe ajusta persona, modelo e base de conhecimento pelo painel, sem "
                "deploy, e vê raciocínio, consulta e custo de cada pergunta.",
                "runs": "Três peças num monorepo: o núcleo do agente, que roda no Claude Agent SDK "
                "ou na Responses API da OpenAI conforme o modelo escolhido; uma API de chat "
                "em FastAPI com streaming por SSE; e um painel em Django. O turno vai até o "
                "fim mesmo se o cliente desconectar, e cada pessoa tem cota própria de "
                "perguntas e de custo. Versão 1.0 publicada em outubro de 2026.",
                "facts": [
                    ["Papel", "Arquitetura e desenvolvimento"],
                    ["Empresa", "Kaya Mind"],
                    ["Versão 1.0", "Outubro de 2026"],
                    ["Modelos", "Claude e OpenAI"],
                    ["Código", "Repositório privado"],
                ],
                "layers": {
                    "interface": "Chat com resposta ao vivo, anexos e voz; o painel instala como aplicativo.",
                    "app": "A API conduz o turno e grava cada evento; o Django é dono do schema.",
                    "ai": "O agente consulta, explica e tem cada turno observado.",
                    "data": "O banco de mercado só aceita leitura; a busca semântica tem índice próprio.",
                    "infra": "Contêineres Docker.",
                },
                "screen": ["Pergunta", "SQL só leitura", "Streaming", "Voz e anexos", "Custo medido"],
                "inside": {},
            },
            "zipzap": {
                "kind": "Motor de WhatsApp",
                "tagline": "Conexão e entrega para WhatsApp com entrega observável: cada estado vem com a evidência.",
                "role": "Autor",
                "problem": "Uma conexão marcada como aberta não prova que a mensagem chegou. Quem "
                "opera atendimento por WhatsApp descobre a falha pelo cliente final.",
                "built": "Um motor multi-tenant que separa aceito, enviado, confirmado pelo "
                "servidor, entregue e lido, cada estado com a sua evidência. A API "
                "responde 202 quando guardou e enfileirou; o resultado chega por webhook "
                "assinado. Envio com resultado ambíguo não é reenviado.",
                "runs": "Symfony em FrankenPHP, PostgreSQL e RabbitMQ, com runtimes em Node "
                "(Baileys) e Go (whatsmeow) atrás do mesmo contrato. Se um worker some, "
                "as contas passam para outro sem novo QR. O Diapasão é um dos "
                "consumidores.",
                "facts": [
                    ["Papel", "Autor"],
                    ["Período", "2026"],
                    ["Modelo", "SaaS multi-tenant"],
                    ["Provedores", "Baileys e whatsmeow"],
                    ["Consumidor", "Diapasão"],
                ],
                "layers": {
                    "interface": "Painel para conectar número, acompanhar a saúde e diagnosticar falha.",
                    "app": "API e painel no mesmo Symfony, em modo worker.",
                    "data": "Fila com confirmação do broker e um journal de eventos.",
                    "integrations": "Dois provedores, o mesmo contrato interno.",
                    "infra": "Stack em contêineres com deploy sem queda.",
                },
                "screen": ["Aceito", "Enviado", "Confirmado", "Entregue", "Lido"],
                "inside": {},
            },
            "duetto": {
                "kind": "Loja de instrumentos",
                "tagline": "Loja física, loja virtual e atendimento ligados no mesmo fluxo.",
                "role": "Desenvolvedor full-stack",
                "problem": "Uma loja de instrumentos com cadastro legado, fotos erradas e "
                "descrição sem ficha técnica, e um atendimento que perdia tempo com "
                "dúvidas simples.",
                "built": "A loja virtual em Django, a automação do atendimento com n8n e "
                "Chatwoot, a atualização de estoque e o enriquecimento de SEO dos "
                "produtos, além da integração com o Dolibarr para a gestão.",
                "runs": "No ar em duettomusical.com.br. Foi daqui que saiu o Diapasão: o que "
                "funcionou nesta loja virou produto para outras.",
                "facts": [
                    ["Papel", "Desenvolvedor full-stack"],
                    ["Período", "Desde março de 2025"],
                    ["Loja", "Instrumentos, áudio e vídeo"],
                    ["Atendimento", "n8n e Chatwoot"],
                    ["Gestão", "Dolibarr"],
                ],
                "layers": {
                    "interface": "A vitrine da loja.",
                    "app": "Catálogo, campanhas e SEO de produto.",
                    "data": "Tarefas em segundo plano para estoque e cadastro.",
                    "integrations": "Atendimento e gestão ligados à loja.",
                    "infra": "Contêineres em Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "optimum": {
                "kind": "Gestora de recursos",
                "tagline": "O novo site de uma gestora independente de São Paulo, com o conteúdo nas mãos da equipe.",
                "role": "Arquitetura e desenvolvimento",
                "problem": "A gestora tinha o site num construtor de páginas, sem espaço para o "
                "que ela precisa publicar: documentos, artigos e ferramentas para o "
                "investidor.",
                "built": "Site e plataforma em Django com Wagtail como CMS: a equipe publica "
                "documentos e artigos sem depender de desenvolvedor. Blog, área de "
                "documentos, calculadora e páginas institucionais.",
                "runs": "No ar em optimumcapital.com.br, em contêineres Docker, com Celery e "
                "Redis para as tarefas em segundo plano.",
                "facts": [
                    ["Papel", "Arquitetura e desenvolvimento"],
                    ["Período", "Desde março de 2026"],
                    ["Cliente", "Optimum Capital, São Paulo"],
                    ["CMS", "Wagtail"],
                ],
                "layers": {
                    "interface": "Páginas institucionais, blog, documentos e calculadora.",
                    "app": "Django com um CMS para a equipe editar sozinha.",
                    "data": "Fila e cache para o que roda fora da requisição.",
                    "infra": "Contêineres Docker.",
                },
                "screen": [],
                "inside": {},
            },
            "standup": {
                "kind": "Reuniões e atas",
                "tagline": "Atas, dailies e reuniões operacionais com edição colaborativa em tempo real.",
                "role": "Autor",
                "problem": "Ata de reunião se perde em documento solto, e uma ferramenta de "
                "gestão completa é pesada demais para registrar uma daily.",
                "built": "Uma alternativa leve para atas, dailies e reuniões operacionais: "
                "participantes, pautas, decisões e as tarefas que saem de cada reunião, "
                "com várias pessoas editando o mesmo texto ao mesmo tempo.",
                "runs": "Em desenvolvimento. Monorepo com API em Django REST Framework, frontend "
                "em Next.js e um serviço de colaboração com Hocuspocus e Yjs; Celery, "
                "Redis e PostgreSQL por trás.",
                "facts": [
                    ["Papel", "Autor"],
                    ["Status", "Em desenvolvimento"],
                    ["Tempo real", "Hocuspocus e Yjs"],
                    ["Código", "Repositório privado"],
                ],
                "layers": {
                    "interface": "Aplicação web em Next.js.",
                    "app": "API REST com autenticação por JWT.",
                    "realtime": "Um serviço próprio sincroniza o texto entre os participantes.",
                    "data": "Banco relacional, fila e cache.",
                    "infra": "Contêineres Docker.",
                },
                "screen": ["Atas", "Dailies", "Pautas e decisões", "Tarefas", "Edição em tempo real"],
                "inside": {},
            },
        },
    },
    "skills": {
        "title": "O que entra em cada mixagem.",
        "lead": "Cada linha é uma tecnologia e cada coluna é um produto: a lâmpada acesa mostra onde ela foi "
        "usada. Isole um produto para ver só a mixagem dele.",
        "solo": "Isolar produto",
        "all": "Todos",
        "used_in": "{count} de {total} produtos",
        "buses": {
            "lang": "Linguagens e frameworks",
            "data": "Dados e filas",
            "ui": "Interface",
            "ai": "IA e agentes",
            "infra": "Infraestrutura",
            "integ": "Integrações",
        },
        "labels": {
            "ai_agents": "Agentes de IA",
            "payments": "Pagamentos",
            "signature": "Assinatura digital",
            "invoicing": "Nota fiscal",
        },
    },
    "services": {
        "title": "O que eu faço.",
        "lead": "Seis barramentos da mesma mesa. Cada um já está no ar em algum produto desta página.",
        "seen_in": "No ar em",
        "more": "Ver todas as tecnologias",
        "items": {
            "lang": {
                "title": "Sistemas web sob medida",
                "body": "Aplicações em Python e Django, do SaaS multi-tenant com isolamento por cliente ao site "
                "institucional com CMS para a equipe editar sozinha.",
            },
            "data": {
                "title": "Dados, extração e filas",
                "body": "Extratores, ETL e cargas que alimentam análise; filas e tarefas em segundo plano para o "
                "que não pode travar a tela.",
            },
            "ui": {
                "title": "Interfaces de trabalho",
                "body": "Painéis, PDV, lojas e áreas logadas com HTMX, Alpine.js e Tailwind; PWA quando o produto "
                "precisa morar no celular.",
            },
            "ai": {
                "title": "IA e agentes ligados ao negócio",
                "body": "Agentes que consultam e agem nos dados da empresa, com confirmação antes de qualquer "
                "operação sensível.",
            },
            "infra": {
                "title": "Hospedagem e operação",
                "body": "Docker em Linux, servidor próprio ou painel de deploy, CI/CD e suporte. Coloco no ar e "
                "continuo cuidando.",
            },
            "integ": {
                "title": "Integrações com o que você já usa",
                "body": "WhatsApp, pagamentos, nota fiscal, assinatura digital, Mercado Livre, n8n, Chatwoot e ERP, "
                "ligados num lugar só.",
            },
        },
    },
    "about": {
        "title": "Sobre Gabriel Accioly.",
        "lead": "Engenheiro de software no Rio de Janeiro. Programo desde 2017 e levo produtos do zero até a "
        "produção, sozinho ou dentro de times enxutos.",
        "teaser_title": "Uma pessoa, todos os instrumentos.",
        "teaser": "Sou Gabriel Accioly. Programo desde 2017, fundei o Diapasão, desenvolvo os produtos da Kaya "
        "Mind e atendo projetos pela oAccioly Faz, a minha empresa.",
        "more": "Mais sobre mim",
        "story_title": "A história.",
        "story": [
            "Comecei como freelancer em janeiro de 2017, escrevendo aplicações Django, raspadores de dados, ETL e "
            "automações em Python. Desde então trabalho com várias faixas tocando ao mesmo tempo: produto "
            "próprio, empresa e cliente.",
            "Entre 2021 e 2026 automatizei o financiamento solar entre vários bancos no Volt-x, da B2W Energia "
            "Solar. Desde junho de 2022 sou cientista de dados e desenvolvedor Django na Kaya Mind, em tempo "
            "integral e remoto: respondo pela arquitetura e pelo desenvolvimento do KayaDoc (cerca de 4.000 "
            "usuários cadastrados), do KayaEducation, dos ambientes de análise por marca e do Sabo, o agente "
            "analista de mercado.",
            "Em março de 2025 entrei na Duetto Musical, uma loja de instrumentos, para fazer a loja virtual, o "
            "atendimento automatizado e a integração com a gestão. O que funcionou ali virou o Diapasão, o SaaS "
            "de varejo que fundei em junho de 2025.",
            "Uso agentes de IA (Claude Code e Codex) como parte do meu jeito de construir, com testes, revisão "
            "de segurança e validação no navegador segurando a qualidade. O código deste site é público, com as "
            "regras que os agentes seguem.",
        ],
        "fde_title": "O que é um Forward Deployed Engineer.",
        "fde": [
            "É o engenheiro que trabalha dentro da operação do cliente: senta com quem usa, entende o trabalho e "
            "entrega software rodando em produção, sem a distância entre quem pede e quem constrói.",
            "É o que faço em todos os projetos desta página. O Diapasão nasceu no balcão de uma loja de "
            "instrumentos; o Sabo, da fila de perguntas de mercado que esperavam um analista; o Desbravador, de "
            "extratores que quebravam sempre que o site de origem mudava.",
        ],
        "company_title": "oAccioly Faz.",
        "company": "A oAccioly Faz é a minha empresa, e é por ela que atendo projetos. O nome diz o que eu faço: "
        "a descoberta, a arquitetura, o código, as integrações, o deploy e o suporte.",
        "facts_title": "Ficha",
        "facts": [
            ["Nome", "Gabriel Accioly"],
            ["Assina como", "oAccioly"],
            ["Base", "Rio de Janeiro, Brasil"],
            ["Programa desde", "2017"],
            ["Formação", "Tecnólogo em Ciência de Dados"],
            ["Hoje", "Fundador do Diapasão e desenvolvedor na Kaya Mind"],
            ["Empresa", "oAccioly Faz"],
        ],
        "teaching": "Antes disso, dei aula de desenvolvimento de jogos na Microcamp (2019 a 2020).",
        "faq_title": "Perguntas frequentes.",
        "faq": [
            {
                "q": "Quem é Gabriel Accioly?",
                "a": "Gabriel Accioly é engenheiro de software brasileiro, do Rio de Janeiro, com perfil Forward "
                "Deployed. Programa desde 2017, fundou o Diapasão e desenvolve os produtos da Kaya Mind.",
            },
            {
                "q": "O que é a oAccioly Faz?",
                "a": "É a empresa de Gabriel Accioly (OACCIOLY FAZ LTDA, Pouso Alegre, MG), pela qual ele atende "
                "projetos. oAccioly é como ele assina no LinkedIn e no GitHub.",
            },
            {
                "q": "Que tipo de projeto ele faz?",
                "a": "Sistemas web sob medida e SaaS multi-tenant, extração e engenharia de dados, agentes de IA "
                "ligados aos dados do negócio, integrações (WhatsApp, pagamentos, nota fiscal, Mercado Livre, "
                "assinatura digital) e a hospedagem e o suporte de tudo isso.",
            },
            {
                "q": "Com quais tecnologias ele trabalha?",
                "a": "Python e Django no centro, com PostgreSQL, Redis, Celery, HTMX, Alpine.js e Tailwind. Também "
                "PHP com Symfony, Node.js, Go, FastAPI e Next.js quando o projeto pede. Em IA, Claude Agent SDK, "
                "MCP, Claude Code e Codex; em infraestrutura, Docker, Linux, Dokploy e CI/CD.",
            },
            {
                "q": "Ele trabalha remoto?",
                "a": "Sim. Na Kaya Mind ele trabalha em tempo integral e remoto desde 2022.",
            },
            {
                "q": "Como falar com ele?",
                "a": "Pelo LinkedIn (linkedin.com/in/oaccioly) ou pelo GitHub (github.com/o-accioly), para vaga "
                "ou para projeto.",
            },
        ],
    },
    "stack": {
        "title": "Tecnologias.",
        "lead": "O que uso, onde já está no ar e por quê. Python e Django no centro; o resto entra quando o "
        "problema pede.",
        "why": {
            "lang": "Python e Django são a base de quase tudo: rápidos de construir, fáceis de manter e com "
            "ecossistema para dados. PHP com Symfony, Node.js e Go entram quando o projeto pede, como os runtimes "
            "de WhatsApp do ZipZap; FastAPI quando a API precisa de streaming, como no Sabo.",
            "data": "PostgreSQL como banco principal, com Row-Level Security quando cada cliente precisa ficar "
            "isolado. Redis, Celery e RabbitMQ para filas; Playwright e scraping para extração; pandas para ETL; "
            "Power BI quando o cliente já analisa por lá.",
            "ui": "HTMX e Alpine.js sobre templates do servidor: interface rápida sem um segundo aplicativo para "
            "manter. Next.js e React quando a colaboração em tempo real pede, como no Standup com Yjs.",
            "ai": "Agentes que consultam e agem pelo Claude Agent SDK e por MCP, sempre com ferramentas de leitura "
            "ou confirmação antes de mexer em dinheiro ou estoque. No dia a dia, Claude Code e Codex aceleram a "
            "escrita do código.",
            "infra": "Docker em Linux, em servidor próprio (bare metal) ou com painel de deploy (Dokploy, "
            "Easypanel), e CI/CD em todo projeto.",
            "integ": "As integrações são onde o negócio vive: WhatsApp, pagamentos (Pagar.me), nota fiscal, "
            "assinatura digital A1 e A3, Mercado Livre, n8n, Chatwoot e Dolibarr.",
        },
        "ai_title": "Como uso IA para construir.",
        "ai": [
            "Trabalho com agentes de código (Claude Code e Codex) desde a primeira linha: eles escrevem, e eu "
            "decido a arquitetura, reviso, testo e valido no navegador. Testes, revisão de segurança e CI seguram "
            "a qualidade.",
            "Cada repositório tem as suas regras escritas para os agentes, num CLAUDE.md e em regras por pasta. "
            "O deste site é público: dá para ler como o trabalho é conduzido.",
            "Nos produtos, a IA tem limite claro. No Desbravador, o agente cria e conserta o extrator, mas nunca "
            "roda em produção. No Diapasão, o assistente pede confirmação antes de qualquer operação sensível. No "
            "Sabo, o banco só aceita leitura.",
        ],
        "repo": "Ler o código deste site",
        "count": "{count} tecnologias",
    },
    "process": {
        "title": "Como um problema vira sistema no ar.",
        "lead": "O mesmo caminho em todo projeto, da primeira conversa ao suporte depois do lançamento.",
        "input": "Entrada",
        "output": "Saída",
        "steps": [
            {
                "stage": "Operação",
                "title": "Sento com quem opera.",
                "body": "Começo no balcão, no consultório ou na planilha do time. O Diapasão nasceu dos "
                "problemas diários de uma loja de instrumentos.",
            },
            {
                "stage": "Descoberta",
                "title": "Separo o pedido do problema.",
                "body": "O pedido era integrar ERP e e-commerce. O problema era cadastro duplicado e estoque "
                "fora de sincronia.",
            },
            {
                "stage": "Arquitetura",
                "title": "Desenho para o segundo cliente.",
                "body": "Multi-tenant, permissão e isolamento de dados entram no primeiro dia, com teste que "
                "prova o isolamento.",
            },
            {
                "stage": "Construção",
                "title": "Escrevo, testo e reviso.",
                "body": "Python e Django no centro. Agentes como Claude Code e Codex aceleram; testes, "
                "revisão de segurança e validação no navegador seguram a qualidade.",
            },
            {
                "stage": "Integrações",
                "title": "Ligo no que o negócio já usa.",
                "body": "Pagamento, nota fiscal, assinatura digital, WhatsApp, Mercado Livre, Power BI e n8n.",
            },
            {
                "stage": "Produção",
                "title": "Coloco no ar e fico.",
                "body": "Docker e Linux em servidor próprio ou painel de deploy, com CI/CD e suporte. O "
                "produto evolui com o uso real.",
            },
        ],
    },
    "journey": {
        "title": "Desde 2017 na sessão.",
        "lead": "Várias faixas tocando ao mesmo tempo: é assim que trabalho desde o começo.",
        "now": "hoje",
        "education": "Tecnólogo em Ciência de Dados, Cruzeiro do Sul Virtual (2020 a 2022)",
        "tracks": {
            "freelance": "Desenvolvedor Python: aplicações Django, scraping, ETL e automação",
            "microcamp": "Instrutor de desenvolvimento de jogos",
            "b2w": "Volt-x: automação de financiamento solar entre vários bancos",
            "gbot": "Scraping, previsão com IA e bot no Telegram",
            "kaya": "Cientista de dados e desenvolvedor Django",
            "duetto": "Desenvolvedor full-stack",
            "diapasao": "Fundador e engenheiro",
        },
    },
    "contact": {
        "title": "Tem um problema para colocar em produção?",
        "lead": "Vaga ou projeto: me chame e conto como eu resolveria.",
        "linkedin": "Conversar no LinkedIn",
        "github": "Ver o GitHub",
        "email": "Escrever um e-mail",
        "tone": "Lá, 440 Hz",
        "tone_hint": "A nota de referência de um diapasão.",
    },
    "detail": {
        "back": "Voltar para a mesa",
        "problem": "O problema",
        "built": "O que construí",
        "runs": "Onde roda",
        "facts": "Ficha",
        "layers": "As camadas do sistema.",
        "layers_lead": "Abra uma unidade do rack para ver o que ela faz neste produto.",
        "inside": "Por dentro.",
        "inside_lead": "O painel de verdade, gravado na loja de demonstração Casa do Som. Todos os dados são "
        "fictícios.",
        "previous": "Anterior",
        "next": "Próximo",
        "stack": "Tecnologias",
        "cycle": "Pausar ou retomar o movimento do monitor",
        "no_shots": "Este produto não tem página pública. O monitor mostra uma ilustração do que ele faz.",
        "inside_pending": "As telas internas deste produto ficam atrás de login e não aparecem aqui.",
        "demo_screens": "O monitor mostra o painel rodando localmente com dados de demonstração.",
        "highlights": "Destaques",
        "screens": "As telas.",
        "screens_lead": "Cada página capturada, no tamanho grande e no celular. Abra uma para ver a página inteira.",
        "screens_demo": "Telas do produto rodando localmente com dados de demonstração. Nenhum dado é real.",
        "full_page": "Ver a página inteira",
        "visit": "Visitar {host}",
    },
    "layers": {
        "interface": "Interface",
        "app": "Aplicação",
        "realtime": "Tempo real",
        "runtime": "Execução",
        "data": "Dados e filas",
        "ai": "Inteligência artificial",
        "integrations": "Integrações",
        "infra": "Infraestrutura",
    },
    "brand": {
        "makes": [
            "a descoberta.",
            "a arquitetura.",
            "o código.",
            "as integrações.",
            "o deploy.",
            "o suporte.",
            "do problema à produção.",
        ],
        "hint": "oAccioly Faz é o nome da minha empresa, e também o que eu faço.",
    },
    "footer": {
        "built": "Feito com Django e Tailwind CSS.",
        "source": "Código aberto no GitHub",
        "location": "Rio de Janeiro, Brasil",
    },
    "errors": {
        "not_found_title": "Essa faixa não está na sessão.",
        "not_found_body": "O endereço não existe ou mudou de lugar.",
    },
    "parts": {
        "Ambiente por marca": "Ambiente por marca",
        "Anexos": "Anexos",
        "Atendimento": "Atendimento",
        "Base de conhecimento": "Base de conhecimento",
        "CI em runner próprio": "CI em runner próprio",
        "Calculadora": "Calculadora",
        "Campanhas": "Campanhas",
        "Catálogo": "Catálogo",
        "Chat com streaming": "Chat com streaming",
        "Configuração em JSONB": "Configuração em JSONB",
        "Correção automática": "Correção automática",
        "Cotas por pessoa": "Cotas por pessoa",
        "Cotas por plano": "Cotas por plano",
        "Deploy sem queda": "Deploy sem queda",
        "Documentos": "Documentos",
        "Estoque": "Estoque",
        "Extratores": "Extratores",
        "Frete": "Frete",
        "Gráficos incorporados": "Gráficos incorporados",
        "Journal de eventos": "Journal de eventos",
        "Lease por número": "Lease por número",
        "Loja virtual": "Loja virtual",
        "Loja white-label": "Loja white-label",
        "Marcas": "Marcas",
        "Modo voz": "Modo voz",
        "Médicos": "Médicos",
        "Nota fiscal": "Nota fiscal",
        "Notas de entrada": "Notas de entrada",
        "Pacientes": "Pacientes",
        "Pagamentos": "Pagamentos",
        "Painel": "Painel",
        "Permissões por papel": "Permissões por papel",
        "Pool de navegadores": "Pool de navegadores",
        "Projetos e papéis": "Projetos e papéis",
        "SEO de produto": "SEO de produto",
        "SQL somente leitura": "SQL somente leitura",
        "Site institucional": "Site institucional",
        "Terminal no navegador": "Terminal no navegador",
        "Trilhas de aprendizagem": "Trilhas de aprendizagem",
        "Webhooks assinados": "Webhooks assinados",
    },
}
