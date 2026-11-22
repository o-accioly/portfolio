"""English copy. Mirrors `pt_br.py` key by key."""

CONTENT = {
    "meta": {
        "title": "Gabriel Accioly (oAccioly) · Software engineer, from problem to production",
        "description": "Gabriel Accioly (oAccioly) is a full-stack, Forward Deployed software engineer. "
        "Live products like Diapasão, KayaDoc and ZipZap, built and run end to end.",
        "job_title": "Full-stack software engineer",
        "og_locale": "en_US",
        "about_title": "About Gabriel Accioly (oAccioly) · Software engineer in Rio de Janeiro",
        "about_description": "Who Gabriel Accioly is: software engineer since 2017, founder of Diapasão, developer "
        "at Kaya Mind, owner of oAccioly Faz. Career, education and way of working.",
        "projects_title": "Gabriel Accioly's projects · SaaS, AI, data and integrations in production",
        "projects_description": "Products Gabriel Accioly built and runs: Diapasão, KayaDoc, Kaya Dashboard, "
        "KayaEducation, Sabo, ZipZap, Desbravador and more, with real screens.",
        "stack_title": "Gabriel Accioly's technologies · Python, Django, PostgreSQL, AI and Docker",
        "stack_description": "Technologies Gabriel Accioly uses and where each runs: Python, Django, PostgreSQL, "
        "HTMX, AI agents, Docker, WhatsApp, payments and invoicing.",
        "project_title": "{name}: {kind} · A project by Gabriel Accioly",
    },
    "nav": {
        "skip": "Skip to content",
        "label": "Sections",
        "projects": "Projects",
        "skills": "Skills",
        "process": "Process",
        "journey": "Journey",
        "contact": "Contact",
        "language": "Language",
        "home": "Home",
        "about": "About",
        "stack": "Technologies",
        "breadcrumb": "You are here",
    },
    "theme": {"label": "Studio lights", "auto": "Auto", "light": "On", "dark": "Dimmed"},
    "hero": {
        "title": "From problem to production.",
        "name": "Gabriel Accioly",
        "role": "Full-stack software engineer with a Forward Deployed profile.",
        "lead": "I go into the operation, build the system and put it in production: discovery, architecture, "
        "code, integrations, hosting and support. I've covered the whole path since 2017.",
        "audiences": [
            {
                "label": "Job",
                "text": "Forward Deployed Engineer or senior full-stack, for teams that need a product in production.",
            },
            {
                "label": "Project",
                "text": "A custom system for your business, from diagnosis to support after launch.",
            },
        ],
        "open": "Open {name}",
        "contact": "Get in touch",
        "about": "About me",
        "monitor": "Monitor",
        "tape": "Projects on the monitor",
        "on_stage": "On stage",
        "no_page": "no public page",
    },
    "devices": {
        "label": "Screen size",
        "ultrawide": "Ultrawide",
        "desktop": "Desktop",
        "laptop": "Laptop",
        "tablet": "Tablet",
        "phone": "Phone",
    },
    "projects": {
        "title": "Every product is a track.",
        "lead": "Each track is a product I work on. Open one to see the screens at every size and the layers "
        "of the system.",
        "open": "Open project",
        "live": "See it live",
        "repo": "View repository",
        "since": "since {year}",
        "illustration": "Illustration. This product has no public page.",
        "all": "All projects, in detail",
        "page_title": "Projects.",
        "page_lead": "{count} products, each with the problem, what I built, where it runs and the real screens. "
        "The live ones have a link; the private ones are shown running with demonstration data.",
        "stack": "Technologies",
        "screens_count": "{count} screens captured",
        "highlights": {
            "diapasao": [
                "Inventory, POS, online store, CRM and invoicing in a single system",
                "AI in product records, in inbound invoices and in the first contact on WhatsApp",
                "Sabo assistant that looks things up and takes action, with confirmation before sensitive operations",
                "Each store isolated by Row-Level Security, with an isolation test in CI",
                "2 stores and 20 users in production",
            ],
            "kayadoc": [
                "Separate experiences for doctors, patients and brands",
                "Payments through Pagar.me",
                "Digital signature with A1 and A3 certificates",
                "PWA with passkeys, second factor and Google sign-in",
                "About 4,000 registered users",
            ],
            "kayamind": [
                "Building the products since 2022, full-time and remote",
                "KayaDoc, KayaEducation, Kaya Dashboard and Sabo",
                "About 20 data extractors a month at the start",
                "Extraction method taught to the team, which went on to build its own",
            ],
            "kaya-dashboard": [
                "One analytics environment per brand",
                "Reports embedded through the official Power BI API",
                "Each brand sees only its own numbers",
                "Team console to manage brands and dashboards",
            ],
            "kayaeducation": [
                "White-label LMS: each brand with its own identity",
                "Courses organized into learning paths",
                "Student area and brand panel",
                "Django, HTMX and Tailwind",
            ],
            "desbravador": [
                "Extractor created in a conversation with a Claude agent, in a terminal inside the browser",
                "Deterministic execution in Playwright, with no language model in the critical path",
                "Quality measured on every run",
                "Up to 3 automatic repair attempts before calling a person",
                "Versioned configuration, with a canary before promotion",
            ],
            "sabo": [
                "Market questions in plain Portuguese, with numbers traceable back to the query",
                "Read-only database tools",
                "Live answers, attachments and voice conversation",
                "Runs on the Claude Agent SDK or on OpenAI's Responses API",
                "Quota and cost measured per person; version 1.0 in October 2026",
            ],
            "zipzap": [
                "Five delivery states, each with its own evidence",
                "API that answers 202 and delivers the result through a signed webhook",
                "Node (Baileys) and Go (whatsmeow) runtimes behind the same contract",
                "Accounts move to another worker without a new QR code",
                "Used by Diapasão",
            ],
            "duetto": [
                "Online store in Django",
                "Automated customer service with n8n and Chatwoot",
                "Up-to-date inventory and enriched product SEO",
                "Integration with Dolibarr for management",
                "Where Diapasão was born",
            ],
            "optimum": [
                "Site and platform in Django with Wagtail",
                "The team publishes documents and articles without depending on a developer",
                "Blog, document area and a calculator for investors",
                "Celery and Redis for background tasks",
            ],
            "standup": [
                "Minutes, dailies and operational meetings",
                "Agendas, decisions and the tasks that come out of each meeting",
                "Real-time collaborative editing with Hocuspocus and Yjs",
                "Next.js on the interface, Django REST Framework on the API",
            ],
        },
        "pages": {
            "diapasao": {
                "home": "Diapasão home page",
                "crm": "CRM",
                "loja": "Online store",
                "assistente": "AI assistant",
            },
            "kayadoc": {"home": "Home page", "funcionalidades": "Features", "planos": "Plans"},
            "kayamind": {"home": "Home page", "relatorios": "Reports"},
            "kaya-dashboard": {
                "home": "Environment of a fictional brand",
                "console": "Team console",
                "paineis": "Brand dashboards",
                "eventos": "Usage events",
                "entrar": "Login screen",
            },
            "kayaeducation": {
                "home": "Student area",
                "aula": "Lesson",
                "conteudo": "Course content",
                "engajamento": "Engagement",
                "entrar": "Login screen",
                "painel": "Brand panel",
                "trilha": "Learning path",
            },
            "desbravador": {
                "home": "Overview",
                "painel": "Project panel",
                "extrator": "Extractor",
                "execucoes": "Runs",
                "dados": "Extracted data",
            },
            "sabo": {
                "home": "Chat with the agent",
                "consultas": "Advanced mode, with the SQL",
                "custo": "Usage and cost",
            },
            "zipzap": {
                "home": "Panel overview",
                "conversas": "Conversations",
                "instancia": "Connected number",
                "webhooks": "Webhooks",
            },
            "duetto": {"home": "Store home page", "categoria": "Mixing console category"},
            "optimum": {"home": "Home page", "quem-somos": "About us", "calculadora": "Calculator"},
            "standup": {
                "home": "Home",
                "operacional": "Operational meeting",
                "daily": "Daily",
                "ata": "Minutes",
            },
        },
        "items": {
            "diapasao": {
                "kind": "Retail SaaS",
                "tagline": "The whole store in one system: inventory, POS, online store, CRM and invoicing.",
                "role": "Founder and engineer",
                "problem": "A store with a large catalog lives on integrating its ERP with its "
                "e-commerce, and the sync always breaks in the same place: duplicate "
                "product records, mismatched stock, slow customer service. The first "
                "system was born inside a musical instrument store. When other "
                "stores asked for the same thing, I rebuilt it all to serve any "
                "retailer.",
                "built": "A Django platform that brings together inventory, POS, online store, "
                "CRM and invoicing. AI improves the product records (description, spec "
                "sheet, image), categorizes inbound invoices and answers the first "
                "contact on WhatsApp. Sabo, an assistant wired to the store's data, "
                "looks things up and takes action, and asks for confirmation before "
                "any sensitive operation.",
                "runs": "Each store is a tenant isolated by Row-Level Security in PostgreSQL, "
                "with an isolation test as a required CI step. It runs on bare metal "
                "with Docker. Today it serves 2 stores and 20 users.",
                "facts": [
                    ["Role", "Founder and engineer"],
                    ["Period", "Since June 2025"],
                    ["In use", "2 stores, 20 users"],
                    ["Isolation", "Row-Level Security per store"],
                    ["Where it runs", "Bare metal, Docker"],
                ],
                "layers": {
                    "interface": "Four surfaces for four audiences: the site, the store "
                    "under the retailer's own brand, the back-office panel "
                    "and the platform console.",
                    "app": "Thin Django apps, one per responsibility. Every screen is "
                    "born with the role's permission and the plan gate.",
                    "data": "A single schema. The database guarantees that one store never reads another's rows.",
                    "ai": "AI that acts: the assistant executes inside the system, "
                    "always with confirmation on operations that touch money or "
                    "stock.",
                    "integrations": "What the store already uses, connected in one "
                    "place, so nobody types anything twice.",
                    "infra": "Container deploys on a self-owned server, with CI running on a self-hosted runner.",
                },
                "screen": [],
                "inside": {
                    "atendimento": "WhatsApp customer service with the bot",
                    "pdv": "Counter sale (POS)",
                    "produtos": "Product records and inventory",
                    "crm": "Kanban CRM",
                    "fatura": "Invoice and fiscal note",
                    "mercadolivre": "Mercado Livre listings",
                },
            },
            "kayadoc": {
                "kind": "Wellness platform",
                "tagline": "Doctors, patients and brands on the same platform, with payments and digital signatures.",
                "role": "Architecture and development · Kaya Mind",
                "problem": "Three audiences with different needs had to live in the same "
                "product: the doctor who prescribes and signs, the patient who "
                "follows along and pays, the brand that takes part. Each with its own "
                "experience, and none able to see the others' data.",
                "built": "A multi-tenant Django platform with dedicated experiences for doctors, "
                "patients and brands. Payments through Pagar.me and digital signatures "
                "with A1 and A3 certificates (VIDaaS, BirdID, Syn and pyHanko). It "
                "works as a PWA, with passkeys, two-factor authentication and Google "
                "sign-in.",
                "runs": "About 4,000 registered users. It runs on Docker on Linux, deployed "
                "through Easypanel, with CI/CD and operational alerts via n8n, Teams and "
                "ntfy.",
                "facts": [
                    ["Role", "Architecture and development"],
                    ["Company", "Kaya Mind, since 2022"],
                    ["Users", "About 4,000 registered"],
                    ["Payments", "Pagar.me"],
                    ["Signature", "A1 and A3 certificates"],
                ],
                "layers": {
                    "interface": "One experience per audience, installable on the phone.",
                    "app": "Strong authentication from sign-up: passkey, second factor and SSO.",
                    "data": "Relational database, cache and queues for whatever can't block the screen.",
                    "integrations": "Payments and legally valid signatures, inside the flow.",
                    "infra": "Linux containers with automated deploys.",
                },
                "screen": [],
                "inside": {},
            },
            "kayamind": {
                "kind": "Cannabis market data",
                "tagline": "The company where I've been responsible for product development since 2022.",
                "role": "Data scientist and Django developer",
                "problem": "A market intelligence startup needs fresh data every week and a "
                "product in production at the same time. With a lean team, the same "
                "person handles extraction, architecture, code and deploys for "
                "several projects in parallel.",
                "built": "Kaya's products: KayaDoc, KayaEducation (a white-label LMS with "
                "learning paths) and the per-brand analytics environments. Early on, "
                "about 20 data extractors a month. Later I taught the method to the "
                "team, who started building their own, and I kept the hardest "
                "extractions.",
                "runs": "I work full-time and remote. Integrations and automated alerts with "
                "n8n, Microsoft Teams and ntfy. Delivery is sped up by agents (Claude "
                "Code and Codex), with CI/CD, tests and security review.",
                "facts": [
                    ["Role", "Data scientist and Django developer"],
                    ["Period", "Since June 2022"],
                    ["Arrangement", "Full-time, remote"],
                    ["Extractors", "About 20 a month early on"],
                ],
                "layers": {
                    "app": "Three Django products maintained in parallel.",
                    "data": "Collecting, cleaning and loading the data that feeds the analyses.",
                    "integrations": "Automation between the systems and the team.",
                    "infra": "Linux containers.",
                },
                "screen": [],
                "inside": {},
            },
            "kaya-dashboard": {
                "kind": "Per-brand analytics",
                "tagline": "Each brand logs in and sees only its own charts, served by the official Power BI API.",
                "role": "Architecture and development · Kaya Mind",
                "problem": "Client brands needed to check their own numbers without being "
                "sent a spreadsheet and without seeing the competition.",
                "built": "Multi-tenant analytics environments in Django. Reports are "
                "embedded through the official Power BI API, and each brand gets "
                "its own charts and insights.",
                "runs": "Access by login at dashboard.kayamind.com. It runs on Docker on "
                "Linux, deployed through Easypanel.",
                "facts": [
                    ["Role", "Architecture and development"],
                    ["Company", "Kaya Mind, since 2022"],
                    ["Charts", "Official Power BI API"],
                    ["Model", "One environment per brand"],
                ],
                "layers": {
                    "interface": "One environment per brand.",
                    "app": "Django decides who sees which report.",
                    "data": "Reports embedded through the official API.",
                    "infra": "Linux containers.",
                },
                "screen": [],
                "inside": {},
            },
            "kayaeducation": {
                "kind": "White-label LMS",
                "tagline": "A course platform with learning paths and a dedicated environment for each brand.",
                "role": "Architecture and development · Kaya Mind",
                "problem": "Each brand wanted to offer courses under its own identity "
                "without building a learning platform from scratch.",
                "built": "A white-label LMS in Django: learning paths and educational "
                "environments that each brand customizes.",
                "runs": "Live at kayaeducation.com.br, behind a login. It runs in Docker on Linux.",
                "facts": [
                    ["Role", "Architecture and development"],
                    ["Company", "Kaya Mind, since 2022"],
                    ["Model", "White-label, one environment per brand"],
                    ["Content", "Learning paths"],
                ],
                "layers": {
                    "interface": "A learning environment with each brand's identity.",
                    "app": "Courses organized into paths.",
                    "data": "Relational database and cache.",
                    "infra": "Linux containers.",
                },
                "screen": [],
                "inside": {},
            },
            "desbravador": {
                "kind": "Web extraction with an AI agent",
                "tagline": "Data extractors created in a conversation with an agent and run "
                "with no AI on the critical path.",
                "role": "Author",
                "problem": "A data extractor breaks every time the source site changes, and "
                "writing each one by hand does not scale.",
                "built": "A platform where an extractor starts as a conversation with a "
                "Claude agent, in a terminal inside the browser: the agent probes "
                "the site and generates a deterministic config. Execution runs on "
                "Playwright with no language model, cheap and predictable. Quality "
                "is measured on every run. When it drops, the system tries to fix "
                "itself up to three times before calling a person.",
                "runs": "Django with Channels for the WebSocket terminal, Postgres with "
                "JSONB, Celery and Redis for scheduling, and a pool of browsers in "
                "containers. Config is data, never code: nothing generated by a "
                "model is executed in production. Everything is versioned and goes "
                "through a canary before promotion.",
                "facts": [
                    ["Role", "Author"],
                    ["Period", "Since May 2026"],
                    ["Execution", "Deterministic, no LLM"],
                    ["Fixing", "Up to 3 automatic attempts"],
                    ["Code", "Private repository"],
                ],
                "layers": {
                    "interface": "A dashboard of extractors, runs and blockers, with an embedded terminal.",
                    "app": "Projects with members and roles.",
                    "ai": "The agent creates and repairs. It never runs in production.",
                    "runtime": "A fixed, tested executor consumes the config.",
                    "data": "Central state, scheduling and extracted data with idempotency.",
                    "infra": "Long-lived browsers in containers.",
                },
                "screen": [
                    "Agent discovery",
                    "Deterministic runs",
                    "Quality checks",
                    "Auto-fix",
                    "Versions and canary",
                ],
                "inside": {},
            },
            "sabo": {
                "kind": "Market analyst agent",
                "tagline": "Market questions asked in plain Portuguese, answered with numbers traceable to the query.",
                "role": "Architecture and development · Kaya Mind",
                "problem": "A brand manager needs market numbers to decide on price, launch and "
                "territory, and cannot wait for an analyst to assemble each answer.",
                "built": "An agent that answers questions about the medical cannabis market from "
                "import and pharmacy dispensing data. It queries the database through "
                "read-only tools, explains the result and only asks back when the doubt is "
                "real. The chat writes the answer as it is generated, takes images, PDFs, "
                "spreadsheets and audio, and has a voice conversation mode. The team tunes "
                "persona, model and knowledge base from the back office, with no deploy, "
                "and sees the reasoning, query and cost of every question.",
                "runs": "Three parts in a monorepo: the agent core, running on the Claude Agent SDK "
                "or the OpenAI Responses API depending on the chosen model; a FastAPI chat "
                "API streaming over SSE; and a Django back office. A turn runs to the end "
                "even if the client disconnects, and each person has their own quota of "
                "questions and cost. Version 1.0 shipped in October 2026.",
                "facts": [
                    ["Role", "Architecture and development"],
                    ["Company", "Kaya Mind"],
                    ["Version 1.0", "October 2026"],
                    ["Models", "Claude and OpenAI"],
                    ["Code", "Private repository"],
                ],
                "layers": {
                    "interface": "Chat with live answers, attachments and voice; the back office installs as an app.",
                    "app": "The API drives the turn and records every event; Django owns the schema.",
                    "ai": "The agent queries, explains and has every turn observed.",
                    "data": "The market database is read-only; semantic search has its own index.",
                    "infra": "Docker containers.",
                },
                "screen": ["Question", "Read-only SQL", "Streaming", "Voice and files", "Measured cost"],
                "inside": {},
            },
            "zipzap": {
                "kind": "WhatsApp engine",
                "tagline": "Connection and delivery for WhatsApp, with observable delivery: every "
                "state comes with its evidence.",
                "role": "Author",
                "problem": "A connection marked as open doesn't prove the message arrived. "
                "Whoever runs customer service over WhatsApp finds out about the "
                "failure from the end customer.",
                "built": "A multi-tenant engine that separates accepted, sent, confirmed by the "
                "server, delivered and read, each state with its own evidence. The API "
                "returns 202 once it has stored and queued the message. The result "
                "arrives by signed webhook. A send with an ambiguous result is not "
                "resent.",
                "runs": "Symfony on FrankenPHP, PostgreSQL and RabbitMQ, with runtimes in Node "
                "(Baileys) and Go (whatsmeow) behind the same contract. If a worker "
                "disappears, its accounts move to another one without a new QR code. "
                "Diapasão is one of the consumers.",
                "facts": [
                    ["Role", "Author"],
                    ["Period", "2026"],
                    ["Model", "Multi-tenant SaaS"],
                    ["Providers", "Baileys and whatsmeow"],
                    ["Consumer", "Diapasão"],
                ],
                "layers": {
                    "interface": "A panel to connect a number, watch its health and diagnose failures.",
                    "app": "API and panel in the same Symfony app, in worker mode.",
                    "data": "A queue with broker confirmation and an event journal.",
                    "integrations": "Two providers, the same internal contract.",
                    "infra": "Containerized stack with zero-downtime deploys.",
                },
                "screen": ["Accepted", "Sent", "Confirmed", "Delivered", "Read"],
                "inside": {},
            },
            "duetto": {
                "kind": "Musical instrument store",
                "tagline": "Physical store, online store and customer service connected in the same flow.",
                "role": "Full-stack developer",
                "problem": "A musical instrument store with legacy product records, wrong photos "
                "and descriptions with no spec sheet, and a customer service team "
                "losing time on simple questions.",
                "built": "The online store in Django, customer service automation with n8n and "
                "Chatwoot, stock updates and SEO enrichment for the products, plus the "
                "integration with Dolibarr for management.",
                "runs": "Live at duettomusical.com.br. This is where Diapasão came from: what "
                "worked in this store became a product for others.",
                "facts": [
                    ["Role", "Full-stack developer"],
                    ["Period", "Since March 2025"],
                    ["Store", "Instruments, audio and video"],
                    ["Customer service", "n8n and Chatwoot"],
                    ["Management", "Dolibarr"],
                ],
                "layers": {
                    "interface": "The storefront.",
                    "app": "Catalog, campaigns and product SEO.",
                    "data": "Background tasks for stock and product records.",
                    "integrations": "Customer service and management connected to the store.",
                    "infra": "Linux containers.",
                },
                "screen": [],
                "inside": {},
            },
            "optimum": {
                "kind": "Asset manager",
                "tagline": "The new site of an independent asset manager in São Paulo, with the "
                "content in the team's hands.",
                "role": "Architecture and development",
                "problem": "The firm's site lived in a page builder, with no room for what it "
                "needs to publish: documents, articles and tools for investors.",
                "built": "A site and platform in Django with Wagtail as the CMS: the team "
                "publishes documents and articles without a developer. Blog, document "
                "area, calculator and company pages.",
                "runs": "Live at optimumcapital.com.br, in Docker containers, with Celery and "
                "Redis for background jobs.",
                "facts": [
                    ["Role", "Architecture and development"],
                    ["Period", "Since March 2026"],
                    ["Client", "Optimum Capital, São Paulo"],
                    ["CMS", "Wagtail"],
                ],
                "layers": {
                    "interface": "Company pages, blog, documents and calculator.",
                    "app": "Django with a CMS the team edits by itself.",
                    "data": "Queue and cache for what runs outside the request.",
                    "infra": "Docker containers.",
                },
                "screen": [],
                "inside": {},
            },
            "standup": {
                "kind": "Meetings and minutes",
                "tagline": "Minutes, dailies and operational meetings with real-time collaborative editing.",
                "role": "Author",
                "problem": "Meeting minutes get lost in loose documents, and a full project "
                "management tool is too heavy for recording a daily.",
                "built": "A lightweight alternative for minutes, dailies and operational "
                "meetings: attendees, agendas, decisions and the tasks that come out of "
                "each meeting, with several people editing the same text at once.",
                "runs": "In development. A monorepo with a Django REST Framework API, a Next.js "
                "frontend and a collaboration service on Hocuspocus and Yjs, with "
                "Celery, Redis and PostgreSQL behind them.",
                "facts": [
                    ["Role", "Author"],
                    ["Status", "In development"],
                    ["Real time", "Hocuspocus and Yjs"],
                    ["Code", "Private repository"],
                ],
                "layers": {
                    "interface": "A Next.js web app.",
                    "app": "A REST API with JWT authentication.",
                    "realtime": "A dedicated service syncs the text between participants.",
                    "data": "Relational database, queue and cache.",
                    "infra": "Docker containers.",
                },
                "screen": ["Minutes", "Dailies", "Agendas and decisions", "Tasks", "Real-time editing"],
                "inside": {},
            },
        },
    },
    "skills": {
        "title": "What goes into each mix.",
        "lead": "Each row is a technology and each column is a product: a lit lamp shows where it was used. Solo "
        "a product to see only its mix.",
        "solo": "Solo a product",
        "all": "All",
        "used_in": "{count} of {total} products",
        "buses": {
            "lang": "Languages and frameworks",
            "data": "Data and queues",
            "ui": "Interface",
            "ai": "AI and agents",
            "infra": "Infrastructure",
            "integ": "Integrations",
        },
        "labels": {
            "ai_agents": "AI agents",
            "payments": "Payments",
            "signature": "Digital signature",
            "invoicing": "Invoicing",
        },
    },
    "services": {
        "title": "What I do.",
        "lead": "Six buses on the same desk. Each one is already live in some product on this page.",
        "seen_in": "Live in",
        "more": "See all technologies",
        "items": {
            "lang": {
                "title": "Custom web systems",
                "body": "Applications in Python and Django, from multi-tenant SaaS with per-client isolation to "
                "company websites with a CMS the team edits on its own.",
            },
            "data": {
                "title": "Data, extraction and queues",
                "body": "Extractors, ETL and loads that feed analysis; queues and background tasks for whatever "
                "must not freeze the screen.",
            },
            "ui": {
                "title": "Work interfaces",
                "body": "Dashboards, POS, stores and logged-in areas with HTMX, Alpine.js and Tailwind; a PWA when "
                "the product needs to live on the phone.",
            },
            "ai": {
                "title": "AI and agents wired to the business",
                "body": "Agents that look up and act on the company's data, with confirmation before any sensitive "
                "operation.",
            },
            "infra": {
                "title": "Hosting and operations",
                "body": "Docker on Linux, own server or deploy panel, CI/CD and support. I put it in production and "
                "keep looking after it.",
            },
            "integ": {
                "title": "Integrations with what you already use",
                "body": "WhatsApp, payments, invoicing, digital signature, Mercado Livre, n8n, Chatwoot and ERP, "
                "connected in one place.",
            },
        },
    },
    "about": {
        "title": "About Gabriel Accioly.",
        "lead": "Software engineer in Rio de Janeiro. I've been programming since 2017 and I take products from "
        "zero to production, on my own or inside lean teams.",
        "teaser_title": "One person, every instrument.",
        "teaser": "I'm Gabriel Accioly. I've been programming since 2017, I founded Diapasão, I build Kaya "
        "Mind's products and I take on projects through oAccioly Faz, my company.",
        "more": "More about me",
        "story_title": "The story.",
        "story": [
            "I started as a freelancer in January 2017, writing Django applications, data scrapers, ETL and "
            "Python automations. Since then I've worked with several tracks playing at once: my own product, "
            "a company and clients.",
            "Between 2021 and 2026 I automated solar financing across several banks at Volt-x, by B2W Energia "
            "Solar. Since June 2022 I've been a data scientist and Django developer at Kaya Mind, full-time and "
            "remote: I'm responsible for the architecture and development of KayaDoc (about 4,000 registered "
            "users), KayaEducation, the per-brand analytics environments and Sabo, the market analyst agent.",
            "In March 2025 I joined Duetto Musical, an instrument store, to build the online store, the "
            "automated customer service and the integration with its management system. What worked there "
            "became Diapasão, the retail SaaS I founded in June 2025.",
            "I use AI agents (Claude Code and Codex) as part of how I build, with tests, security review and "
            "browser validation holding up the quality. The code for this site is public, along with the rules "
            "the agents follow.",
        ],
        "fde_title": "What a Forward Deployed Engineer is.",
        "fde": [
            "The engineer who works inside the client's operation: sits with the people who use the system, "
            "understands the work and delivers software running in production, with no gap between who asks "
            "and who builds.",
            "It's what I do on every project on this page. Diapasão was born at the counter of an instrument "
            "store; Sabo, from the queue of market questions waiting for an analyst; Desbravador, from "
            "extractors that broke every time the source site changed.",
        ],
        "company_title": "oAccioly Faz.",
        "company": "oAccioly Faz is my company, and it's through it that I take on projects. The name says what "
        "I do: discovery, architecture, code, integrations, deployment and support.",
        "facts_title": "Fact sheet",
        "facts": [
            ["Name", "Gabriel Accioly"],
            ["Goes by", "oAccioly"],
            ["Based in", "Rio de Janeiro, Brazil"],
            ["Programming since", "2017"],
            ["Education", "Technologist degree in Data Science"],
            ["Today", "Founder of Diapasão and developer at Kaya Mind"],
            ["Company", "oAccioly Faz"],
        ],
        "teaching": "Before that, I taught game development at Microcamp (2019 to 2020).",
        "faq_title": "Frequently asked questions.",
        "faq": [
            {
                "q": "Who is Gabriel Accioly?",
                "a": "Gabriel Accioly is a Brazilian software engineer from Rio de Janeiro with a Forward "
                "Deployed profile. He has been programming since 2017, founded Diapasão and builds Kaya Mind's "
                "products.",
            },
            {
                "q": "What is oAccioly Faz?",
                "a": "It's Gabriel Accioly's company (OACCIOLY FAZ LTDA, Pouso Alegre, MG), through which he takes "
                "on projects. oAccioly is the name he goes by on LinkedIn and GitHub.",
            },
            {
                "q": "What kind of projects does he take on?",
                "a": "Custom web systems and multi-tenant SaaS, data extraction and engineering, AI agents wired "
                "to business data, integrations (WhatsApp, payments, invoicing, Mercado Livre, digital "
                "signature) and the hosting and support of all of it.",
            },
            {
                "q": "Which technologies does he work with?",
                "a": "Python and Django at the core, with PostgreSQL, Redis, Celery, HTMX, Alpine.js and Tailwind. "
                "Also PHP with Symfony, Node.js, Go, FastAPI and Next.js when the project calls for it. In AI, "
                "Claude Agent SDK, MCP, Claude Code and Codex; in infrastructure, Docker, Linux, Dokploy and CI/CD.",
            },
            {
                "q": "Does he work remotely?",
                "a": "Yes. At Kaya Mind he has worked full-time and remotely since 2022.",
            },
            {
                "q": "How can I reach him?",
                "a": "Through LinkedIn (linkedin.com/in/oaccioly) or GitHub (github.com/o-accioly), for a job "
                "or for a project.",
            },
        ],
    },
    "stack": {
        "title": "Technologies.",
        "lead": "What I use, where it's already live and why. Python and Django at the core; the rest comes in "
        "when the problem calls for it.",
        "why": {
            "lang": "Python and Django are the base of almost everything: quick to build, easy to maintain and "
            "with an ecosystem for data. PHP with Symfony, Node.js and Go come in when the project calls for "
            "it, like ZipZap's WhatsApp runtimes; FastAPI when the API needs streaming, as in Sabo.",
            "data": "PostgreSQL as the main database, with Row-Level Security when each client must stay "
            "isolated. Redis, Celery and RabbitMQ for queues; Playwright and scraping for extraction; pandas for "
            "ETL; Power BI when the client already does its analysis there.",
            "ui": "HTMX and Alpine.js on top of server templates: a fast interface without a second application "
            "to maintain. Next.js and React when real-time collaboration calls for it, as in Standup with Yjs.",
            "ai": "Agents that look things up and act through the Claude Agent SDK and MCP, always with read-only "
            "tools or confirmation before touching money or inventory. Day to day, Claude Code and Codex speed "
            "up writing the code.",
            "infra": "Docker on Linux, on my own server (bare metal) or with a deploy panel (Dokploy, "
            "Easypanel), and CI/CD on every project.",
            "integ": "Integrations are where the business lives: WhatsApp, payments (Pagar.me), invoicing, "
            "A1 and A3 digital signature, Mercado Livre, n8n, Chatwoot and Dolibarr.",
        },
        "ai_title": "How I use AI to build.",
        "ai": [
            "I work with coding agents (Claude Code and Codex) from the first line: they write, and I decide "
            "the architecture, review, test and validate in the browser. Tests, security review and CI hold up "
            "the quality.",
            "Each repository has its own rules written for the agents, in a CLAUDE.md and in per-folder rules. "
            "This site's is public: you can read how the work is run.",
            "In the products, AI has clear limits. In Desbravador, the agent creates and fixes the extractor, "
            "but never runs in production. In Diapasão, the assistant asks for confirmation before any "
            "sensitive operation. In Sabo, the database only accepts reads.",
        ],
        "repo": "Read this site's code",
        "count": "{count} technologies",
    },
    "process": {
        "title": "How a problem becomes a system in production.",
        "lead": "The same path on every project, from the first conversation to support after launch.",
        "input": "Input",
        "output": "Output",
        "steps": [
            {
                "stage": "Operation",
                "title": "I sit with the people who run it.",
                "body": "I start at the counter, in the doctor's office or in the team's spreadsheet. "
                "Diapasão was born from the daily problems of a musical instrument store.",
            },
            {
                "stage": "Discovery",
                "title": "I separate the request from the problem.",
                "body": "The request was to integrate ERP and e-commerce. The problem was duplicate product "
                "records and stock out of sync.",
            },
            {
                "stage": "Architecture",
                "title": "I design for the second customer.",
                "body": "Multi-tenancy, permissions and data isolation go in on day one, with a test that "
                "proves the isolation.",
            },
            {
                "stage": "Build",
                "title": "I write, test and review.",
                "body": "Python and Django at the core. Agents like Claude Code and Codex speed things up. "
                "Tests, security review and in-browser validation hold the quality.",
            },
            {
                "stage": "Integrations",
                "title": "I plug into what the business already uses.",
                "body": "Payments, invoicing, digital signatures, WhatsApp, Mercado Livre, Power BI and n8n.",
            },
            {
                "stage": "Production",
                "title": "I ship it and I stay.",
                "body": "Docker and Linux on a self-owned server or a deploy panel, with CI/CD and support. "
                "The product evolves with real use.",
            },
        ],
    },
    "journey": {
        "title": "In the session since 2017.",
        "lead": "Several tracks playing at once: that's how I've worked from the start.",
        "now": "now",
        "education": "Associate degree (technologist) in Data Science, Cruzeiro do Sul Virtual (2020 to 2022)",
        "tracks": {
            "freelance": "Python developer: Django applications, scraping, ETL and automation",
            "microcamp": "Game development instructor",
            "b2w": "Volt-x: solar financing automation across several banks",
            "gbot": "Scraping, AI forecasting and a Telegram bot",
            "kaya": "Data scientist and Django developer",
            "duetto": "Full-stack developer",
            "diapasao": "Founder and engineer",
        },
    },
    "contact": {
        "title": "Got a problem to put into production?",
        "lead": "A job or a project: reach out and I'll tell you how I'd solve it.",
        "linkedin": "Talk on LinkedIn",
        "github": "See my GitHub",
        "email": "Write me an email",
        "tone": "A, 440 Hz",
        "tone_hint": "The reference note of a tuning fork.",
    },
    "detail": {
        "back": "Back to the console",
        "problem": "The problem",
        "built": "What I built",
        "runs": "Where it runs",
        "facts": "Spec sheet",
        "layers": "The layers of the system.",
        "layers_lead": "Open a rack unit to see what it does in this product.",
        "inside": "Inside.",
        "inside_lead": "The real back office, recorded in the Casa do Som demo store. All data is fictional.",
        "previous": "Previous",
        "next": "Next",
        "stack": "Technologies",
        "cycle": "Pause or resume the monitor's motion",
        "no_shots": "This product has no public page. The monitor shows an illustration of what it does.",
        "inside_pending": "This product's internal screens sit behind a login and are not shown here.",
        "demo_screens": "The monitor shows the panel running locally with demonstration data.",
        "highlights": "Highlights",
        "screens": "The screens.",
        "screens_lead": "Every captured page, at full size and on the phone. Open one to see the whole page.",
        "screens_demo": "Screens of the product running locally with demonstration data. None of the data is real.",
        "full_page": "See the whole page",
        "visit": "Visit {host}",
    },
    "layers": {
        "interface": "Interface",
        "app": "Application",
        "realtime": "Real time",
        "runtime": "Runtime",
        "data": "Data and queues",
        "ai": "Artificial intelligence",
        "integrations": "Integrations",
        "infra": "Infrastructure",
    },
    "brand": {
        "makes": [
            "discovery.",
            "architecture.",
            "code.",
            "integrations.",
            "deploys.",
            "support.",
            "from problem to production.",
        ],
        "hint": "oAccioly Faz is my company. In Portuguese it also reads “Accioly does it”.",
    },
    "footer": {
        "built": "Built with Django and Tailwind CSS.",
        "source": "Open source on GitHub",
        "location": "Rio de Janeiro, Brazil",
    },
    "errors": {
        "not_found_title": "That track isn't in the session.",
        "not_found_body": "The address doesn't exist or has moved.",
    },
    "parts": {
        "Ambiente por marca": "One environment per brand",
        "Anexos": "Attachments",
        "Atendimento": "Customer service",
        "Base de conhecimento": "Knowledge base",
        "CI em runner próprio": "CI on a self-hosted runner",
        "Calculadora": "Calculator",
        "Campanhas": "Campaigns",
        "Catálogo": "Catalog",
        "Chat com streaming": "Streaming chat",
        "Configuração em JSONB": "Config as JSONB",
        "Correção automática": "Auto-fix",
        "Cotas por pessoa": "Per-person quotas",
        "Cotas por plano": "Plan quotas",
        "Deploy sem queda": "Zero-downtime deploy",
        "Documentos": "Documents",
        "Estoque": "Inventory",
        "Extratores": "Extractors",
        "Frete": "Shipping",
        "Gráficos incorporados": "Embedded charts",
        "Journal de eventos": "Event journal",
        "Lease por número": "Lease per number",
        "Loja virtual": "Online store",
        "Loja white-label": "White-label store",
        "Marcas": "Brands",
        "Modo voz": "Voice mode",
        "Médicos": "Physicians",
        "Nota fiscal": "Invoicing",
        "Notas de entrada": "Inbound invoices",
        "Pacientes": "Patients",
        "Pagamentos": "Payments",
        "Painel": "Back office",
        "Permissões por papel": "Role-based permissions",
        "Pool de navegadores": "Browser pool",
        "Projetos e papéis": "Projects and roles",
        "SEO de produto": "Product SEO",
        "SQL somente leitura": "Read-only SQL",
        "Site institucional": "Company site",
        "Terminal no navegador": "In-browser terminal",
        "Trilhas de aprendizagem": "Learning paths",
        "Webhooks assinados": "Signed webhooks",
    },
}
