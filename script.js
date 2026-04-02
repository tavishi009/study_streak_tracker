async function fetchStats() {
    const res = await fetch("/stats");
    const data = await res.json();

    document.getElementById("total").innerText = data.total_days;
    document.getElementById("streak").innerText = data.streak;
}

async function addSession() {
    await fetch("/add", { method: "POST" });
    fetchStats();
}

fetchStats();