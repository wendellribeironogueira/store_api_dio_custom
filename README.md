# Store API - Bootcamp Santander 2025

API REST com FastAPI + MongoDB + TDD com Pytest

## Funcionalidades:

✅ CRUD de produtos com MongoDB  
✅ TDD com testes unitários e de integração  
✅ Docker para banco MongoDB  
✅ Estrutura profissional com separação de camadas  
✅ `.env.example` para configuração de ambiente

## Execução

```bash
docker-compose up -d
cp .env.example .env
uvicorn main:app --reload
```

## Testes

```bash
pytest tests/unit
pytest tests/integration
```

---

> GitHub: https://github.com/wendellribeironogueira