from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()

service = QiskitRuntimeService(channel="ibm_cloud", token="2wmA_BpLEyJtw3dRJBVrIzXbKSCuNFTkk9-_N2PfUh4Q", instance="crn:v1:bluemix:public:quantum-computing:us-east:a/2f65af1de45a479c978de8d7db945b1b:0180c04d-ad4d-4ce6-ba28-14dc3345f618::")
backend = service.least_busy()

sampler = Sampler(backend)
job = sampler.run([example_circuit])
print(f"job id: {job.job_id()}")
result = job.result()
print(result)