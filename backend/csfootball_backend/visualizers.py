import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta


class CacheMonitoringVisualizer:
    @staticmethod
    def create_performance_chart(metrics):
        fig = make_subplots(rows=2, cols=1)

        timestamps = [m['timestamp'] for m in metrics]
        hits = [m['hits'] for m in metrics]
        misses = [m['misses'] for m in metrics]

        fig.add_trace(
            go.Scatter(x=timestamps, y=hits, name="Cache Hits"),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=timestamps, y=misses, name="Cache Misses"),
            row=1, col=1
        )

        return fig.to_html()

    @staticmethod
    def create_memory_usage_chart(metrics):
        fig = go.Figure()

        timestamps = [m['timestamp'] for m in metrics]
        memory_usage = [m['memory_usage'] for m in metrics]

        fig.add_trace(
            go.Scatter(x=timestamps, y=memory_usage, name="Memory Usage")
        )

        return fig.to_html()
