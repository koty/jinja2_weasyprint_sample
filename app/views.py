from django.conf import settings
from django.http import HttpResponse
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def pdf_sample(request):
    template_dir = settings.TEMPLATES[0]['DIRS'][0]
    env = Environment(loader=FileSystemLoader(template_dir, encoding='utf8'))
    tpl = env.get_template('pdf_sample.html')
    html_str = tpl.render({
        'title':'私のスキル',
        'skills': ('python', 'django', 'C#', 'WPF', '立ち泳ぎ'),
    })
    pdf_file = HTML(string=html_str).write_pdf()
    return HttpResponse(pdf_file, content_type='application/pdf')
