"""
AOXCORE - Sentinel Node (Neuron-0)
Objective: Multi-chain integrity monitoring.
"""
from core.neuron import BaseNeuron

class SentinelNode(BaseNeuron):
    def __init__(self, neuron_id):
        super().__init__(neuron_id, architecture="sentinel-v1")
        self.monitored_chains = ["X-Layer", "Sui", "Cardano"]

    def scan(self):
        for chain in self.monitored_chains:
            result = self.process(f"ping_{chain}")
            print(f"🔍 [Sentinel] {chain}: {result}")

if __name__ == "__main__":
    sentinel = SentinelNode("SN-001")
    sentinel.heartbeat()
    sentinel.scan()
