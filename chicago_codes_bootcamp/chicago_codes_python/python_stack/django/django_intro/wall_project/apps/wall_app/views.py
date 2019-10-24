from django.shortcuts import render, redirect
from .models import Message, Comment
from django.contrib import messages
from apps.log_reg.models import User
from django.http import HttpResponse


def index(request):
    if request.session['logged']:
        user = User.objects.get(id=request.session['user_id'])
        all_messages = Message.objects.all()
        context = {
            'all_messages': all_messages,
            'user': user
        }
        return render(request, 'wall_app/index.html', context)
    else:
        return redirect('/')

def logout(request):
    return redirect('/logout')

def process_message(request):
    errors = Message.objects.msg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='message')
        return redirect('/wall')
    else:
        user = User.objects.get(id=request.session['user_id'])
        Message.objects.create(text=request.POST['message'], user=user)
        return redirect('/wall')

def process_comment(request):
    errors = Message.objects.cmt_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='comment')
        return redirect('/wall')
    else:
        user = User.objects.get(id=request.session['user_id'])
        message_parent = Message.objects.get(id=request.POST['message_id'])
        Comment.objects.create(text=request.POST['comment'], user=user, message=message_parent)
        return redirect('/wall')

def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('/wall')

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/wall')

def like_message(request, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    message.likes.add(user)
    message.save()
    print('*'*50)
    print(f'USER: {user.username}, MESSAGE: {message.id}')
    return HttpResponse('Success!')

def like_comment(request, comment_id):
    user = User.objects.get(id=request.session['user_id'])
    comment = Comment.objects.get(id=comment_id)
    comment.likes.add(user)
    comment.save()
    print('*'*50)
    print(f'USER: {user.username}, COMMENT: {comment.id}')
    return redirect('/wall')

def unlike_message(request, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    message.likes.remove(user)
    print('*'*50)
    print(f'USER: {user.username}, MESSAGE: {message.id}')
    return redirect('/wall')

def unlike_comment(request, comment_id):
    user = User.objects.get(id=request.session['user_id'])
    comment = Comment.objects.get(id=comment_id)
    comment.likes.remove(user)
    print('*'*50)
    print(f'USER: {user.username}, COMMENT: {comment.id}')
    return redirect('/wall')