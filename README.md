# Flask Blog Application
A simple blog application built with Flask and SQLite.
## Features
- View all blog posts on the home page
 Create new blog posts
 Posts stored with timestamps
 Reverse chronological order display
## Installation
1. Clone the repository
2. bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

2. Create a virtual environment and activate it
cd YOUR-REPO-NAME
bash
python -m venv venv
On Windows
venv\Scripts\activate
On macOS/Linux
source venv/bin/activate

3. Install required packages
bash
pip install flask

4. Run the application
bash
python app.py

The application will be available at `http://localhost:5000`

## Project Structure

flask-blog/
├── app.py # Main application file
├── blog.db # SQLite database
├── templates/ # HTML templates
│ ├── home.html # Home page template
│ └── create.html # Create post template
└── README.md # This file

## Usage

- Visit the home page at `http://localhost:5000`
- Click "Create New Post" to add a new blog post
- Fill in the title and content
- Submit to create a new post
- View all posts on the home page

## Technologies Used

- Python
- Flask
- SQLite
- HTML

## Future Improvements

- Add user authentication
- Add edit/delete functionality
- Add styling (CSS)
- Add comments feature
- Add categories/tags

## License

This project is licensed under the MIT License - see the LICENSE file for details.
