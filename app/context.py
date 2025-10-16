# myapp/context.py
from contextvars import ContextVar
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Company

# Create context variable for the current company
_current_company: ContextVar = ContextVar('current_company', default=None)


def get_current_company() -> Optional['Company']:
    """
        Function to get the current company from context.
        Returns None if no company is set in the context.
    """
    return _current_company.get()


def set_current_company(company: Optional['Company']) -> None:
    """
        Function to set the current company in context.
        Pass None to clear the current company.
    """
    _current_company.set(company)
