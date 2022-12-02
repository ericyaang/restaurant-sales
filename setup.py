from pathlib import Path
from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

setup(
    name="restaurant-sales",
    version=0.1,
    description="Private project for sales prediction.",
    author="Eric Yang",
    python_requires=">=3.7",
    packages=find_namespace_packages(),    
    install_requires=[required_packages],
)

#than run this: pip install -e .  
