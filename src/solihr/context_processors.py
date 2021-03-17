from jobs.models import choices, Industry


def cities_and_industries(request):
    return {
        'all_cities': choices['city'][:5],
        'all_industries': Industry.objects.all()[:5]
    }