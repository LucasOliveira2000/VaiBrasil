# Alembic - Comandos Uteis

## Criar Migrations

Migration vazia (controle total):
```bash
alembic revision -m "cria tabela usuarios"
```

Migration automatica (compara models x banco):
```bash
alembic revision --autogenerate -m "cria tabela x"
```

## Aplicar Migrations

Aplicar todas as pendentes:
```bash
alembic upgrade head
```

Aplicar ate uma versao especifica:
```bash
alembic upgrade 3fa2c1b9a123
```

Aplicar proxima migration:
```bash
alembic upgrade +1
```

## Reverter Migrations

Voltar uma migration:
```bash
alembic downgrade -1
```

Voltar ate uma versao especifica:
```bash
alembic downgrade d3e6c5672310
```

Voltar tudo (banco limpo):
```bash
alembic downgrade base
```

## Consultar Status

Versao atual do banco:
```bash
alembic current
```

Historico de migrations:
```bash
alembic history
```

Historico detalhado:
```bash
alembic history --verbose
```

## Utilitarios

Ver SQL sem aplicar:
```bash
alembic upgrade head --sql
```

Marcar migration como aplicada (sem rodar SQL):
```bash
alembic stamp head
```

Criar estrutura inicial do alembic:
```bash
alembic init alembic
```

## Fluxo Basico do Dia a Dia

1. Crie/altere o model em `app/models/`
2. Gere a migration:
   ```bash
   alembic revision --autogenerate -m "descricao da mudanca"
   ```
3. Revise o arquivo gerado em `migrations/versions/`
4. Aplique no banco:
   ```bash
   alembic upgrade head
   ```

## Fluxo Manual Recomendado

1. Crie a migration vazia:
   ```bash
   alembic revision -m "descricao da mudanca"
   ```
2. Preencha `upgrade()` e `downgrade()` manualmente
3. Confira o SQL antes de aplicar:
   ```bash
   alembic upgrade head --sql
   ```
4. Aplique no banco:
   ```bash
   alembic upgrade head
   ```
