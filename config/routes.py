"""
Routing configuration.
"""
from handlers.index_handler import IndexHandler
from handlers.instructor_handler import InstructorHandler
from handlers.course_handler import CourseHandler
from handlers.department_handler import DepartmentHandler
from handlers.api.api_handler import ApiHandler
from handlers.ajax.fcqcard_handler import FcqCardHandler
from handlers.foobar import Foobar
# Tornado pro-tip: regex routing is optimized by putting more frequently
# accessed routes and simpler regexes before other routes.
routes = [
    (r"/", IndexHandler),
    (r"/courses", CourseHandler),
    (r"/foobar", Foobar),
    # (r"/departments", DepartmentHandler),
    (r"/ajax/fcqcard/([\w-]+)", FcqCardHandler),
    (r"/instructor/([\w-]+)", InstructorHandler),
    (r"/course/([\w-]+)", CourseHandler),
    (r"/department/([\w-]+)", DepartmentHandler),
    (r"/api/(instructor|course|fcq|grade|department)/([\w-]+)", ApiHandler)
]
