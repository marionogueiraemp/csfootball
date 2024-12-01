<script>
    class DashboardUpdater {
        constructor() {
            this.updateInterval = 30000;
            this.charts = {};
            this.initializeCharts();
            this.startAutoUpdate();
        }
    
        async fetchLatestData() {
            const response = await fetch('/api/monitoring/cache-monitor/stats/');
            return await response.json();
        }
    
        updateCharts(data) {
            this.charts.performance.update(data.metrics);
            this.charts.memory.update(data.memory_usage);
            this.updateStats(data.stats);
            this.updateAlerts(data.alerts);
        }
    
        updateStats(stats) {
            document.getElementById('hit-rate').textContent = `${stats.hit_rate.toFixed(2)}%`;
            document.getElementById('memory-usage').textContent = `${stats.memory_usage} MB`;
            document.getElementById('total-keys').textContent = stats.total_keys;
        }
    
        startAutoUpdate() {
            setInterval(async () => {
                const data = await this.fetchLatestData();
                this.updateCharts(data);
            }, this.updateInterval);
        }
    }
    
    const dashboardUpdater = new DashboardUpdater();
    </script>
    