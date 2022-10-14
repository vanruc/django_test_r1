from celery import shared_task, Celery
from .models import Leads, Store
from django.utils import timezone
app = Celery()


@shared_task()
def send_leads_statistics():
    # get list of store, then loop through them
    stores = Store.objects.all()
    for store in stores:
        # looking for store-owner information
        store_owner = store.store_owner
        store_email = store_owner.email
        # get number of store's leads subscribed in current calendar month
        store_leads_count = Leads.objects.filter(
            store=store,
            created__year= timezone.now().year,
            created__month= timezone.now().month
        ).count()
        email_content = f"""
        store name: {store.store_name}
        email to: {store_email}
        subject: Leads statistics
        message: Number subscribed in this month: { store_leads_count } 
        =============================================="""
        print(email_content)
