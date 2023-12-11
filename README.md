# instawork
Assignment for instawork

I have deployed the applicataion on Amazon EC2 server. 
Try directly at [link](http://3.137.198.14:8000/)


<img width="391" alt="image" src="https://github.com/kevin3010/instawork/assets/42439376/0003dbee-22fd-4ab9-92a3-ba2af08b23b6"> <br>
<img width="385" alt="image" src="https://github.com/kevin3010/instawork/assets/42439376/11e13f03-f8c8-4859-8d71-ce409c3597d3"> <br>
<img width="377" alt="image" src="https://github.com/kevin3010/instawork/assets/42439376/43414a85-3a5b-461f-8f9d-645adee7806b"> <br>






# How to run the application 

## Docker
git clone https://github.com/kevin3010/instawork.git <br>
cd instawork <br>
docker build -t instawork . <br>
docker run -d -p 8080:80 instawork <br>

## Build locally
git clone https://github.com/kevin3010/instawork.git <br>
cd instwork <br>
pip install -r requirements.txt <br>
cd team_management <br>
python manage.py makemigrations <br>
python manage.py migrate <br>
python maange.py runserver <br>
