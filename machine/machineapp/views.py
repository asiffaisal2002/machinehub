from django.shortcuts import render
import mysql.connector
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
db = mysql.connector.connect(host="localhost",user="root",password="",database="machine")
c = db.cursor()



# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    msg = ""
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        s = "select count(*) from login where username='" + email + "'"
        c.execute(s)
        i = c.fetchone()
        if i[0] > 0:
            s = "select * from login where username='" + email + "'"
            c.execute(s)
            i = c.fetchone()
            if i[1] == password:
                    request.session["email"] = email
                    if i[2] == "admin":
                        return HttpResponseRedirect("/adminhome")
                    if i[2] == "user":
                        return HttpResponseRedirect("/userhome")
                    if i[2] == "staff":
                        return HttpResponseRedirect("/staffhome")

            else:
                msg = "Wrong password"
        else:
            msg = "User does not exist"
    return render(request, "login.html", {"msg": msg})

def register(request):
    msg = " "
    if request.POST:

        name = request.POST.get('name')
        place = request.POST.get('place')
        address = request.POST.get('address')
        email = request.POST.get('email')
        mobno = request.POST.get('mob')
        password = request.POST.get('password')
        cpassword= request.POST.get('cpassword')
        s = "select count(*) from login where username='" + email + "'"
        c.execute(s)
        col = c.fetchone()
        print(col)
        if col[0]:
            msg = "Already Registered"
        else:
            print(name)
            print(email)
            s = "insert into register(name,place,address,email,mobno,password,cpassword) values('" + name + "','" + place + "','" + address + "','" + email + "','" + mobno + "','" + password + "','" + cpassword + "')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Error"
            else:
                msg = "Registration Succesfull"
            s = "insert into login(username,password,role) values('" + email + "','" + password + "','user')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Error"
            else:
                msg ="Registration Succesfull"
    return render(request,"register.html",{"msg":msg})

def adminhome(request):
    return render(request,"adminhome.html")
def contact(request):
    return render(request,"contact.html")
def staffregister(request):
    msg = " "
    if request.POST:

        name = request.POST.get('name')
        mobno = request.POST.get('mob')
        email = request.POST.get('email')
        img = request.FILES["logo"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        logo = fs.url(filename)
        password = request.POST.get('password')
        cpassword= request.POST.get('cpassword')
        s = "select count(*) from login where username='" + email + "'"
        c.execute(s)
        col = c.fetchone()
        print(col)
        if col[0]:
            msg = "Already Registered"
        else:
            print(name)
            print(email)
            s = "insert into staffregister(sname,smobno,semail,staffimage,password,cpassword) values('" + name + "','" + mobno + "','" + email + "','" + logo + "','" + password + "','" + cpassword + "')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Error"
            else:
                msg = "Registration Succesfull"
            s = "insert into login(username,password,role) values('" + email + "','" + password + "','staff')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Error"
            else:
                msg ="Registration Succesfull"
    return render(request,"staffregister.html",{"msg":msg})
def staffhome(request):
    return render(request,"staffhome.html")
def staffview(request):
    s = "select * from staffregister"
    c.execute(s)
    x = c.fetchall()
    return render(request,"staffview.html",{"x":x})
def userhome(request):
    s = "select * from addrenting"
    c.execute(s)
    x = c.fetchall()
    return render(request,"userhome.html",{"x": x})
def userviewprofile(request):
    email = request.session.get("email")
    s = "select * from register where email='" + email + "'"
    c.execute(s)
    x = c.fetchall()
    return render(request,"userviewprofile.html",{"x" : x})
def staffprofileview(request):
    email = request.session.get("email")
    s = "select * from staffregister where semail='" + email + "'"
    c.execute(s)
    x = c.fetchall()
    return render(request,"staffprofileview.html",{"x" : x})
def addproduct(request):
    msg = ""
    email = request.session.get("email")

    if not email:
        return HttpResponseRedirect("/login")

    c.execute("select sid from staffregister where semail=%s", (email,))
    row = c.fetchone()

    if not row:
        msg = "Staff not found"
        return render(request, "addproduct.html", {"msg": msg})

    sid = row[0]

    if request.method == "POST":
        try:
            name = request.POST.get('name')
            model = request.POST.get('model')
            company = request.POST.get('company')
            price = request.POST.get('price')

            img = request.FILES.get("logo")
            if not img:
                return render(request, "addproduct.html", {"msg": "Image required"})

            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            logo = fs.url(filename)

            s = """
            insert into addproduct
            (sid, proname, promodel, procompany, proimage, proprice)
            values (%s,%s,%s,%s,%s,%s)
            """
            c.execute(s, (sid, name, model, company, logo, price))
            db.commit()
            msg = "Product added successfully"

        except Exception as e:
            print("ADD PRODUCT ERROR:", e)
            msg = str(e)

    return render(request, "addproduct.html", {"msg": msg})

def adminproductview(request):
    email = request.session.get("email")
    s = "select * from addproduct"
    c.execute(s)
    x = c.fetchall()
    return render(request,"adminproductview.html",{"x":x})
def adminuserview(request):
    email = request.session.get("email")
    s = "select * from register"
    c.execute(s)
    x = c.fetchall()
    return render(request,"adminuserview.html",{"x":x})
def admindeletestaff(request):
    semail =request.GET.get("semail")
    s = "delete staffregister,login from staffregister inner join login on staffregister.semail= login.username where username='" + semail + "'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Error"
    else:
        msg = " Succesfull"
    return HttpResponseRedirect("/staffview")
def addrenting(request):
    msg = " "
    email = request.session.get("email")
    s = "select sid from staffregister where semail='" + email + "'"
    c.execute(s)
    x = c.fetchall()
    sid = x[0]
    if request.POST:
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        img = request.FILES["logo"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        logo = fs.url(filename)
        usage = request.POST.get('usage')
        price = request.POST.get('price')
        s = "insert into addrenting(sid,rname,rbrand,rimage,rusage,rprice) values((select sid from staffregister where semail='" + email + "'),'" + name + "','" + brand + "','" + logo + "','" + usage + "','" + price + "')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Error"
        else:
            msg = "Registration Succesfull"
    return render(request,"addrenting.html")
def adminrentingview(request):
    email = request.session.get("email")
    s = "select * from addrenting"
    c.execute(s)
    x = c.fetchall()
    return render(request,"adminrentingview.html",{"x":x})
def rentbook(request):
    return render(request,"rentbook.html")
def userproductview(request):
    s = "select * from addproduct"
    c.execute(s)
    x = c.fetchall()
    return render(request,"userproductview.html",{"x":x})
def payment(request):
    msg = " "
    email = request.session.get("email")
    purid = request.session.get("purid")

    s = "select uid from purchase where purid='" + str(purid) + "'"

    c.execute(s)
    x = c.fetchone()
    uid = x[0]
    if request.POST:
        purid = request.POST.get("purid")

        ctype = request.POST.get('ctype')
        cnumber = request.POST.get('cnumber')
        cvv = request.POST.get('cvv')
        s = "insert into payment(purid,uid,ctype,cnumber,cvv) values('" + str(purid) + "','" + str(uid) + "','" + ctype + "','" + cnumber + "','" + cvv + "')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Error"
        else:
            msg = "Registration Succesfull"

            q = "update purchase set pstatus='Paid' where purid='" + str(purid) + "'"
            try:
                c.execute(q)
                db.commit()
            except:
                msg = "Error"
            else:
                msg = "Updation Succesfull"
            return HttpResponseRedirect("/userhome")
    return render(request,"payment.html",{"msg": msg})
def userpurchase(request):
    msg = " "
    email = request.session.get("email")
    proid = request.GET.get("proid")

    s = "select uid from register where email=%s"
    c.execute(s, (email,))
    x = c.fetchone()

    if request.POST:
        name = request.POST.get('name')
        place = request.POST.get('place')
        address = request.POST.get('address')
        mobileno = request.POST.get("mob")
        pincode = request.POST.get("pincode")
        ttype = request.POST.get("ttype")

        # ✅ FIXED INSERT QUERY (IMPORTANT)
        s = """
        insert into purchase
        (uid,rid,sid,purname,purplace,puraddress,purmobile,pincode,status,pstatus,dstatus)
        values (
            (select uid from register where email=%s),
            %s,
            (select sid from addproduct where proid=%s),
            %s,%s,%s,%s,%s,
            'Ordered','Not Paid','Pending'
        )
        """

        try:
            c.execute(s, (email, proid, proid, name, place, address, mobileno, pincode))
            db.commit()
        except Exception as e:
            print("ERROR:", e)
            msg = "Error"
        else:
            msg = "Succesfull"

            c.execute("select LAST_INSERT_ID()")
            purid = c.fetchone()[0]
            request.session["purid"] = purid

            if ttype == 'card':
                return HttpResponseRedirect("/payment")
            else:
                return HttpResponseRedirect("/userhome")

    return render(request, "userpurchase.html", {"x": x, "proid": proid})
def adminbookingdetails(request):
    import mysql.connector

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="machine"
    )
    c = db.cursor()

    # 🔹 Get filters from URL
    status = request.GET.get("status")
    pstatus = request.GET.get("pstatus")

    # =========================
    # 🛒 PURCHASE FILTER
    # =========================
    purchase_query = """
        SELECT purid, purname, purplace, puraddress, purmobile, status, pstatus, dstatus
        FROM purchase WHERE 1=1
    """
    purchase_values = []

    if status:
        purchase_query += " AND dstatus=%s"
        purchase_values.append(status)

    if pstatus:
        purchase_query += " AND pstatus=%s"
        purchase_values.append(pstatus)

    c.execute(purchase_query, purchase_values)
    rows = c.fetchall()

    x = []
    for r in rows:
        x.append({
            "purid": r[0],
            "name": r[1],
            "place": r[2],
            "address": r[3],
            "mobile": r[4],
            "status": r[5],
            "pstatus": r[6],
            "dstatus": r[7],
        })

    # =========================
    # 🚜 RENT FILTER
    # =========================
    rent_query = """
        SELECT rentid, name, mob, pname, ndays, tamount, status, pstatus
        FROM rent WHERE 1=1
    """
    rent_values = []

    if status:
        rent_query += " AND status=%s"
        rent_values.append(status)

    if pstatus:
        rent_query += " AND pstatus=%s"
        rent_values.append(pstatus)

    c.execute(rent_query, rent_values)
    rows = c.fetchall()

    y = []
    for r in rows:
        y.append({
            "rentid": r[0],
            "name": r[1],
            "mob": r[2],
            "pname": r[3],
            "ndays": r[4],
            "amount": r[5],
            "status": r[6],
            "pstatus": r[7],
        })

    return render(request, "adminbookingdetails.html", {"x": x, "y": y})
def bookingdetails(request):
    import mysql.connector

    email = request.session.get("email")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="machine"
    )
    c = db.cursor()

    # =========================
    # 🛒 BUYING (USER BOOKINGS)
    # =========================
    c.execute("""
        SELECT purid, purname, purplace, puraddress, purmobile, status, dstatus, pstatus
        FROM purchase
        WHERE uid = (SELECT uid FROM register WHERE email=%s)
    """, (email,))

    rows = c.fetchall()

    x = []
    for r in rows:
        x.append({
            "purid": r[0],
            "name": r[1],
            "place": r[2],
            "address": r[3],
            "mobile": r[4],
            "status": r[5],
            "dstatus": r[6],
            "pstatus": r[7],
        })

    # =========================
    # 🚜 RENT (USER BOOKINGS)
    # =========================
    c.execute("""
        SELECT rentid, name, mob, pname, ndays, tamount, status, pstatus
        FROM rent
        WHERE uid = (SELECT uid FROM register WHERE email=%s)
    """, (email,))

    rows = c.fetchall()

    y = []
    for r in rows:
        y.append({
            "rentid": r[0],
            "name": r[1],
            "mob": r[2],
            "pname": r[3],
            "ndays": r[4],
            "amount": r[5],
            "status": r[6],
            "pstatus": r[7],
        })

    return render(request, "bookingdetails.html", {"x": x, "y": y})
def rent(request):
    msg = " "
    email = request.session.get("email")
    rid = request.GET.get("rid")

    q = "select * from addrenting where rid='" + str(rid) + "'"
    c.execute(q)
    y = c.fetchone()
    pname = y[2]
    sid = y[1]
    print(pname)
    rate = y[6]
    s = "select uid from register where email='" + email + "'"
    c.execute(s)
    x = c.fetchone()
    if request.POST:
        name = request.POST.get('name')
        mob = request.POST.get('mob')

        ndays = request.POST.get('ndays')
        tamount = int(rate) * int(ndays)
        ttype = request.POST.get("ttype")

        s = "insert into rent(proid,uid,sid,name,mob,pname,ndays,amount,tamount,status,pstatus) values('" + str(rid) + "',(select uid from register where email='" + email + "'),'" + str(sid) + "','" + name + "','" + mob + "','" + str(pname) + "','" + ndays + "','" + str(rate) + "','" + str(tamount) + "','Processing','Not Paid')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Error"
        else:
            msg = "Succesfull"
            c.execute("select LAST_INSERT_ID()")
            rentid = c.fetchone()[0]
            request.session["rentid"] = rentid
            print(rentid)
            if ttype == 'card':
                return HttpResponseRedirect("/rentpayment")
            else:
                return HttpResponseRedirect("/userhome")
    return render(request, "rent.html", {"y": y})
def rentpayment(request):
    msg = " "
    email = request.session.get("email")
    rid = request.session.get("rentid")

    s = "select uid from rent where rentid='" + str(rid) + "'"

    c.execute(s)
    x = c.fetchone()
    uid = x[0]
    if request.POST:
        ctype = request.POST.get('ctype')
        cnumber = request.POST.get('cnumber')
        cvv = request.POST.get('cvv')
        s = "insert into rentpayment(rid,uid,ctype,cnumber,cvv) values('" + str(rid) + "','" + str(uid) + "','" + ctype + "','" + cnumber + "','" + cvv + "')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Error"
        else:
            msg = "Registration Succesfull"
            q = "update rent set pstatus='Paid' where rentid='" + str(rid) + "'"
            try:
                c.execute(q)
                db.commit()
            except:
                msg = "Error"
            else:
                msg = "Updation Succesfull"
            return HttpResponseRedirect("/userhome")
    return render(request, "rentpayment.html", {"msg": msg})
def paymentdetails(request):
    email = request.session.get("email")

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="machine"
        )
        c = db.cursor()

        # Purchase details
        s = """
        SELECT * FROM purchase 
        WHERE uid = (SELECT uid FROM register WHERE email=%s)
        """
        c.execute(s, (email,))
        x = c.fetchall()

        # Rent details
        q = """
        SELECT * FROM rent 
        WHERE uid = (SELECT uid FROM register WHERE email=%s)
        """
        c.execute(q, (email,))
        y = c.fetchall()

    except Exception as e:
        print("ERROR:", e)
        x = []
        y = []

    return render(request, "paymentdetails.html", {"x": x, "y": y})
def staffbookingdetails(request):
    email = request.session.get("email")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="machine"
    )
    c = db.cursor()

    # ✅ Get staff id
    c.execute("SELECT sid FROM staffregister WHERE semail=%s", (email,))
    staff = c.fetchone()

    if not staff:
        return render(request, "staffbookingdetails.html", {"x": [], "y": []})

    sid = staff[0]

    # =========================
    # ✅ PURCHASE DETAILS (FIXED)
    # =========================
    c.execute("SELECT * FROM purchase WHERE sid=%s", (sid,))
    rows = c.fetchall()

    x = []
    for r in rows:
        x.append({
            "purid": r[0],
            "name": r[4],      # purname
            "place": r[5],     # purplace
            "address": r[6],   # puraddress
            "mobile": r[7],    # purmobile
            "status": r[10],   # dstatus
        })

    # =========================
    # ✅ RENT DETAILS (ALREADY CORRECT)
    # =========================
    c.execute("""
        SELECT rentid, name, mob, pname, ndays, tamount, status, pstatus
        FROM rent WHERE sid=%s
    """, (sid,))

    rows = c.fetchall()

    y = []
    for r in rows:
        y.append({
            "rentid": r[0],
            "name": r[1],
            "mob": r[2],
            "pname": r[3],
            "ndays": r[4],
            "amount": r[5],
            "status": r[6],
            "pstatus": r[7],
        })

    print("STAFF PURCHASE:", x)
    print("STAFF RENT:", y)

    return render(request, "staffbookingdetails.html", {"x": x, "y": y})

def orderstatus(request):
    purid = request.GET.get("purid")

    print("PURID RECEIVED:", purid)  # DEBUG

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="machine"
    )
    c = db.cursor()

    # 🔥 FIRST CHECK IF ROW EXISTS
    c.execute("SELECT purid, pstatus FROM purchase WHERE purid=%s", (purid,))
    row = c.fetchone()
    print("BEFORE UPDATE:", row)

    # 🔥 UPDATE BOTH STATUS + PAYMENT
    c.execute("""
        UPDATE purchase 
        SET dstatus='Delivered', pstatus='Paid' 
        WHERE purid=%s
    """, (purid,))
    db.commit()

    # 🔥 VERIFY AFTER UPDATE
    c.execute("SELECT purid, pstatus FROM purchase WHERE purid=%s", (purid,))
    row = c.fetchone()
    print("AFTER UPDATE:", row)

    return HttpResponseRedirect("/staffbookingdetails")
def staffdeliverydetails(request):
    import mysql.connector

    email = request.session.get("email")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="machine"
    )
    c = db.cursor()

    # ✅ Get staff id
    c.execute("SELECT sid FROM staffregister WHERE semail=%s", (email,))
    staff = c.fetchone()

    if not staff:
        return render(request, "staffdeliverydetails.html", {"x": [], "y": []})

    sid = staff[0]

    # ✅ AUTO FIX: mark delivered purchases as Paid
    c.execute("""
        UPDATE purchase 
        SET pstatus='Paid'
        WHERE dstatus='Delivered' AND pstatus!='Paid'
    """)
    db.commit()

    # =========================
    # ✅ PURCHASE (FIXED)
    # =========================
    c.execute("""
        SELECT purid, purname, purplace, puraddress, purmobile, dstatus, pstatus
        FROM purchase
        WHERE sid=%s AND dstatus=%s
    """, (sid, "Delivered"))

    rows = c.fetchall()

    x = []
    for r in rows:
        x.append({
            "purid": r[0],
            "name": r[1],
            "place": r[2],
            "address": r[3],
            "mobile": r[4],
            "status": r[5],
            "pstatus": r[6],
        })

    # =========================
    # ✅ RENT (ALREADY CORRECT)
    # =========================
    c.execute("""
        SELECT rentid, name, mob, pname, ndays, tamount, status, pstatus
        FROM rent
        WHERE sid=%s AND status=%s
    """, (sid, "Delivered"))

    rows = c.fetchall()

    y = []
    for r in rows:
        y.append({
            "rentid": r[0],
            "name": r[1],
            "mob": r[2],
            "pname": r[3],
            "ndays": r[4],
            "amount": r[5],
            "status": r[6],
            "pstatus": r[7],
        })

    print("PURCHASE:", x)
    print("RENT:", y)

    return render(request, "staffdeliverydetails.html", {"x": x, "y": y})
def rentstatus(request):
    rentid = request.GET.get("rentid")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="machine"
    )
    c = db.cursor()

    q = """
    UPDATE rent 
    SET status=%s, pstatus=%s 
    WHERE rentid=%s
    """

    try:
        c.execute(q, ("Delivered", "Paid", rentid))
        db.commit()
        print("RENT UPDATED")
    except Exception as e:
        print("ERROR:", e)

    return HttpResponseRedirect("/staffbookingdetails")
def staffproductview(request):
    email = request.session.get("email")
    s = "select * from addproduct"
    c.execute(s)
    x = c.fetchall()
    return render(request,"staffproductview.html",{"x":x})