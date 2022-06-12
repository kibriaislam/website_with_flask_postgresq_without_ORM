from flask import Blueprint, render_template
from db_connection import db_conn


blog_list_bp = Blueprint('main', __name__,
    template_folder='templates',
    static_folder='static',)

@blog_list_bp.route('/')
def blog_list():
    conn = db_conn()
    cursor = conn.cursor()

    query = '''
    SELECT title,content,user_name,posts.create_at 
    FROM posts
    JOIN users ON  users.id = posts.user_id
    '''

    # query = '''SELECT * FROM posts'''

    cursor.execute(query)
    data =cursor.fetchall()
    result = []

    for i in data:
        result.append({"title":i[0],"content":i[1],"user_name":i[2],'created_at':i[3]})

    conn.close()

    return render_template('home.html', data = result)

