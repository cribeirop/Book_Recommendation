python -m venv venv

source venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python scraper.py

python main.py