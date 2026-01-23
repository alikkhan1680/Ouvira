# Authentication Service

This project provides authentication and authorization APIs
implemented with Django and JWT.

## Authentication Overview
- Authentication logic is handled by Django
- JWT tokens are issued by backend
- API access control is enforced via API Gateway (Kong in production)

## API Access Rules
- Some endpoints are **OPEN** (no token required)
- All sensitive endpoints are **PROTECTED** (JWT required)

Detailed API Gateway (Kong) access rules can be found here:
👉 `docs/kong-notes.md`

Authentication flow and logic documentation:
👉 `docs/api.md`

## Auth Type
- JWT
- Header format:
  Authorization: Bearer <ACCESS_TOKEN>
