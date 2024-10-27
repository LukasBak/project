from taskmanager import db


class Category(db.Model):

    id = db.Column(db.Interger, primary_key=TRUE)
    category_name = db.Column(db.string(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all,delete", lazy=True)


class Task(db.Model):

    id = db.Column(db.Interger, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Interger, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

def __repr__(self):
        return "#{0} - Task:{1} | Urgent:{2}".format(
            self.id, self.task_name, self.is_urgent
        )

