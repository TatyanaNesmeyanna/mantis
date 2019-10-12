from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def return_to_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill project form
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_to_projects_page()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        return len(wd.find_elements_by_name("selected[]"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            table = wd.find_element_by_xpath("//body//table[3]")
            table_rows = table.find_elements_by_tag_name("tr")
            for row in table_rows[1: len(table_rows)]:
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                enabled = cells[2].text
                view_status = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name = name, status = status, enabled = enabled, view_status = view_status, description = description))
        return list(self.project_cache)


