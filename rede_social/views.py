from django.shortcuts import render
from .models import Post, Invite, Friendship

def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'pages/index.html', {'posts':posts})


# def envio_de_convites(request):
#     pass

#     meus_convites = Invite.objects.filter(reciever_id=request.user)

#     meus_convites.status = "APROVED" 
    
    # Friendship.objects.create(
    #     sender=meus_convites.sender.
    # )

# def alterar_status(request, id):
#     meus_convites = Invite.objects.filter(id=id)


