from django.shortcuts import render
from django.utils import timezone
from core.data import datastore
from .models import ShopScheduler


def shop_view(request):
    page_url = "shop/shop.html"
    final_list = []
    now = timezone.now()
    active_schedules = ShopScheduler.objects.filter(
        start_time__lte=now,
        end_time__gte=now
    )
    for schedule in active_schedules:
        scheduled_items = schedule.scheduled_items.all()
        for item in scheduled_items:
            if item.character.can_participate_in_rotation:
                char_id = item.character.id
                for legend in datastore.legends:
                    legend_id = legend["id"]
                    if legend_id == char_id:
                        total_power = sum(legend["powerstats"].values())
                        pair = {
                            "model": item.character,
                            "json": legend,
                            "power": total_power
                        }
                        final_list.append(pair)
    final_list.sort(key=lambda pair:pair["model"].name)

    context = {
        "characters":final_list
    }
    return render(request, page_url, context)
