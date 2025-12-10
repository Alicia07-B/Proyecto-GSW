def global_context(request):
    """Contexto global para todas las templates"""
    return {
        'site_name': 'GESINFRA-WEB',
        'current_year': 2025,
        'user': request.user,
    }