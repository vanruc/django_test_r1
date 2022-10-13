from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Leads


def lead_listing(request):
    leads_list = Leads.objects.all()

    # filter leads subscribed in current month of year
    current_month_leads = leads_list.filter(
        created__year=timezone.now().year,
        created__month=timezone.now().month
    ).count()

    # filter un-subscribed leads
    unsub_leads = leads_list.filter(
        status='UNS'
    ).count()

    # hard-coded item per page = 15
    item_per_page = 15
    paginator = Paginator(leads_list, item_per_page)

    # get page number from request url, if there are no page parameter then
    # get default = 1
    page_number = request.GET.get('page', 1)

    leads = paginator.get_page(page_number)
    context = {
        'total_leads': leads_list.count(),
        'leads': leads,
        'current_month_leads_count': current_month_leads,
        'unsub_leads': unsub_leads,
    }
    return render(request, 'unity/leads/list.html', context)


def todo_task_list():
    """
    1) Copy, edit and get js widget to consume Lead API
    2) done: create django project
    3) done: create unit app
    4) done: create data model store subscribed email
    5) expose an REST API to be used by the widget to submit the email data.
    6) done: Create a Django view for listing the emails.
    As shown in the figma file for reference :
    https://www.figma.com/file/CYhfwmtEK4Xm7ZsNM6Swej/Unity?node-id=0%3A1
    7) Bonus - set up a celery task that runs every Monday and Wednesday and
    prints the number
    of new emails added in the current calendar month to the console.
    """
    pass
