clientes_validos = ["7290992"]

def verificar_cliente(ci):
    if ci in clientes_validos:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        }
    else:
        return {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }
