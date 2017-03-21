from app import db

base_str = 'single_page_website_'

class Author(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'about_author']
    def __repr__(self):
        return self.title


class AuthorLink(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'about_author_link']
    def __repr__(self):
        return self.url_title


class Project(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'project']
    def __repr__(self):
        return self.title


class ProjectsToCategories(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'project_categories']
    def __repr__(self):
        return self.id


class ProjectCategories(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'project_category']
    def __repr__(self):
        return self.human_display_category


class ProjectImages(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'project_image']
    def __repr__(self):
        return self.title


class ProjectLinks(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'project_link']
    def __repr__(self):
        return self.url_title


class ProjectTools(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'project_tool']
    def __repr__(self):
        return self.human_display_tool


class ProjectsToTools(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'project_tools']
    def __repr__(self):
        return self.id


class Skills(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'skill']
    def __repr__(self):
        return self.title


class SkillCategories(db.Model):
    __table__ = db.Model.metadata.tables[base_str + 'skill_category']
    def __repr__(self):
        return self.title


