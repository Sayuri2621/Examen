from abc import ABC, abstractmethod
import re
# from .operation import Operation
from utils.logger import Logger

class Operation(ABC):
    def __init__(self, field_name, target_type, **kwargs):
        self.field_name = field_name
        self.target_type = target_type
        self.params = kwargs

    @abstractmethod
    def transformar(self, record: dict) -> dict:
        pass

    @abstractmethod
    def validar(self, record: dict) -> list:
        pass
    
class NormalizeAmountOperation(Operation):
    def transformar(self, record: dict) -> dict:
        raw_value = record.get(self.field_name)
        type_value = record.get(self.target_type)
        errors = []
        
        if raw_value is None or (isinstance(raw_value, str) and raw_value.strip() == ""):
            errors.append(f"Error: Campo '{self.field_name}' es None.")
            Logger.add_to_log("error",f"Error: Campo requerido '{self.field_name}' ausente o vacío.")
            return errors
                    
        pattern = r"^(?:\d+(?:[.,]\d+)?)([A-Za-z]*)$"
        match = re.fullmatch(pattern, raw_value)
        
        if not match:
            errors.append(f"Error: Campo '{self.field_name}' es None.")
            Logger.add_to_log("error",f"Error: El valor del campo '{self.field_name}' = '{raw_value}' no coincide con el formato numérico estándar (float). ")
            return errors
                    
        raw_value = match.group(1).replace(",", ".") 
        record[self.field_name]=raw_value
        return record
        
    
    def validar(self, record: dict) -> list:
        errors = []
        value = record.get(self.field_name)

        if value is None:
            errors.append(f"Error: Campo '{self.field_name}' es inválido o no fue transformado correctamente.")
            Logger.add_to_log("error", f"Error: Campo '{self.field_name}' es inválido o no fue transformado correctamente.")

        return errors

    

class ContextualFieldValidation(Operation):
    def __init__(self, field_name, target_type, **kwargs):
        super().__init__(field_name, target_type, **kwargs )
        self.required = self.params.get("required", True) 
        regex_pattern = self.params.get("regex") 
        self.regex = re.compile(regex_pattern) if regex_pattern else None

    def transformar(self, record: dict) -> dict:
        return record

    def validar(self, record: dict) -> list:
        Logger.add_to_log("info",f"\n\n\n LOGGERS DE VALIDAR \n\n\n")
        errors = []
        value = record.get(self.field_name)

        if self.required:
            if value is None or (isinstance(value, str) and value.strip() == ""):
                errors.append(f"Error: Campo requerido '{self.field_name}' ausente o vacío.")
                Logger.add_to_log("error",f"Error: Campo requerido '{self.field_name}' ausente o vacío.")

        if value and self.regex:
            if not self.regex.fullmatch(str(value)):
                errors.append(f"Error: campo '{self.field_name}' no cumple con el patrón requerido 'ORD###', el valor recibido es '{value}'.")
                Logger.add_to_log("error",f"Error: campo '{self.field_name}' no cumple con el patrón requerido 'ORD###' , el valor recibido es '{value}'.")

        return errors
