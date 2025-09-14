from .models import List,  Category
from django.utils import timezone
from datetime import timedelta


class TaskService:
    def get_all_tasks(self):
        return List.objects.all()

    def get_task_by_id(self, list_id):
        return List.objects.get(pk=list_id)

    def get_tasks_for_today(self):
        today = timezone.now().date()
        return List.objects.filter(date=today)

    def get_tasks_by_category(self, category_name):
        return List.objects.filter(category__name=category_name)

    def delete_task(self, list_id):
        task = self.get_task_by_id(list_id)
        task.delete()

    def mark_completed(self, list_id, completed=True):
        task = self.get_task_by_id(list_id)
        task.completed = completed
        task.save()

    def update_task(self, list_id, item, completed):
        task = self.get_task_by_id(list_id)
        task.item = item
        task.completed = completed
        task.save()
        return task



class CategoryService:
    def get_all_categories(self):
        return Category.objects.all()

    def get_category_by_name(self, name):
        return Category.objects.filter(name=name).first()


class CalendarService:
    def __init__(self):
        self.task_service = TaskService()
        

    def get_task_events(self):
        tasks = self.task_service.get_all_tasks()
        events = []

        for task in tasks:
            event = {
                'title': task.item,
                'start': task.date.strftime('%Y-%m-%d'),
                'color': task.category.color if task.category else '#3B82F6',
                'category': task.category.name if task.category else 'No Category',
                'description': task.item
            }
            events.append(event)
        return events

    

    def get_all_events(self):
        return self.get_task_events() + self.get_calendar_events()
