import os
import sys

print("sys path:", sys.path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openwisp.settings")
    os.environ["DJANGO_SETTINGS_MODULE"] = "openwisp.settings"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
