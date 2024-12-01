from datetime import datetime, timedelta
import json
from .task_monitoring import TaskMonitor


class TaskReporting:
    @staticmethod
    def generate_daily_report():
        stats = TaskMonitor.get_task_stats()
        total_tasks = stats['success_count'] + stats['failure_count']

        return {
            'date': datetime.now().date().isoformat(),
            'summary': {
                'total_tasks': total_tasks,
                'success_rate': (stats['success_count'] / total_tasks * 100) if total_tasks > 0 else 0,
                'failure_rate': (stats['failure_count'] / total_tasks * 100) if total_tasks > 0 else 0
            },
            'task_history': stats['history']
        }

    @staticmethod
    def export_report(format='json'):
        report = TaskReporting.generate_daily_report()
        if format == 'json':
            return json.dumps(report, indent=2)
        return report
