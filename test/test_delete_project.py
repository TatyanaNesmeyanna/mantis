# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_delete_some_group(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="delete"))
    old_projects_list = app.project.get_project_list()
    index = random.randint(0, app.project.count()-1)
    project = old_projects_list[index]
    app.project.delete_project(project)
    assert len(old_projects_list) - 1 == app.project.count()
    new_projects_list = app.project.get_project_list()
    old_projects_list.remove(project)
    assert sorted(old_projects_list, key=lambda pr: pr.name) == sorted(new_projects_list, key=lambda pr: pr.name)