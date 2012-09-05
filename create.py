#=============================================================================
# Auto-site builds for you an academic-style web presence in minutes using
# the powerful Bootstrap from Twitter, and certain design aesthetic principles
# You can arbitrarily add sections or choose from a set of preset ones defined
# here, to get the barebones structure of your website, which can be further
# tweaked from the HTML/JS source.
# The required libraries are Bootstrap and jQuery, both of which are already
# included in this directory.
#=============================================================================
from constants import *
def base_header():
  code = ' \
    <!DOCTYPE html>\n \
    <html>\n \
      <head>\n \
        <title>{0}</title>\n \
        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n \
        <meta name="description" content="Home page of {0}, {1}, {2}">\n \
        <meta name="author" content="{0}">\n \
        <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css"/>\n \
        <link rel="stylesheet" href="style.css"/>\n \
      </head>\n'.format(myname, mydegree, mycollege)
  return code

def navbar_code(section=''):
  code = '<body id="{1}">\n \
    <div class="navbar navbar-fixed-top">\n \
      <div class="navbar-inner">\n \
        <div class="container">\n \
          <a class="brand" href="index.html" class="active">{0}</a>\n \
        <div class="nav-collapse">\n \
          <ul class="nav">\n'.format(myname, section)
  
  for section in sections:
    secid = section[0:4]
    code += ' \
      <li><a href="' + secid + '.html" id="' + secid  + '">' + \
        section + '</a></li>\n'
  
  code += ' \
            </ul>\n \
          </div>\n \
        </div>\n \
      </div>\n \
    </div>\n \
      '
  return code

def index_code():
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
  </div>'.format(index_page_desc, myimg)
  return code

def section_code(section):
  code = '\
    <div class="container well">\n \
      <h2>{0}</h2>\n \
      <p>\n'.format(section)
  if section[0:4] in section_desc.keys():
    code += section_desc[section[0:4]]
  code += '\
      </p>\n \
    </div>'
  return code
  
def footer_scripts():
  code = '\
    <script src="jquery-1.7.2.min.js"></script>\n \
    <script src="bootstrap/js/bootstrap.min.js"></script>\n \
    <script src="script.js"></script>\n \
    </body>\n \
    </html>'
  return code
  
def index_create():
  code = base_header()
  code += navbar_code()
  code += index_code()
  code += footer_scripts()
  outfile = open('index.html', 'w')
  outfile.write(code)
  outfile.close()

def sections_create():
  for section in sections:
    code = base_header()
    code += navbar_code(section[0:4])
    code += section_code(section)
    code += footer_scripts()
    outfile = open(section[0:4] + '.html', 'w')
    outfile.write(code)
    outfile.close()
  
if __name__ == '__main__':
  index_create()
  sections_create()
