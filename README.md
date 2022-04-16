## Beswor
- destination for building your resumes
---
#### About
BesWor is a simple resume builder application that allows you to build your resume in a few clicks. This was made possible with flask. 

---
#### Configuration
The configuration is done in the `config.py` file.
either create environment variables or use the `config.py` file.
Change the below code to your needs.
```python
host = os.environ.get('AZURE_DATABASE_HOST', '<host>')
user = os.environ.get('AZURE_DATABASE_USER', '<username>')
password = os.environ.get('AZURE_DATABASE_PASSWORD', '<password>')
database = os.environ.get('AZURE_DATABASE_DB', '<database>')
ssl_ca = os.environ.get('AZURE_DIGITAL_CERTIFICATE_PEM', '<ssl_ca document path>')
```

---
#### Requirements
```python
click==8.1.1
colorama==0.4.4
Flask==2.1.1
importlib-metadata==4.11.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
mysql-connector-python==8.0.23
Werkzeug==2.1.0
zipp==3.7.0
```

---
#### Usage
```bash
# Clone the url to your local system
git clone https://github.com/pamarthiabhinav/BesWor.git

# Change to the directory to the project folder
cd BesWor

# Install the requirements
pip install -r requirements.txt

# Run the application
flask run
```

---
<div center>Copyright&copy;: <a href="https://github.com/yaravagopi" target="_blank">Gopinath Reddy</a></div>
