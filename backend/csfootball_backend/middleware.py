from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .cache_keys import CacheKeyGenerator
from .monitoring import CacheMonitor
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        jwt_authenticator = JWTAuthentication()
        try:
            auth_result = jwt_authenticator.authenticate(request)
            if auth_result:
                user, token = auth_result
                request.user = user
                request.token = token
            else:
                request.user = AnonymousUser()
        except:
            request.user = AnonymousUser()


class CacheMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method != 'GET':
            return None

        if hasattr(request, 'resolver_match') and request.resolver_match:
            model_name = getattr(request.resolver_match, 'app_name', 'default')
        else:
            model_name = 'default'

        cache_key = CacheKeyGenerator.get_list_key(
            model_name=model_name,
            user_id=request.user.id if request.user.is_authenticated else None
        )

        response = cache.get(cache_key)
        if response:
            return response

        return None

    def process_response(self, request, response):
        if request.method == 'GET' and response.status_code == 200:
            if hasattr(request, 'resolver_match') and request.resolver_match:
                model_name = getattr(
                    request.resolver_match, 'app_name', 'default')
            else:
                model_name = 'default'

            cache_key = CacheKeyGenerator.get_list_key(
                model_name=model_name,
                user_id=request.user.id if request.user.is_authenticated else None
            )

            cache.set(cache_key, response)

        return response


class CacheMonitorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method != 'GET':
            return None

        if hasattr(request, 'resolver_match') and request.resolver_match:
            model_name = getattr(request.resolver_match, 'app_name', 'default')
        else:
            model_name = 'default'

        cache_key = CacheKeyGenerator.get_list_key(
            model_name=model_name,
            user_id=request.user.id if request.user.is_authenticated else None
        )

        response = cache.get(cache_key)
        if response:
            CacheMonitor.log_cache_hit(cache_key)
            return response

        CacheMonitor.log_cache_miss(cache_key)
        return None

    def process_response(self, request, response):
        if request.method == 'GET' and response.status_code == 200:
            if hasattr(request, 'resolver_match') and request.resolver_match:
                model_name = getattr(
                    request.resolver_match, 'app_name', 'default')
            else:
                model_name = 'default'

            cache_key = CacheKeyGenerator.get_list_key(
                model_name=model_name,
                user_id=request.user.id if request.user.is_authenticated else None
            )

            cache.set(cache_key, response)

        return response


class MonitoringDashboardMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'monitoring' in request.path and not request.user.is_staff:
            messages.error(
                request, 'Access denied. Staff privileges required.')
            return redirect(reverse('admin:login'))
        return None
