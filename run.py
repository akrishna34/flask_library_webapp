from app import create_app,db
from app.auth.models import User
from sqlalchemy import exc
from app.catalog.models import Book,Publication

##dev


p1 = Publication("Oxford Publications")





# if __name__ == '__main__':
#     flask_app=create_app('dev')
#
#     with flask_app.app_context():
#         db.create_all()
#
#
#         db.session.add_all([p1])
#         db.session.commit()
#
#         if not User.query.filter_by(user_name='harry'):
#             User.create_user(user='harry', email='harry@potter.com', password='secret')
#
#     flask_app.run()


##prod
#
#
flask_app=create_app('prod')
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry',email='harry@potter.com',password='secret')
    except exc.IntrigityError:


            flask_app.run()