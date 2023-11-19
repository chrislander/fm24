### Env

python -m venv .venv (.venv is a common name for Python virtual environments, but you can name it anything).
Activate the virtual environment. On Windows, use .venv\Scripts\activate. On Unix or MacOS, use source .venv/bin/activate.

### Install libraries

pip install -r requirements.txt


### Tests
To run tests, in the root directory run

python -m tests.test_positions
python -m tests.test_personalities

Or to run all tests
python -m unittest discover -s tests


### Run Script

Just run fm.py
