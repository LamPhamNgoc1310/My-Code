import csv
import secrets
import subprocess
from pathlib import Path

cwd = Path.cwd()

with open(cwd / "user_in.csv", "r") as file_in, open(cwd / "user_out.csv", "w") as file_out:
    reader = csv.DictReader(file_in)
writer = csv.DictWriter(file_out, fieldnames=reader.fieldnames)
writer.writeheader()
