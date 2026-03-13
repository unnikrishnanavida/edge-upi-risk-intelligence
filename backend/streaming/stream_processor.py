from backend.app.services.transaction_processor import TransactionProcessor


processor = TransactionProcessor()


def process_transaction(transaction):

    result = processor.process_transaction(transaction)

    return result