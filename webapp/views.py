from email.mime import audio
import random
from django.shortcuts import redirect, render
from .models import PhelkayWord, ZhebsaWord
from .forms import ContactDetailsForm
# Create your views here.

def index(request):
    if 'searchQuery' in request.GET != '' and (q := request.GET['searchQuery']):
        search_dzongkha = ZhebsaWord.objects.filter(zhebsa_word__contains = q).values('zhebsa_word','phelkay__p_phrase','phelkay__phelkay_word')
        search_zhesa = ZhebsaWord.objects.filter(phelkay__phelkay_word__contains = q).prefetch_related('zhesa').values('zhebsa_word','z_phrase','audio','phelkay__phelkay_word')

        if search_dzongkha.exists():
            context = {
                'search': search_dzongkha,
                'q':q
            }
        elif search_zhesa.exists():
            context = {
                'search_zhesa': search_zhesa,
                'q':q
            }

        else:
            context = {
                'noresult': q,
                'q':q
                }
    else:
        all_zhebsa = list(ZhebsaWord.objects.all())
        day_zhesa = random.sample(all_zhebsa,3)[0]
        day_phalkay = ZhebsaWord.objects.filter(zhebsa_word__contains = day_zhesa).values('phelkay__phelkay_word')
        context = {
            'day_zhebsa': day_zhesa,
            'day_phalkay': day_phalkay,
            'q':''
            }

    return render(request, 'webapp/index.html', context)



def about(request):
    return render(request, 'webapp/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactDetailsForm()
    context = {
        'form': form
    }

    return render(request, 'webapp/contact.html', context)
