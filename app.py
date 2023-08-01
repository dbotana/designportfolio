from flask import Flask, render_template

app = Flask(__name__)

# Project data 
all_projects = [ {'id': 1, 'title':'Paid Internship', 'image':'intern.jpg', 'url':'intern'},
  {'id': 2, 'title':'Undergraduate Research', 'image':'research.jpg', 'url':'research'},
  {'id': 3, 'title':'Project Manager', 'image':'manager.jpg', 'url':'manager'},
  {'id': 4, 'title':'Design Consultant', 'image':'consultant.jpg', 'url':'consultant'} ]

def get_project(project_id):
  for project in all_projects:
    if project['id'] == project_id:
      return project

@app.route('/project/<int:project_id>')
def new_project(project_id):

  project = get_project(project_id)
  
  return render_template('new_project.html', project=project)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')  

@app.route('/work')
def work():
  return render_template('work.html', projects=all_projects)


@app.route('/contact') 
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)