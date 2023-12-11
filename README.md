# instawork
Assignment for instawork

I have deployed the applicataion on Amazon EC2 server. 
Try directly at [link](http://3.137.198.14:8000/)


<img width="356" alt="image" src="https://github.com/kevin3010/instawork/assets/42439376/c7c029cf-8619-4a23-9d27-2fa84373c152">
<img width="386" alt="image" src="https://github.com/kevin3010/instawork/assets/42439376/d28a08c3-af81-4e58-b20d-75334ef1d14e">


# How to run the application 

## Docker
git clone https://github.com/kevin3010/instawork.git
cd instawork 
docker build -t instawork .
docker run -d -p 8080:80 instawork

## Build locally
git clone https://github.com/kevin3010/instawork.git
cd instwork
pip install -r requirements.txt
cd team_management
python manage.py makemigrations
python manage.py migrate
python maange.py runserver
