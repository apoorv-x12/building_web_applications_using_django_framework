from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AuthorForm
import datetime
import sqlite3


def list_authors(request):
    try:
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        cur.execute("select * from authors")
        authors = cur.fetchall()
        con.close()
        return render(request, 'db/list_authors.html', {'authors': authors})
    except Exception as ex:
        print("Error :", ex)
        return render(request, 'db/list_authors.html')


def add_author(request):
    if request.method == "GET":
        return render(request, 'db/add_author.html')
    else:
        # Process data sent from client
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        try:
            con = sqlite3.connect(r"db.sqlite3")
            cur = con.cursor()
            cur.execute("insert into authors(fullname,email,mobile) values(?,?,?)",
                        (fullname, email, mobile))
            con.commit()
            con.close()
            return render(request, 'db/add_author.html',
                          {'message': f'Added [{fullname}] Successfully!'})
        except Exception as ex:
            print("Error :", ex)
            return render(request, 'db/add_author.html',
                          {'message': 'Sorry! Could not add author!',
                           'fullname': fullname,
                           'email': email,
                           'mobile': mobile
                           }
                          )


def add_author_form(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, 'db/add_author_form.html', {'form' : form})
    else:
        # Process data sent from client
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                fullname = form.cleaned_data['fullname']
                email = form.cleaned_data['email']
                mobile = form.cleaned_data['mobile']
                con = sqlite3.connect("db.sqlite3")
                cur = con.cursor()
                cur.execute("insert into authors(fullname,email,mobile) values(?,?,?)",
                            (fullname, email, mobile))
                con.commit()
                con.close()
                return redirect("/basics/authors")
            except Exception as ex:
                print("Error :", ex)
                return render(request, 'db/add_author_form.html',
                              {'form' : form,
                               'message': 'Sorry! Could not add author!'}
                              )
        else:
            return render(request, 'db/add_author_form.html', {'form': form})
