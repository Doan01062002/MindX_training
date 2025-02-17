from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(200), nullable=True)

products = [
    {"id": 1, "name": "Nồi cơm điện", "price": "800,000đ", "image": "https://bluestonevn.com/wp-content/uploads/2019/09/noi-com-dien-bluestone-rcb-5512-1.jpg", "desc": "Nồi cơm điện cao cấp."},
    {"id": 2, "name": "Máy sinh tố", "price": "500,000đ", "image": "https://product.hstatic.net/200000700229/product/blb-5341_c710028f71b749a291978b7918f4be20_master.jpg", "desc": "Máy xay sinh tố đa năng."},
    {"id": 3, "name": "Quạt điện", "price": "650,000đ", "image": "https://thegioidodung.vn/wp-content/uploads/2023/04/quat-ban-sankyo-b300-vn-6.jpg", "desc": "Quạt điện tiết kiệm điện năng."},
    {"id": 4, "name": "Ấm siêu tốc", "price": "450,000đ", "image": "https://kenhxachtayduc.com/wp-content/uploads/2020/02/Am-sieu-toc-Bosch-TWK7804.jpg", "desc": "Bình đun nước siêu tốc, an toàn."},
    {"id": 5, "name": "Bếp từ", "price": "1,200,000đ", "image": "https://cdn.tgdd.vn/Products/Images/1982/319780/bep-tu-ava-md-dc01-071223-031842-600x600.jpg", "desc": "Bếp hồng ngoại tiện dụng."},
    {"id": 6, "name": "Lò vi sóng", "price": "2,500,000đ", "image": "https://kitchenhome.vn/wp-content/uploads/2019/06/26494_18377_lo-vi-song-electrolux-impreso-30l-ems3087x.jpg", "desc": "Lò vi sóng đa chức năng."}
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template("product.html", product=product) if product else "Không tìm thấy sản phẩm!"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        avatar = request.form['avatar']
        
        new_user = User(username=username, email=email, password=password, avatar=avatar)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        
        if user:
            login_user(user, remember=True) 
            session.permanent = True
            return redirect(url_for('index'))
        else:
            flash('Invalid login credentials!')

    return render_template('login.html')

@app.route("/home")
def index_tr():
    return render_template('index.html', products=products, user=current_user)

@app.route('/home')
@login_required
def home_page():
    return render_template('index.html', user=current_user, products=products) 


@app.route('/logout')
def logout():
    logout_user() 
    session.clear() 
    return redirect(url_for('index'))

# Cart

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart=cart_items)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    name = data.get('name')
    price = data.get('price')
    
    cart = session.get('cart', [])
    
    product_in_cart = next((item for item in cart if item['id'] == product_id), None)
    
    if product_in_cart:
        product_in_cart['quantity'] += 1
    else:
        cart.append({
            'id': product_id,
            'name': name,
            'price': price,
            'quantity': 1
        })
    
    session['cart'] = cart

    return {'cart_count': len(cart)}

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    
    cart = [item for item in cart if item['id'] != product_id]
    
    session['cart'] = cart
    
    return redirect(url_for('cart'))


app.config['SECRET_KEY'] = '12345' # Lưu ý đây là phần đặt lại cookie khi muốn đăng xuất tài khoản bằng cách thay đổi phần dữ liệu được gán

if __name__ == "__main__":
    app.run(debug=True)
