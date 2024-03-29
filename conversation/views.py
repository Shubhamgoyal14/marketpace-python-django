from django.shortcuts import get_object_or_404, redirect, render 
from conversation.models import Conversation 
from item.models import Item 
from .forms import ConversationMessageForm 
# Create your views here. 

def new_conversation(request, item_pk): 
    item = get_object_or_404(Item, pk = item_pk) 
    
    if item.created_by == request.user: 
        return redirect('dashboard:index') 
    
    converstions = Conversation.objects.filter(item=item).filter(members__in=[request.user.id]) 
     
    if request.method == 'POST': 
        form = ConversationMessageForm(request.POST) 
        
        if form.is_valid(): 
            conversation = Conversation.objects.create(item = item) 
            conversation.members.add(request.user) 
            conversation.members.add(item.created_by) 
            conversation.save() 
            
            conversation_message = form.save(commit=True) 
            conversation_message.created_by = request.user 
            conversation_message.save() 
            
            return redirect('item:detail', pk = item_pk) 
    else: 
        form = ConversationMessageForm() 
        
    return render(request, 'conversation/new.html',{ 
        'form': form, 
    }) 