# Heroku

[Heroku](https://www.heroku.com/)

## 🧭 Heroku — Platforma jako Usługa (PaaS) dla Twórców Aplikacji

**Heroku** to w pełni zarządzana platforma chmurowa typu **PaaS (Platform as a Service)**, umożliwiająca szybkie wdrażanie, zarządzanie i skalowanie aplikacji webowych oraz agentów AI bez konieczności utrzymywania infrastruktury.

---

### 🔧 Kluczowe funkcje

- **Heroku Runtime**: Aplikacje uruchamiane są w izolowanych kontenerach zwanych *dynos*, które zapewniają niezawodne środowisko wykonawcze.
- **Heroku Postgres & pgvector**: Wbudowana baza danych PostgreSQL z obsługą wektorów do aplikacji typu RAG (Retrieval-Augmented Generation).
- **Heroku AI**:
  - **Managed Inference & Agents**: Szybkie wdrażanie modeli AI i agentów za pomocą prostych komend CLI (`heroku ai:models:create`).
  - **Model Context Protocol (MCP)**: Rozszerzanie agentów AI o zewnętrzne narzędzia i API.
- **Heroku Elements**: Ekosystem ponad 150 dodatków i 380 buildpacków do rozszerzania funkcjonalności aplikacji.
- **Heroku Teams & Enterprise**: Zarządzanie zespołami, uprawnieniami, SSO, prywatnymi przestrzeniami i zgodnością z normami (PCI, HIPAA, SOC).

---

### 🛠️ Obsługiwane języki

- Oficjalnie: **Node.js, Python, Ruby, Java, PHP, Go, Scala, Clojure, .NET**
- Nieoficjalnie: Dowolny język działający na Linuksie poprzez buildpacki społeczności

---

### 🚀 Przykładowe zastosowania

- Prototypowanie aplikacji webowych
- Wdrażanie agentów AI z dostępem do narzędzi zewnętrznych
- Integracja z GitHub (Review Apps, CI/CD)
- Skalowanie aplikacji e-commerce, SaaS, API

---

### 📦 CLI i DevOps

Heroku oferuje prosty interfejs CLI (`heroku login`, `heroku create`, `git push heroku main`) oraz integrację z GitHub i Heroku Flow do ciągłego wdrażania.

---
