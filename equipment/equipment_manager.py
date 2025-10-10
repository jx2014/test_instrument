import json
import importlib
from pathlib import Path


class EquipmentManager:
    def __init__(self, config_file_path=None):
        if config_file_path is None:
            current_dir = Path(__file__).parent
            config_path = current_dir.parent / 'config' / 'equipment_config.json'
            self.config_file_path = config_path
        else:
            self.config_file_path = Path(config_file_path)

        self.equipment = {}
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file_path, 'r') as f:
                config = json.load(f)

            for eq_config in config.get('equipment', []):
                self._create_equipment_instance(eq_config)

        except Exception as e:
            print(f"Error loading equipment configuration: {e}")

    def _create_equipment_instance(self, eq_config):
        equipment_name = eq_config['equipment_name']
        equipment_model = eq_config['equipment_model']
        class_name = eq_config['equipment_class_name']
        try:
            module = importlib.import_module(f'equipment.{equipment_model}')
            equipment_class = getattr(module, class_name)

            # Create the instance
            instance = equipment_class(eq_config)
            self.equipment[equipment_name] = instance
            print(f"Created {equipment_name} as {equipment_model}")

        except Exception as e:
            print(f"Failed to create {equipment_name} ({equipment_model}): {e}")

    def connect_all(self):
        """Connect to all equipment"""
        for name, instrument in self.equipment.items():
            print(f"Connecting to {name}...")
            success = instrument.connect()
            if success:
                print(f"  → Connected to {name}: {instrument.get_idn()}")
            else:
                print(f"  ✗ Failed to connect to {name}")

    def disconnect_all(self):
        """Disconnect from all equipment"""
        for name, instrument in self.equipment.items():
            instrument.disconnect()

    def __getattr__(self, name):
        """Allow equipment access via attributes: eq_manager.dc_supply"""
        if name in self.equipment:
            return self.equipment[name]
        raise AttributeError(f"No equipment named '{name}'")

    def __getitem__(self, name):
        """Allow equipment access via dictionary: eq_manager['dc_supply']"""
        return self.equipment.get(name)

    def list_equipment(self):
        """List all loaded equipment"""
        print("Loaded Equipment:")
        for name, instrument in self.equipment.items():
            status = "Connected" if instrument.is_connected else "Disconnected"
            print(f"  {name}: {instrument.equipment_model} ({status})")