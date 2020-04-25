from django.shortcuts import render, get_object_or_404
# from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question,Choice

# Create your views here.
def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date') [:5]
# 	# output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse("Hello World!")
# 	# template = loader.get_template('poll/index.html')
# 	context = {'latest_question_list': latest_question_list,}
# 	# return HttpResponse(template.render(context, request))
# 	return render(request, 'poll/index.html', context)

# def details(request, question_id):
# 	# try:
# 	# 	question = Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question Does Not Exist")
# 	# return render(request, 'poll/detail.html', {'question': question})
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'poll/detail.html',{'question': question})

# def results(request, question_id):
# 	# response = "You're looking at the results of question %s."
# 	# return HttpResponse(response %question_id)
# 	question = get_object_or_404(Question, pk = question_id)
# 	return render(request, 'poll/results.html', {'question': question})


# def vote(request, question_id):
# 	# return HttpResponse("You're voting on question %s." %question_id)
# 	question = Question.objects.get(pk = question_id)
# 	try:
# 		selected_choice = question.choice_set.get(pk = request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 		return render(request, 'poll/detail.html', {'question': question, 'error_msg': "You didn't select a choice"})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		return HttpResponseRedirect(reverse('poll:results',args=(question_id,)))

class IndexView(generic.ListView):
	template_name = 'poll/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions"""
		return Question.objects.order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
	template_name = 'poll/detail.html'
	model = Question

class ResultsView(generic.DetailView):
	template_name = 'poll/results.html'
	model = Question

def vote(request, question_id):
	# return HttpResponse("You're voting on question %s." %question_id)
	question = Question.objects.get(pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'poll/detail.html', {'question': question, 'error_msg': "You didn't select a choice"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('poll:results',args=(question_id,)))