from typing import Callable, Any
import inspect

calls = 1


def run(func: Callable[[str], Any]) -> None:
    file = inspect.getmodulename(inspect.getfile(func))
    with open(f"{file}.txt", "r") as f:
        data = f.read()
    res = func(data)
    global calls
    print(f"Day {file[3:]} - Problem {calls} - Result: {res}")
    calls += 1
