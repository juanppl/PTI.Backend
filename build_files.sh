# build_files.sh
# python3.12 -m venv venv
# source venv/bin/activate

echo "BUILD START"
 python3.10 -m pip install -r requirements.txt
 python3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"