import requests

url = "https://api.bitingenieria.com.ar/silex/feafip/fe_autorizar"

data = {
    "date" : "26/2/2023",
    "tipo_comp" : 11,
    "pto_vta" : 1,
    "pyment_m" : "Efectivo",
    "company_data" : {
        "name" : "Instituto crenna",
        "address" : "Italia",
        "postal_code" : "1392",
        "city" : "casilda",
        "country" : "argentina",
        "ident" : "20438414887"
    },
    "customer_data" : {
        "name" : "cliente",
        "address" : "Italia",
        "postal_code" : "1392",
        "city" : "casilda",
        "country" : "argentina",
        "ident" : "0",
        "doc_type" : 99  
    },
    "products" : [
        {
            "description" : "Hola carola",
            "price" : 1000,
            "quantity" : 1,
            "sum_tax" : 0,
            "total" : 1000
        }],
    "base" : {
        "subtotal" : 1000,
        "sum_tax" : 0,
        "total" : 1000
    }
}

req = requests.post(url=url, json=data)

print(req.text)