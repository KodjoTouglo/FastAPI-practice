from fastapi import APIRouter, Header, Form
from typing import Optional
from fastapi.responses import Response, HTMLResponse, PlainTextResponse


router = APIRouter(prefix="/product", tags=["Product"])


products = ["watch", "coding", "camera", "phone", "FastAPI"]


@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products


@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: Optional[str] = Header(None)
    ):
    return products


@router.get('/all')
def get_all_products():
    product = " ".join(products)
    response = Response(content=product, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get('/get/{id}', responses={ 
    200: {
        "content":{
            "text/html":{
                "example": "<div>Product</div>"
            }
        },
        "description": "Return the HTML for an object."
    },
    400:{
        "content":{
            "text/plain": {
               "example": "Product not available"
            }
        },
        "description": "A clear text error message."
    }
 })
def get_product(id: int):
    if id > len(products):
        out = "Product not available."
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
                .product {{
                    width: 500px;
                    height: 30px;
                    border: 2px inset green;
                    text-align: center;
                }}
            </style>
        </head>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")