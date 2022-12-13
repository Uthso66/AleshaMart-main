# AleshaMart

To run this project

 
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



API Project

Objectives:
• To develop API-based websites to simulate the functionalities of e-commerce
services among different organisations.
Submission:
• Project showcasing.
Description:
In this project, you will simulate the e-commerce functionalities among different
organisations. You will need to consider three different organisations: an e-commerce
organisation (similar to Daraz), a backend product supplier which supplies required products
to the e-commerce organisation and a Bank to facilitate transactions between different
entities within this eco-system.
Within this setting, the assumptions for each organisation are the following:
• The e-commerce organisation only sells three products.
• These products are supplied by the supplier after its corresponding charges are
transacted via the bank from the e-commerce organisation.
• A user can buy any amount of these three products from the e-commerce website
after making a successful transaction via the bank.
The flow among these entities will be something like this:
1. A user first registers and then logs in to the e-commerce website. After a successful
login, the user lands into the home page.
2. When in the home page for the first time, the user needs to set up his/her bank
information (account number) and add a secret which can be used to transact with
the bank.
3. The user can view and buy the products from a corresponding page.
4. The user chooses products from these three products and decides to buy them.
5. The amount required to buy them is calculated and a transaction request is sent to
the bank with other bank information related to the user.
6. The bank settles the transaction and returns a transaction number to the e-Commerce
website.
7. The e-commerce website interacts with the bank similarly to transfer the required
amount from its account to the supplier’s account.
8. The bank settles the transaction and returns a transaction number to the e-Commerce
website.
9. The e-commerce website submits a request of the ordered products to the supplier
with the transaction number.
10. Then a successful message is shown to the user.
11. The e-commerce organisation updates its record so that the user can see that the
chosen products have been supplied.
12. There must be a mechanism for these entities – a user, the e-commerce organisation
and the supplier- to show their bank balance.

CSE446 Web Technologies

Dept. of CSE, SUST
Figure 1: Architecture of the system

These three organisations (e-commerce, supplier, bank) will expose their corresponding web
APIs (see Figure 1). All interactions among these organisations need to be carried out using
these APIs. It is upto you how you design the APIs and urls. It is recommended to use the
technologies you have learned in this course such as Nodejs, Express, mongoDB.
It is to be noted that we have not considered many security considerations in this project as
our focus is on the functionalities.
Mark distribution:
The total mark of the project is 100. The mark distribution of the project is as follows:

Description Mark
Requirements fulfilment 60
Design & Aesthetics 20
Q/A during showcasing 20

Submission:
This project needs to be showcased to your teacher on a group basis. It is expected that
everyone in the group will contribute equally during the development of the project. There
will be rigorous Q/A session during the showcasing where each member of the group is
expected to answer any question when asked.
The date of final submission and showcasing will be announced later.
