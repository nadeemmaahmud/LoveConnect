from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponse
from django.conf import settings
from .forms import UserRegistrationForm, UserProfileForm, AdminUserEditForm, UserPasswordChangeForm
from .models import User


@login_required
def debug_profile_pic(request):
    """Debug view to check profile picture configuration"""
    user = request.user
    
    try:
        pic_url = user.profile_pic.url if user.profile_pic else 'None'
    except Exception as e:
        pic_url = f'ERROR: {str(e)}'
    
    info = {
        'username': user.username,
        'has_profile_pic_field': bool(user.profile_pic),
        'profile_pic_path': str(user.profile_pic) if user.profile_pic else 'None',
        'profile_pic_url': pic_url,
        'default_file_storage': getattr(settings, 'DEFAULT_FILE_STORAGE', 'NOT SET'),
        'cloudinary_configured': 'cloudinary' in str(getattr(settings, 'DEFAULT_FILE_STORAGE', '')),
        'cloudinary_storage': getattr(settings, 'CLOUDINARY_STORAGE', {}),
    }
    html = "<h2>Profile Picture Debug</h2><ul>"
    for key, value in info.items():
        html += f"<li><strong>{key}:</strong> {value}</li>"
    html += "</ul><hr>"
    html += "<h3>Instructions:</h3>"
    html += "<ol>"
    html += "<li>If 'cloudinary_configured' is True, Cloudinary is working</li>"
    html += "<li>If 'has_profile_pic_field' is True but image doesn't show, the old file was deleted</li>"
    html += "<li><strong>Solution:</strong> Go to profile, upload a NEW image to replace the broken one</li>"
    html += "</ol>"
    html += "<p><a href='/user/profile/'>Go to Profile</a></p>"
    return HttpResponse(html)


@login_required
def promote_to_admin(request):
    """One-time use endpoint to promote current user to admin"""
    # Security: Only allow if there are no admin users yet
    if User.objects.filter(role='admin').exists():
        return HttpResponse('Admin users already exist. This endpoint is disabled.', status=403)
    
    user = request.user
    user.role = 'admin'
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    messages.success(request, f'Congratulations! You have been promoted to admin.')
    return redirect('admin_dashboard')


def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to our dating website.')
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'user/login.html')


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('landing')


@login_required
def profile_view(request):
    """View and edit user profile"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            # Debug: Log what happened with profile_pic
            import logging
            logger = logging.getLogger(__name__)
            logger.info(f"Profile updated for {user.username}")
            logger.info(f"Profile pic field: {user.profile_pic}")
            logger.info(f"Profile pic URL: {user.profile_pic.url if user.profile_pic else 'None'}")
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'user/profile.html', {'form': form})


@login_required
def admin_dashboard(request):
    """Admin dashboard to view all users"""
    if request.user.role != 'admin':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('profile')
    
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'user/admin_dashboard.html', {'users': users})


@login_required
def admin_edit_user(request, user_id):
    """Admin view to edit any user's credentials"""
    if request.user.role != 'admin':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('profile')
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = AdminUserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'User {user.username} updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = AdminUserEditForm(instance=user)
    
    return render(request, 'user/admin_edit_user.html', {'form': form, 'edited_user': user})


@login_required
def admin_delete_user(request, user_id):
    """Admin view to delete a user"""
    if request.user.role != 'admin':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('profile')
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'User {username} deleted successfully!')
        return redirect('admin_dashboard')
    
    return render(request, 'user/admin_delete_user.html', {'deleted_user': user})


@login_required
def change_password(request):
    """View for users to change their own password"""
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserPasswordChangeForm(request.user)
    
    return render(request, 'user/change_password.html', {'form': form})
