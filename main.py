from equipment.equipment_manager import EquipmentManager
from test.opamp_frequency_response import OpampFrequencyResponse
import logging
from logger import setup_logging
from logger import get_logger


def main():
    eq_manager = EquipmentManager("config/equipment_configuration.json")
    setup_logging(level=logging.DEBUG)
    logger = get_logger("main")
    logger.info("Starting test automation")
    OpampFrequencyResponse(equipment_manager=eq_manager)

    # Use equipment by name (as defined in JSON)
    try:
        # These names come from equipment_name in JSON
        eq_manager.dc_supply.set_voltage(5.0)
        eq_manager.dc_supply.turn_on()

        eq_manager.dc_supply2.set_voltage(3.3)
        eq_manager.dc_supply2.turn_on()

        # Or access via dictionary
        voltage = eq_manager['dc_supply'].get_voltage()
        print(f"DC Supply Voltage: {voltage}V")

    except Exception as e:
        print(f"Test error: {e}")

    finally:
        eq_manager.disconnect_all()


if __name__ == "__main__":
    main()