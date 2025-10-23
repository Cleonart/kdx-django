from django.core.cache import cache
from .context import set_current_company
from .models import Company


class CompanyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session = request.session
        session_company_code: str = session.get('kdx.company_code')
        company: Company = None

        if session_company_code:
            cache_key: str = f'company_code_{session_company_code}'
            company: Company = cache.get(cache_key)
            if company is None:
                try:
                    company = Company.objects.get(code=session_company_code)
                    cache.set(cache_key, company, 3600)
                except Company.DoesNotExist:
                    company = None

        # Set the company in context
        set_current_company(company)

        # Process the request
        response = self.get_response(request)
        return response
