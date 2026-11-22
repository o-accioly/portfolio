"""Language-neutral facts: projects, skills, devices and the career timeline.

Everything here is a fact with a source (the author's LinkedIn, the projects' READMEs or the
live sites). Translatable copy lives in `portfolio/content/`; this module never holds prose.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

# --- Devices ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Device:
    key: str
    width: int  # CSS pixels of the captured viewport
    height: int

    @property
    def ratio(self) -> float:
        return self.width / self.height


DEVICES: tuple[Device, ...] = (
    Device("ultrawide", 2560, 1080),
    Device("desktop", 1920, 1080),
    Device("laptop", 1440, 900),
    Device("tablet", 820, 1180),
    Device("phone", 390, 844),
)
DEVICE_BY_KEY = {device.key: device for device in DEVICES}
DEFAULT_DEVICE = "laptop"

# --- Skills ----------------------------------------------------------------------------
# A bus groups skills the way a console groups channels; each bus owns one cap colour.

BUSES: tuple[str, ...] = ("lang", "data", "ui", "ai", "infra", "integ")

# id -> (label, bus). Labels that are plain words are translated in `content`; product and
# technology names stay as written here.
SKILLS: dict[str, tuple[str, str]] = {
    "python": ("Python", "lang"),
    "django": ("Django", "lang"),
    "fastapi": ("FastAPI", "lang"),
    "php": ("PHP", "lang"),
    "symfony": ("Symfony", "lang"),
    "javascript": ("JavaScript", "lang"),
    "nodejs": ("Node.js", "lang"),
    "go": ("Go", "lang"),
    "typescript": ("TypeScript", "lang"),
    "wagtail": ("Wagtail", "lang"),
    "channels": ("Django Channels", "lang"),
    "postgresql": ("PostgreSQL", "data"),
    "redis": ("Redis", "data"),
    "celery": ("Celery", "data"),
    "rabbitmq": ("RabbitMQ", "data"),
    "scraping": ("Web scraping", "data"),
    "etl": ("ETL & pandas", "data"),
    "powerbi": ("Power BI", "data"),
    "playwright": ("Playwright", "data"),
    "htmx": ("HTMX", "ui"),
    "alpine": ("Alpine.js", "ui"),
    "tailwind": ("Tailwind CSS", "ui"),
    "pwa": ("PWA", "ui"),
    "nextjs": ("Next.js & React", "ui"),
    "yjs": ("Yjs", "ui"),
    "claude_code": ("Claude Code", "ai"),
    "codex": ("OpenAI Codex", "ai"),
    "ai_agents": ("ai_agents", "ai"),
    "mcp": ("MCP", "ai"),
    "agent_sdk": ("Claude Agent SDK", "ai"),
    "docker": ("Docker", "infra"),
    "linux": ("Linux", "infra"),
    "dokploy": ("Dokploy", "infra"),
    "easypanel": ("Easypanel", "infra"),
    "baremetal": ("Bare metal", "infra"),
    "cicd": ("CI/CD", "infra"),
    "whatsapp": ("WhatsApp", "integ"),
    "payments": ("payments", "integ"),
    "signature": ("signature", "integ"),
    "invoicing": ("invoicing", "integ"),
    "mercadolivre": ("Mercado Livre", "integ"),
    "n8n": ("n8n", "integ"),
    "chatwoot": ("Chatwoot", "integ"),
    "dolibarr": ("Dolibarr", "integ"),
}
# Skill ids whose label is a translatable word rather than a product name.
TRANSLATED_SKILLS = frozenset({"ai_agents", "payments", "signature", "invoicing"})

# --- Projects --------------------------------------------------------------------------

LAYER_KEYS: tuple[str, ...] = ("interface", "app", "realtime", "runtime", "data", "ai", "integrations", "infra")


@dataclass(frozen=True)
class Layer:
    key: str  # one of LAYER_KEYS
    parts: tuple[str, ...]  # component names; plain words are translated by content["parts"]


@dataclass(frozen=True)
class Project:
    slug: str
    code: str  # two-letter legend used in the routing matrix
    name: str
    since: int = 0  # 0: no start year to show
    url: str = ""
    host: str = ""
    repo: str = ""
    skills: tuple[str, ...] = ()
    layers: tuple[Layer, ...] = ()
    # True when the captures on the monitor are the product's own screens (a local run with
    # demonstration data) rather than a public page.
    demo_screens: bool = False

    @property
    def buses(self) -> frozenset[str]:
        return frozenset(SKILLS[skill][1] for skill in self.skills)


PROJECTS: tuple[Project, ...] = (
    Project(
        slug="diapasao",
        code="DI",
        name="Diapasão",
        since=2025,
        url="https://diapasao.com/",
        host="diapasao.com",
        skills=(
            "python",
            "django",
            "javascript",
            "postgresql",
            "redis",
            "celery",
            "htmx",
            "alpine",
            "tailwind",
            "claude_code",
            "codex",
            "ai_agents",
            "mcp",
            "docker",
            "linux",
            "dokploy",
            "baremetal",
            "cicd",
            "whatsapp",
            "payments",
            "invoicing",
            "mercadolivre",
        ),
        layers=(
            Layer(
                "interface", ("Marketing", "Loja white-label", "Painel", "Maestro", "HTMX", "Alpine.js", "Tailwind v4")
            ),
            Layer("app", ("Django", "Multi-tenant", "Permissões por papel", "Cotas por plano")),
            Layer("data", ("PostgreSQL + RLS", "PgBouncer", "Redis", "Celery", "MinIO")),
            Layer("ai", ("Sabo", "Catálogo", "Notas de entrada", "Atendimento", "MCP")),
            Layer("integrations", ("WhatsApp", "Pagamentos", "Nota fiscal", "Mercado Livre", "Frete")),
            Layer("infra", ("Docker", "Dokploy", "Bare metal", "CI em runner próprio")),
        ),
    ),
    Project(
        slug="kayadoc",
        code="KD",
        name="KayaDoc",
        since=2022,
        url="https://kayadoc.com.br/",
        host="kayadoc.com.br",
        skills=(
            "python",
            "django",
            "javascript",
            "postgresql",
            "redis",
            "celery",
            "htmx",
            "pwa",
            "claude_code",
            "codex",
            "docker",
            "linux",
            "easypanel",
            "cicd",
            "payments",
            "signature",
            "n8n",
        ),
        layers=(
            Layer("interface", ("Médicos", "Pacientes", "Marcas", "PWA", "HTMX")),
            Layer("app", ("Django", "Multi-tenant", "Passkeys", "2FA", "SSO Google")),
            Layer("data", ("PostgreSQL", "Redis", "Celery")),
            Layer("integrations", ("Pagar.me", "VIDaaS", "BirdID", "Syn", "pyHanko", "n8n", "Teams", "ntfy")),
            Layer("infra", ("Docker", "Linux", "Easypanel", "CI/CD")),
        ),
    ),
    Project(
        slug="kayamind",
        code="KM",
        name="Kaya Mind",
        since=2022,
        url="https://kayamind.com/",
        host="kayamind.com",
        skills=("python", "django", "scraping", "etl", "claude_code", "codex", "docker", "linux", "n8n"),
        layers=(
            Layer("app", ("KayaDoc", "KayaEducation", "Kaya Dashboard")),
            Layer("data", ("Extratores", "ETL", "pandas")),
            Layer("integrations", ("n8n", "Microsoft Teams", "ntfy")),
            Layer("infra", ("Docker", "Linux", "Easypanel")),
        ),
    ),
    Project(
        slug="kaya-dashboard",
        code="DB",
        name="Kaya Dashboard",
        since=2022,
        demo_screens=True,
        url="https://dashboard.kayamind.com/",
        host="dashboard.kayamind.com",
        skills=("python", "django", "postgresql", "powerbi", "etl", "docker", "linux", "easypanel"),
        layers=(
            Layer("interface", ("Ambiente por marca", "Gráficos incorporados")),
            Layer("app", ("Django", "Multi-tenant", "SSO Google")),
            Layer("data", ("PostgreSQL", "Power BI API")),
            Layer("infra", ("Docker", "Linux", "Easypanel")),
        ),
    ),
    Project(
        slug="kayaeducation",
        code="KE",
        name="KayaEducation",
        demo_screens=True,
        url="https://kayaeducation.com.br/",
        host="kayaeducation.com.br",
        skills=("python", "django", "postgresql", "redis", "htmx", "tailwind", "docker", "linux"),
        layers=(
            Layer("interface", ("Ambiente por marca", "Trilhas de aprendizagem", "HTMX", "Tailwind")),
            Layer("app", ("Django", "White-label")),
            Layer("data", ("PostgreSQL", "Redis")),
            Layer("infra", ("Docker", "Linux")),
        ),
    ),
    Project(
        slug="zipzap",
        code="ZZ",
        name="ZipZap",
        since=2026,
        demo_screens=True,
        repo="https://github.com/o-accioly/zipzap",
        host="github.com/o-accioly/zipzap",
        skills=(
            "php",
            "symfony",
            "javascript",
            "nodejs",
            "go",
            "postgresql",
            "rabbitmq",
            "htmx",
            "alpine",
            "tailwind",
            "claude_code",
            "codex",
            "docker",
            "dokploy",
            "cicd",
            "whatsapp",
        ),
        layers=(
            Layer("interface", ("Painel", "Twig", "Tailwind", "Flowbite", "HTMX", "Alpine.js")),
            Layer("app", ("Symfony 8.1", "FrankenPHP worker", "API v1", "Webhooks assinados")),
            Layer("data", ("PostgreSQL", "RabbitMQ", "Journal de eventos", "Lease por número")),
            Layer("integrations", ("Baileys · Node 24", "whatsmeow · Go")),
            Layer("infra", ("Docker Compose", "Dokploy", "Deploy sem queda")),
        ),
    ),
    Project(
        slug="duetto",
        code="DU",
        name="Duetto Musical",
        since=2025,
        url="https://duettomusical.com.br/",
        host="duettomusical.com.br",
        skills=(
            "python",
            "django",
            "javascript",
            "celery",
            "htmx",
            "ai_agents",
            "mcp",
            "docker",
            "linux",
            "n8n",
            "chatwoot",
            "dolibarr",
        ),
        layers=(
            Layer("interface", ("Loja virtual", "HTMX")),
            Layer("app", ("Django", "SEO de produto", "Campanhas")),
            Layer("data", ("Celery", "Estoque")),
            Layer("integrations", ("n8n", "Chatwoot", "Dolibarr")),
            Layer("infra", ("Docker", "Linux")),
        ),
    ),
    Project(
        slug="optimum",
        code="OC",
        name="Optimum Capital",
        since=2026,
        url="https://optimumcapital.com.br/",
        host="optimumcapital.com.br",
        skills=(
            "python",
            "django",
            "wagtail",
            "javascript",
            "redis",
            "celery",
            "htmx",
            "tailwind",
            "claude_code",
            "docker",
        ),
        layers=(
            Layer(
                "interface", ("Site institucional", "Blog", "Documentos", "Calculadora", "Tailwind", "HTMX", "Flowbite")
            ),
            Layer("app", ("Django", "Wagtail")),
            Layer("data", ("Celery", "Redis")),
            Layer("infra", ("Docker",)),
        ),
    ),
    Project(
        slug="desbravador",
        code="DV",
        name="Desbravador",
        since=2026,
        demo_screens=True,
        skills=(
            "python",
            "django",
            "channels",
            "postgresql",
            "redis",
            "celery",
            "scraping",
            "playwright",
            "htmx",
            "alpine",
            "tailwind",
            "claude_code",
            "ai_agents",
            "agent_sdk",
            "docker",
        ),
        layers=(
            Layer("interface", ("Painel", "Terminal no navegador", "HTMX", "Alpine.js", "Tailwind")),
            Layer("app", ("Django", "Channels", "Projetos e papéis")),
            Layer("ai", ("Claude Code", "Claude Agent SDK", "Correção automática")),
            Layer("runtime", ("Playwright", "Camoufox", "Configuração em JSONB")),
            Layer("data", ("Postgres + JSONB", "Celery", "Redis")),
            Layer("infra", ("Docker", "Pool de navegadores")),
        ),
    ),
    Project(
        slug="sabo",
        code="SB",
        name="Sabo",
        since=2026,
        demo_screens=True,
        skills=(
            "python",
            "django",
            "fastapi",
            "postgresql",
            "tailwind",
            "pwa",
            "claude_code",
            "ai_agents",
            "agent_sdk",
            "docker",
        ),
        layers=(
            Layer("interface", ("Chat com streaming", "Anexos", "Modo voz", "PWA")),
            Layer("app", ("FastAPI", "SSE", "Django", "Cotas por pessoa")),
            Layer("ai", ("Claude Agent SDK", "OpenAI Responses API", "Base de conhecimento", "Langfuse")),
            Layer("data", ("MariaDB", "SQL somente leitura", "pgvector")),
            Layer("infra", ("Docker Compose",)),
        ),
    ),
    Project(
        slug="standup",
        code="SU",
        name="Standup",
        since=2026,
        demo_screens=True,
        skills=(
            "python",
            "django",
            "typescript",
            "postgresql",
            "redis",
            "celery",
            "tailwind",
            "nextjs",
            "yjs",
            "claude_code",
            "docker",
        ),
        layers=(
            Layer("interface", ("Next.js 15", "React 19", "Tailwind v4")),
            Layer("app", ("Django", "DRF", "JWT")),
            Layer("realtime", ("Hocuspocus", "Yjs")),
            Layer("data", ("PostgreSQL", "Celery", "Redis")),
            Layer("infra", ("Docker",)),
        ),
    ),
)
PROJECT_BY_SLUG = {project.slug: project for project in PROJECTS}

# --- Career timeline -------------------------------------------------------------------


@dataclass(frozen=True)
class Track:
    key: str
    name: str
    start: date
    end: date | None  # None: still running
    bus: str  # reuses a bus colour so the lane has a cap colour


TIMELINE_START = date(2017, 1, 1)

TRACKS: tuple[Track, ...] = (
    Track("freelance", "Freelance", date(2017, 1, 1), date(2025, 11, 30), "lang"),
    Track("microcamp", "Microcamp", date(2019, 6, 1), date(2020, 1, 31), "ui"),
    Track("b2w", "B2W Energia Solar", date(2021, 4, 1), date(2026, 1, 31), "data"),
    Track("gbot", "G Bot", date(2021, 4, 1), date(2023, 6, 30), "ai"),
    Track("kaya", "Kaya Mind", date(2022, 6, 1), None, "infra"),
    Track("duetto", "Duetto Musical", date(2025, 3, 1), None, "integ"),
    Track("diapasao", "Diapasão", date(2025, 6, 1), None, "lang"),
)

# --- Author ----------------------------------------------------------------------------

AUTHOR_NAME = "Gabriel Accioly"
# How the author signs online (linkedin.com/in/oaccioly, github.com/o-accioly).
AUTHOR_ALIAS = "oAccioly"
AUTHOR_LOCALITY = "Rio de Janeiro"
AUTHOR_COUNTRY = "BR"
AUTHOR_SCHOOL = "Cruzeiro do Sul Virtual"
# Last time the site's facts or copy changed: the sitemap's lastmod.
SITE_UPDATED = date(2026, 11, 21)
# The author's company, which hosts the site. Registration data as published on diapasao.com.
BRAND_NAME = "oAccioly Faz"
COMPANY_LEGAL_NAME = "OACCIOLY FAZ LTDA"
COMPANY_CNPJ = "65.469.093/0001-43"
COMPANY_CITY = "Pouso Alegre, MG"
LINKEDIN_URL = "https://www.linkedin.com/in/oaccioly/"
GITHUB_URL = "https://github.com/o-accioly"
CAREER_START_YEAR = 2017
