class Website:
  def __init__(self):
    self.name = 'Enter your name'
    self.college = 'Enter your college name'
    self.degree = 'Enter your degree (BTech etc)'
    self.description = 'Brief description'
    self.img = 'Profile image URL'
    self.about_me = 'Longer about me section'
    self.academic_interests = 'Line separated academic interests'
    self.tech_skills = 'Line separated technical skills'
    self.sections = [ # name all the sections of your site.
                      'About Me',
                      'Academics',
                      'Projects',
                      'Technical Skills',
                      'Miscellaneous'
                    ]
    self.section_desc = {  # section description hash-function which is currently
                    # defined for preset sections, but can be extended for
                    # new custom sections
      'Abou': self.getAboutMe(),
      'Acad': '\
        <h3>\n \
        Interests\n \
      </h3>\n \
      <ul class="unstyled">\n \
        <blockquote>\n \
        <li>INTEREST 1</li>\n \
        <li>INTEREST 2</li>\n \
        <li>INTEREST 3</li>\n \
        <li>INTEREST 4</li>\n \
        </blockquote>\n \
      </ul>\n \
      <h3>\n \
        Courses\n \
      </h3>\n \
      <blockquote>\n \
        <table class="table table-bordered">\n \
          <thead>\n \
            <tr>\n \
              <th>Computer Science (Core)</th>\n \
              <th>Computer Science (Electives)</th>\n \
              <th>Sciences, Mathematics & Humanities</th>\n \
            </tr>\n \
          </thead>\n \
          <tbody>\n \
            <tr>\n \
              <td width="300px">\n \
                <ul class="unstyled">\n \
                  <li>COURSE 1</li>\n \
                  <li>COURSE 2</li>\n \
                </ul>\n \
              </td>\n \
              <td width="300px">\n \
                <ul class="unstyled">\n \
                  <li>COURSE 3</li>\n \
                  <li>COURSE 4</li>\n \
                </ul>\n \
              </td>\n \
              <td width="300px">\n \
                <ul class="unstyled">\n \
                  <li>COURSE 5</li>\n \
                  <li>COURSE 6</li>\n \
                </ul>\n \
              </td>\n \
            </tr>\n \
          </tbody>\n \
        </table>\n \
      </blockquote>\n \
      ',
      'Proj': '\
        <div class="tabbable">\n \
          <ul class="nav nav-tabs">\n \
            <li class="active">\n \
              <a href="#tab1" data-toggle="tab">Data Mining</a>\n \
            </li>\n \
            <li><a href="#tab2" data-toggle="tab">Image Processing</a></li>\n \
          </ul>\n \
          <div class="tab-content">\n \
            <div class="tab-pane active" id="tab1">\n \
              <ul class="unstyled">\n \
                <li>\n \
                <span class="heading">Data Mining Project Title: <a href="PROFESSOR URL" target="_blank">PROFESSOR NAME 2</a>, PROFESSOR AFFLIATION</span><br>\n \
              Project Description.\n \
                </li>\n \
                <li>\n \
                <span class="heading">Data Mining Project Title 2: <a href="PROFESSOR URL" target="_blank">PROFESSOR NAME 2</a>, PROFESSOR AFFLIATION</span><br>\n \
              Project Description.\n \
                </li>\n \
              </ul>\n \
            </div>\n \
            <div class="tab-pane" id="tab2">\n \
              <ul class="unstyled">\n \
                <li>\n \
                <span class="heading">Image Processing Project Title: <a href="PROFESSOR URL" target="_blank">PROFESSOR NAME</a>, PROFESSOR AFFLIATION</span><br>\n \
              Project Description.\n \
                </li>\n \
              </ul>\n \
            </div>\n \
          </div>\n \
        </div>\n \
      ',
      'Tech': '\
        <table class="table table-striped">\n \
          <tbody>\n \
            <tr>\n \
              <td><strong>Programming Languages</strong> </td><td> 1, 2, 3, 4...</td>\n \
            </tr>\n \
            <tr>\n \
              <td><strong>Web & Scripting Languages</strong></td><td>1, 2, 3, 4...</td>\n \
            </tr>\n \
            <tr>\n \
              <td><strong>Tools & IDE</strong></td><td>1, 2, 3, 4...</td>\n \
            </tr>\n \
            <tr>\n \
              <td><strong>Operating Systems</strong></td> <td>1, 2, 3, 4...</td>\n \
            </tr>\n \
            <tr>\n \
              <td><strong>Hardware Description Languages</strong></td><td>1, 2, 3, 4...</td>\n \
            </tr>\n \
          </tbody>\n \
        </table>\n \
      ',
      'Misc': 'GENERIC SECTION DESCRIPTION'
    }


  def setUpAcad(self, interests):
    code = '<h3>Interests</h3><ul class="unstyled">'
    code += '<blockquote>'
    for interest in interests:
      code += '<li>{0}</li>'.format(interest)
    code += '</blockquote></ul>'
    code += '<h3>Courses</h3>'
    code += '<blockquote>\n \
      <table class="table table-bordered">\n \
        <thead>\n \
          <tr>\n \
            <th>Computer Science (Core)</th>\n \
            <th>Computer Science (Electives)</th>\n \
            <th>Sciences, Mathematics & Humanities</th>\n \
          </tr>\n \
        </thead>\n \
        <tbody>\n \
          <tr>\n \
            <td width="300px">\n \
              <ul class="unstyled">\n \
                <li>COURSE 1</li>\n \
                <li>COURSE 2</li>\n \
              </ul>\n \
            </td>\n \
            <td width="300px">\n \
              <ul class="unstyled">\n \
                <li>COURSE 3</li>\n \
                <li>COURSE 4</li>\n \
              </ul>\n \
            </td>\n \
            <td width="300px">\n \
              <ul class="unstyled">\n \
                <li>COURSE 5</li>\n \
                <li>COURSE 6</li>\n \
              </ul>\n \
            </td>\n \
          </tr>\n \
        </tbody>\n \
      </table>\n</blockquote>'
    return code

  def createWebsite(self):
    interests = self.getAcademicInterests().split('\n')[:-1]
    self.section_desc['Acad'] = self.setUpAcad(interests)
    self.indexCreate()
    self.sectionsCreate()

  def baseHeader(self):
    code = ' \
            <!DOCTYPE html>\n \
            <html>\n \
              <head>\n \
                <title>{0}</title>\n \
                <meta name="viewport" content="width=device-width, initial-scale=1.0">\n \
                <meta name="description" content="Home page of {0}, {1}, {2}">\n \
                <meta name="author" content="{0}">\n \
                <link rel="stylesheet" href="css/bootstrap/css/bootstrap.min.css"/>\n \
                <link rel="stylesheet" href="css/style.css"/>\n \
              </head>\n'.format(self.getName(), \
                                self.getDegree(), \
                                self.getCollege())
    return code


  def navbarCode(self, section='index'):
    code = '<body id="{1}">\n \
              <div class="navbar navbar-fixed-top">\n \
                <div class="navbar-inner">\n \
                  <div class="container">\n \
                    <a class="brand" href="index.html" class="active">{0}</a>\n \
                  <div class="nav-collapse">\n \
                    <ul class="nav">\n'.format(self.getName(), \
                                               section)
    for section in self.sections:
      secid = section[0:4]
      code += ' \
                <li><a href="' + secid + '.html" id="' + secid  + '">' + \
                  section + '</a></li>\n'
        
    code += ' \
            </ul>\n \
          </div>\n \
        </div>\n \
      </div>\n \
    </div>\n\
    '
    return code

  def indexCode(self):

    code = '\
      <div class="container">\n \
        <div class="hero-unit">\n \
        <div class="row-fluid">\n \
          <div class="span9">\n{0} \n \
          </div>\n \
          <div class="span3 me">\n \
            <img alt="My Photo" title="My Photo" src="{1}"/>\n \
          </div>\n \
        </div>\n \
      </div>\n \
    </div>'.format(self.getDescription(), self.getImg())
    return code
    
  def sectionCode(self, section):
    code = '\
      <div class="container well">\n \
        <h2>{0}</h2>\n \
        <p>\n'.format(section)
    if section[0:4] in self.section_desc.keys():
      code += self.section_desc[section[0:4]]
    code += '\
        </p>\n \
      </div>'
    return code

  def footerScripts(self):
    code = '\
            <script src="js/jquery-1.7.2.min.js"></script>\n \
            <script src="css/bootstrap/js/bootstrap.min.js"></script>\n \
            <script src="js/script.js"></script>\n \
            </body>\n \
            </html>'
    return code
        

  def indexCreate(self):
    code = self.baseHeader()
    code += self.navbarCode()
    code += self.indexCode()
    code += self.footerScripts()
    outfile = open('website/index.html', 'w')
    outfile.write(code)
    outfile.close()

  def sectionsCreate(self):
    for section in self.sections:
      code = self.baseHeader()
      code += self.navbarCode(section[0:4])
      code += self.sectionCode(section)
      code += self.footerScripts()
      outfile = open('website/' + section[0:4] + '.html', 'w')
      outfile.write(code)
      outfile.close()
                                                      
  def getName(self):
    return self.name
  def getCollege(self):
    return self.college
  def getDegree(self):
    return self.degree
  def getDescription(self):
    return self.description
  def setAcademicInterests(self, academic_interests):
    self.academic_interests = academic_interests
  def getAcademicInterests(self):
    return self.academic_interests
  def setAboutMe(self, about_me):
    self.about_me = about_me
  def getAboutMe(self):
    return self.about_me
  def getImg(self):
    return self.img
  def setName(self, name):
    self.name = name
  def setDegree(self, degree):
    self.degree = degree
  def setImg(self, img):
    self.img = img
  def setDescription(self, description):
    self.description = description
  def setCollege(self, college):
    self.college = college
