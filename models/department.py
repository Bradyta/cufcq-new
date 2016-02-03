from models.basemodel import BaseModel

class Department(BaseModel):
    CAMPUS_CODES = ['BD', 'DN', 'CS']
    LONG_NAMES = {
        'AAST': 'Asian American Studies'
        'ACCT': 'Accounting'
        'AIRR': 'Air Force Aerospace Studies'
        'AIST': 'American Indian Studies'
        'AMST': 'American Studies'
        'ANTH': 'Anthropology'
        'APPM': 'Applied Math'
        'ARAB': 'Arabic Languages'
        'ARCH': 'Architecture'
        'AREN': 'Architectural Engineering'
        'ARSC': 'Arts & Sciences Courses'
        'ARTF': 'Art Film Studies'
        'ARTH': 'Art History'
        'ARTS': 'Art Studio and Non-Studio'
        'ASEN': 'Aerospace Engineering'
        'ASIA': 'Asian Studies'
        'ASTR': 'Astrophysical & Planetary Sciences'
        'ATLS': 'ATLAS'
        'ATOC': 'Atmospheric & Oceanic Sciences'
        'BADM': 'Business Administration'
        'BAKR': 'Baker Residential Academic Program'
        'BCOR': 'Business Core'
        'BLST': 'Afroamerican Studies'
        'BPOL': 'Business Environment & Policy'
        'BSLW': 'Business Law'
        'BUSM': 'Business Minor'
        'CAMW': 'Center of the American West'
        'CEES': 'Central & East European Studies'
        'CESR': 'Current Emphasis in Social Responsibility'
        'CHEM': 'Chemistry'
        'CHEN': 'Chemical Engineering'
        'CHIN': 'Chinese'
        'CHST': 'Chicano/a Studies'
        'CLAS': 'Classics'
        'CNCR': 'Concurrent Placeholder'
        'COML': 'Comparative Literature'
        'COMM': 'Communication'
        'COMR': 'Communication Residential Academic Program'
        'CONV': 'Convocation Music'
        'CSCI': 'Computer Science'
        'CSVC': 'Career Services'
        'CVEN': 'Civil Engineering'
        'CWCV': 'Center for Western Civilization'
        'DNCE': 'Dance'
        'EALC': 'East Asian Languages & Civilizations'
        'EBIO': 'Ecology & Evolutionary Biology'
        'ECEN': 'Electrical & Computer Engineering'
        'ECON': 'Economics'
        'EDUC': 'Education'
        'EHON': 'Engineering Honors'
        'EMEN': 'Engineering Management'
        'EMUS': 'Music Ensemble'
        'ENGL': 'English'
        'ENVD': 'Environmental Design'
        'ENVS': 'Environmental Studies'
        'ESBM': 'Entrepreneurship and Small Business Management '
        'ETHN': 'Ethnic Studies'
        'EVEN': 'Environmental Engineering'
        'FARR': 'Farrand Residential Academic Program'
        'FILM': 'Film Studies'
        'FNCE': 'Finance'
        'FREN': 'French'
        'FRSI': 'Farsi'
        'GEEN': 'General Engineering'
        'GEOG': 'Geography'
        'GEOL': 'Geological Sciences'
        'GRMN': 'German'
        'GSAP': 'Global Studies Residential Academic Program'
        'GSLL': 'Germanic & Slavic Languages & Literature'
        'HEBR': 'Hebrew'
        'HIND': 'Hindi'
        'HIST': 'History'
        'HONR': 'Honors'
        'HUEN': 'Humanities for Engineers'
        'HUMN': 'Humanities'
        'IAFS': 'International Affairs'
        'INBU': 'International Business Cert'
        'INDO': 'Indonesian'
        'INVS': 'INVST Community Studies'
        'IPHY': 'Integrative Physiology'
        'ITAL': 'Italian'
        'JOUR': 'Journalism'
        'JPNS': 'Japanese'
        'JWST': 'Jewish Studies'
        'KREN': 'Korean'
        'LAMS': 'Latin American Studies'
        'LAWS': 'Law School'
        'LDSP': 'Leadership Residential Academic Program'
        'LEAD': 'Leadership Minor'
        'LGBT': 'Lesbian/Gay/Bisexual Studyies'
        'LIBB': 'Libby Residential Academic Program'
        'LIBR': 'Libraries'
        'LING': 'Linguistics'
        'MATH': 'Mathematics'
        'MBAC': 'MBA Core'
        'MBAX': 'MBA Advanced Electives'
        'MCDB': 'Molecular Cell & Developmental Biology'
        'MCEN': 'Mechanical Engineering'
        'MEMS': 'Medieval & Early Modern Studies'
        'MGMT': 'Management'
        'MILR': 'Military Science'
        'MKTG': 'Marketing'
        'MUEL': 'Music Electives'
        'MUSC': 'Music'
        'MUSM': 'Museum'
        'NAVR': 'Naval Science'
        'NRLN': 'Norlin Scholars'
        'NRSC': 'Neuroscience'
        'OPIM': 'Operations & Information Management'
        'OPMG': 'Operations Management'
        'ORMG': 'Organization Management'
        'PACS': 'Peace & Conflict Studies'
        'PHED': 'Physical Education'
        'PHIL': 'Philosophy'
        'PHYS': 'Physics'
        'PMUS': 'Performance Music'
        'PORT': 'Portuguese'
        'PRLC': 'Presidents Leadership Class'
        'PSCI': 'Political Science'
        'PSYC': 'Psychology'
        'RCPR': 'Reciprocal Exchange'
        'REAL': 'Real Estate'
        'RLST': 'Religious Studies'
        'RSEI': 'Renewable & Sustainable Energy Institute'
        'RUSS': 'Russian'
        'SCAN': 'Scandinavian'
        'SEWL': 'Sewall Residential Academic Program'
        'SLHS': 'Speech, Language & Hearing Sciences'
        'SOCY': 'Sociology'
        'SPAN': 'Spanish'
        'SSIR': 'Sustainability and Social Innovation RAP'
        'STDY': 'Study Abroad'
        'SWED': 'Swedish'
        'SYST': 'Systems'
        'THTR': 'Theatre'
        'TLEN': 'Telecommunications'
        'TMUS': 'Thesis Music'
        'TOMG': 'Tourism Management'
        'WMST': 'Womens Studies'
        'WRTG': 'Writing and Rhetoric'
    }

    def requiredFields(self):
        return ['campus', 'college', 'name', 'fcqs', 'courses', 'instructors', 'long_name', 'slug']

    def fields(self):
        return {
            'campus': (self.is_in_list(CAMPUS_CODES), ),
            'name': (self.is_string, self.is_not_empty, ),
            'long_name': (self.is_string, self.is_not_empty, ),
            'college': (self.is_string, ),
            'fcqs': (self.is_list, self.schema_list_check(self.is_string, )),  # TODO: exists_in_table is supposed to check for string components
            'courses': (self.is_list, self.schema_list_check(self.is_string, )),
            'instructors': (self.is_list, self.schema_list_check(self.is_string, )),
            'slug': (self.string, self.is_not_empty, self.is_unique('slug')),
        }

    def default(self):
        return {
            'campus': '',
            'name': '',
            'long_name': '',
            'college': '',
            'fcqs': [],
            'courses': [],
            'instructors': [],
            'slug': '',
        }

    def generate_slug(self, data):
        campus = data['campus']
        name = data['name']
        slug = "{0}-{1}".format(campus, name)
        return slug.lower()

    def sanitize_from_raw(self, raw):
        sanitized = self.default()
        name = raw['name']
        sanitized['campus'] = raw['campus']
        sanitized['name'] = name
        sanitized['college'] = raw['college']
        sanitized['long_name'] = self.LONG_NAMES.get(name, name)
        sanitized['slug'] = self.generate_slug(sanitized)
        return sanitized
