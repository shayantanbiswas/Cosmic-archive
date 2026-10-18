from django.shortcuts import render
from .models import CosmicObject


def cosmic_home(request):
    objects = CosmicObject.objects.all()

    selected_planet = request.GET.get("planet")
    selected_object = None

    if selected_planet:
        selected_object = CosmicObject.objects.filter(
            name=selected_planet
        ).first()

    return render(
        request,
        "archive/cosmic.html",
        {
            "objects": objects,
            "selected_object": selected_object,
        }
    )