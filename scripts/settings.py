class Settings:
    def __init__(self):
        self.settings = {
            "theme": "light",
            "language": "es",
            "notifications": True,
            "auto_update": True,
        }
        self.options = [
            "Inicio",
            "Estadisticas Básicas",
            "Gráficos",
            "Configuración"
        ]

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value

    def reset_settings(self):
        self.settings = {
            "theme": "light",
            "language": "en",
            "notifications": True,
            "auto_update": True,
        }

if __name__ == "__main__":
    settings = Settings()
    print("Configuración inicial:", settings.settings)
    print("Tema actual:", settings.options)
    settings.set_setting("theme", "dark")
    print("Configuración actualizada:", settings.settings)