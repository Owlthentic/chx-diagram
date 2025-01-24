import json
import os


class Settings:
    DEFAULT_FILE = 'settings.json'
    _instances = {}

    def __new__(cls, settings_file=DEFAULT_FILE):
        # Determine the settings file path
        directory = os.path.dirname(__file__)
        settings_file = os.path.join(directory, settings_file)

        # Check if an instance already exists for this settings file
        if settings_file in cls._instances:
            return cls._instances[settings_file]

        # Create a new instance and load the settings
        instance = super(Settings, cls).__new__(cls)
        instance._load_settings(settings_file)
        cls._instances[settings_file] = instance
        return instance

    def _load_settings(self, settings_file):
        self.settings_file = settings_file
        try:
            with open(settings_file, 'r') as f:
                self.settings = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Settings file {settings_file} not found")

    def get(self, key, default=None):
        return self.settings.get(key, default)


if __name__ == '__main__':
    test = Settings()
    print(test.settings)
