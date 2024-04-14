# Debbie's Recipe Blog

Please navigate this website with the deployed link:  https://debbies-blog-9734dd06035e.herokuapp.com/ 

Table of contents
 1. UX
 2. Agile Development
 3. Features 
 4. Technology used
 5. Testing 
 6. Validating, errors and bugs
 7. Deployment
 8. Resources
 9. Credits and acknowledgements


 # 1. UX
### ERD
![ERD](static/images/readme-images/ERD.png)

### Design
#### Site User
Debbie's Recipe Blog is a website for people of any age who like to cook and seek inspiration for plant-based recipes. 

#### Goals for the website
The goal for the website is to provide plant based recipes in a simple yet visually appealing format, providing the possibility to interact with the author and other users through likes, comments and the collaboration contact form.
 
#### Wireframes
See below part of the initial planning for the blog, a simple sketch of the home page, about page and sign up form in different screen sizes.
![wireframe big screen home](static/images/readme-images/wireframe-bigscreen-home.png)
![wireframe big screen about](static/images/readme-images/wireframe-bigscreen-about.png)
![wireframe phone screen](static/images/readme-images/wireframe-phonescreen.png)

#### Color palette, fonts
The color palette of beiges and browns has been chosen to convey a simple, clean but also warm appearance to the blog. The beige and brown tones are a good combination with the colorful recipe pictures. The font has been chosen to give a clean and elegant appearance to the site.

# 2. Agile Development
## User Stories
Throughout the development process, Agile methodologies have been applied to ensure adaptability and responsiveness to the evolving project needs. While  planning and creating user stories partially offline since pen and paper work best for me, I have used GitHub's Kanban board for task management and updates, and all the user stories can be found there. This mix of different tools is what has worked best for me to adapt and re-think features during the process of coding this blog. 

Some of the user stories are inspired from Code Institute's own Django walkthrough project, and I progressively added my own as the project took more shape and its needs evolved. 
See the Kanban board with my user stories [here](https://github.com/users/Ikayherce/projects/4/views/1 )  



# 3. Features 
## Features implemented
- Navbar
    - Toggle down in small sizes
- Home page with the latest post highlighted on top
- Pagination system to navigate the rest of the post list pages
- About page with collaboration form 
- Category system to categorize posts
- Category page (toggle down menu from some of)
- User can register, log in, and log out
- Authenticated user can like and unlike posts
- Authenticated user can comment, read, delete and update their comments
- Superuser has front end CRUD for posts
    - Create new post page with rich text field
    - Edit post page with rich text field
    - Read posts
    - Delete posts
- Superuser can add new post categories
    
## Features Left to Implement
With more time, these would have been, among others, some  good additions to the project. 
- Password change for users
- Possibility for users to reply to a comment thread (not just posting new comment but as a reply to a specific comment)
- Possibility to assign multiple categories to one post (i.e. cake can be dessert and snack)
- Dropdown category menu in navbar implemented in all pages (right now it's not, even though categories are 
    accessible through the category list page from any page)
- Admin's ability to delete or edit categories from front end
- Admin's ability to approve or discard comments from front end
- Subscribing model 

# 4. Technologies used
- Html - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for handling comments
- Django - framework used to build this blog
- Bootstrap 5.01 - front end framework used to style this project 
- Elephant SQL - used as the database
- Font Awesome - for social media icons
- Google Fonts- currently only for the hero image font
- GitHub - for storing the code and for the project's Kanban board
- Heroku - for hosting and deployement of this project
- Cloudinary - hosting the static files
- Git - version control tool  
- Gitpod - IDE used for building this project

# 5. Testing
## Reponsiveness
Responsiveness has been achieved mainly through the use bootstrap classes.
![Home page AMIRESPONSIVE](static/images/readme-images/amiresponsive-home.png)
![Home page AMIRESPONSIVE](static/images/readme-images/amiresponsive-about.png)
![Home page AMIRESPONSIVE](static/images/readme-images/amiresponsive-postdetail.png)
![Home page AMIRESPONSIVE](static/images/readme-images/amiresponsive-signup.png)
 
## Manual testing
### Account Registration Tests - PASSED
- User can create profile	 
- User can log into profile	 
- User can log out of profile	 

### User Navigation Tests - PASSED
- User can easily navigate to individual posts
- User can easily navigate to category menu	 
- User can access About page	 
- User can submit a message in contact form in About page 
- User can like and unlike posts when registered
- User can comment on posts when registered
- User can access the footer's social media links, which open in a new tab
- Authenticated user can delete and edit their comments 
- SuperUser can access add new post page, edit and delete post pages, add category page

### Account Authorisation Tests - PASSED
- Only Superuser can access admin page	 
- Non authorised user book a table	 
- Non authorised user won't access profile page	 

### Admin Tests - PASSED
- Items display correctly on front-end when updating post	 
- Items display correctly on front-end when adding new post	
- Items display correctly on front-end when deleting post	 
- Items display correctly on front-end when adding category

    
# 6. Validating, errors and bugs
## Validating and errors

### HTML
I validated my HTML by copying and pasting the "source code" from the app's deployed link. I got some errors pertaining my base.html that I could not fix, indicating that <li> tags in my navbar were not supposed to be under <div> and that there were "a" stray tags. 
Nevertheless, the structure of my html is in principle  correct and trying to change my code according to these error messages caused the links in my navbar to look bad, and showed other errors instead. so I had to change the code back.
![<a> tag error ](static/images/readme-images/a.tag.error.png)
![<a> tag error ](static/images/readme-images/li.tag.error.png)

### CSS 
The style.css file came back with no errors.
![CSS validation](static/images/readme-images/css.validation.png)

### Python
The files I have coded in, that is, models.py, urls.py, views.py and admin.py are error free, except a line that is too long in my urls.py. I tried to correct his but then the terminal wouldn't open the browser, even though the Python linter indicated that that was the correct code. 
![Line too long in urls.py](static/images/readme-images/urls.py.validation.png)

### JS
The only javascript file in my project, handling the comments, is not coded by me, it is code included in the Code Institute's walkthrough. The JS Hint did not indicate the presence of errors. 

### Bugs
Sometimes while inspecting in devtools and looking at middle-sized and smaller screen sizes the container looks funny, but it doesn't happen looking at the website from the phone screen. 

# 7. Deployment
The steps to deploy this website to Heroku were the steps described in Code Institute's blog walkthrough project, as described below.

1. Create the Heroku app:
- Sign up or log in to Heroku.
- Go to the Heroku Dashboard and click on "New" -> "Create New App".
- Name your project, in my case "Debbie's Blog".
- Choose your region - EU.
- Click "Create App".

2. Set up environment variables:
- Create a file named env.py in the top level of your Django app.
- Import os in env.py.
- Set necessary environment variables:
- Set the secret key using: os.environ['SECRET_KEY'] = 'your secret key'.
- For the database variable, use: os.environ['DATABASE_URL'] = 'Paste the database link in here'.
- In settings.py, replace the value of SECRET_KEY variable with os.environ.get('SECRET_KEY').
- Change the value of DATABASES variable to: 'default': dj_database_url.parse(os.environ.get("DATABASE_URL")).

3. Configure Heroku:
- Navigate to the "Settings" tab in Heroku.
- Open the "Config Vars" section and add:
- DATABASE_URL as Key and the database link from your app's env.py as Value.
- SECRET_KEY as Key and the secret key value from env.py as Value.

4. Migrate models:
- In the terminal, migrate the models over to the new database connection.

5. Configure static files:
- In settings.py, add the following static files settings:

![Static files](static/images/readme-images/deployment-staticfiles-screenshot.png)

- Change the templates directory to: TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates').
- Update the DIRS key in the TEMPLATES variable to look like this: 'DIRS': [TEMPLATES_DIR].

6. Update ALLOWED_HOSTS:
- Add your Heroku app's domain to the ALLOWED_HOSTS list (e.g., your-app-name.herokuapp.com).

7. Create necessary directories and files:
- If not already done, create top-level folders named static and templates.
- Create a Procfile with the following content: web: gunicorn PROJECT_NAME.wsgi.

8. Final steps:
- In the terminal, add the changed files, commit, and push to GitHub.


# 8. Resources, Credits and acknowledgements
### The code
- "I think therefore I blog" walkthrough project by Code Institute
- Tutorial series 1  https://www.youtube.com/watch?v=k_RY1og4Zj0&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd
- Tutorial series 2 https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy 
- Tutorial series 3 https://www.youtube.com/watch?v=Mezody4yiXw&list=PLVBKjEIdL9bvCdI4l1Emvbezv10GjUaLk 
- Tutorial series 4 https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi 
### The user stories
- Partially sourced from the "I think therefore I blog" walkthrough project by Code Institute
### The README
- Readme inspired in this project : https://github.com/TulaUnogi/cat-beans-cafe/blob/main/README.md
### The pictures
- All pictures, both for the recipes and the about page, have been sourced from unsplash.com 
### The text of the recipes
- The text of the recipe posts has been created with the assistance of AI (Chat GPT). 
### Other resources
- Slack 
Fellow students at the Swedish Community channel have helped me with troubleshooting.
- Tutor assistance
Some of Code Institute's tutors have been helpful for identifying and solving bugs and errors. 
