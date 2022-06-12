from sqlite3 import Cursor
from flask import Blueprint, render_template
from db_connection import db_conn


blog_list_bp = Blueprint('blog_list_bp', __name__,
    template_folder='templates',
    static_folder='static',)

@blog_list_bp.route('/')
def blog_list():
    conn = db_conn()
    cursor = conn.cursor()

    query = '''
    SELECT posts.id,title,content,user_name,posts.create_at 
    FROM posts
    JOIN users ON  users.id = posts.user_id
    '''

    # query = '''SELECT * FROM posts'''

    cursor.execute(query)
    data =cursor.fetchall()
    result = []

    for i in data:
        result.append({"id":i[0],"title":i[1],"content":i[2],"user_name":i[3],'created_at':i[4]})

    conn.close()

    return render_template('home.html', data = result)


@blog_list_bp.route('/<int:id>')
def blog_details(id):

    conn = db_conn()
    cursor = conn.cursor()

    query = '''
    SELECT posts.id,title,content,user_name,posts.create_at
    FROM posts
    JOIN users ON users.id = posts.user_id
    WHERE posts.id = %s
    ''' % (id)

    cursor.execute(query)
    data = cursor.fetchall()
    result = []

    for i in data:
        result.append({"id":i[0],"title":i[1],"content":i[2],"user_name":i[3],'created_at':i[4]})
    
    conn.close()

    return render_template('home.html',data = result)

@blog_list_bp.route("/latest")
def latest_posts():

    conn = db_conn()

    cursor = conn.cursor()

    query = '''
    SELECT posts.id,title,content,user_name,posts.create_at
    FROM posts
    JOIN users ON users.id = posts.user_id
    ORDER BY posts.id DESC
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    result = []

    for i in data:
        result.append({"id":i[0],"title":i[1],"content":i[2],"user_name":i[3],'created_at':i[4]})
    
    conn.close()

    return render_template('home.html',data = result)

