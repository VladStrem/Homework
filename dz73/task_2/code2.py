import json
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def access_number_set(self) -> List[int]:
        pass


class RealSubject(Subject):
    def access_number_set(self) -> List[int]:
        try:
            with open('numbers.json', mode='r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("RealSubject: File not found.")
            return []


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def access_number_set(self) -> List[int]:
        if self.check_access():
            data = self._real_subject.access_number_set()
            self.log_access()
            return data
        else:
            print("Proxy: Access denied.")
            return []

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        # Implement your access control logic here
        return True

    def log_access(self) -> None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{current_time} - Proxy: Logging the time of request.\n"
        with open('access_log.txt', mode='a') as log_file:
            log_file.write(log_entry)


def client_code(subject: Subject) -> None:
    data = subject.access_number_set()
    total_sum = sum(data)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{current_time} - Client: Calculated sum of numbers: {total_sum}\n"
    with open('access_log.txt', mode='a') as log_file:
        log_file.write(log_entry)
    print(f"Client: Calculated sum of numbers: {total_sum}")


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
