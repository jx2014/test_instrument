from equipment.equipment_manager import EquipmentManager
import argparse
import importlib
# from test.opamp_frequency_response import OpampFrequencyResponse
# from test.instrument_test import InstrumentTest
import logging
from logger import setup_logging
from logger import get_logger

TEST_MAP = {
    "instrument_test": ("test.instrument_test", "InstrumentTest"),
    "opamp_frequency_response": ("test.opamp_frequency_response", "OpampFrequencyResponse"),
    "default_test": ("test.instrument_test", "InstrumentTest")
}

def print_available_tests():
    print("\nAvailable tests:")
    print("-" * 50)
    for test_name in sorted(TEST_MAP.keys()):
        module_path, class_name = TEST_MAP[test_name]
        print(f"  {test_name:20} -> {module_path}.{class_name}")
    print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description='Main test script')
    parser.add_argument('--test-name', type=str, default='instrument_test',
                        help='Name of the test to run')

    args = parser.parse_args()

    if args.test_name not in TEST_MAP:
        print(f"Error: Test '{args.test_name}' not found!")
        print_available_tests()
        return 1

    module_path, class_name = TEST_MAP[args.test_name]
    eq_manager = None
    logger = get_logger("main")
    logger.info("Starting test automation")
    setup_logging(level=logging.INFO)

    try:
        module = importlib.import_module(module_path)
        test_class = getattr(module, class_name)
        eq_manager = EquipmentManager("config/equipment_configuration.json")

        test_instance = test_class(equipment_manager=eq_manager)

        if not hasattr(test_instance, "run_test"):
            logger.error(f"No run_test method found in {class_name}")
            return 1

        try:
            test_instance.run_test()
            logger.info("Test completed successfully")
            return 0
        except Exception as e:
            logger.error(f"Test execution failed: {e}")
            return 1

    except Exception as e:
        logger.error(f"Test setup failed: {e}")
        return 1

    finally:
        if eq_manager:
            eq_manager.disconnect_all()

if __name__ == "__main__":
    main()