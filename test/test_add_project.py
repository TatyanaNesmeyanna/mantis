from model.project import Project
import string
import random

def test_add_project(app):
    app.session.login("administrator", "root")
    # project = json_projects
    symbols = string.ascii_letters + string.digits
    project = Project(name="Test"+"".join([random.choice(symbols) for i in range(random.randrange(3))]))
    old_projects_list = app.soap.get_projects_list("administrator", "root")
    app.project.create(project)
    new_projects_list = app.soap.get_projects_list("administrator", "root")
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=lambda pr: pr.name) == sorted(new_projects_list, key=lambda pr: pr.name)

