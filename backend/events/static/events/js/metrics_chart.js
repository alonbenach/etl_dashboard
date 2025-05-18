export function renderMetricsChart(data) {
  const ctx = document.getElementById("metricsChart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: data.labels,
      datasets: [
        {
          label: "DAU",
          data: data.dau,
          borderColor: "blue",
          backgroundColor: "rgba(0,0,255,0.1)",
          fill: true,
          tension: 0.3,
        },
        {
          label: "Avg Events/User",
          data: data.avg,
          borderColor: "green",
          backgroundColor: "rgba(0,255,0,0.1)",
          fill: true,
          tension: 0.3,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true },
      },
    },
  });
}
