from django.contrib import admin
# Corrigido: removemos 'Friendship' da lista de importação
from .models import Post, Comment, Invite 

# Registrando os modelos que existem para aparecerem na área de admin
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Invite)

