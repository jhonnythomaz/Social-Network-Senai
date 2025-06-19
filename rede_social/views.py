# Arquivo completo: rede_social/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post, Comment, Invite, Notification
from .forms import PostForm, CommentForm, CustomUserCreationForm
from django.contrib.auth import login

@login_required 
def home_page(request):
    friends_from_sent = Invite.objects.filter(sender=request.user, status=Invite.Status.ACCEPTED).values_list('receiver_id', flat=True)
    friends_from_received = Invite.objects.filter(receiver=request.user, status=Invite.Status.ACCEPTED).values_list('sender_id', flat=True)
    friend_ids = list(friends_from_sent) + list(friends_from_received)
    posts = Post.objects.filter(Q(user_id__in=friend_ids) | Q(user=request.user)).order_by('-created_at')
    contexto = {'posts': posts}
    return render(request, 'pages/index.html', contexto)

@login_required
def all_users_view(request):
    friends1 = Invite.objects.filter(sender=request.user, status=Invite.Status.ACCEPTED).values_list('receiver_id', flat=True)
    friends2 = Invite.objects.filter(receiver=request.user, status=Invite.Status.ACCEPTED).values_list('sender_id', flat=True)
    friend_ids = list(friends1) + list(friends2)
    sent_pending_ids = Invite.objects.filter(sender=request.user, status=Invite.Status.SENT).values_list('receiver_id', flat=True)
    received_pending_ids = Invite.objects.filter(receiver=request.user, status=Invite.Status.SENT).values_list('sender_id', flat=True)
    users_to_exclude = [request.user.id] + friend_ids + list(sent_pending_ids) + list(received_pending_ids)
    users = User.objects.exclude(id__in=users_to_exclude)
    contexto = {'users': users}
    return render(request, 'pages/all_users.html', contexto)

@login_required
def send_invite_view(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    _, created = Invite.objects.get_or_create(sender=request.user, receiver=receiver)
    if created:
        Notification.objects.create(
            recipient=receiver,
            sender=request.user,
            notification_type=Notification.NotificationType.INVITE,
            text=f'{request.user.username} te enviou um convite de amizade.'
        )
    return redirect('all_users')

@login_required
def invites_view(request):
    invites = Invite.objects.filter(receiver=request.user, status=Invite.Status.SENT)
    contexto = {'invites': invites}
    return render(request, 'pages/invites.html', contexto)

@login_required
def accept_invite_view(request, invite_id):
    invite = get_object_or_404(Invite, id=invite_id, receiver=request.user)
    invite.status = Invite.Status.ACCEPTED
    invite.save()
    return redirect('invites')

@login_required
def reject_invite_view(request, invite_id):
    invite = get_object_or_404(Invite, id=invite_id, receiver=request.user)
    invite.status = Invite.Status.REJECTED
    invite.save()
    return redirect('invites')

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home_page')
    else:
        form = PostForm()
    return render(request, 'pages/create_post.html', {'form': form})

@login_required
def profile_view(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    contexto = {'profile_user': profile_user, 'posts': posts}
    return render(request, 'pages/profile.html', contexto)

@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            if post.user != request.user:
                Notification.objects.create(
                    recipient=post.user,
                    sender=request.user,
                    notification_type=Notification.NotificationType.COMMENT,
                    text=f'{request.user.username} comentou no seu post.',
                    post=post
                )
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'pages/post_detail.html', context)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {'form': form})

@login_required
def like_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        if post.user != request.user:
            Notification.objects.create(
                recipient=post.user,
                sender=request.user,
                notification_type=Notification.NotificationType.LIKE,
                text=f'{request.user.username} curtiu seu post.',
                post=post
            )
    return redirect(request.META.get('HTTP_REFERER', 'home_page'))

@login_required
def notification_view(request):
    # Busca todas as notificações para o usuário logado, da mais nova para a mais antiga
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')

    # Marca todas as notificações não lidas como lidas
    # Isso acontece assim que o usuário visita a página
    notifications.filter(is_read=False).update(is_read=True)

    context = {
        'notifications': notifications
    }
    return render(request, 'pages/notifications.html', context)