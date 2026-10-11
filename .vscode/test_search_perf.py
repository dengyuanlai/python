import argparse
import statistics
import time


def average_time(func, trials):
	timings = []
	for _ in range(trials):
		start = time.perf_counter()
		func()
		end = time.perf_counter()
		timings.append(end - start)
	return statistics.mean(timings)


def format_seconds(value):
	return f"{value * 1000:.6f} ms"


def run_benchmark(size, trials):
	values = list(range(size))
	value_list = values
	value_dict = {v: True for v in values}

	present_target = size - 1
	absent_target = -1

	list_present = average_time(lambda: present_target in value_list, trials)
	dict_present = average_time(lambda: present_target in value_dict, trials)
	list_absent = average_time(lambda: absent_target in value_list, trials)
	dict_absent = average_time(lambda: absent_target in value_dict, trials)

	print(f"size={size:,}, trials={trials}")
	print("present lookup")
	print(f"  list: {format_seconds(list_present)}")
	print(f"  dict: {format_seconds(dict_present)}")
	print("absent lookup")
	print(f"  list: {format_seconds(list_absent)}")
	print(f"  dict: {format_seconds(dict_absent)}")

	present_speedup = list_present / dict_present if dict_present > 0 else float("inf")
	absent_speedup = list_absent / dict_absent if dict_absent > 0 else float("inf")
	print("speedup (list_time / dict_time)")
	print(f"  present: {present_speedup:.2f}x")
	print(f"  absent: {absent_speedup:.2f}x")


def main():
	parser = argparse.ArgumentParser(description="Compare search performance between list and dict.")
	parser.add_argument("--size", type=int, default=1_000_000, help="Number of elements")
	parser.add_argument("--trials", type=int, default=20, help="Number of repeated timings")
	args = parser.parse_args()

	if args.size <= 0:
		raise ValueError("--size must be > 0")
	if args.trials <= 0:
		raise ValueError("--trials must be > 0")

	run_benchmark(args.size, args.trials)


if __name__ == "__main__":
	main()
