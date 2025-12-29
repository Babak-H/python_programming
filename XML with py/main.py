# add css design to program
from flask import Flask, render_template, flash, redirect, url_for, session, request, make_response
import requests
import xml.etree.ElementTree as et
import json
import pdfkit

app = Flask(__name__)

list_rates = {}
calc_res = ""
url = "http://api.nbp.pl/api/exchangerates/tables/a"


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/display_res')
def display_res():
    return render_template('display_res.html', calc_res=calc_res)


@app.route('/display_rate')
def display_rate():
    return render_template('display_rate.html', list_rates=list_rates)


@app.route("/control", methods = ['GET', 'POST'])
def control():
    global calc_res
    calc_res = ""
    options = ['USD', 'AUD', 'CAD', 'NZD', 'EUR', 'GBP', 'JPY', 'SEK', 'CNY', 'RUB']
    if request.method == 'POST':
        base_amount = request.form.get("pln_amount")
        curr = request.form.get("curr")
        transaction_type = request.form.get("type")
        # foreign_amount = request.form.get("foreign_amount")

        address = 'http://api.nbp.pl/api/exchangerates/rates/a/'+curr
        result = requests.get(address, headers={"Accept":"application/xml"})
        root = et.fromstring(result.text)
        Rates = root.find("Rates")
        Rate = Rates.find("Rate")
        rate = Rate.find("Mid").text
        
        if (transaction_type == "sell"):
            value = float(base_amount) * float(rate)
            calc_res = "You can sell it for " + str(round(value, 2)) + " PLN."
        if (transaction_type == "buy"):
            value = float(base_amount) / float(rate)
            calc_res = "You can buy " + str(round(value, 2)) + " " + curr
        return redirect(url_for('display_res'))
    return render_template("rate_control.html", options=options)


@app.route("/exchange", methods=['GET', 'POST'])
def exchange():
    global list_rates
    list_rates = {}
    options = ['USD', 'AUD', 'CAD', 'NZD', 'EUR', 'GBP', 'JPY', 'SEK', 'CNY', 'RUB']
    if request.method == 'POST':
        ops = request.form.getlist("my_checkbox")

        result = requests.get(url, headers={"Accept":"application/xml"})
        root = et.fromstring(result.text)
        ExchangeRatesTableates = root.find("ExchangeRatesTable")
        Rates = ExchangeRatesTableates.find("Rates")
        all_rate = Rates.findall("Rate")
        for rate in all_rate:
            if rate.find("Code").text in ops:
                list_rates[rate.find("Code").text] = rate.find("Mid").text
        return redirect(url_for('display_rate'))
    return render_template("currency_exchange.html", options=options)

@app.route("/chart/<string:currency>", methods=['GET'])
def chart(currency):
    l_rate = []
    address = "http://api.nbp.pl/api/exchangerates/rates/a/{}/last/7".format(currency)
    result = requests.get(address, headers={"Accept" : "application/xml"})
    root = et.fromstring(result.text)
    rates = root.find("Rates")
    all_rate = rates.findall("Rate")
    for rate in all_rate:
        l_rate.append(float(rate.find("Mid").text))
    return render_template("display_chart.html", rates=l_rate, curr=currency)

@app.route("/pdf_template/<curr>", methods=['GET'])
def pdf_template(curr):

    path_wkthmltopdf = r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    
    l_rate = {}
    address = "http://api.nbp.pl/api/exchangerates/rates/a/{}/last/7".format(curr)
    result = requests.get(address, headers={"Accept" : "application/xml"})
    root = et.fromstring(result.text)
    rates = root.find("Rates")
    all_rate = rates.findall("Rate")
    for rate in all_rate:
        l_rate[rate.find("EffectiveDate").text] = float(rate.find("Mid").text)

    rendered  = render_template('pdf_template.html', dic = l_rate, currency=curr)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = "application/pdf"
    response.headers['Content-Disposition'] = "inline; filename=output.pdf"
    return response


if __name__ == "__main__":
    app.run(debug=True)