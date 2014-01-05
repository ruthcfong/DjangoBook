# from django.template.loader import get_template
# from django.template import Context
# from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals()) #local() -> {'current_date': now}
    # now = datetime.datetime.now()
    # return render_to_response('current_datetime.html',{'current_date': now})
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, hours_offset):
    try:
        hours_offset = int(hours_offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hours_offset)
    return render_to_response('hours_ahead.html', locals())
    # html = "<html><body>In %s hours(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)