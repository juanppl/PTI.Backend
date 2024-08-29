# build_files.sh
# python3.12 -m venv venv
# source venv/bin/activate

pip install django
pip install -r requirements.txt
python manage.py collectstatic --no-input --clear