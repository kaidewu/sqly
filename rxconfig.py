import reflex as rx
from sqly.core.config import settings

config = rx.Config(
    app_name=settings.APP_NAME,
    telemetry_enabled=False,
    tailwind={
        "theme": {
            "extend": {},
            "container": {
                "center": True,
            },
        },
        "plugins": ["@tailwindcss/typography"],
    },
)