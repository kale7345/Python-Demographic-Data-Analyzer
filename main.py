import demographic_data_analyzer
from unittest import main


def run() -> None:
	"""Print the analysis summary and run the project's test suite."""
	demographic_data_analyzer.calculate_demographic_data()
	main(module='test_module', exit=False)


if __name__ == '__main__':
	run()