<h1 align="center">Plantastic (ms4)</h1>

<span id="plantastic"></span>

<h2 align="center"><img src=""></h2>

Plantastic is an online store that allows the users to purchase specific plants from the comfort of their own home. They can make an account to see what they've bought in the past and to save their details. The user will also be able to sign up for a newsletter and make safe payments using stripe.

This project is my fourth assignment of the Full stack development course I am following at CodeInstitute. This is why the site is slightly limited in functionality, meaning you can't actually make a purchase. If you'd like to test it out you can use the following details for making a payment:
- Card number: 4242 4242 4242 4242
- Date: 04/24
- CVC: 242
- Postal code or ZIP: 42424

[View the live project here.](https://plantastic-lon.herokuapp.com/)

---

## Index 

- <a href="#ux">1. User experience (UX)</a>
  - <a href= "#ux-goals">1.1 Project Goals</a>
  - <a href= "#ux-target">1.2 User Target</a>
  - <a href="#ux-stories">1.3 User stories</a>
  - <a href="#ux-design">1.4 Design</a>
  - <a href="#ux-mockup">1.5 Mockup designs</a>
- <a href="#features">2. Features</a>
  - <a href="#features-existing">2.1 Existing features</a>
  - <a href="#features-future">2.2 Features left to implement in the future</a>
- <a href="#technologies">3. Technologies used</a>
- <a href="#testing">4. Testing</a>
- <a href="#deployment">5. Deployment</a>
- <a href="#credits">6. Credits</a>
- <a href="#Acknowledge">7. Acknowledge</a>
- <a href="#Acknowledge">8. Disclaimer</a>

---

<span id="ux"></span>

<h1>1. User experience (UX)</h1>

<span id="ux-goals"></span>

### 1.1 Project Goals

<br>

The purpose of this project is to 

*"...build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service"* using HTML, CSS, JavaScript, Python+Django, a relational database (recommending MySQL or Postgres), Stripe payments
and possible additional libraries and API's. 

As said by Codeinstitute who i=has assigned this project.

This project has a full set of CRUD (creation, reading, updating and deletion of data records) features. CRUD at user interface level:

|Operation|HTTP|DDS|Description|
|---|----|----|----|
|**Create**|PUT/POST|Write|Create a resource: Users can create profiles by signing up. Users can create orders by adding items to bag and then follow the checkout procedure. Admin can create products and send newsletters.
|**Read**|GET|Read|Retrieve a resource: Users can retrieve, search and view products.
|**Update**|PUT/PATCH/POST|Write|Update a resource: Users can update/edit the delivery information. Admin can update/edit products.
|**Delete**|DELETE|Dispose|Delete a resource: Admin can delete products.

<span id="ux-target"></span>

### 1.2 User target

The target group for plantastic is customers who like plants and want to have specific ones for their own. It is therefor important that the customer/user can have a full overview of the different products the site offers and also be able to easily checkout. It is necessary that no things get in the way of the user, because this will potentially make the owner lose a customer.

<span id="ux-stories"></span>

### 1.3 User stories 

As a | I want to be able to | So that I can 
------- | -------- | ------- 
Shopper | View a list of products | Select some to purchase 
Shopper | View individual product details | See the price/description
Shopper | View the total of my purchases at any time | Avoid spending too much 
Site User | Easily register for account | Have an account/view my profile 
Site User | Easily login/logout | Access my account  
Site User | Easily recover my password | Recover access to account 
Site User | Receive email confirmation after registering | Verify registration successful 
Site User | Have a personalised user profile | View order history/save payment info 
Shopper | Search for a product | Find a specific product 
Shopper | Easily see what I've searched for | Quickly decide if what I want is there
Shopper | Select qty of product when purchasing | Ensure I don't select wrong product
Shopper | View basket items | See total cost/all items I'll receive 
Shopper | Adjust qty of items in my bag | Easily make changes to bag before checkout 
Shopper | Easily enter payment info | Checkout quickly 
Shopper | View an order confirmation after checkout | Ensure no mistakes made 
Shopper | Sign up for a newsletter | Get updates of new products and info
Store Owner | Add a product | Add new items to store 
Store Owner | Edit/update a product | Change product details
Store Owner | Delete a product | Remove items not for sale 
Store Owner | Send Newsletter | Keep customers up to date of new products or info  

<span id="ux-design"></span>

### 1.4 Design 
    
- #### Colour Scheme
The colours used throughout this project are shades of green, white and black to keep the visuals simple and clean. This colour scheme has also been choosen to stay in the theme of plants. 

- Green: mostly the "success" colour of Bootstrap 5 to give buttons a clear colour.
- White: To use as background of different parts because of the dark background.
- Black: Mostly used for the text on the white backgrounds for easy readability.

Some red and other colours have been used for the messages shown if something goes wrong or succesfull, to show a good difference between the messages.

- #### Fonts
The **Preahvihear font** is used throughout the whole website for all text. sans serif is the fallback in case the main font isn't being imported to the site correctly. I used this font because it's easy to look at.

- #### Icons
In this project the icons used are provided by [fontawesome](https://fontawesome.com/). The icons used have a practical and functional purpose for example the magnifying glass icon for the search box. They also give character to the website.

- #### Images
The images I used for this project came mostly from [Pexels](https://www.pexels.com/): 
- The background image: [Pexels](https://www.pexels.com/) uploaded by: [Catia Matos](https://www.pexels.com/@catiamatos). 
- All images for the products were taken from: [home-designing](http://www.home-designing.com/best-low-light-indoor-house-plants-for-sale)
- backup image for product without image: [pexels](https://www.pexels.com/) uploaded by: [Daria Shevtsova](https://www.pexels.com/@daria)

- #### Interactive design 

    - The website has to be easy to navigate. 
    - The user can quickly find the information he/she wants to find. 

<span id="ux-mockup"></span>

### 1.5 Mockup designs
See all Wireframes [here](wireframes/ms4.pdf)

The wireframes were made with [Balsamiq](https://balsamiq.com/)

<span id="features"></span>

<h1>2. Features</h1>

### 2.1 Existing features 

#### 1. Design 
- An attractive and simple layout with consistency.
- Simple navigation throughout the website by using the navigation bar. 
- Showing the products simple and clearly.

#### 2. General 
- Main navigations links in navigation bar shown as a collapsible navbar (hamburger button) shown at tablets and mobile devices.
- There are links to the social media platforms at the bottom of the website. 
- People can sign up for the newsletter in the footer.
- Back to top button.
- the index page shows some text with an immediat link to the products.

#### 3. Products
- Products can be created, read, updated and deleted (CRUD) by the super-user. 
- People can search for products with the search bar. 
- Users have access to their profile, with an overview of all their orders.

#### 4. Signup, signin and signout 
- People can create a new account on the web application. 
- People can signin with their existing accounts. 
- People can easily sign out.
- If a person creates a new account, signs in or signs out, a flashed message will appear with the action the person has done.

#### 5. Profile 
If not signed in:
- Sign up - allows visitor to sign up. If user already has an account there is also a link to log in instead. When signing up a toast with success message is shown and a confirmation mail is sent.
- Sign in - allows registered users to log in. When signed in, a welcome toast is shown.

If signed in:
- Profile - if saved, users delivery information is shown, with the possibility to update the information. If user has an order history it is shown here. 
- Logout - a confirmation page "Are you sure you want to signout?" and a sign out button. 

If signed in as a superuser:
- Product management - when signed in a product management link is shown in "My Account" dropdown where you can add products by choosing category, SKU, name, description, size, prize, rating, image url.

#### 6. Basket

- When basket is empty, an "Your bag is empty" message displays at a new page, along with a "keep shopping" button below the message. 

- When basket has items, the basket page is displayed along with the products that are added in bag (including product info, prize, quantity, subtotal, product image, product name, size, update, remove, bag total, delivery cost, grand total, message of how much more to spend to get free delivery, "Keep shopping" and "Checkout" button). "Keep shopping" button links to "All products" page. "Checkout" button links to checkout page. 

#### 7. Checkout
- Checkout page contains of two sections, one column with a form including details, delivery and payment details, "Adjust bag" and "Complete order" button. The other section (second column) consists of an order summary. When completing the order, a success toast is shown in upper right corner and user get redirected to the product page. 

<span id="features-future"></span>

<br>

### 2.2 Features left to implement in the future 

- Product reviews: Letting the user review the products sold on the website to stimulate other customers.
- Contact page: where the user can directly send a message to the store owner from within the website.
- Categories: For example when the owner decides to sell gardening equipment and such and when there are more products, I want to implement the categories where the user can choose.

<span id="technologies"></span>

<h1>3. Technologies used</h1>

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://nl.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Django](https://nl.wikipedia.org/wiki/Django) 

#### Frameworks, libraries & Other
- [Gitpod](https://www.gitpod.io/) 
    - The GitPod is used to develop the project.
- [Git](https://git-scm.com/)
    - The Git was used for version control to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
    - The GitHub is used to host the project.
- [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
- [Google Fonts](https://fonts.google.com/)
    - Google Fonts is used to provide the font Itim for all the text that is used in the project. 
- [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
- [Bootstrap](https://getbootstrap.com/)
    - Materialize is used for the design framework.
- [Heroku](https://dashboard.heroku.com/)
    - Heroku is the cloud platform to deploying the app.
- [Heroku Postgres](https://www.heroku.com/home)
    - Database used for production/deployed app.
- [Django](https://www.djangoproject.com/)
    - Django is used as framework for the website.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Jinja is used for templating Python
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - django allauth is used for authentication and autohorization.
- [Amazon AWS S3](https://aws.amazon.com/)
    - The Amazon Web Service s3 Bucket was used to store media and static files.
- [Stripe](https://stripe.com/nl)
    - Stripe was used as the payment platform.

#### Testing tools used 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/open) is used to detect problems and test responsiveness.
- [Autoprefixer](https://autoprefixer.github.io/)
    - Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules. 
- [W3C Markup Validation Service](https://validator.w3.org/)
    - The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code. 
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    - The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
- [JShint](https://jshint.com/)
    - JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code. 
- [PEP8](http://pep8online.com/)
    - The PEP8 validator is used to check whether there were any errors in the Python code.

<span id="testing"></span>

<h1>4. Testing</h1>

The testing process can be found [here](TESTING.md).

<span id="deployment"></span>

<h1>5. Deployment</h1>

This project has been developed using Gitpod and GitHub. The project was regularly committed to GitHub during the initial development phase.
The website was stored as a repository in GitHub, and has later been deployed using Heroku. Static files are stored using Amazon AWS in an Amazon Web Services S3 Bucket.

Requirements to deploy:

* An IDE (Such as GitPod or VSCode)
* Git for version control 
* GitHub account
* Heroku account
* AWS S3 account
* Stripe account
* Email account
* Python3 
* pip for Python package installation

<br>

## Forking the GitHub Repository
Making a copy of the original repository on our GitHub account to view or to make changes without affecting the original repository, follow the steps below;

1. Log into [GitHub](https://github.com/) and locate the repository.
2. Click on `Fork` on the top right of the page.
3. You should now have a copy of the original repository in your GitHub account.

<br>

## Making a Local Clone

1. Log in to [www.github.com](https://github.com/)) with your GitHub account.
2. Click the profile dropdown in the upper right corner.
3. Choose `Your repositories`
4. Navigate to the relevant [repository](https://github.com/lonneke-dev/Plantastic) in the main page of the repositories.
5. Click the `Code` button.
6. To clone the repository using HTTPS, under `Clone with HTTPS`, click the icon marked in the screenshot. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the icon marked in the screenshot. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the icon marked in the screenshot.
7. Open terminal.
8. Change the current working directory to the location where you want the cloned directory.
9. Type **git clone**, and then paste the URL you copied earlier.
10. Press `Enter` to create your local clone.

<br>

## Download the project

1. Go to [Project Code Repository Location](https://github.com/lonneke-dev/Plantastic) on Github. 
2. Select the Code dropdown and choose the Download ZIP option.
3. This will download a copy of the entire project locally as a zip file.
4. Any required Python dependencies should be installed locally using the terminal command $ pip install -r requirements.txt.

## Set up local testing environment

To set up the local testing environment once the code has been Cloned or Forked, the following environment variables should be added to the Gitpod environment variables.
Gitpod environment variables can be accessed from the top right of the Gitpod home screen, by clicking on the User icon and selecting Settings, then Variables from the left hand menu.

Variable|Value|
--------|-----|
DEVELOPMENT|True|
SECRET_KEY|`your_django_secret_key`
STRIPE_PUBLIC_KEY|`your_stripe_public_key`
STRIPE_SECRET_KEY|`your_stripe_secret_key`
STRIPE_WH_SECRET|`your_stripe_webhook_secret_key`

## Deploy website to Heroku

1. Create an account at [Heroku](https://id.heroku.com/login).
2. Choose a name for your application, select the region closest to your, and then click `Create app`.
4. After you created your app click on Resources tab, using the `Add ons` search field find, and select `Heroku Postgres`.
5. Select your plan and click confirm.
6. In order to use Heroku Postgres you need to install two dependencies `dj_database_url` and `psycopg2-binary`
7. After installing the dependencies, freeze your requirements into `requirements.txt`
8. In your settings.py file import `dj_database_url` and replace your current Database settings to:
    Your `DATABASE_URL` can be found in your Heroku Apps `Config Var`
9. After setting your Database, run the following commands to migrate models:
10. Load the data to the database from the db.json file by running following command:
11. Create a superuser for your app 
12. Heroku setup is complete, now add an if statement in your settings.py file to set the DATABASES:
13. Install `gunicorn` and freeze your requirements
14. Create a `Procfile` and add the following code in your `Procfile`
15. Connect to Heroku fom the terminal:
16. Go to back to the Settings tab on your Heroku dashboard, and click "Reveal Config Vars" and add the following Config Variable, to temporarily disable `COLLECTSTATIC`:
17. In your settings.py file add your Heroku app, and `localhost`
18. In your Heroku app dashboard, click on `Settings` tab on your Heroku dashboard, and click `Reveal Config Vars` and add the following Config Variables:

    |Key|Value|
    |---|----|
    |SECRET_KEY|YOUR_SECRET_KEY|
    |STRIPE_PUBLIC_KEY|YOUR_STRIPE_PUBLIC_KEY|
    |STRIPE_SECRET_KEY|YOUR_STRIPE_SECRET_KEY|
    |STRIPE_WH_SECRET|YOUR_STRIPE_WH_SECRET|
    |EMAIL_HOST_USER|YOUR_EMAIL_ADDRESS|
    |EMAIL_HOST_PASS|YOUR_EMAIL_APP_PASSWORD|

19. Then push to Heroku:
20. Navigate to `Deploy` tab on your Heroku apps Dashboard, and click on `Enable Automatic Deploys`.
21. Site is successfully deployed, and any futher changes on the app will automatically be updated everytime they are commited and pushed on Github.

## AWS 

The deployed version of this website has static and media files hosted to it via the web based service; Amazon Web Services S3 Bucket.

1. Create or login to your AWS account at [aws.amazon.com](https://aws.amazon.com/) and click on `Amazon S3`.  
2. Create a new bucket with the following settings:

* An appropriate name (your project name)

* Region (closest to you)

* Uncheck `Block all Public Access`

* Open the new bucket and `Enable Static Website Hosting` (bottom of page)

* In the permissions tab, edit the CORS configuration (near bottom) and use the following code to set up the required connection between the Heroku app and the bucket:

![Allows](media/allows.png)

* In the permissions tab, click `Edit` on the Bucket Policy and open the policy generator

* Use the following settings to setup the policy correctly:

  + *Type of Policy: `S3 Bucket Policy`*

  + *Principal: `*` to allow all principles*

  + *Action: `Get Object`*

  + *Amazon Resource Name (ARN): Paste your Bucket ARN and add * at the and of your Bucket Resource key arn:aws:s3:::bucket_name/* and then save*

**IMPORTANT! Add "/*" to the end of the resource key to ensure all files are loaded**

* Click on Access Control List (ACL), and enable `List` on `Everyone (public access)` tab.

* On the top of your AWS Management Console, Search for `IAM` or `Identity Access Management`

  + * Click on `User Groups` on the left panel, and `Create Group`

  + * Click on `Policies` and `Create Policy`

  + * Click on JSON and select `Import Managed Policy` and search for `AmazonS3FullAccess` and click import

  + * Copy your `Bucket ARN` and paste it in the `Resource`

  + * `Click on Review Policy`

* Go back to `User Groups` and click on the group name you just created, click on `Permissions` then `Attach Policies` and search for the policy you've just created and then click on `Attach Policy` to attach the policy to the group

* Click on `Users` and then click on `Add Users`

  + * Set your user's name and give `Programmatic Access`

  + * Click `Next` and add the user in your New Group and `Create User`

  + * After you created the user download user's `.csv` file which contains user's access key and secret access key.

* Go back to your IDE and install the following dependencies in order to connect Django to AWS S3

* Freeze your requirements

* Add it to your installed apps in your settings.py

* Create `custom_storages.py` file in your project root and add the following code, and then save

* In your `settings.py` file add the following code

* Add the following config variables in your Heroku App, and remove `DISABLE_COLLECTSTATIC=1`

|Key|Value|
|---|----|
|USE_AWS|True|
|AWS_ACCESS_KEY_ID|YOUR_AWS_ACCESS_KEY_ID|
|AWS_SECRET_ACCESS_KEY|YOUR_AWS_SECRET_ACCESS_KEY|

* Deployment complete!

<span id="credits"></span>

<h1>6. Credits</h1>

#### Code
- [Codeinstitute](https://codeinstitute.net/): For teaching me the basics and making it possible to do this project especially the task manager mini project was helpful to this project. And for almost all of the code from for this project.

<span id="Acknowledge"></span>

<h1>7. Acknowledge</h1>

## content
- [KenBroTech](https://github.com/KenBroTech/Django-Newsletter-Project/blob/master/newsletter/settings.py):
    Used his explenation for the newslette setup.

A lot of thanks to the following:

- The support and guidance of my mentor Precious Ijege. 
- The lessons and knowledge of [Code Institute.](https://codeinstitute.net/)
- The mental support of my friends and family.

<span id="Disclaimer"></span>

<h1>8. Disclaimer</h1>
This project is for educational purposes only. If there is an issue with the copyright or the content, please contact me: lonneke1908@gmail.com

Thanks for visiting

<a href="#plantastic">Back to top!</a>