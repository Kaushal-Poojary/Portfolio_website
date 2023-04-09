# Portfolio_website

This is my personal portfolio website, built using Flask. It showcases my projects, skills, and interests. The website is static, meaning all the content is pre-generated and served as static HTML pages.

## Technologies used

* Flask web framework
* HTML, CSS, and JavaScript for front-end
* Bootstrap for styling
* Git for version control

## Setup instructions

To set up this project locally, follow these steps:

1. Clone the repository to your local machine.
2. Install flask if not done
3. Run the Flask development server using python app.py.

$ git clone https://github.com/nilay-2/Portfolio_website.git <br/>
$ cd Portfolio_website <br/>
$ pip install flask <br/>
$ flask run

The website should now be accessible at http://localhost:5000.

## Project structure

The project is organized as follows:

├── app.py            # Flask app <br/>
├── static/           # Static assets (CSS, JavaScript, images) <br/>
├── templates/        # HTML templates <br/>
└── README.md         # This README file

The app.py file contains the Flask app code, which serves the static HTML pages and assets. The static directory contains CSS, JavaScript, and image files used by the website. The templates directory contains the Jinja2 templates used to generate the HTML pages.

## Deployment

To deploy this website, you can use a cloud hosting provider like Heroku or AWS Elastic Beanstalk. Simply create an account, create a new application, and follow the instructions to deploy the website.

## Contributing

If you find a bug or want to suggest an improvement, please create a new issue or pull request. I'm always happy to receive feedback and contributions!
