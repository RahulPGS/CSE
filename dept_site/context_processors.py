from .models import Timetablenacedemics

def get_time_n_academics(res):
    return {
        'time_table': Timetablenacedemics.objects.get(is_time=True),
        'academics': Timetablenacedemics.objects.get(is_time=False)
    }