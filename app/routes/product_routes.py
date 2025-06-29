from fastapi import APIRouter, HTTPException, Depends
from fastapi import Request
from app.schemas.product_schema import Product, ProductResponse, UpdateProduct
from app.models.product_model import product_helper
from bson import ObjectId

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
async def create_product(product: Product, request: Request):
    product_dict = product.dict()
    result = await request.app.mongodb["products"].insert_one(product_dict)
    new_product = await request.app.mongodb["products"].find_one({"_id": result.inserted_id})
    return product_helper(new_product)

@router.get("/", response_model=list[ProductResponse])
async def list_products(request: Request):
    products = []
    async for p in request.app.mongodb["products"].find():
        products.append(product_helper(p))
    return products

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, request: Request):
    product = await request.app.mongodb["products"].find_one({"_id": ObjectId(product_id)})
    if product:
        return product_helper(product)
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product: UpdateProduct, request: Request):
    update_data = {k: v for k, v in product.dict().items() if v is not None}
    result = await request.app.mongodb["products"].update_one({"_id": ObjectId(product_id)}, {"$set": update_data})
    if result.modified_count == 1:
        updated = await request.app.mongodb["products"].find_one({"_id": ObjectId(product_id)})
        return product_helper(updated)
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.delete("/{product_id}")
async def delete_product(product_id: str, request: Request):
    result = await request.app.mongodb["products"].delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 1:
        return {"message": "Produto removido com sucesso"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")