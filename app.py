from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import sqlite3, os, random, string

app = Flask(__name__)
app.secret_key = "magic-movies-ultra-secret-2025"
DB = os.path.join(os.path.dirname(__file__), "movies.db")

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db(); c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL, created_at TEXT DEFAULT (datetime('now')))""")

    c.execute("""CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, genre TEXT, language TEXT, duration TEXT,
        release_date TEXT, rating REAL DEFAULT 0, votes TEXT, description TEXT,
        cast_crew TEXT, print_type TEXT, poster_key TEXT, poster_color TEXT,
        is_recommended INTEGER DEFAULT 0, is_recent INTEGER DEFAULT 0, booked_24h INTEGER DEFAULT 0)""")

    c.execute("""CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_id TEXT UNIQUE, user_name TEXT, user_email TEXT,
        movie_id INTEGER, movie_title TEXT, theatre TEXT,
        show_date TEXT, show_time TEXT, seats TEXT, seat_category TEXT,
        total_amount INTEGER, payment_method TEXT,
        booked_at TEXT DEFAULT (datetime('now')))""")

    c.execute("SELECT COUNT(*) FROM movies")
    if c.fetchone()[0] == 0:
        movies = [
            ("RRR","Action/Drama","Telugu","3h 2m","25 Mar 2022",8.8,"1.2M",
             "Two legendary revolutionaries join forces to fight British colonial rule in the most epic action spectacle ever made in Indian cinema. Directed by SS Rajamouli, this story of friendship and sacrifice broke every box office record.",
             "Jr. NTR (Bheem), Ram Charan (Ram), Alia Bhatt (Sita), Ajay Devgn (Venkata), SS Rajamouli (Director), MM Keeravani (Music)",
             "2D / 3D / IMAX","rrr","#8B1A00",1,1,4280),
            ("KGF Chapter 2","Action/Thriller","Kannada","2h 48m","14 Apr 2022",8.2,"980K",
             "Rocky's name echoes in every corner of the world. Powerful new enemies rise to end his reign over the gold mines of Kolar. The empire of gold must be defended — at any cost.",
             "Yash (Rocky), Sanjay Dutt (Adheera), Raveena Tandon (Ramika Sen), Srinidhi Shetty (Reena), Prashanth Neel (Director), Ravi Basrur (Music)",
             "2D / 3D / IMAX","kgf2","#2D1B00",1,0,3950),
            ("Pushpa: The Rule","Action/Drama","Telugu","3h 21m","05 Dec 2024",8.0,"870K",
             "Pushpa Raj further cements his iron grip over the red sandalwood smuggling empire. When SP Shekhawat returns more dangerous than ever, the jungle lord faces the ultimate test of his rule.",
             "Allu Arjun (Pushpa), Rashmika Mandanna (Srivalli), Fahadh Faasil (Shekhawat), Sukumar (Director), Devi Sri Prasad (Music)",
             "2D / 3D","pushpa2","#1A2E00",1,1,5120),
            ("Kalki 2898 AD","Sci-Fi/Mythology","Telugu","3h 1m","27 Jun 2024",7.9,"720K",
             "In a dystopian future, the last avatar of Vishnu rises to challenge the all-powerful Supreme Yaskin. Blending Hindu mythology with breathtaking sci-fi, India's most ambitious cinematic universe begins.",
             "Prabhas (Kalki), Deepika Padukone (SUM-80), Amitabh Bachchan (Ashwatthama), Kamal Haasan (Yaskin), Nag Ashwin (Director)",
             "2D / 3D / IMAX","kalki","#001A3A",1,1,3670),
            ("Devara Part 1","Action/Drama","Telugu","2h 56m","27 Sep 2024",7.8,"540K",
             "A ferocious chieftain who commands fear across the seas creates a legend his enemies dare not challenge. When his son is deemed cowardly, old enemies return — forcing a deadly revelation about the real Devara.",
             "Jr. NTR (Devara/Chaitanya), Janhvi Kapoor (Thangam), Saif Ali Khan (Bhaira), Koratala Siva (Director), Anirudh Ravichander (Music)",
             "2D / 3D","devara","#001A2E",1,1,2890),
            ("Salaar","Action/Crime","Telugu","2h 58m","22 Dec 2023",7.5,"680K",
             "A savage conflict erupts in the violent city of Khansaar. A ferocious man torn between a dying friend's promise and his own brutal nature must choose — peace or all-out war. Some men were never meant for peace.",
             "Prabhas (Salaar/Deva), Prithviraj Sukumaran (Vardha), Shruti Haasan (Aadya), Prashanth Neel (Director), Ravi Basrur (Music)",
             "2D / 3D / IMAX","salaar","#1A0000",1,0,2340),
            ("Hi Nanna","Romance/Drama","Telugu","2h 25m","07 Dec 2023",8.2,"420K",
             "A single father's unconditional love for his daughter forms the heart of this tearjerker. When the daughter sets out to find her missing mother, buried secrets and a beautiful love story come to light.",
             "Nani (Viraj), Mrunal Thakur (Yashna), Baby Kiara Khanna (Mahi), Shouryuv (Director), Hesham Abdul Wahab (Music)",
             "2D","hi_nanna","#1A0014",0,1,1840),
            ("Animal","Action/Drama","Hindi","3h 21m","01 Dec 2023",7.6,"890K",
             "Ranvijay Singh's obsessive love for his estranged father drives him to violent, extreme lengths. A dark, provocative portrait of toxic masculinity and unconditional love that divided audiences and shattered box office records.",
             "Ranbir Kapoor (Ranvijay), Rashmika Mandanna (Geetanjali), Anil Kapoor (Balbir), Bobby Deol (Abrar), Sandeep Reddy Vanga (Director)",
             "2D / 3D","animal","#0A0A1A",0,1,3210),
            ("Dunki","Drama/Comedy","Hindi","2h 41m","21 Dec 2023",7.4,"560K",
             "A group of friends attempts the illegal 'donkey flight' immigration route to reach their dream country abroad. Shah Rukh Khan and Taapsee Pannu shine in this heartfelt Rajkumar Hirani film about hope, love, and belonging.",
             "Shah Rukh Khan (Hardy), Taapsee Pannu (Manu), Vicky Kaushal (Sukhi), Rajkumar Hirani (Director), Pritam (Music)",
             "2D","dunki","#001A1A",0,1,2180),
            ("Fighter","Action/Thriller","Hindi","2h 47m","25 Jan 2024",7.2,"480K",
             "India's first aerial action film follows elite IAF officers on a mission to neutralise a massive terrorist threat. Breathtaking dogfight sequences and patriotic fervour at 40,000 feet above the ground.",
             "Hrithik Roshan (Patty), Deepika Padukone (Minal), Anil Kapoor (Rocky), Siddharth Anand (Director), Vishal-Shekhar (Music)",
             "2D / 3D / IMAX","fighter","#001A0A",0,1,1950),
            ("Merry Christmas","Thriller/Romance","Hindi","2h 10m","12 Jan 2024",7.8,"310K",
             "On Christmas Eve, a lonely man and a mysterious woman meet and are drawn into a deadly web of romance and murder. Sriram Raghavan crafts a masterful noir thriller dripping with tension and festive dread.",
             "Katrina Kaif (Maria), Vijay Sethupathi (Albert), Sriram Raghavan (Director), Pritam (Music)",
             "2D","merry_christmas","#1A001A",0,1,1430),
            ("Guntur Kaaram","Drama/Family","Telugu","2h 26m","12 Jan 2024",6.8,"280K",
             "A son torn between his mother and father navigates deep family wounds and the long road to reconciliation. Trivikram Srinivas pens an emotionally charged drama about ego, love, and the bonds that can never truly break.",
             "Mahesh Babu (Ramana), Sreeleela (Sarasa), Meenakshi Chaudhary (Varalakshmi), Trivikram Srinivas (Director)",
             "2D","guntur_kaaram","#1A1A00",0,1,1120),
        ]
        c.executemany("""INSERT INTO movies
            (title,genre,language,duration,release_date,rating,votes,description,cast_crew,
             print_type,poster_key,poster_color,is_recommended,is_recent,booked_24h)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", movies)
    conn.commit(); conn.close()

@app.route("/")
def index(): return redirect(url_for("signup"))

@app.route("/signup", methods=["GET","POST"])
def signup():
    error = None
    if request.method == "POST":
        name=request.form.get("full_name","").strip()
        email=request.form.get("email","").strip().lower()
        pw=request.form.get("password","")
        cpw=request.form.get("confirm_password","")
        if pw!=cpw: error="Passwords do not match."
        else:
            try:
                conn=get_db(); conn.execute("INSERT INTO users (name,email,password) VALUES (?,?,?)",(name,email,pw)); conn.commit(); conn.close()
                session["user_name"]=name; session["user_email"]=email; session["signup_done"]=True
                return redirect(url_for("login"))
            except sqlite3.IntegrityError: error="An account with this email already exists."
    return render_template("signup.html",error=error)

@app.route("/login", methods=["GET","POST"])
def login():
    error=None
    if request.method=="POST":
        email=request.form.get("email","").strip().lower()
        pw=request.form.get("password","")
        conn=get_db(); user=conn.execute("SELECT * FROM users WHERE email=? AND password=?",(email,pw)).fetchone(); conn.close()
        if user:
            session["user_name"]=user["name"]; session["user_email"]=user["email"]
            session["user_id"]=user["id"]; session["logged_in"]=True; session.pop("signup_done",None)
            return redirect(url_for("movies"))
        error="Invalid email or password."
    return render_template("login.html",error=error,
        user_name=session.get("user_name",""),user_email=session.get("user_email",""),
        signup_done=session.get("signup_done",False))

@app.route("/movies")
def movies():
    conn=get_db()
    recommended=conn.execute("SELECT * FROM movies WHERE is_recommended=1 ORDER BY rating DESC").fetchall()
    recent=conn.execute("SELECT * FROM movies WHERE is_recent=1 ORDER BY release_date DESC").fetchall()
    conn.close()
    return render_template("movies.html",user_name=session.get("user_name","Guest"),recommended=recommended,recent=recent)

@app.route("/search")
def search():
    q=request.args.get("q","").strip()
    if not q: return jsonify([])
    conn=get_db()
    rows=conn.execute("SELECT id,title,genre,language,rating,poster_key,poster_color FROM movies WHERE title LIKE ? OR genre LIKE ? OR language LIKE ? LIMIT 8",
        (f"%{q}%",f"%{q}%",f"%{q}%")).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    conn=get_db(); movie=conn.execute("SELECT * FROM movies WHERE id=?",(movie_id,)).fetchone(); conn.close()
    if not movie: return redirect(url_for("movies"))
    return render_template("movie_details.html",user_name=session.get("user_name","Guest"),movie=dict(movie))

@app.route("/booking/<int:movie_id>")
def booking(movie_id):
    conn=get_db(); movie=conn.execute("SELECT * FROM movies WHERE id=?",(movie_id,)).fetchone(); conn.close()
    if not movie: return redirect(url_for("movies"))
    session["booking_movie_id"]=movie_id
    return render_template("booking.html",user_name=session.get("user_name","Guest"),movie=dict(movie))

@app.route("/payment", methods=["GET","POST"])
def payment():
    if request.method=="POST":
        session["booking_data"]={
            "movie_id":request.form.get("movie_id"),
            "movie_title":request.form.get("movie_title"),
            "poster_key":request.form.get("poster_key"),
            "theatre":request.form.get("theatre"),
            "show_date":request.form.get("show_date"),
            "show_time":request.form.get("show_time"),
            "seats":request.form.get("seats"),
            "seat_cat":request.form.get("seat_cat"),
            "total":request.form.get("total"),
        }
    bd=session.get("booking_data",{})
    return render_template("payment.html",user_name=session.get("user_name","Guest"),bd=bd)

@app.route("/confirm-payment", methods=["POST"])
def confirm_payment():
    bd=session.get("booking_data",{})
    method=request.form.get("pay_method","UPI")
    bk_id="MM"+"".join(random.choices(string.ascii_uppercase+string.digits,k=8))
    conn=get_db()
    conn.execute("""INSERT INTO bookings
        (booking_id,user_name,user_email,movie_id,movie_title,theatre,show_date,show_time,seats,seat_category,total_amount,payment_method)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",(
        bk_id,session.get("user_name","Guest"),session.get("user_email",""),
        bd.get("movie_id"),bd.get("movie_title"),bd.get("theatre"),
        bd.get("show_date"),bd.get("show_time"),bd.get("seats"),
        bd.get("seat_cat"),bd.get("total",0),method))
    conn.commit(); conn.close()
    session["last_booking_id"]=bk_id
    session["last_poster_key"]=bd.get("poster_key","")
    return redirect(url_for("ticket"))

@app.route("/ticket")
def ticket():
    bk_id=session.get("last_booking_id")
    if not bk_id: return redirect(url_for("movies"))
    conn=get_db(); bk=conn.execute("SELECT * FROM bookings WHERE booking_id=?",(bk_id,)).fetchone(); conn.close()
    movie=None
    if bk and bk["movie_id"]:
        conn2=get_db(); movie=conn2.execute("SELECT poster_key,poster_color FROM movies WHERE id=?",(bk["movie_id"],)).fetchone(); conn2.close()
    return render_template("ticket.html",user_name=session.get("user_name","Guest"),
        booking=dict(bk) if bk else {},
        poster_key=movie["poster_key"] if movie else "",
        poster_color=movie["poster_color"] if movie else "#111")

@app.route("/logout")
def logout():
    session.clear(); return redirect(url_for("login"))

if __name__=="__main__":
    init_db(); app.run(debug=True,port=5000)
