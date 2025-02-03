# Python Threading vs. Multiprocessing Performance Comparison

This Python project compares the performance of `threading` and `multiprocessing` for CPU-bound tasks. It provides a hands-on demonstration of how Python handles parallelism with threads (subject to the Global Interpreter Lock, or GIL) and processes (which can run on multiple CPU cores). The project includes a script that measures execution time for both approaches.

## Key Features:
- **Threading Performance**: Measure the time taken when using threads to perform CPU-bound tasks.
- **Multiprocessing Performance**: Measure the time taken when using multiple processes to perform the same tasks.
- **Real-Time Execution Comparison**: Compare the execution times of threading vs. multiprocessing, with detailed output showing the performance differences.
- **CPU-bound Task**: A CPU-intensive task (summation of squares) is used to demonstrate the parallel execution.

---

### Example Execution:

Here’s a comparison of the two methods when running the project. This table summarizes the expected output:



| Method             | Core Usage      | True Parallelism | Best For                                |
|--------------------|-----------------|------------------|-----------------------------------------|
| `threading`        | 1 core          | ❌ No            | I/O-bound tasks (network, file handling)|
| `multiprocessing`  | Multiple cores  | ✅ Yes           | CPU-bound tasks (heavy computations)    |

---

## Requirements

This project requires the following Python libraries to run:

- `threading`: Built-in Python library for creating threads.
- `multiprocessing`: Built-in Python library for creating separate processes.
- `time`: Built-in Python library for measuring execution time.

No additional packages are required to run the script, as these libraries are part of Python's standard library.

---

## Setup and Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Jonahida/python-threading-vs-multiprocessing
cd python-threading-vs-multiprocessing
```

### Run the Script

To compare the performance of threading and multiprocessing, simply run the `multitasking.py` script:

```bash
python multitasking.py
```

The script will measure and print the execution time for both threading and multiprocessing approaches.

---

**Example Output**:
```bash
Running test with 10000000 iterations
Time with threading: 2.01 seconds
Time with multiprocessing: 1.01 seconds
```

---

## How the Script Works

### CPU-bound Task:
The script uses a task where it calculates the sum of squares for a large range of numbers. This is a CPU-intensive operation that benefits from true parallelism when executed with multiple processes.

### Threading vs. Multiprocessing:
- **Threading**: Python threads are limited by the **Global Interpreter Lock (GIL)**, meaning only one thread can execute Python code at a time. This results in little to no speed improvement for CPU-bound tasks.
- **Multiprocessing**: By using separate processes, Python can bypass the GIL and utilize multiple CPU cores, providing true parallelism and significantly faster execution for CPU-heavy tasks.

### Output:
After running the script, you’ll see the time it takes to execute the same task using both threading and multiprocessing. The script compares the times to illustrate the impact of the GIL and the benefits of using multiple processes.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
