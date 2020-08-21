# Creating a BUDGET and EXPENSES program for Perimeter83

import plotly.graph_objects as go
###########################CGI TEST AREA################################
# This is nothing of value
# References to understanding CGI, this is the highly recommended way to get a simple program like this
# up on a website, at least as far as I know.
# https://docs.python.org/2/library/cgi.html
# https://www.tutorialspoint.com/python/python_cgi_programming.htm
# https://httpd.apache.org/docs/current/howto/cgi.html
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")
print("<p>name:", form["name"].value)
print("<p>addr:", form["addr"].value)

###########################CGI TEST AREA################################

# For Simply Uploading to Plotly.
# import chart_studio.plotly as py

# Plotly user and api key input (use your own, mine is just for reference)
# username = 'dsduncan' # your username
# api_key = 'smz56cXYzPoYIAfea2EN' # your api key - go to profile > settings > regenerate keychart_studio.tools.set_credentials_file

# Creating Graphs in HTML
import plotly.io as pio

# Labels And Values Corresponding to Eachother By Their Position In The List
labels = ['Payroll','Rent','Utilities','Taxes','Insurance','Office Supplies','Transportation','Marketing','Memberships','Professional Services']

# Get user input for each value.
pay = input("\nEnter Payroll Expenses: ")
rent = input("\nEnter Rent Expenses: ")
util = input("\nEnter Utilities Expenses: ")
tax = input("\nEnter Taxes Expenses: ")
insur = input("\nEnter Insurance Expenses: ")
os = input("\nEnter Office Supplies Expenses: ")
trans = input("\nEnter Transportation Expenses: ")
mark = input("\nEnter Marketing Expenses: ")
memb = input("\nEnter Memberships Expenses: ")
ps = input("\nEnter Professional Services Expenses: ")

# Create a general list of values to be replaced by actual numbers input by the user.
values = [pay, rent, util, tax, insur, os, trans, mark, memb, ps]
# Calculate Minimum and Maximum Values Input By The User
maxi = max(values)
mini = min(values)

print(maxi)
print(mini)

# Array / List in which determines what slice of the "pie" is cut out for display
cut = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Determining which spot the max value belongs in the "cut" list.
if (maxi == pay):
    cut[0] = 0.2
elif (maxi == rent):
    cut[1] = 0.2
elif (maxi == util):
    cut[2] = 0.2
elif (maxi == tax):
    cut[3] = 0.2
elif (maxi == insur):
    cut[4] = 0.2
elif (maxi == os):
    cut[5] = 0.2
elif (maxi == trans):
    cut[6] = 0.2
elif (maxi == mark):
    cut[7] = 0.2
elif (maxi == memb):
    cut[8] = 0.2
elif (maxi == ps):
    cut[9] = 0.2

# Determining which spot the min value belongs in the "cut" list.
if (mini == pay):
    cut[0] = 0.2
elif (mini == rent):
    cut[1] = 0.2
elif (mini == util):
    cut[2] = 0.2
elif (mini == tax):
    cut[3] = 0.2
elif (mini == insur):
    cut[4] = 0.2
elif (mini == os):
    cut[5] = 0.2
elif (mini == trans):
    cut[6] = 0.2
elif (mini == mark):
    cut[7] = 0.2
elif (mini == memb):
    cut[8] = 0.2
elif (mini == ps):
    cut[9] = 0.2

print(cut)

# Use `hole` to create a donut-like pie chart
# `pull` uses the cut list in order to determine which pieces of the pie to pull out
dcFig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, pull=cut)])
dcFig.show()

# Creates a general bar graph with the same labels and values
bFig = go.Figure([go.Bar(x=labels, y=values)])
bFig.show()

# Upload to Plotly
# py.plot(dcFig, filename = 'DC_BUDGET_AND_EXPENSES', auto_open=True)
# py.plot(bFig, filename = 'B_BUDGET_AND_EXPENSES', auto_open=True)

# Export graphs to HTML file
# pio.write_html(dcFig, file=’DC_BUDGET_AND_EXPENSES.html’, auto_open=True)
# pio.write_html(bFig, file=’B_BUDGET_AND_EXPENSES.html’, auto_open=True)
