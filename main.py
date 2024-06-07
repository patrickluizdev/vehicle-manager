from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, PointStruct
from qdrant_client.models import Distance, VectorParams
from qdrant_client import *

app = FastAPI()

qdrant_client = QdrantClient(host="qdrant", port=6333)

qdrant_client.create_collection(
    collection_name="vehicles",
    vectors_config=VectorParams(size=5, distance=Distance.DOT),
)

class Vehicle(BaseModel):
    plate: str
    model: str
    color: str
    owner: str
    cpf: str

@app.post("/register")
async def register_vehicle(vehicle: Vehicle):
    point = PointStruct(
        id=vehicle.plate,
        vector=[0] * 5,
        payload=vehicle.dict()
    )
    qdrant_client.upsert(
        collection_name="vehicles",
        points=[point]
    )
    return {"message": "Vehicle registered successfully"}

@app.get("/identification/{plate}")
async def identify_vehicle(plate: str):
    result = qdrant_client.scroll(
        collection_name="vehicles",
        scroll_filter={"must": [{"key": "id", "match": {"value": plate}}]}
    )
    if not result or not result.points:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    vehicle = result.points[0].payload
    return vehicle

@app.put("/update/{plate}")
async def update_vehicle(plate: str, vehicle: Vehicle):
    result = qdrant_client.scroll(
        collection_name="vehicles",
        scroll_filter={"must": [{"key": "id", "match": {"value": plate}}]}
    )
    if not result or not result.points:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    point = PointStruct(
        id=plate,
        vector=[0] * 5,
        payload=vehicle.dict()
    )
    qdrant_client.upsert(
        collection_name="vehicles",
        points=[point]
    )
    return {"message": "Vehicle updated successfully"}