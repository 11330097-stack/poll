from django.shortcuts import render 
from .models import polll, Option 
from django.views.generic import ListView ,DetailView, RedirectView
from django.urls import reverse
# Create your views here.
def polll_list(req):
    pollls = polll.objects.all()
    return render(req, "default/list.html",{'polll_list':pollls, 'msg': 'Hello!'})

class PollList(ListView):
    model = polll

    #應用程式名稱/資料模型_list.html
    #default/poll_list.html

class PollView(DetailView):
    model =polll
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        option_list =Option.objects.filter(poll_id=self.object.id)
        ctx['option_list']=option_list
        return ctx

class PollVote(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        option =Option.objects.get(id = self.kwargs['oid'])
        option.votes += 1   # option.votes = option.votes + 1
        option.save()
        return reverse('poll_view' , args=[option.poll_id]) 
        #return reverse('poll_view' ,kwargs=['pk':option.poll_id])
        #return "/poll/{}/".format(option.poll_id)
        #return f"/poll/{option.poll_id}"