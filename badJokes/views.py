from django.shortcuts import render, redirect
from django.template import loader

from django.http import HttpResponse
from .models import Players, Badjokes
# import pandas as pd
from django.db.models import Count, Sum, Max
from django.utils import timezone

def round_num():
	return Badjokes.objects.all().aggregate(Max('game_round'))['game_round__max']

def index(request):
    all_players = Players.objects.all()
    # new_score(request, round_num)
    scores = list(Badjokes.objects.filter(game_round=round_num()).values('players').annotate(acc_score=Sum('scores')))
    for player in all_players:
    	player.acc_score = 0
    	for i in scores:
    		if i['players']== player.id:
    			player.acc_score = i['acc_score']

    template = loader.get_template('index.html')
    context = {
        'all_players': all_players,
        'round_num': round_num,
    	}
    return HttpResponse(template.render(context, request))

def new_score(request):
	joke = Badjokes(players_id = request.POST['player_id'],
					game_round = round_num(),
					scores = request.POST['new_score'],
					pub_date=timezone.now())
	joke.save()
	return redirect('/badJokes/')

def new_player(request):
	if request.method == 'POST':
		player = Players(person = request.POST['person'],
						photo_link = request.POST['photo_link'],
						is_active = 1,
						pub_date=timezone.now())
		player.save()
	template = loader.get_template('new_player.html')
	context = {}
	return HttpResponse(template.render(context, request))

		


