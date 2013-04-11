import web
from web import form

render = web.template.render('templates/')

urls = (
  '/calc', 'calc',
  '/(.*)', 'hello',
)
app = web.application(urls, globals())

calc_input = form.Form(
    form.Textbox('value 1',
        form.notnull,
        form.regexp('\d+', 'Must be a number.')),
    form.Dropdown('operator', ['+', '-', '*', '/']),
    form.Textbox('value 2'),
)

class calc:
  def GET(self):
    form = calc_input()
    return render.formtest(form)

  def POST(self):
    form = calc_input()
    if not form.validates():
      return render.formtest(form)
    else:
      val1 = int(form['value 1'].value)
      val2 = int(form['value 2'].value)
      op = form['operator'].value
      answer = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y,
          }[op](val1, val2)
      return '%d %s %d = %s' % (val1, op, val2, answer)

class hello:        
  def GET(self, name):
    return render.index(name)

if __name__ == "__main__":
  app.run()
