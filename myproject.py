from flask_mail import Mail, Message
from flask import Flask,request
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
mail_settings = {
"MAIL_SERVER" : "smtp.gmail.com",
"MAIL_PORT":465,
"MAIL_USE_TLS":False,
"MAIL_USE_SSL":True,
"MAIL_USERNAME":'coffycloud14@gmail.com',
"MAIL_PASSWORD":'Aks@apr2020'
}
app.config.update(mail_settings)
mail = Mail(app)
CORS(app)



@app.route('/membership', methods=['POST'])
def user_records():
    name = request.form.get('name')
    dob = request.form.get('dob')
    blood = request.form.get('blood')
    phno = request.form.get('phnonumber')
    email = request.form.get('email')
    volo = request.form.get('volunteer1')
    volou = request.form.get('volunteer2')
    address = request.form.get('address')
    sugg = request.form.get('suggestion')
    hdk = request.form.get('hdk')
    nationality = request.form.get('nationality')
    
    msg = Message(subject="Thank you!",sender=mail_settings['MAIL_USERNAME'],recipients=[f'{email}'])
    msg.body = f'Hey {name},\n\nWe are glad that you got in touch with us. We will get back to you as soon as possible.\n\nBest,\nTKT Team'
    mail.send(msg) 
    msg = Message(subject="New Member!",sender=mail_settings['MAIL_USERNAME'],recipients=['coffycloud14@gmail.com'])
    msg.body = f'Hey team,\n\nWe have {name} who is interested to join us. He can be reached at {email} {phno}.\n\nBest,\nCoffyCloud Team'
    mail.send(msg)
   
    if name and email:
        existing_user = User.query.filter(
            User.name == name or User.email == email
        ).first()
        if existing_user:
            return make_response(f'{name} ({email}) already created!')
        new_user = User(
            name=name,
            dob=dob,
            blood=blood,
            phno=phno,
            email=email,
            volo=volo,
            volou=volou,
            address=address,
            sugg=sugg,
            hdk=hdk,
            nationality=nationality
        )  
          
    
    return 'mail sent and database added'

@app.route('/blood', methods=['POST'])
def user_records_blood():
    req_data = request.get_json()
    name = req_data.get('name')
    phno = req_data.get('phonenumber')
    email = req_data.get('email')
    lastdonated = req_data.get('lastdonatedon')
    bloodgroup = req_data.get('blood')
    address = req_data.get('address')
    msg = Message(subject="Thank you!",sender=mail_settings['MAIL_USERNAME'],recipients=[f'{email}'])
    msg.body = f'Hey {name},\n\nWe are glad that you came forward to donate your blood. We will get in touch with you if there is a requirement.Thanks.\n\nBest,\nTKT Team'
    mail.send(msg) 
    msg = Message(subject="New Member!",sender=mail_settings['MAIL_USERNAME'],recipients=['coffycloud14@gmail.com'])
    msg.body = f'Hey team,\n\nWe have {name} who is interested to donate blood. He can be reached at {email} {phno}.\n\nBest,\nCoffyCloud Team'
    mail.send(msg)
    return 'mail sent'

@app.route('/Educate', methods=['POST'])
def user_records_education():
    name = request.form.get('name')
    phno = request.form.get('phnonumber')
    email = request.form.get('email')
    pan = request.form.get('pan')
    address = request.form.get('address')
    amount = request.form.get('amount')
    msg = Message(subject="Thank you!",sender=mail_settings['MAIL_USERNAME'],recipients=[f'{email}'])
    msg.body = f'Hey {name},\n\n Thanks a lot for chosing to sponsor a child\'s education\n\nBest,\nTKT Team'
    mail.send(msg) 
    msg = Message(subject="New Member!",sender=mail_settings['MAIL_USERNAME'],recipients=['coffycloud14@gmail.com'])
    msg.body = f'Hey team,\n\nWe have {name} who is interested to donate blood. He can be reached at {email} {phno}.\n\nBest,\nCoffyCloud Team'
    mail.send(msg)
    return 'mail sent'
    
if __name__ == "__main__": 
    app.run(host = '0.0.0.0') 