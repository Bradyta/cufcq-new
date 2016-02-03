from models.basemodel import BaseModel

def cast_to_float(string):
    try:
        return float(string)
    except:
        return None

class Fcq(BaseModel):
    CAMPUS_CODES = ['BD', 'DN', 'CS']
    VALID_TERMS = {1: 'Spring', 4: 'Summer', 7: 'Fall'}
    INSTRUCTOR_GROUPS = ['TA', 'TTT', 'OTH']

    def requiredFields(self):
        return ['campus', 'department_id', 'course_id', 'instructor_id', 'yearterm', 'course_number', 'course_subject', 'section', 'course_title', 'instructor_first', 'instructor_last', 'instructor_group', 'instructoroverall', 'courseoverall', 'forms_requested', 'forms_returned', 'slug']

    def strictSchema(self):
        return False

    def fields(self):
        return {
            'campus': (self.is_in_list(self.CAMPUS_CODES), ),
            'department_id': (self.schema_or(self.is_none, self.exists_in_table('Department')),),
            'course_id': (self.schema_or(self.is_none, self.exists_in_table('Course')),),
            'instructor_id': (self.schema_or(self.is_none, self.exists_in_table('Instructor')),),
            'yearterm': (self.is_yearterm, ),
            'course_number': (self.is_int, self.is_truthy),
            'course_subject': (self.is_string, self.is_not_empty),
            'section': (self.is_string, ),
            'course_title': (self.is_string, self.is_not_empty),
            'instructor_first': (self.is_string, self.is_not_empty, ),
            'instructor_last': (self.is_string, self.is_not_empty, ),
            'instructor_group': (self.is_in_list(self.INSTRUCTOR_GROUPS), ),
            'forms_requested': (self.is_int, self.is_truthy),
            'forms_returned': (self.is_int, ),
            'courseoverall': (self.schema_or(self.is_none, self.is_fcq_value),),
            'instructoroverall': (self.schema_or(self.is_none, self.is_fcq_value),),
            'slug': (self.is_string, self.is_not_empty, self.is_unique('slug'),)
        }

    def is_yearterm(self, data):
        self.is_int(data)
        key = data % 10
        assert key in [1, 4, 7]

    def is_fcq_value(self, data):
        self.is_int(data)
        self.is_in_range(1.0, 6.0)(data)

    def generate_slug(self, data):
        yearterm = data['yearterm']
        course_subject = data['course_subject']
        course_number = data['course_number']
        section = data['section']
        index = data['index_number']
        slug = "{0}-{1}-{2}-{3}-{4}".format(yearterm, course_subject, course_number, section, index)
        return slug.lower()

    def default(self):
        return {
            'campus': '',
            'department_id': None,
            'course_id': None,
            'instructor_id': None,
            'yearterm': 0,
            'course_number': 0,
            'course_subject': '',
            'course_title': '',
            'instructor_first': '',
            'instructor_last': '',
            'instructor_group': '',
            'courseoverall': None,
            'instructoroverall': None,
            'forms_requested': 0,
            'forms_returned': 0,
            'slug': ''
        }

    def sanitize_from_raw(self, raw):
        sanitized = self.default()
        sanitized['yearterm'] = int(raw['Yearterm'])
        sanitized['course_subject'] = raw['Subject']
        sanitized['course_number'] = int(raw['Crse'])
        sanitized['section'] = raw['Sec']
        sanitized['online_fcq'] = True if len(raw['OnlineFCQ']) else False
        sanitized['bd_continuing_education'] = True if len(raw['BDContinEdCrse']) else False
        instructor_names = raw['Instructor'].split(',')
        if len(instructor_names) < 2:
            sanitized['instructor_last'] = instructor_names[0].strip()
            sanitized['instructor_first'] = instructor_names[0].strip()
        else:
            sanitized['instructor_last'] = instructor_names[0].strip()
            sanitized['instructor_first'] = instructor_names[1].strip()
        sanitized['forms_requested'] = int(raw['FormsRequested'])
        sanitized['forms_returned'] = int(raw['FormsReturned'])
        sanitized['courseoverall_pct_valid'] = cast_to_float(raw['CourseOverallPctValid'])
        sanitized['courseoverall'] = cast_to_float(raw['CourseOverall'])
        sanitized['courseoverall_sd'] = cast_to_float(raw['CourseOverall_SD'])
        sanitized['instructoroverall'] = cast_to_float(raw['InstructorOverall'])
        sanitized['instructoroverall_sd'] = cast_to_float(raw['InstructorOverall_SD'])
        sanitized['hours_per_week_in_class_string'] = raw['HoursPerWkInclClass']
        sanitized['prior_interest'] = cast_to_float(raw['PriorInterest'])
        sanitized['instructor_effectiveness'] = cast_to_float(raw['InstrEffective'])
        sanitized['instructor_availability'] = cast_to_float(raw['Availability'])
        sanitized['instructor_challenge'] = cast_to_float(raw['Challenge'])
        sanitized['how_much_learned'] = cast_to_float(raw['HowMuchLearned'])
        sanitized['instructor_respect'] = cast_to_float(raw['InstrRespect'])
        sanitized['course_title'] = raw['CrsTitle'].capitalize()
        sanitized['r_fairness'] = cast_to_float(raw['R_Fair'])
        sanitized['r_presentation'] = cast_to_float(raw['R_Presnt'])
        sanitized['r_workload'] = cast_to_float(raw['Workload'])
        sanitized['r_diversity'] = cast_to_float(raw['R_Divstu'])
        sanitized['r_accessibility'] = cast_to_float(raw['R_Access'])
        sanitized['r_learning'] = cast_to_float(raw['R_Learn'])
        sanitized['campus'] = raw['Campus']
        sanitized['college'] = raw['College']
        sanitized['asdiv'] = raw['ASdiv']
        sanitized['level'] = raw['Level']
        sanitized['fcq_department'] = raw['Fcqdept']
        sanitized['instructor_group'] = raw['Instr_Group']
        sanitized['index_number'] = int(raw['I_Num'])
        sanitized['slug'] = self.generate_slug(sanitized)
        return sanitized