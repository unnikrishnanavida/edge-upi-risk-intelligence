from simulator.advanced_fraud_simulator import AdvancedFraudSimulator
from backend.stream_processor import StreamProcessor


class SimulationRunner:

    def __init__(self):

        self.simulator = AdvancedFraudSimulator()
        self.processor = StreamProcessor()

    def run(self):

        transaction = self.simulator.generate_account_takeover()

        result = self.processor.handle_transaction(transaction)

        print("Transaction Result")

        print(result)


if __name__ == "__main__":

    runner = SimulationRunner()

    runner.run()