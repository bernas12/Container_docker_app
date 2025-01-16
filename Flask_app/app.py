from flask import Flask, render_template, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)

#enable CORS to solve DNS problems
CORS(app)

#setting up the home page of the frontend
#@app.route('/')
#def frontend_page():
    #return render_template('index.html')

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

    #setting up the connection configuration to the database
    DB_HOST = 'database'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWORD = 'myDBpassword'
    DB_NAME = 'metrics'

    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        #Create the table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS metrics (
            id INT AUTO_INCREMENT PRIMARY KEY,
            NofNodes INT,
            Market VARCHAR(255),
            Country VARCHAR(255),
            Customer VARCHAR(255),
            Activity VARCHAR(255),
            Product VARCHAR(255),
            Site VARCHAR(255),
            NofSites INT,
            UpgradeVersion VARCHAR(255),
            Remarks VARCHAR(255)
        );
        """
        cursor.execute(create_table_query)
        #cursor.fetchall()

        # Insert the data into the database
        insert_query = "INSERT INTO metrics (NofNodes, Market, Country, Customer, Activity, Product, Site, NofSites, UpgradeVersion, Remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        values = (n_of_nodes, market, country, customer, activity, product, site, n_of_sites, upgrade_version, remarks)
        cursor.execute(insert_query, values)
        #cursor.fetchall()

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()
        return "Form submitted successfully!"
    
    except Exception  as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)