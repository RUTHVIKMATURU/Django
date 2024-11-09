from django.shortcuts import render,redirect
from .models import Entry
# Create your views here.
def home(request):
  return render(request,'Home.html')
def getAllEntries(request):
  objs =Entry.objects.all().order_by('timestamp')
  context = {
    'entries':objs
  }
  return render(request,'viewDiaryEntries.html',context=context)
def addnewEntry(request):
  if request.method == 'POST':
    heading = request.POST.get('heading')
    entry = request.POST.get('entry')
    obj = Entry.objects.create(header=heading,entry=entry)
    return redirect('/')
  return render(request,'Entry.html')

def custom_404_view(request, exception=None):
    return render(request,'notFound.html', status=404)
def getIndividualEntry(request,id):
  context ={}
  obj = Entry.objects.get(id=id)
  if obj:
    context['entry'] = obj
    return render(request,'diaryEntry.html',context)
  else:
    context['entry']= "Invalid ID"
    return render(request,'notFound.html')