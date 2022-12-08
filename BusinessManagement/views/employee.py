from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():

    rows = []

    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    
    query = "SELECT IS601_MP2_Employees.id, IS601_MP2_Employees.first_name, IS601_MP2_Employees.last_name, IS601_MP2_Employees.email, IS601_MP2_Employees.company_id, IS601_MP2_Companies.name AS company_name FROM IS601_MP2_Employees LEFT JOIN IS601_MP2_Companies ON IS601_MP2_Employees.company_id = IS601_MP2_Companies.id WHERE 1=1"
    
    args = [] # <--- append values to replace %s placeholders
    
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    
    # jp2267 22 Nov
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    email = request.args.get("email")
    company = request.args.get("company")
    col = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    
    #jp2267 22 Nov
    # TODO search-3 append like filter for first_name if provided    
    if first_name:
        query += " AND IS601_MP2_Employees.first_name like %s"
        args.append(f"%{first_name}%")

    # TODO search-4 append like filter for last_name if provided
    if last_name:
        query += " AND IS601_MP2_Employees.last_name like %s"
        args.append(f"%{last_name}%")

    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND IS601_MP2_Employees.email like %s"
        args.append(f"%{email}%")

    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND IS601_MP2_Employees.company_id = %s"
        args.append(company)    

    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if col and order:
        if col in allowed_columns \
            and order in ["asc", "desc"]:
                query += f" ORDER BY {col} {order}"

    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100 :
        query += " LIMIT %s"
        args.append(int(limit))
    else:
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
        flash('limit should be a numeric value or try entering values between 1 to 100', "warning")
        return redirect(request.url)    


    print("query",query)
    print("args", args)
    try:
        print(query)
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        print(e)
        flash("There was something wrong in listing the employee data","error")
    # hint: use allowed_columns in template to generate sort dropdown
    allowed_list = [(v,v) for v in allowed_columns]
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_list)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message) 
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        first_name = request.form.get("first_name", None)
        last_name = request.form.get("last_name", None)
        email = request.form.get("email", None)
        company_id = request.form.get("company", None)

        #ucid: jp2267    date: 11-17-2022
        if first_name == "":
            flash('first_name field should not be empty', "warning")
            return redirect(request.url)

        if last_name == "":
            flash('last_name field should not be empty', "warning")
            return redirect(request.url)
        
        if email == "":
            flash('email field should not be empty', "warning")
            return redirect(request.url)
        
        #ucid: jp2267    date: 11-17-2022
        try:
            if company_id == "":
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Employees (first_name, last_name, email) VALUES(%s, %s, %s)"""
                ,first_name, last_name, email
                )
            else:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id) VALUES(%s, %s, %s, %s)"""
                ,first_name, last_name, email, company_id
                ) # <-- TODO add-6 add query and add arguments
            if result.status:
                flash("Created Employee Record", "success")

        except Exception as e:
            # TODO add-7 make message user friendly
            #flash(str(e), "danger")
            print(e)
            flash('There is some error in adding employee record', "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)

    #jp2267 3 dec 
    id = request.args.get("id")
    print(id)
    resp = None
    row = None


    if id is None: # TODO update this for TODO edit-1
        return redirect("employee.search")
    else:
        if request.method == "POST" and request.form.get("first_name") and request.form.get("last_name") and request.form.get("email"):
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company may be None
            # TODO edit-5 email is required (flash proper error message)
                #jp2267 3 dec 
            fn = request.form.get("first_name")
            ln = request.form.get("last_name")
            c = request.form.get("company")
            em = request.form.get("email")
            # data = [first_name, last_name, company_id, email]
            #data.append(id)

            if fn == "":
                flash('First name is required', "danger")

            if ln == "":
                flash('Last name is required', "danger")

            if c == "":
                c = None

            if em == "":
                flash('Email is required', "danger")

            try:
                # TODO edit-6 fill in proper update query
                result = DB.update("""
                UPDATE IS601_MP2_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s
                """, fn,ln,c,em,id)

                if result.status:
                    resp = "Updated"
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash('There was an error in editing the employee record', "danger")
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            result = DB.selectOne("SELECT IS601_MP2_Employees.id, IS601_MP2_Employees.first_name, IS601_MP2_Employees.last_name, IS601_MP2_Employees.email, IS601_MP2_Employees.company_id, IS601_MP2_Companies.name FROM IS601_MP2_Employees LEFT JOIN IS601_MP2_Companies ON IS601_MP2_Employees.company_id = IS601_MP2_Companies.id WHERE IS601_MP2_Employees.id = %s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash('There was an error in editing the employee record', "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row, resp=resp)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    id = request.args.get("id")
    args = {**request.args}
    if id:
        result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id = %s", id)
        flash("Deleted Employee Record", "success")
        del args["id"]
    return redirect(url_for("employee.search", **args))    

