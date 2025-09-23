from operations.operation import NormalizeAmountOperation
from operations.operation import ContextualFieldValidation
from processor.processing import RecordContextManager

from mock_data.records import records

if __name__ == "__main__":
    operaciones_order_event = [
    
        NormalizeAmountOperation(field_name="amount",target_type="__type__"),
        ContextualFieldValidation(field_name="order_id",target_type="__type__", required=True, regex=r"^ORD\d{3}$"),
        ContextualFieldValidation(field_name="customer_name",target_type="__type__", required=True),
    ]

    operaciones_product_type = [
        NormalizeAmountOperation(field_name="price",target_type="__type__"),
        ContextualFieldValidation(field_name="product_sku",target_type="__type__", required=True, regex=r"^SKU_P\d{3}$"),
    ]
    
    required_fields = {
        "order_event": ["order_id", "customer_name", "amount", "timestamp"],
        "product_update": ["product_sku", "price", "is_active"]
    }

    gestor = RecordContextManager(required_fields=required_fields)
    
    for objeto in operaciones_order_event:
        gestor.registrar_contexto("order_event", operaciones_order_event)
        gestor.registrar_contexto("product_type", operaciones_product_type)

    

    for reg, errores in gestor.process_stream(records):
        print(reg)
        if errores:
            print("Errores:")
            for e in errores:
                print(e)
        print("--------")


