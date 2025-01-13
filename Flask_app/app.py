from flask import Flask, render_template, request

app = Flask(__name__)

#setting up the home page of the frontend
@app.route('/')
def frontend_page():
    return render_template('index.html')

#get the data from the POST request
@app.route('/submit', methods=['POST'])
def submit_data():

    #Parce the POST request
    n_of_nodes = request.form['n_of_nodes']
    market = request.form['market']
    country = request.form['country']
    customer = request.form['customer']
    activity = request.form['activity']
    product = request.form['product']
    site = request.form['site']
    n_of_sites = request.form['n_of_sites']
    upgrade_version = request.form['upgrade_version']
    remarks = request.form['remarks']
    
    #Construct dcionary with all the data
    metrics_data = {
        'NofNodes': n_of_nodes,
        'Market': market,
        'Country': country,
        'Customer': customer,
        'Activity': activity,
        'Product': product,
        'Site': site,
        'NofSites': n_of_sites,
        'UpgradeVersion': upgrade_version,
        'Remarks': remarks
    }
    print(metrics_data)
    return "Form submited!"


if __name__ == '__main__':
    app.run()