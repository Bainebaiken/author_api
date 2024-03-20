from flask import Blueprint,request,jsonify
from authors_app.models.user import User

from authors_app.extensions import db,bcrypt

#auth Blueprint
auth = Blueprint('auth',__name__,url_prefix='/api/v1/auth')


@auth.route('/register',methods=['POST'])
#creating a function for use register
def register():
    #storing viables
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    contact=request.json['contact']
    user_type=request.json['user_type']
    image=request.json['image']
    password=request.json['password']
    biography = request.json['biography']

    #checking the null validations and  null contraints
    # first approach for lito viables
    #it only for field/viables dat are required only, neccessary/complusary
    if not first_name:
        return jsonify({'error':"Your first_name is required"})
    if not last_name:
        return jsonify({'error':"Your last_name is required"})
    if not email:
        return jsonify({'error':"Your email is required"})
    if not contact:
        return jsonify({'error':"Your contact is required"})
    if not user_type:
        return jsonify({'error':"Your user_type is required"})
    if len(password)<8:
        return jsonify({'error':"Your password still short"})
    #only if u are not an author
    if user_type == 'author' and not biography:
        return jsonify({'error':"Your biography is required"})
    #searching whthr the email exists 
    if User.query.filter_by(email=email).first():
        return jsonify({'error':"email already exists"})
    if User.query.filter_by(contact=contact).first():
        return jsonify({'error':"contact already exists"})
    


    try:
      #hashing the password
      hashed_password =bcrypt.generate_password_hash(password)
      #creating auser
      new_user = User(first_name=first_name,last_name=last_name,password =hashed_password,email=email,contact=contact)
      db.session.add(User)
      db.session.commit()
      # defining avariable that gives track to the user name

      username=User.get_full_name() 
      return jsonify({
          'message':username+'has been successfully created as an'+User.user_type,
          'user':{
             "id":User.id,
             "first_name":User.first_name,
             "last_name":User.last_name,
             "password":User.password,
             "email":User.email,
             "contact":User.contact,
             "User-type":User.user_type,
             "biography":User.biography,
             "created_at":User.created_at,
          }
      })

    except Exception as e:
     db.session.rollback()
     return jsonify({'error':str(e)}) 
  