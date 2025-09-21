"""

### ✅ 1. **Navigate to your project folder**

Open your terminal or command prompt and go to your project directory:
cd path/to/your/project

### ✅ 2. **Create the virtual environment**

Run this command (replace `venv` with your desired folder name if needed):
python -m venv venv


### ✅ 3. **Activate the virtual environment**

#### 🔹 On **Windows**:
venv\Scripts\activate

#### 🔹 On **MacOS/Linux**:
source venv/bin/activate


### ✅ 4. **Check if it’s activated**

You should see `(venv)` in your terminal prompt. Then check Python version and path:
which python     # or `where python` on Windows
python --version


### ✅ 5. **Install project dependencies**

If you have a `requirements.txt` file:
pip install -r requirements.txt


Or install packages manually, e.g.:
pip install flask

### ✅ 6. **Freeze dependencies (optional)**

To save the current installed packages:
pip freeze > requirements.txt

### ✅ 7. **Deactivate when done**

To leave the virtual environment:
deactivate

"""