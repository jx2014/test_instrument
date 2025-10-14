from equipment.equipment_manager import EquipmentManager
from test.opamp_frequency_response import OpampFrequencyResponse
import logging
from logger import setup_logging
from logger import get_logger


def main():
    eq_manager = EquipmentManager("config/equipment_configuration.json")
    setup_logging(level=logging.INFO)
    logger = get_logger("main")
    logger.info("Starting test automation")
    test = OpampFrequencyResponse(equipment_manager=eq_manager)
    try:
        test.run_test()
    except Exception as e:
        print(f"Test error: {e}")

    finally:
        eq_manager.disconnect_all()


if __name__ == "__main__":
    main()