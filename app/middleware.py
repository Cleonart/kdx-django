from django.core.cache import cache
from .context import set_current_company
from .models import Company


class CompanyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Option 1: Get company from subdomain
        if hasattr(request, 'tenant'):
            company = request.tenant

        # Option 2: Get company from header (API)
        elif 'X-Company-Code' in request.headers:
            company_code = request.headers['X-Company-Code']
            cache_key: str = f'company_code_{company_code}'
            company = cache.get(cache_key)

            # if not in cache, fetch from DB and set cache
            if company is None:
                company = Company.objects.get(code=company_code)
                cache.set(cache_key, company, 3600)
        else:
            company = None

        # Set the company in context
        set_current_company(company)

        # Process the request
        response = self.get_response(request)
        return response
