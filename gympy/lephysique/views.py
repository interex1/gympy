# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import date

def show_card(request, cardnumber):
    
    from lephysique.models import Card, Exercise1, Exercise2, Exercise3, Exercise4, Exercise5
    
	# We get Card object with cardnumber specified in URL
	
    c = Card.objects.get(number = cardnumber)

	
    # For each Exercise table we retrieve only the rows (records) related to the number of linked card.
	
    w1 = Exercise1.objects.filter(card__number=cardnumber).all()
    
    w2 = Exercise2.objects.filter(card__number=cardnumber).all()
    
    w3 = Exercise3.objects.filter(card__number=cardnumber).all()
  
    w4 = Exercise4.objects.filter(card__number=cardnumber).all()
            
    w5 = Exercise5.objects.filter(card__number=cardnumber).all() 
    
    
	
	# Check if logged user is_staff and pass this information to the template system
	
    if request.user.is_staff:
	    staff = 1
    else:
        staff = 0
	
	# Check if account is expired 
    if (c.account_expiration is not None and date.today() >= c.account_expiration):
        account_expired = 1
    else:
        account_expired = 0
	
	# Check if card is expired
    if (c.card_expiration is not None and date.today() >= c.card_expiration):
        card_expired = 1
    else:
        card_expired = 0

	
	# Render page
	
    return render_to_response('card.html', {'staff': staff, 'account_expired': account_expired, 'card_expired': card_expired, 'card': c, 'w1': w1, 'w2': w2, 'w3': w3, 'w4': w4, 'w5': w5})