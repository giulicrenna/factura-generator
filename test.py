import requests

atoken = "9f038f553674c96fba176ddfcb8ad4a7"
akey = "56518"
usertoken = "f801f889dafb63284522ab45b83ab2535e20229985fbc7c5ae9cb02e1dade29c"
url = "https://www.tusfacturas.app/app/api/v2/facturacion/nuevo"

data = {
    "usertoken" : usertoken,
    "apikey" : akey,
    "apitoken" : atoken,
    "cliente"   :
                {   "documento_tipo":       "DNI",
                    "documento_nro":        "1292963535",
                    "razon_social":         "Pirulo",
                    "email":                "test@test.com",
                    "domicilio":            "Av Sta Fe 123",
                    "provincia":            "2",
                    "envia_por_mail":       "S",
                    "condicion_pago":       "214",
                    "condicion_pago_otra":  "Cobrado en ventanilla",
                    "condicion_iva":        "CF"
                },
    "comprobante": {
		"rubro": "Sevicios web",
		"percepciones_iva": 0,
		"tipo": "FACTURA C",
		
		"percepciones_iibb": 0,
		"bonificacion": 0,
		"operacion": "V",
		"detalle": [{
			"cantidad": 1,
			"producto": {
				"descripcion": "Hosting pagina web ",
				"codigo": 37,
				"lista_precios": "standard",
				"leyenda": "",
				"unidad_bulto": 1,
				"alicuota": 0,
				"precio_unitario_sin_iva": 100
			}
		},
              {
			"cantidad": 2,
			"producto": {
				"descripcion": "Hosting kk web ",
				"codigo": 37,
				"lista_precios": "standard",
				"leyenda": "",
				"unidad_bulto": 1,
				"alicuota": 0,
				"precio_unitario_sin_iva": 100
			}
		}],
		"fecha": "26/02/2023",
		"rubro_grupo_contable": "Sevicios",
		"total": 300,
		"cotizacion": 1,
		"moneda": "PES",
		"punto_venta": 1,
        	"percepciones_iibb":        "0",
        	"percepciones_iibb_base":   "0",
        	"percepciones_iibb_alicuota": "0",
        	"percepciones_iva":         "0",
        	"percepciones_iva_base":    "0",
        	"percepciones_iva_alicuota": "0",
        	"exentos":                  "0", 
        	"impuestos_internos":       "0",
        	"impuestos_internos_base":   "0",
        	"impuestos_internos_alicuota": "0"
	},
}


req = requests.post(url=url, json=data)

print(req.text)