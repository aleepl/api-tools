import os

CURRENT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)
BASE_PATH = os.path.abspath(CURRENT_PATH)
PROJECT3_PATH = os.path.join(BASE_PATH, "Project3")

if __name__ == "__main__":
    print(CURRENT_PATH)
    print(BASE_PATH)
    print(PROJECT3_PATH)