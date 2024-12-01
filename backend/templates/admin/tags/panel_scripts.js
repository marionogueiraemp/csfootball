<script>
class PanelUpdater {
    constructor() {
        this.updateInterval = 30000;
        this.initializeUpdates();
    }

    async updateStats() {
        const response = await fetch('/api/monitoring/stats/');
        const data = await response.json();
        this.updateStatsPanel(data.cache_stats);
        this.updateAlertPanel(data.alerts);
        this.updateTaskPanel(data.task_stats);
    }

    updateStatsPanel(stats) {
        document.querySelector('.stats-panel .hit-rate').textContent = `${stats.hit_rate}%`;
        document.querySelector('.stats-panel .memory-usage').textContent = this.formatMemory(stats.memory_usage);
        document.querySelector('.stats-panel .total-keys').textContent = stats.total_keys;
    }

    updateAlertPanel(alerts) {
        const alertList = document.querySelector('.alert-list');
        alertList.innerHTML = alerts.map(alert => this.createAlertItem(alert)).join('');
    }

    updateTaskPanel(stats) {
        document.querySelector('.task-stats .success-rate').textContent = `${stats.success_rate}%`;
        document.querySelector('.task-stats .total-tasks').textContent = stats.total_tasks;
    }

    initializeUpdates() {
        setInterval(() => this.updateStats(), this.updateInterval);
    }
}

const panelUpdater = new PanelUpdater();
</script>
