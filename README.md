# CharityWebsite

##  active virtualenv for linux
```bash
source venv/bin/activate
```

## active virtualenv for windows
```bash
Set-ExecutionPolicy Unrestricted -Scope Process
venv/Scripts/activate
```
## Install reuirements
```bash
pip install -r requirements.txt
```


## install tailwind
```bash
npm install -D tailwindcss
npx tailwindcss init
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css
```

```bash
python manage.py collectstatics
``` 

### running celery

```bash
python -m celery -A Charity worker -l info -P gevent
```