from flask import Flask
from blog.blog_bp import blog_list_bp






app = Flask(__name__)

app.register_blueprint(blog_list_bp)





if __name__ =="__main__" :
    app.run(debug = True)