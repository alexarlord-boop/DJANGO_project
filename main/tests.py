from django.test import TestCase
from .models import Activity, Goal
from .views import is_goal_in_list
from .views import get_data
from .views import make_map_with_filter_options


# Create your tests here.
class GoalTestCase(TestCase):
    def setUp(self):
        Goal.objects.create(title='serf')

    def test_goal_list(self):
        # test_goal = Goal.objects.get(title='')
        title1 = 'on_water'
        title2 = 'under_water'
        title3 = 's_mount'
        title4 = 'air1'
        title5 = 'air2'
        title6 = 'air3'
        self.assertEqual(is_goal_in_list(title1), True)
        self.assertEqual(is_goal_in_list(title2), True)
        self.assertEqual(is_goal_in_list(title3), True)
        self.assertEqual(is_goal_in_list(title4), False)
        self.assertEqual(is_goal_in_list(title5), False)
        self.assertEqual(is_goal_in_list(title6), False)


class DataTestCase(TestCase):
    def test_get_data(self):
        self.assertEqual(bool(get_data()), True)


class MapActivTestCase(TestCase):
    def test_method(self):
        post_data = {'type': 's_mount',
                     'season': 'summer',
                     'enviroment_chars': '1',
                     'extreme': '1'}

        map, activities = make_map_with_filter_options(post_data)
        self.assertEqual(bool(activities), True)