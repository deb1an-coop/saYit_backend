# Working structure

```
app/
├── main.py
├── core/           # Configs and DB setup
│   ├── config.py
│   └── database.py
├── models/         # SQLAlchemy models (User, Message)
├── schemas/        # Pydantic models for request/response
├── services/       # Logic (user auth, chat logic)
├── api/            # Route definitions
│   ├── auth.py
│   └── chat.py
├── sockets/        # WebSocket connection manager
├── utils/          # JWT, password utils
└── migrations/     # Alembic migrations
```