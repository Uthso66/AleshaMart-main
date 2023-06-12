# AleshaMart


## Description

This project simulates e-commerce functionalities among different organizations. It involves three main entities: an e-commerce organization (similar to Daraz), a backend product supplier, and a bank. The objective is to replicate the flow of transactions and interactions within this ecosystem.

The following assumptions are made for each organization:

    The e-commerce organization offers three specific products for sale.
    The product supplier provides the required products to the e-commerce organization after receiving the corresponding charges.
    Users can purchase any quantity of these three products from the e-commerce website by making successful transactions through the bank.

The flow among these entities follows these steps:

    User Registration and Login:
        Shows the homepage of the website.
        Users register and log in to the e-commerce website are in choice option.
        User can login if they are registered else they have ot registered.

    Bank Information Setup:
        After buying a product user have to include their account number and a secret key for transactions. Which works like a popup of paypal window.

    Product Viewing and Purchase:
        Users can view and select products from the available options.
        Users decide on the quantity of each product they want to purchase.

    Transaction Initiation:
        The e-commerce website calculates the total amount required for the purchase.
        A transaction request, along with the user's bank information provided by user, is sent to the bank.

    User Transaction Approval:
        The bank verifies the user's bank account and processes the transaction.
        Upon successful processing, the bank returns a transaction number to the e-commerce website.

    Product Order Placement:
        The e-commerce website submits an order request to the supplier, including the transaction number. Suplier is a subsidary organization of e-commerce website.

    Confirmation and Feedback:
        A success message is displayed to the user, indicating that the ordered products will be supplied.
        The e-commerce organization updates its records to reflect the user's purchase.

    Bank Balance Display:
        All entities involved, including the user, e-commerce organization have mechanisms to display their respective bank balances.


## To run this project

 
Step 1. Clone the project
    $ git clone https://github.com/Uthso66/AleshaMart-main.git
    
Step 2: $ cd AleshaMart    

Step 3: Install dependencies 

asgiref==3.2.10 
Django==3.1
 Pillow==7.2.0
pytz==2020.1 
requests==2.22.0
six==1.14.0 
sqlparse==0.3.1

  
Step 4: Apply the migration
    $ python manage.py migrate
    

Step 6: Run Development server
    $ python manage.py runserver


Feel free to customize and modify the code to suit your specific requirements.
If you are feeling generous buy me a coffee. https://www.buymeacoffee.com/uthso
