"""Spanish copy. Mirrors `pt_br.py` key by key."""

CONTENT = {
    "meta": {
        "title": "Gabriel Accioly (oAccioly) · Ingeniero de software, del problema a producción",
        "description": "Gabriel Accioly (oAccioly), ingeniero full-stack con perfil Forward Deployed: productos "
        "reales en producción, como Diapasão, KayaDoc y ZipZap, de punta a punta.",
        "job_title": "Ingeniero de software full-stack",
        "og_locale": "es_ES",
        "about_title": "Sobre Gabriel Accioly (oAccioly) · Ingeniero de software en Río de Janeiro",
        "about_description": "Gabriel Accioly: ingeniero de software desde 2017, fundador de Diapasão, "
        "desarrollador en Kaya Mind y dueño de oAccioly Faz. Trayectoria, formación y método.",
        "projects_title": "Proyectos de Gabriel Accioly · SaaS, IA, datos e integraciones en producción",
        "projects_description": "Productos que Gabriel Accioly construyó y opera: Diapasão, KayaDoc, Kaya "
        "Dashboard, KayaEducation, Sabo, ZipZap, Desbravador y más, con pantallas y tecnologías.",
        "stack_title": "Tecnologías de Gabriel Accioly · Python, Django, PostgreSQL, IA y Docker",
        "stack_description": "Tecnologías que usa Gabriel Accioly y dónde corre cada una: Python, Django, "
        "PostgreSQL, HTMX, agentes de IA, Docker, WhatsApp, pagos y factura electrónica.",
        "project_title": "{name}: {kind} · Proyecto de Gabriel Accioly",
    },
    "nav": {
        "skip": "Saltar al contenido",
        "label": "Secciones",
        "projects": "Proyectos",
        "skills": "Habilidades",
        "process": "Proceso",
        "journey": "Trayectoria",
        "contact": "Contacto",
        "language": "Idioma",
        "home": "Inicio",
        "about": "Sobre mí",
        "stack": "Tecnologías",
        "breadcrumb": "Estás en",
    },
    "theme": {"label": "Luz del estudio", "auto": "Automática", "light": "Encendida", "dark": "Baja"},
    "hero": {
        "title": "Del problema a producción.",
        "name": "Gabriel Accioly",
        "role": "Ingeniero de software full-stack, con perfil Forward Deployed.",
        "lead": "Me meto en la operación, construyo el sistema y lo pongo en producción: descubrimiento, "
        "arquitectura, código, integraciones, hosting y soporte. Hago el camino completo desde 2017.",
        "audiences": [
            {
                "label": "Empleo",
                "text": "Forward Deployed Engineer o full-stack sénior, para equipos que necesitan producto en "
                "producción.",
            },
            {
                "label": "Proyecto",
                "text": "Un sistema a medida para tu negocio, del diagnóstico al soporte después del lanzamiento.",
            },
        ],
        "open": "Abrir {name}",
        "contact": "Hablemos",
        "about": "Sobre mí",
        "monitor": "Monitor",
        "tape": "Proyectos en el monitor",
        "on_stage": "En escena",
        "no_page": "sin página pública",
    },
    "devices": {
        "label": "Tamaño de pantalla",
        "ultrawide": "Ultrawide",
        "desktop": "Monitor",
        "laptop": "Laptop",
        "tablet": "Tablet",
        "phone": "Celular",
    },
    "projects": {
        "title": "Cada producto, una pista.",
        "lead": "Cada pista es un producto en el que trabajo. Abre una para ver las pantallas en cada tamaño y "
        "las capas del sistema.",
        "open": "Abrir proyecto",
        "live": "Ver en línea",
        "repo": "Ver repositorio",
        "since": "desde {year}",
        "illustration": "Ilustración. Este producto no tiene página pública.",
        "all": "Todos los proyectos, en detalle",
        "page_title": "Proyectos.",
        "page_lead": "{count} productos, cada uno con el problema, lo que construí, dónde corre y las pantallas "
        "reales. Los que están en línea tienen enlace; los privados aparecen funcionando con datos de demostración.",
        "stack": "Tecnologías",
        "screens_count": "{count} pantallas capturadas",
        "highlights": {
            "diapasao": [
                "Inventario, punto de venta, tienda en línea, CRM y factura electrónica en un solo sistema",
                "IA en el registro de productos, en las facturas de compra y en el primer contacto por WhatsApp",
                "Asistente Sabo que consulta y actúa, con confirmación antes de cada operación sensible",
                "Cada tienda aislada con Row-Level Security, con prueba de aislamiento en el CI",
                "2 tiendas y 20 usuarios en producción",
            ],
            "kayadoc": [
                "Experiencias separadas para médicos, pacientes y marcas",
                "Pagos con Pagar.me",
                "Firma digital con certificado A1 y A3",
                "PWA con passkeys, segundo factor e inicio de sesión con Google",
                "Cerca de 4.000 usuarios registrados",
            ],
            "kayamind": [
                "Desarrollo de los productos desde 2022, a tiempo completo y remoto",
                "KayaDoc, KayaEducation, Kaya Dashboard y Sabo",
                "Cerca de 20 extractores de datos por mes al principio",
                "Método de extracción enseñado al equipo, que empezó a construir los suyos",
            ],
            "kaya-dashboard": [
                "Un entorno de análisis para cada marca",
                "Informes incrustados con la API oficial de Power BI",
                "Cada marca ve solo sus propios números",
                "Consola del equipo para gestionar marcas y paneles",
            ],
            "kayaeducation": [
                "LMS white-label: cada marca con su propia identidad",
                "Cursos organizados en rutas de aprendizaje",
                "Área del alumno y panel de la marca",
                "Django, HTMX y Tailwind",
            ],
            "desbravador": [
                "Extractor creado en una conversación con un agente Claude, en una terminal dentro del navegador",
                "Ejecución determinística en Playwright, sin modelo de lenguaje en el camino crítico",
                "Calidad medida en cada ejecución",
                "Hasta 3 intentos de corrección automática antes de llamar a una persona",
                "Configuración versionada, con canario antes de promover",
            ],
            "sabo": [
                "Preguntas de mercado en portugués, con números rastreables hasta la consulta",
                "Herramientas de base de datos de solo lectura",
                "Respuesta en vivo, adjuntos y conversación por voz",
                "Corre en el Claude Agent SDK o en la Responses API de OpenAI",
                "Cuota y costo medidos por persona; versión 1.0 en octubre de 2026",
            ],
            "zipzap": [
                "Cinco estados de entrega, cada uno con su evidencia",
                "API que responde 202 y entrega el resultado por webhook firmado",
                "Runtimes en Node (Baileys) y Go (whatsmeow) detrás del mismo contrato",
                "Las cuentas pasan a otro worker sin un nuevo QR",
                "Usado por Diapasão",
            ],
            "duetto": [
                "Tienda en línea en Django",
                "Atención automatizada con n8n y Chatwoot",
                "Inventario actualizado y SEO de producto enriquecido",
                "Integración con Dolibarr para la gestión",
                "Donde nació Diapasão",
            ],
            "optimum": [
                "Sitio y plataforma en Django con Wagtail",
                "El equipo publica documentos y artículos sin depender de un desarrollador",
                "Blog, área de documentos y calculadora para el inversor",
                "Celery y Redis para las tareas en segundo plano",
            ],
            "standup": [
                "Actas, dailies y reuniones operativas",
                "Temas, decisiones y las tareas que salen de cada reunión",
                "Edición colaborativa en tiempo real con Hocuspocus y Yjs",
                "Next.js en la interfaz, Django REST Framework en la API",
            ],
        },
        "pages": {
            "diapasao": {
                "home": "Página inicial de Diapasão",
                "crm": "CRM",
                "loja": "Tienda en línea",
                "assistente": "Asistente de IA",
            },
            "kayadoc": {"home": "Página inicial", "funcionalidades": "Funcionalidades", "planos": "Planes"},
            "kayamind": {"home": "Página inicial", "relatorios": "Informes"},
            "kaya-dashboard": {
                "home": "Entorno de una marca ficticia",
                "console": "Consola del equipo",
                "paineis": "Paneles de la marca",
                "eventos": "Eventos de uso",
                "entrar": "Pantalla de inicio de sesión",
            },
            "kayaeducation": {
                "home": "Área del alumno",
                "aula": "Clase",
                "conteudo": "Contenido del curso",
                "engajamento": "Participación",
                "entrar": "Pantalla de inicio de sesión",
                "painel": "Panel de la marca",
                "trilha": "Ruta de aprendizaje",
            },
            "desbravador": {
                "home": "Visión general",
                "painel": "Panel del proyecto",
                "extrator": "Extractor",
                "execucoes": "Ejecuciones",
                "dados": "Datos extraídos",
            },
            "sabo": {"home": "Chat con el agente", "consultas": "Modo avanzado, con el SQL", "custo": "Uso y costo"},
            "zipzap": {
                "home": "Visión general del panel",
                "conversas": "Conversaciones",
                "instancia": "Número conectado",
                "webhooks": "Webhooks",
            },
            "duetto": {"home": "Página inicial de la tienda", "categoria": "Categoría de mesas de mezcla"},
            "optimum": {"home": "Página inicial", "quem-somos": "Quiénes somos", "calculadora": "Calculadora"},
            "standup": {
                "home": "Inicio",
                "operacional": "Reunión operativa",
                "daily": "Daily",
                "ata": "Acta",
            },
        },
        "items": {
            "diapasao": {
                "kind": "SaaS para comercio minorista",
                "tagline": "La tienda entera en un solo sistema: inventario, punto de venta, "
                "tienda en línea, CRM y facturación electrónica.",
                "role": "Fundador e ingeniero",
                "problem": "Una tienda con catálogo grande vive integrando el ERP con el "
                "e-commerce, y la sincronización se rompe siempre en el mismo lugar: "
                "productos duplicados, inventario que no coincide, atención lenta. "
                "El primer sistema nació dentro de una tienda de instrumentos; "
                "cuando otras tiendas pidieron lo mismo, rehíce todo para que "
                "sirviera a cualquier comercio minorista.",
                "built": "Una plataforma en Django que reúne inventario, punto de venta, tienda "
                "en línea, CRM y facturación electrónica. La IA mejora los datos de "
                "cada producto (descripción, ficha técnica, imagen), clasifica las "
                "facturas de compra y responde el primer contacto por WhatsApp. Sabo, "
                "el asistente conectado a los datos de la tienda, consulta y actúa, y "
                "pide confirmación antes de cualquier operación sensible.",
                "runs": "Cada tienda es un tenant aislado con Row-Level Security en PostgreSQL, "
                "y la prueba de aislamiento es un paso obligatorio del CI. Corre en "
                "bare metal con Docker; hoy atiende 2 tiendas y 20 usuarios.",
                "facts": [
                    ["Rol", "Fundador e ingeniero"],
                    ["Período", "Desde junio de 2025"],
                    ["En uso", "2 tiendas, 20 usuarios"],
                    ["Aislamiento", "Row-Level Security por tienda"],
                    ["Dónde corre", "Bare metal, Docker"],
                ],
                "layers": {
                    "interface": "Cuatro superficies para cuatro públicos: el sitio, la "
                    "tienda con la marca del comerciante, el panel de "
                    "trabajo y la consola de la plataforma.",
                    "app": "Apps Django delgadas, una por responsabilidad. Cada pantalla "
                    "nace con el permiso del rol y el límite del plan.",
                    "data": "Un solo esquema; la base de datos garantiza que una tienda nunca lea la fila de otra.",
                    "ai": "IA que actúa: el asistente ejecuta en el sistema, siempre con "
                    "confirmación en las operaciones que tocan dinero o "
                    "inventario.",
                    "integrations": "Lo que la tienda ya usa, conectado en un solo "
                    "lugar, para que nadie escriba lo mismo dos veces.",
                    "infra": "Despliegue por contenedores en servidor propio, con el CI "
                    "corriendo en un runner de la casa.",
                },
                "screen": [],
                "inside": {
                    "atendimento": "Atención por WhatsApp con el bot",
                    "pdv": "Venta en mostrador (POS)",
                    "produtos": "Registro de producto e inventario",
                    "crm": "CRM en kanban",
                    "fatura": "Factura y factura electrónica",
                    "mercadolivre": "Publicaciones en Mercado Livre",
                },
            },
            "kayadoc": {
                "kind": "Plataforma de bienestar",
                "tagline": "Médicos, pacientes y marcas en la misma plataforma, con pagos y firma digital.",
                "role": "Arquitectura y desarrollo · Kaya Mind",
                "problem": "Tres públicos con necesidades distintas tenían que convivir en el "
                "mismo producto: el médico que prescribe y firma, el paciente que "
                "hace seguimiento y paga, la marca que participa. Cada uno con su "
                "propia experiencia y sin ver los datos del otro.",
                "built": "Plataforma multi-tenant en Django con experiencias dedicadas para "
                "médicos, pacientes y marcas. Pagos con Pagar.me y firma digital con "
                "certificado A1 y A3 (VIDaaS, BirdID, Syn y pyHanko). Funciona como "
                "PWA, con passkeys, autenticación de dos factores e inicio de sesión "
                "con Google.",
                "runs": "Cerca de 4.000 usuarios registrados. Corre en Docker sobre Linux, con "
                "despliegue por Easypanel, CI/CD y alertas operativas por n8n, Teams y "
                "ntfy.",
                "facts": [
                    ["Rol", "Arquitectura y desarrollo"],
                    ["Empresa", "Kaya Mind, desde 2022"],
                    ["Usuarios", "Cerca de 4.000 registrados"],
                    ["Pagos", "Pagar.me"],
                    ["Firma", "Certificado A1 y A3"],
                ],
                "layers": {
                    "interface": "Una experiencia para cada público, instalable en el celular.",
                    "app": "Autenticación fuerte desde el registro: passkey, segundo factor y SSO.",
                    "data": "Base de datos relacional, caché y colas para lo que no puede bloquear la pantalla.",
                    "integrations": "Pago y firma con validez legal, dentro del flujo.",
                    "infra": "Contenedores en Linux con despliegue automatizado.",
                },
                "screen": [],
                "inside": {},
            },
            "kayamind": {
                "kind": "Datos del mercado de cannabis",
                "tagline": "La empresa donde estoy a cargo del desarrollo de los productos desde 2022.",
                "role": "Científico de datos y desarrollador Django",
                "problem": "Una startup de inteligencia de mercado necesita datos nuevos cada "
                "semana y producto en producción al mismo tiempo. Con un equipo "
                "reducido, la misma persona se encarga de la extracción, la "
                "arquitectura, el código y el despliegue de varios proyectos en "
                "paralelo.",
                "built": "Los productos de Kaya: KayaDoc, KayaEducation (un LMS white-label con "
                "rutas de aprendizaje) y los entornos de análisis por marca. Al "
                "principio, cerca de 20 extractores de datos por mes; después le "
                "enseñé el método al equipo, que empezó a construir los suyos, y me "
                "quedé con las extracciones más difíciles.",
                "runs": "Trabajo a tiempo completo y remoto. Integraciones y alertas "
                "automatizadas con n8n, Microsoft Teams y ntfy; entrega acelerada por "
                "agentes (Claude Code y Codex), con CI/CD, pruebas y revisión de "
                "seguridad.",
                "facts": [
                    ["Rol", "Científico de datos y desarrollador Django"],
                    ["Período", "Desde junio de 2022"],
                    ["Modalidad", "Tiempo completo, remoto"],
                    ["Extractores", "Cerca de 20 por mes al principio"],
                ],
                "layers": {
                    "app": "Tres productos Django mantenidos en paralelo.",
                    "data": "Recolección, limpieza y carga de los datos que alimentan los análisis.",
                    "integrations": "Automatización entre los sistemas y el equipo.",
                    "infra": "Contenedores en Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "kaya-dashboard": {
                "kind": "Análisis por marca",
                "tagline": "Cada marca entra y ve solo sus propios gráficos, servidos por la API oficial de Power BI.",
                "role": "Arquitectura y desarrollo · Kaya Mind",
                "problem": "Las marcas clientes necesitaban consultar sus propios números "
                "sin recibir una hoja de cálculo y sin ver los de la "
                "competencia.",
                "built": "Entornos de análisis multi-tenant en Django. Los informes se "
                "incrustan con la API oficial de Power BI, y cada marca recibe "
                "sus gráficos y sus insights.",
                "runs": "Acceso con inicio de sesión en dashboard.kayamind.com. Corre en "
                "Docker sobre Linux, con despliegue por Easypanel.",
                "facts": [
                    ["Rol", "Arquitectura y desarrollo"],
                    ["Empresa", "Kaya Mind, desde 2022"],
                    ["Gráficos", "API oficial de Power BI"],
                    ["Modelo", "Un entorno por marca"],
                ],
                "layers": {
                    "interface": "Un entorno para cada marca.",
                    "app": "Django decide quién ve qué informe.",
                    "data": "Informes incrustados con la API oficial.",
                    "infra": "Contenedores en Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "kayaeducation": {
                "kind": "LMS white-label",
                "tagline": "Plataforma de cursos con rutas de aprendizaje y un entorno propio para cada marca.",
                "role": "Arquitectura y desarrollo · Kaya Mind",
                "problem": "Cada marca quería ofrecer cursos con su propia identidad, sin "
                "montar una plataforma de enseñanza desde cero.",
                "built": "Un LMS white-label en Django: rutas de aprendizaje y entornos "
                "educativos que cada marca personaliza.",
                "runs": "En línea en kayaeducation.com.br, con acceso por inicio de "
                "sesión. Corre en Docker sobre Linux.",
                "facts": [
                    ["Rol", "Arquitectura y desarrollo"],
                    ["Empresa", "Kaya Mind, desde 2022"],
                    ["Modelo", "White-label, un entorno por marca"],
                    ["Contenido", "Rutas de aprendizaje"],
                ],
                "layers": {
                    "interface": "Un entorno de enseñanza con la identidad de cada marca.",
                    "app": "Cursos organizados en rutas.",
                    "data": "Base de datos relacional y caché.",
                    "infra": "Contenedores en Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "desbravador": {
                "kind": "Extracción web con agente de IA",
                "tagline": "Extractores de datos creados en una conversación con un agente y "
                "ejecutados sin IA en el camino crítico.",
                "role": "Autor",
                "problem": "Un extractor de datos se rompe cada vez que cambia el sitio de "
                "origen, y escribir cada uno a mano no escala.",
                "built": "Una plataforma donde el extractor nace de una conversación con un "
                "agente Claude, en una terminal dentro del navegador: el agente "
                "sondea el sitio y genera una configuración determinística. La "
                "ejecución corre en Playwright, sin modelo de lenguaje, barata y "
                "predecible. La calidad se mide en cada ejecución. Cuando cae, el "
                "sistema intenta corregirse hasta tres veces antes de llamar a una "
                "persona.",
                "runs": "Django con Channels para la terminal por WebSocket, Postgres con "
                "JSONB, Celery y Redis para la programación y un pool de navegadores "
                "en contenedores. La configuración es dato, nunca código: nada "
                "generado por un modelo se ejecuta en producción. Todo se versiona y "
                "pasa por canario antes de promoverse.",
                "facts": [
                    ["Rol", "Autor"],
                    ["Período", "Desde mayo de 2026"],
                    ["Ejecución", "Determinística, sin LLM"],
                    ["Corrección", "Hasta 3 intentos automáticos"],
                    ["Código", "Repositorio privado"],
                ],
                "layers": {
                    "interface": "Panel de extractores, ejecuciones y bloqueos, con una terminal integrada.",
                    "app": "Proyectos con miembros y roles.",
                    "ai": "El agente crea y repara. Nunca corre en producción.",
                    "runtime": "Un ejecutor fijo y probado consume la configuración.",
                    "data": "Estado central, programación y datos extraídos con idempotencia.",
                    "infra": "Navegadores de larga duración en contenedores.",
                },
                "screen": [
                    "Descubrimiento con agente",
                    "Ejecución determinística",
                    "Control de calidad",
                    "Corrección automática",
                    "Versión y canario",
                ],
                "inside": {},
            },
            "sabo": {
                "kind": "Agente analista de mercado",
                "tagline": "Preguntas de mercado en portugués, respondidas con números rastreables hasta la consulta.",
                "role": "Arquitectura y desarrollo · Kaya Mind",
                "problem": "Quien gestiona una marca necesita números de mercado para decidir "
                "precio, lanzamiento y territorio, y no puede esperar a que un analista "
                "arme cada respuesta.",
                "built": "Un agente que responde sobre el mercado de cannabis medicinal a partir de "
                "los datos de importación y de dispensación en farmacias. Consulta la base "
                "con herramientas de solo lectura, explica el resultado y solo vuelve a "
                "preguntar cuando la duda es real. El chat escribe la respuesta mientras "
                "se genera, acepta imagen, PDF, hoja de cálculo y audio, y tiene "
                "conversación por voz. El equipo ajusta persona, modelo y base de "
                "conocimiento desde el panel, sin deploy, y ve el razonamiento, la "
                "consulta y el costo de cada pregunta.",
                "runs": "Tres piezas en un monorepo: el núcleo del agente, que corre en el Claude "
                "Agent SDK o en la Responses API de OpenAI según el modelo elegido; una API "
                "de chat en FastAPI con streaming por SSE; y un panel en Django. El turno "
                "llega hasta el final aunque el cliente se desconecte, y cada persona tiene "
                "su propia cuota de preguntas y de costo. Versión 1.0 publicada en octubre "
                "de 2026.",
                "facts": [
                    ["Rol", "Arquitectura y desarrollo"],
                    ["Empresa", "Kaya Mind"],
                    ["Versión 1.0", "Octubre de 2026"],
                    ["Modelos", "Claude y OpenAI"],
                    ["Código", "Repositorio privado"],
                ],
                "layers": {
                    "interface": "Chat con respuesta en vivo, adjuntos y voz; el panel se instala como aplicación.",
                    "app": "La API conduce el turno y registra cada evento; Django es dueño del esquema.",
                    "ai": "El agente consulta, explica y tiene cada turno observado.",
                    "data": "La base de mercado solo admite lectura; la búsqueda semántica tiene su propio índice.",
                    "infra": "Contenedores Docker.",
                },
                "screen": ["Pregunta", "SQL solo lectura", "Streaming", "Voz y adjuntos", "Costo medido"],
                "inside": {},
            },
            "zipzap": {
                "kind": "Motor de WhatsApp",
                "tagline": "Conexión y entrega para WhatsApp con entrega observable: cada estado "
                "llega con su evidencia.",
                "role": "Autor",
                "problem": "Una conexión marcada como abierta no prueba que el mensaje llegó. "
                "Quien opera atención por WhatsApp se entera de la falla por el "
                "cliente final.",
                "built": "Un motor multi-tenant que separa aceptado, enviado, confirmado por el "
                "servidor, entregado y leído, cada estado con su evidencia. La API "
                "responde 202 cuando guardó y encoló el mensaje; el resultado llega por "
                "webhook firmado. Un envío con resultado ambiguo no se reenvía.",
                "runs": "Symfony sobre FrankenPHP, PostgreSQL y RabbitMQ, con runtimes en Node "
                "(Baileys) y Go (whatsmeow) detrás del mismo contrato. Si un worker "
                "desaparece, las cuentas pasan a otro sin un nuevo QR. Diapasão es uno de "
                "los consumidores.",
                "facts": [
                    ["Rol", "Autor"],
                    ["Período", "2026"],
                    ["Modelo", "SaaS multi-tenant"],
                    ["Proveedores", "Baileys y whatsmeow"],
                    ["Consumidor", "Diapasão"],
                ],
                "layers": {
                    "interface": "Panel para conectar un número, seguir su salud y diagnosticar fallas.",
                    "app": "API y panel en el mismo Symfony, en modo worker.",
                    "data": "Cola con confirmación del broker y un journal de eventos.",
                    "integrations": "Dos proveedores, el mismo contrato interno.",
                    "infra": "Stack en contenedores con despliegue sin caídas.",
                },
                "screen": ["Aceptado", "Enviado", "Confirmado", "Entregado", "Leído"],
                "inside": {},
            },
            "duetto": {
                "kind": "Tienda de instrumentos",
                "tagline": "Tienda física, tienda en línea y atención al cliente conectadas en el mismo flujo.",
                "role": "Desarrollador full-stack",
                "problem": "Una tienda de instrumentos con un catálogo heredado, fotos "
                "equivocadas y descripciones sin ficha técnica, y una atención al "
                "cliente que perdía tiempo con dudas simples.",
                "built": "La tienda en línea en Django, la automatización de la atención con n8n "
                "y Chatwoot, la actualización de inventario y el enriquecimiento de SEO "
                "de los productos, además de la integración con Dolibarr para la "
                "gestión.",
                "runs": "En línea en duettomusical.com.br. De aquí salió Diapasão: lo que "
                "funcionó en esta tienda se convirtió en producto para otras.",
                "facts": [
                    ["Rol", "Desarrollador full-stack"],
                    ["Período", "Desde marzo de 2025"],
                    ["Tienda", "Instrumentos, audio y video"],
                    ["Atención", "n8n y Chatwoot"],
                    ["Gestión", "Dolibarr"],
                ],
                "layers": {
                    "interface": "La vitrina de la tienda.",
                    "app": "Catálogo, campañas y SEO de producto.",
                    "data": "Tareas en segundo plano para inventario y catálogo.",
                    "integrations": "Atención y gestión conectadas a la tienda.",
                    "infra": "Contenedores en Linux.",
                },
                "screen": [],
                "inside": {},
            },
            "optimum": {
                "kind": "Gestora de activos",
                "tagline": "El nuevo sitio de una gestora independiente de São Paulo, con el "
                "contenido en manos del equipo.",
                "role": "Arquitectura y desarrollo",
                "problem": "La gestora tenía su sitio en un constructor de páginas, sin espacio "
                "para lo que necesita publicar: documentos, artículos y herramientas "
                "para el inversor.",
                "built": "Sitio y plataforma en Django con Wagtail como CMS: el equipo publica "
                "documentos y artículos sin depender de un desarrollador. Blog, área de "
                "documentos, calculadora y páginas institucionales.",
                "runs": "En línea en optimumcapital.com.br, en contenedores Docker, con Celery y "
                "Redis para las tareas en segundo plano.",
                "facts": [
                    ["Rol", "Arquitectura y desarrollo"],
                    ["Período", "Desde marzo de 2026"],
                    ["Cliente", "Optimum Capital, São Paulo"],
                    ["CMS", "Wagtail"],
                ],
                "layers": {
                    "interface": "Páginas institucionales, blog, documentos y calculadora.",
                    "app": "Django con un CMS que el equipo edita por su cuenta.",
                    "data": "Cola y caché para lo que corre fuera de la petición.",
                    "infra": "Contenedores Docker.",
                },
                "screen": [],
                "inside": {},
            },
            "standup": {
                "kind": "Reuniones y actas",
                "tagline": "Actas, dailies y reuniones operativas con edición colaborativa en tiempo real.",
                "role": "Autor",
                "problem": "El acta de una reunión se pierde en un documento suelto, y una "
                "herramienta de gestión completa es demasiado pesada para registrar "
                "una daily.",
                "built": "Una alternativa ligera para actas, dailies y reuniones operativas: "
                "participantes, temas, decisiones y las tareas que salen de cada "
                "reunión, con varias personas editando el mismo texto a la vez.",
                "runs": "En desarrollo. Monorepo con API en Django REST Framework, frontend en "
                "Next.js y un servicio de colaboración con Hocuspocus y Yjs, con Celery, "
                "Redis y PostgreSQL por detrás.",
                "facts": [
                    ["Rol", "Autor"],
                    ["Estado", "En desarrollo"],
                    ["Tiempo real", "Hocuspocus y Yjs"],
                    ["Código", "Repositorio privado"],
                ],
                "layers": {
                    "interface": "Aplicación web en Next.js.",
                    "app": "API REST con autenticación por JWT.",
                    "realtime": "Un servicio propio sincroniza el texto entre los participantes.",
                    "data": "Base de datos relacional, cola y caché.",
                    "infra": "Contenedores Docker.",
                },
                "screen": ["Actas", "Dailies", "Temas y decisiones", "Tareas", "Edición en tiempo real"],
                "inside": {},
            },
        },
    },
    "skills": {
        "title": "Lo que entra en cada mezcla.",
        "lead": "Cada fila es una tecnología y cada columna es un producto: la luz encendida muestra dónde se "
        "usó. Aísla un producto para ver solo su mezcla.",
        "solo": "Aislar producto",
        "all": "Todos",
        "used_in": "{count} de {total} productos",
        "buses": {
            "lang": "Lenguajes y frameworks",
            "data": "Datos y colas",
            "ui": "Interfaz",
            "ai": "IA y agentes",
            "infra": "Infraestructura",
            "integ": "Integraciones",
        },
        "labels": {
            "ai_agents": "Agentes de IA",
            "payments": "Pagos",
            "signature": "Firma digital",
            "invoicing": "Factura electrónica",
        },
    },
    "services": {
        "title": "Lo que hago.",
        "lead": "Seis buses de la misma mesa. Cada uno ya está en producción en algún producto de esta página.",
        "seen_in": "En producción en",
        "more": "Ver todas las tecnologías",
        "items": {
            "lang": {
                "title": "Sistemas web a medida",
                "body": "Aplicaciones en Python y Django, del SaaS multi-tenant con aislamiento por cliente al sitio "
                "institucional con CMS para que el equipo edite por su cuenta.",
            },
            "data": {
                "title": "Datos, extracción y colas",
                "body": "Extractores, ETL y cargas que alimentan el análisis; colas y tareas en segundo plano para "
                "lo que no puede bloquear la pantalla.",
            },
            "ui": {
                "title": "Interfaces de trabajo",
                "body": "Paneles, punto de venta, tiendas y áreas privadas con HTMX, Alpine.js y Tailwind; PWA "
                "cuando el producto necesita vivir en el celular.",
            },
            "ai": {
                "title": "IA y agentes conectados al negocio",
                "body": "Agentes que consultan y actúan sobre los datos de la empresa, con confirmación antes de "
                "cualquier operación sensible.",
            },
            "infra": {
                "title": "Hosting y operación",
                "body": "Docker en Linux, servidor propio o panel de despliegue, CI/CD y soporte. Lo pongo en "
                "producción y sigo cuidándolo.",
            },
            "integ": {
                "title": "Integraciones con lo que ya usas",
                "body": "WhatsApp, pagos, factura electrónica, firma digital, Mercado Livre, n8n, Chatwoot y ERP, "
                "conectados en un solo lugar.",
            },
        },
    },
    "about": {
        "title": "Sobre Gabriel Accioly.",
        "lead": "Ingeniero de software en Río de Janeiro. Programo desde 2017 y llevo productos de cero a "
        "producción, solo o dentro de equipos reducidos.",
        "teaser_title": "Una persona, todos los instrumentos.",
        "teaser": "Soy Gabriel Accioly. Programo desde 2017, fundé Diapasão, desarrollo los productos de Kaya "
        "Mind y atiendo proyectos a través de oAccioly Faz, mi empresa.",
        "more": "Más sobre mí",
        "story_title": "La historia.",
        "story": [
            "Empecé como freelancer en enero de 2017, escribiendo aplicaciones Django, scrapers de datos, ETL y "
            "automatizaciones en Python. Desde entonces trabajo con varias pistas sonando al mismo tiempo: "
            "producto propio, empresa y cliente.",
            "Entre 2021 y 2026 automaticé el financiamiento solar entre varios bancos en Volt-x, de B2W Energia "
            "Solar. Desde junio de 2022 soy científico de datos y desarrollador Django en Kaya Mind, a tiempo "
            "completo y remoto: estoy a cargo de la arquitectura y el desarrollo de KayaDoc (cerca de 4.000 "
            "usuarios registrados), de KayaEducation, de los entornos de análisis por marca y de Sabo, el agente "
            "analista de mercado.",
            "En marzo de 2025 entré a Duetto Musical, una tienda de instrumentos, para hacer la tienda en línea, "
            "la atención automatizada y la integración con la gestión. Lo que funcionó ahí se convirtió en "
            "Diapasão, el SaaS para comercio minorista que fundé en junio de 2025.",
            "Uso agentes de IA (Claude Code y Codex) como parte de mi forma de construir, con pruebas, revisión "
            "de seguridad y validación en el navegador sosteniendo la calidad. El código de este sitio es "
            "público, con las reglas que siguen los agentes.",
        ],
        "fde_title": "Qué es un Forward Deployed Engineer.",
        "fde": [
            "Es el ingeniero que trabaja dentro de la operación del cliente: se sienta con quien usa el sistema, "
            "entiende el trabajo y entrega software funcionando en producción, sin la distancia entre quien pide "
            "y quien construye.",
            "Es lo que hago en todos los proyectos de esta página. Diapasão nació en el mostrador de una tienda "
            "de instrumentos; Sabo, de la fila de preguntas de mercado que esperaban a un analista; Desbravador, "
            "de extractores que se rompían cada vez que cambiaba el sitio de origen.",
        ],
        "company_title": "oAccioly Faz.",
        "company": "oAccioly Faz es mi empresa, y a través de ella atiendo proyectos. El nombre dice lo que hago "
        "(en portugués, “faz” es “hace”): el descubrimiento, la arquitectura, el código, las integraciones, el "
        "deploy y el soporte.",
        "facts_title": "Ficha",
        "facts": [
            ["Nombre", "Gabriel Accioly"],
            ["Firma como", "oAccioly"],
            ["Base", "Río de Janeiro, Brasil"],
            ["Programa desde", "2017"],
            ["Formación", "Tecnólogo en Ciencia de Datos"],
            ["Hoy", "Fundador de Diapasão y desarrollador en Kaya Mind"],
            ["Empresa", "oAccioly Faz"],
        ],
        "teaching": "Antes de eso, di clases de desarrollo de videojuegos en Microcamp (2019 a 2020).",
        "faq_title": "Preguntas frecuentes.",
        "faq": [
            {
                "q": "¿Quién es Gabriel Accioly?",
                "a": "Gabriel Accioly es un ingeniero de software brasileño, de Río de Janeiro, con perfil Forward "
                "Deployed. Programa desde 2017, fundó Diapasão y desarrolla los productos de Kaya Mind.",
            },
            {
                "q": "¿Qué es oAccioly Faz?",
                "a": "Es la empresa de Gabriel Accioly (OACCIOLY FAZ LTDA, Pouso Alegre, MG), a través de la cual "
                "atiende proyectos. oAccioly es como firma en LinkedIn y en GitHub.",
            },
            {
                "q": "¿Qué tipo de proyectos hace?",
                "a": "Sistemas web a medida y SaaS multi-tenant, extracción e ingeniería de datos, agentes de IA "
                "conectados a los datos del negocio, integraciones (WhatsApp, pagos, factura electrónica, Mercado "
                "Livre, firma digital) y el hosting y el soporte de todo eso.",
            },
            {
                "q": "¿Con qué tecnologías trabaja?",
                "a": "Python y Django en el centro, con PostgreSQL, Redis, Celery, HTMX, Alpine.js y Tailwind. "
                "También PHP con Symfony, Node.js, Go, FastAPI y Next.js cuando el proyecto lo pide. En IA, Claude "
                "Agent SDK, MCP, Claude Code y Codex; en infraestructura, Docker, Linux, Dokploy y CI/CD.",
            },
            {
                "q": "¿Trabaja en remoto?",
                "a": "Sí. En Kaya Mind trabaja a tiempo completo y en remoto desde 2022.",
            },
            {
                "q": "¿Cómo contactarlo?",
                "a": "Por LinkedIn (linkedin.com/in/oaccioly) o por GitHub (github.com/o-accioly), para una "
                "vacante o un proyecto.",
            },
        ],
    },
    "stack": {
        "title": "Tecnologías.",
        "lead": "Lo que uso, dónde ya está en producción y por qué. Python y Django en el centro; el resto entra "
        "cuando el problema lo pide.",
        "why": {
            "lang": "Python y Django son la base de casi todo: rápidos de construir, fáciles de mantener y con "
            "ecosistema para datos. PHP con Symfony, Node.js y Go entran cuando el proyecto lo pide, como los "
            "runtimes de WhatsApp de ZipZap; FastAPI cuando la API necesita streaming, como en Sabo.",
            "data": "PostgreSQL como base de datos principal, con Row-Level Security cuando cada cliente necesita "
            "quedar aislado. Redis, Celery y RabbitMQ para colas; Playwright y scraping para extracción; pandas "
            "para ETL; Power BI cuando el cliente ya analiza ahí.",
            "ui": "HTMX y Alpine.js sobre plantillas del servidor: interfaz rápida sin una segunda aplicación que "
            "mantener. Next.js y React cuando la colaboración en tiempo real lo pide, como en Standup con Yjs.",
            "ai": "Agentes que consultan y actúan con el Claude Agent SDK y MCP, siempre con herramientas de "
            "lectura o confirmación antes de tocar dinero o inventario. En el día a día, Claude Code y Codex "
            "aceleran la escritura del código.",
            "infra": "Docker en Linux, en servidor propio (bare metal) o con panel de despliegue (Dokploy, "
            "Easypanel), y CI/CD en todos los proyectos.",
            "integ": "Las integraciones son donde vive el negocio: WhatsApp, pagos (Pagar.me), factura "
            "electrónica, firma digital A1 y A3, Mercado Livre, n8n, Chatwoot y Dolibarr.",
        },
        "ai_title": "Cómo uso la IA para construir.",
        "ai": [
            "Trabajo con agentes de código (Claude Code y Codex) desde la primera línea: ellos escriben, y yo "
            "decido la arquitectura, reviso, pruebo y valido en el navegador. Las pruebas, la revisión de "
            "seguridad y el CI sostienen la calidad.",
            "Cada repositorio tiene sus reglas escritas para los agentes, en un CLAUDE.md y en reglas por "
            "carpeta. El de este sitio es público: se puede leer cómo se conduce el trabajo.",
            "En los productos, la IA tiene un límite claro. En Desbravador, el agente crea y repara el "
            "extractor, pero nunca corre en producción. En Diapasão, el asistente pide confirmación antes de "
            "cualquier operación sensible. En Sabo, la base de datos solo admite lectura.",
        ],
        "repo": "Leer el código de este sitio",
        "count": "{count} tecnologías",
    },
    "process": {
        "title": "Cómo un problema se convierte en un sistema en producción.",
        "lead": "El mismo camino en cada proyecto, de la primera conversación al soporte después del lanzamiento.",
        "input": "Entrada",
        "output": "Salida",
        "steps": [
            {
                "stage": "Operación",
                "title": "Me siento con quien opera.",
                "body": "Empiezo en el mostrador, en el consultorio o en la hoja de cálculo del equipo. "
                "Diapasão nació de los problemas diarios de una tienda de instrumentos.",
            },
            {
                "stage": "Descubrimiento",
                "title": "Separo lo que piden del problema.",
                "body": "Lo que pedían era integrar el ERP y el e-commerce. El problema eran productos "
                "duplicados e inventario desincronizado.",
            },
            {
                "stage": "Arquitectura",
                "title": "Diseño para el segundo cliente.",
                "body": "Multi-tenant, permisos y aislamiento de datos entran desde el primer día, con una "
                "prueba que demuestra el aislamiento.",
            },
            {
                "stage": "Construcción",
                "title": "Escribo, pruebo y reviso.",
                "body": "Python y Django en el centro. Agentes como Claude Code y Codex aceleran; las "
                "pruebas, la revisión de seguridad y la validación en el navegador sostienen la "
                "calidad.",
            },
            {
                "stage": "Integraciones",
                "title": "Conecto con lo que el negocio ya usa.",
                "body": "Pagos, factura electrónica, firma digital, WhatsApp, Mercado Livre, Power BI y n8n.",
            },
            {
                "stage": "Producción",
                "title": "Lo pongo en producción y me quedo.",
                "body": "Docker y Linux en servidor propio o panel de despliegue, con CI/CD y soporte. El "
                "producto evoluciona con el uso real.",
            },
        ],
    },
    "journey": {
        "title": "Desde 2017 en la sesión.",
        "lead": "Varias pistas sonando al mismo tiempo: así trabajo desde el principio.",
        "now": "hoy",
        "education": "Tecnólogo en Ciencia de Datos, Cruzeiro do Sul Virtual (2020 a 2022)",
        "tracks": {
            "freelance": "Desarrollador Python: aplicaciones Django, scraping, ETL y automatización",
            "microcamp": "Instructor de desarrollo de videojuegos",
            "b2w": "Volt-x: automatización de financiamiento solar entre varios bancos",
            "gbot": "Scraping, predicción con IA y bot en Telegram",
            "kaya": "Científico de datos y desarrollador Django",
            "duetto": "Desarrollador full-stack",
            "diapasao": "Fundador e ingeniero",
        },
    },
    "contact": {
        "title": "¿Tienes un problema para llevar a producción?",
        "lead": "Vacante o proyecto: escríbeme y te cuento cómo lo resolvería.",
        "linkedin": "Conversar en LinkedIn",
        "github": "Ver GitHub",
        "email": "Escribir un correo",
        "tone": "La, 440 Hz",
        "tone_hint": "La nota de referencia de un diapasón.",
    },
    "detail": {
        "back": "Volver a la mesa",
        "problem": "El problema",
        "built": "Lo que construí",
        "runs": "Dónde corre",
        "facts": "Ficha",
        "layers": "Las capas del sistema.",
        "layers_lead": "Abre una unidad del rack para ver qué hace en este producto.",
        "inside": "Por dentro.",
        "inside_lead": "El panel real, grabado en la tienda de demostración Casa do Som. Todos los datos son "
        "ficticios.",
        "previous": "Anterior",
        "next": "Siguiente",
        "stack": "Tecnologías",
        "cycle": "Pausar o reanudar el movimiento del monitor",
        "no_shots": "Este producto no tiene página pública. El monitor muestra una ilustración de lo que hace.",
        "inside_pending": "Las pantallas internas de este producto están detrás de un inicio de sesión y no se "
        "muestran aquí.",
        "demo_screens": "El monitor muestra el panel ejecutándose en local con datos de demostración.",
        "highlights": "Destacados",
        "screens": "Las pantallas.",
        "screens_lead": "Cada página capturada, en tamaño grande y en el celular. Abre una para ver la página "
        "completa.",
        "screens_demo": "Pantallas del producto ejecutándose en local con datos de demostración. Ningún dato es real.",
        "full_page": "Ver la página completa",
        "visit": "Visitar {host}",
    },
    "layers": {
        "interface": "Interfaz",
        "app": "Aplicación",
        "realtime": "Tiempo real",
        "runtime": "Ejecución",
        "data": "Datos y colas",
        "ai": "Inteligencia artificial",
        "integrations": "Integraciones",
        "infra": "Infraestructura",
    },
    "brand": {
        "makes": [
            "el descubrimiento.",
            "la arquitectura.",
            "el código.",
            "las integraciones.",
            "el deploy.",
            "el soporte.",
            "del problema a producción.",
        ],
        "hint": "oAccioly Faz es mi empresa. En portugués también se lee “Accioly lo hace”.",
    },
    "footer": {
        "built": "Hecho con Django y Tailwind CSS.",
        "source": "Código abierto en GitHub",
        "location": "Río de Janeiro, Brasil",
    },
    "errors": {
        "not_found_title": "Esa pista no está en la sesión.",
        "not_found_body": "La dirección no existe o cambió de lugar.",
    },
    "parts": {
        "Ambiente por marca": "Un entorno por marca",
        "Anexos": "Adjuntos",
        "Atendimento": "Atención",
        "Base de conhecimento": "Base de conocimiento",
        "CI em runner próprio": "CI en runner propio",
        "Calculadora": "Calculadora",
        "Campanhas": "Campañas",
        "Catálogo": "Catálogo",
        "Chat com streaming": "Chat con streaming",
        "Configuração em JSONB": "Configuración en JSONB",
        "Correção automática": "Corrección automática",
        "Cotas por pessoa": "Cuotas por persona",
        "Cotas por plano": "Cuotas por plan",
        "Deploy sem queda": "Deploy sin caída",
        "Documentos": "Documentos",
        "Estoque": "Inventario",
        "Extratores": "Extractores",
        "Frete": "Envíos",
        "Gráficos incorporados": "Gráficos integrados",
        "Journal de eventos": "Journal de eventos",
        "Lease por número": "Lease por número",
        "Loja virtual": "Tienda en línea",
        "Loja white-label": "Tienda white-label",
        "Marcas": "Marcas",
        "Modo voz": "Modo voz",
        "Médicos": "Médicos",
        "Nota fiscal": "Factura electrónica",
        "Notas de entrada": "Facturas de compra",
        "Pacientes": "Pacientes",
        "Pagamentos": "Pagos",
        "Painel": "Panel",
        "Permissões por papel": "Permisos por rol",
        "Pool de navegadores": "Pool de navegadores",
        "Projetos e papéis": "Proyectos y roles",
        "SEO de produto": "SEO de producto",
        "SQL somente leitura": "SQL de solo lectura",
        "Site institucional": "Sitio institucional",
        "Terminal no navegador": "Terminal en el navegador",
        "Trilhas de aprendizagem": "Rutas de aprendizaje",
        "Webhooks assinados": "Webhooks firmados",
    },
}
