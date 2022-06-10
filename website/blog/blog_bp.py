from flask import Blueprint, render_template
from db_connection import cursor


main = Blueprint('main', __name__,
    template_folder='templates',
    static_folder='static',)

@main.route('/')
def blog_list():

    query = '''
    SELECT content,user_name,posts.create_at 
    FROM posts
    JOIN users ON  users.id = posts.user_id
    '''

    # query = '''SELECT * FROM posts'''

    cursor.execute(query)
    data =cursor.fetchall()
    result = []

    for i in data:
        result.append({"content":i[0],"user_name":i[1],'created_at':i[2]})


    print("kibria: ", data)




    return render_template('home.html', data = result)

