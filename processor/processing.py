class RecordContextManager:
    def __init__(self):
        self.contexts = {}

    def registrar_contexto(self, tipo_registro: str, operaciones: list):
        self.contexts[tipo_registro] = operaciones

    def process_stream(self, record_iterator):
        for record in record_iterator:
            tipo = record.get("__type__")
            operaciones = self.contexts.get(tipo, [])

            errores = []
            
            for op in operaciones:
                errores.extend(op.transformar(record))
            
            for op in operaciones:
                errores.extend(op.validar(record))
                
            record["_valido"] = len(errores) == 0
            record["_errores"] = errores
            print("\n\n\>>>>>>>>>>>>>REGISTRO<<<<<<<<<<<<\n\n")
            
            yield (record, errores)