#=============================================================================
# set of constants which are used through-out
#=============================================================================
myname = 'Alpha'
mycollege = 'IIT Delhi'
mydegree = 'Computer Science'
index_page_desc = ' \
  <h1>Welcome!</h1>\n \
  Include here, a brief description of yourself. With optional links to your \
  other profiles like those at Github, etc. You can <strong>directly</strong> \
  embed HTML content here, or change this after creating from AutoSite'

myimg = 'xyz.jpg'  # url for profile shot/some other image

#=============================================================================
# The variables below need not be changed here, it is better if you keep them
# as is, run create.py and then tune them from the HTML file. In most cases,
# the generic headings will work for an academic-style website and you only
# need to put in your specific details direclty into the appropriate HTML
# file.
#=============================================================================
sections = [ # name all the sections of your site.
  'About Me',
  'Academics',
  'Projects',
  'Technical Skills',
  'Miscellaneous'
]

section_desc = {  # section description hash-function which is currently
                  # defined for preset sections, but can be extended for
                  # new custom sections
  'Abou': 'GENERIC SECTION DESCRIPTION',
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
