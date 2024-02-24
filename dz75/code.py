from typing import Union, List
from abc import ABC, abstractmethod
import json


class ArrayHandler(ABC):
    @abstractmethod
    def check_type(self) -> bool:
        pass

    @abstractmethod
    def output(self, output_format: str = "json") -> None:
        pass

    @abstractmethod
    def sort_array(self, ascending: bool = True) -> None:
        pass

    @abstractmethod
    def add_element(self, element: Union[int, float, str]) -> None:
        pass

    @abstractmethod
    def remove_element(self) -> Union[int, float, str, None]:
        pass

    @abstractmethod
    def count_elements(self, value: Union[int, float, str]) -> int:
        pass

    @abstractmethod
    def calculate_average(self) -> Union[float, None]:
        pass


class Logger:
    @staticmethod
    def log(message: str, log_file: str = "log.txt"):
        with open(log_file, mode="a") as log:
            log.write(message + "\n")


class ArrayManager(ArrayHandler):
    def __init__(self, array: List[Union[int, float, str]]):
        self.array = array

    def check_type(self) -> bool:
        types = set(map(type, self.array))
        return len(types) == 1

    def output(self, output_format: str = "json") -> None:
        output_handler = OutputHandlerFactory.create_handler(output_format)
        output_handler.handle_output(self.array)

    def sort_array(self, ascending: bool = True) -> None:
        self.array.sort(reverse=not ascending)
        Logger.log(f"Array sorted {'ascending' if ascending else 'descending'}")

    def add_element(self, element: Union[int, float, str]) -> None:
        self.array.insert(0, element)
        Logger.log(f"Element {element} added to the beginning of the array")

    def remove_element(self) -> Union[int, float, str, None]:
        if self.array:
            removed_element = self.array.pop(0)
            Logger.log(f"Element {removed_element} removed from the beginning of the array")
            return removed_element
        else:
            Logger.log("Cannot remove element from an empty array")
            return None

    def count_elements(self, value: Union[int, float, str]) -> int:
        count = self.array.count(value)
        Logger.log(f"Number of elements equal to {value}: {count}")
        return count

    def calculate_average(self) -> Union[float, None]:
        if self._validate_numeric_array():
            average = sum(self.array) / len(self.array)
            Logger.log(f"Average value of the array: {average}")
            return average
        else:
            Logger.log("Cannot calculate average for a non-numeric array")
            return None

    def _validate_numeric_array(self) -> bool:
        return all(isinstance(item, (int, float)) for item in self.array)


class OutputHandler(ABC):
    @abstractmethod
    def handle_output(self, data: List[Union[int, float, str]]) -> None:
        pass


class JsonOutputHandler(OutputHandler):
    def handle_output(self, data: List[Union[int, float, str]]) -> None:
        with open("output.json", mode="w") as json_file:
            json.dump(data, json_file)


class TextOutputHandler(OutputHandler):
    def handle_output(self, data: List[Union[int, float, str]]) -> None:
        with open("output.txt", mode="w") as txt_file:
            for item in data:
                txt_file.write(str(item) + "\n")


class ConsoleOutputHandler(OutputHandler):
    def handle_output(self, data: List[Union[int, float, str]]) -> None:
        print(data)


class OutputHandlerFactory:
    @staticmethod
    def create_handler(output_format: str) -> OutputHandler:
        if output_format == "json":
            return JsonOutputHandler()
        elif output_format == "txt":
            return TextOutputHandler()
        elif output_format == "console":
            return ConsoleOutputHandler()
        else:
            raise ValueError("Invalid output format")


initial_array = [1, 3, 5, 2, 4, 6, 8, 10]
array_manager = ArrayManager(initial_array)

print("Are all elements of the same type?", array_manager.check_type())

array_manager.output(output_format="json")
array_manager.output(output_format="txt")
array_manager.output(output_format="console")

array_manager.sort_array(ascending=True)
print("Sorted array:", array_manager.array)

array_manager.add_element(10)
print("Array after adding an element:", array_manager.array)

removed_element = array_manager.remove_element()
print(f"Removed element: {removed_element}")
print("Array after removing an element:", array_manager.array)

count = array_manager.count_elements(5)
print(f"Number of elements equal to 5: {count}")

array_manager_numeric = ArrayManager([1, 2, 3, 4, 5])
average = array_manager_numeric.calculate_average()
print(f"Average value of the numeric array: {average}")
