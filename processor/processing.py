class RecordContextManager:
    def __init__(self, required_fields: dict = None):
        self.contexts = {}

        self.required_fields = required_fields or {}

    def registrar_contexto(self, tipo_registro: str, operaciones: list):
        self.contexts[tipo_registro] = operaciones

    def process_stream(self, record_iterator):
        for record in record_iterator:
            errores = []
            
            if not record:
                print("Registro vacío")
                errores.append("Registro vacío")
            else:
                tipo = record.get("__type__")
                operaciones = self.contexts.get(tipo, [])

                if tipo not in self.required_fields:
                    errores.append(f"Tipo de registro desconocido: {tipo}")
                else:
                    requeridos = self.required_fields[tipo]
                    faltantes = []
                    for campo in requeridos:
                        if campo not in record:
                            faltantes.append(campo)

                    if faltantes:
                        errores.append(f"Faltan campos requeridos: {faltantes}")


                for op in operaciones:
                    errores.extend(op.transformar(record))


                for op in operaciones:
                    errores.extend(op.validar(record))
                
            record["_valido"] = len(errores) == 0
            record["_errores"] = errores
            print("\n\n>>>>>>>>>>>>> REGISTRO <<<<<<<<<<<<<\n\n")
            
            yield (record, errores)
