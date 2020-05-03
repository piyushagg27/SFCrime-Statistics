import producer_server
from pathlib import Path

def run_kafka_server():
	# TODO get the json file path
    #input_file = f"{Path(__file__).parents[0]}/radio_code.json"
    input_file = "police_department_calls_for_service.json"
    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="org.sanfrancisco.policecall.service.v1",
        bootstrap_servers="localhost:9092",
        client_id="producer001"
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
