## Cadastro de Veículos com FastAPI e Qdrant

### Visão Geral

Este projeto é uma API de cadastro de veículos construída utilizando FastAPI e Qdrant. Ele permite registrar, identificar e atualizar informações de veículos. A API possui três endpoints principais: `/register`, `/identification/{plate}` e `/update/{plate}`.

### Estrutura do Projeto

```
/app
|-- main.py
|-- requirements.txt
|-- Dockerfile
|-- docker-compose.yml
```

### Dependências

- FastAPI
- Uvicorn
- Qdrant-client
- Pydantic

### Endpoints

#### 1. Registrar Veículo

**Endpoint:** `/register`

**Método:** `POST`

**Corpo da Requisição:**

```json
{
  "plate": "ABC-1234",
  "model": "Corsa Classic",
  "color": "Branco",
  "owner": "Patrick Luiz",
  "cpf": "123.456.789-00"
}
```

**Resposta de Sucesso:**

```json
{
  "message": "Vehicle registered successfully"
}
```

#### 2. Identificar Veículo

**Endpoint:** `/identification/{plate}`

**Método:** `GET`

**Parâmetros da URL:**

- `plate` (string): Placa do veículo a ser identificado.

**Resposta de Sucesso:**

```json
{
  "plate": "ABC-1234",
  "model": "Corsa Classic",
  "color": "Branco",
  "owner": "Patrick Luiz",
  "cpf": "123.456.789-00"
}
```

**Resposta de Erro:**

```json
{
  "detail": "Vehicle not found"
}
```

#### 3. Atualizar Veículo

**Endpoint:** `/update/{plate}`

**Método:** `PUT`

**Parâmetros da URL:**

- `plate` (string): Placa do veículo a ser atualizado.

**Corpo da Requisição:**

```json
{
  "plate": "ABC-1234",
  "model": "Corsa Classic",
  "color": "Prata",
  "owner": "Patrick Luiz",
  "cpf": "123.456.789-00"
}
```

**Resposta de Sucesso:**

```json
{
  "message": "Vehicle updated successfully"
}
```

**Resposta de Erro:**

```json
{
  "detail": "Vehicle not found"
}
```

### Utilização

#### 1. Clonar o Repositório

```bash
git clone https://github.com/patrickluizdev/vehicle-manager
cd vehicle-manager
```

#### 2. Executar com Docker Compose

```bash
docker-compose up
```