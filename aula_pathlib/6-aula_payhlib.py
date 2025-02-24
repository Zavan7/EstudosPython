from pathlib import Path

DIR = Path(__file__).parent / 'oi.txt'
DIR.unlink()

print(DIR)