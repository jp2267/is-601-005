from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():

    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    query = "SELECT id, name, address, city, country, state, zip, website FROM IS601_MP2_Companies WHERE 1=1"
        
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    col = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10) 

    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds

    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND IS601_MP2_Companies.name like %s"
        args.append(f"%{name}%")

    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND IS601_MP2_Companies.country like %s"
        args.append(f"%{country}%")

    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND IS601_MP2_Companies.state like %s"
        args.append(f"%{state}%")
    
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if col and order:
        if col in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {col} {order}"
    
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100 :
        query += " LIMIT %s"
        args.append(int(limit))
    else:
        flash('limit should be a numeric value or try entering 1 or 100 ', "warning")
        return redirect(request.url)  

    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        flash('There was an error getting company records', "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    allowed_list = [(v,v) for v in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_list)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
    
        has_error = False # use this to control whether or not an insert occurs

        #jp2267 3 Dec
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        n = request.form.get("name", None)
        ad = request.form.get("address", None)
        c = request.form.get("city", None)
        s = request.form.get("state", None)
        country = request.form.get("country", None)
        z = request.form.get("zip", None)
        w = request.form.get("website", None)

        # TODO add-2 name is required (flash proper error message)
        if n == "":
            flash('Company name is required', "danger")
            has_error = True

        # TODO add-3 address is required (flash proper error message)
        if ad == "":
            flash('Address is required', "danger")
            has_error = True

        # TODO add-4 city is required (flash proper error message)
        if c == "":
            flash('City is required', "danger")
            has_error = True

        # TODO add-5 state is required (flash proper error message)
        if s == "":
            flash('State is required', "danger")
            has_error = True

        # TODO add-6 country is required (flash proper error message)
        if country == "":
            flash('Country is required', "danger")
            has_error = True

        # TODO add-7 website is not required
        if w == "":
            pass

        #jp2267 3 Dec
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT
                INTO IS601_MP2_Companies (name,address,city,country,state,zip,website)
                VALUES(%s, %s, %s, %s, %s, %s, %s)""", n,ad,c,country,s,z,w) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash('There was something wrong while adding the company data', "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    
    id = request.args.get("id")
    resp = None
    row = None
    
    print("request", request.args)


    if id is None: # TODO update this for TODO edit-1
        return redirect("company.search")
    else:
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-3 name is required (flash proper error message)
            # TODO edit-4 address is required (flash proper error message)
            # TODO edit-5 city is required (flash proper error message)
            # TODO edit-6 state is required (flash proper error message)
            # TODO edit-7 country is required (flash proper error message)
            # TODO edit-8 website is not required
            # 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            #data = [name, address, city, state, country, zipcode, website]
            #data.append(id)
            n = request.form.get("name")
            ad = request.form.get("address")
            ci = request.form.get("city")
            s = request.form.get("state")

            co = request.form.get("country")
            z = request.form.get("zip")
            w = request.form.get("website")

            print(request.args.get("country" + "no country found")) 
            try:
                # TODO edit-9 fill in proper update query
                result = DB.update("""
                UPDATE IS601_MP2_Companies SET 
                name = %s,
                address = %s,
                city = %s,
                state = %s,
                country = %s,
                zip = %s,
                website = %s
                WHERE id = %s
                """, n,ad,ci,s,co,z,w,id)

                if result.status:
                    resp = "Updated"
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                flash(str(e), "danger")
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT id, name, address, city, country, state, zip, website FROM IS601_MP2_Companies WHERE id = %s", id)
            if result.status:
                row = result.row
                print(row)
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", row=row, resp=resp)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    id = request.args.get("id")
    args = {**request.args}
    if id:
        result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE ID = %s", id)
        flash("Deleted Company Record", "success")
        del args["id"]
    return redirect(url_for("company.search", **args))