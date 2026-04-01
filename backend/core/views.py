import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import SocialAccount, ScheduledPost, Analytics


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['socialaccount_count'] = SocialAccount.objects.count()
    ctx['socialaccount_facebook'] = SocialAccount.objects.filter(platform='facebook').count()
    ctx['socialaccount_instagram'] = SocialAccount.objects.filter(platform='instagram').count()
    ctx['socialaccount_twitter'] = SocialAccount.objects.filter(platform='twitter').count()
    ctx['scheduledpost_count'] = ScheduledPost.objects.count()
    ctx['scheduledpost_draft'] = ScheduledPost.objects.filter(status='draft').count()
    ctx['scheduledpost_scheduled'] = ScheduledPost.objects.filter(status='scheduled').count()
    ctx['scheduledpost_published'] = ScheduledPost.objects.filter(status='published').count()
    ctx['analytics_count'] = Analytics.objects.count()
    ctx['analytics_daily'] = Analytics.objects.filter(period='daily').count()
    ctx['analytics_weekly'] = Analytics.objects.filter(period='weekly').count()
    ctx['analytics_monthly'] = Analytics.objects.filter(period='monthly').count()
    ctx['analytics_total_value'] = Analytics.objects.aggregate(t=Sum('value'))['t'] or 0
    ctx['recent'] = SocialAccount.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def socialaccount_list(request):
    qs = SocialAccount.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(platform__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(platform=status_filter)
    return render(request, 'socialaccount_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def socialaccount_create(request):
    if request.method == 'POST':
        obj = SocialAccount()
        obj.platform = request.POST.get('platform', '')
        obj.username = request.POST.get('username', '')
        obj.followers = request.POST.get('followers') or 0
        obj.status = request.POST.get('status', '')
        obj.profile_url = request.POST.get('profile_url', '')
        obj.save()
        return redirect('/socialaccounts/')
    return render(request, 'socialaccount_form.html', {'editing': False})


@login_required
def socialaccount_edit(request, pk):
    obj = get_object_or_404(SocialAccount, pk=pk)
    if request.method == 'POST':
        obj.platform = request.POST.get('platform', '')
        obj.username = request.POST.get('username', '')
        obj.followers = request.POST.get('followers') or 0
        obj.status = request.POST.get('status', '')
        obj.profile_url = request.POST.get('profile_url', '')
        obj.save()
        return redirect('/socialaccounts/')
    return render(request, 'socialaccount_form.html', {'record': obj, 'editing': True})


@login_required
def socialaccount_delete(request, pk):
    obj = get_object_or_404(SocialAccount, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/socialaccounts/')


@login_required
def scheduledpost_list(request):
    qs = ScheduledPost.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'scheduledpost_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def scheduledpost_create(request):
    if request.method == 'POST':
        obj = ScheduledPost()
        obj.title = request.POST.get('title', '')
        obj.platform = request.POST.get('platform', '')
        obj.content = request.POST.get('content', '')
        obj.scheduled_date = request.POST.get('scheduled_date') or None
        obj.status = request.POST.get('status', '')
        obj.likes = request.POST.get('likes') or 0
        obj.shares = request.POST.get('shares') or 0
        obj.save()
        return redirect('/scheduledposts/')
    return render(request, 'scheduledpost_form.html', {'editing': False})


@login_required
def scheduledpost_edit(request, pk):
    obj = get_object_or_404(ScheduledPost, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.platform = request.POST.get('platform', '')
        obj.content = request.POST.get('content', '')
        obj.scheduled_date = request.POST.get('scheduled_date') or None
        obj.status = request.POST.get('status', '')
        obj.likes = request.POST.get('likes') or 0
        obj.shares = request.POST.get('shares') or 0
        obj.save()
        return redirect('/scheduledposts/')
    return render(request, 'scheduledpost_form.html', {'record': obj, 'editing': True})


@login_required
def scheduledpost_delete(request, pk):
    obj = get_object_or_404(ScheduledPost, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/scheduledposts/')


@login_required
def analytics_list(request):
    qs = Analytics.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(platform__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(period=status_filter)
    return render(request, 'analytics_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def analytics_create(request):
    if request.method == 'POST':
        obj = Analytics()
        obj.platform = request.POST.get('platform', '')
        obj.metric = request.POST.get('metric', '')
        obj.period = request.POST.get('period', '')
        obj.value = request.POST.get('value') or 0
        obj.change_percent = request.POST.get('change_percent') or 0
        obj.date = request.POST.get('date') or None
        obj.save()
        return redirect('/analyticses/')
    return render(request, 'analytics_form.html', {'editing': False})


@login_required
def analytics_edit(request, pk):
    obj = get_object_or_404(Analytics, pk=pk)
    if request.method == 'POST':
        obj.platform = request.POST.get('platform', '')
        obj.metric = request.POST.get('metric', '')
        obj.period = request.POST.get('period', '')
        obj.value = request.POST.get('value') or 0
        obj.change_percent = request.POST.get('change_percent') or 0
        obj.date = request.POST.get('date') or None
        obj.save()
        return redirect('/analyticses/')
    return render(request, 'analytics_form.html', {'record': obj, 'editing': True})


@login_required
def analytics_delete(request, pk):
    obj = get_object_or_404(Analytics, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/analyticses/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['socialaccount_count'] = SocialAccount.objects.count()
    data['scheduledpost_count'] = ScheduledPost.objects.count()
    data['analytics_count'] = Analytics.objects.count()
    return JsonResponse(data)
