const ACTION_COPY = {
  2: "Stabilize regional reserve dispatch windows before the next demand swing.",
  3: "Validate export balance and confirm reserve coverage on the evening ramp.",
  5: "Review hydro and storage availability against weather-linked load shifts.",
  7: "Rebalance import exposure and verify alternate routing for constrained supply.",
  11: "Verify industrial load-shed readiness and dispatch communications coverage.",
  13: "Prepare operator escalation pack and issue a high-risk telemetry briefing.",
  19: "Stage emergency procurement options and notify cross-border support partners.",
};

function formatObserved(timestamp) {
  const date = new Date(timestamp);
  return new Intl.DateTimeFormat("en-US", {
    dateStyle: "medium",
    timeStyle: "short",
    timeZone: "UTC",
  }).format(date) + " UTC";
}

function riskTone(vulnerability) {
  if (vulnerability >= 0.7) {
    return "Critical posture. Immediate intervention and escalation are required.";
  }
  if (vulnerability >= 0.4) {
    return "Stressed posture. Conditions are elevated and need active management.";
  }
  return "Managed posture. Current conditions remain below critical thresholds.";
}

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error("Unable to load feed JSON.");
  }
  return response.json();
}

function renderFeed(country, feed) {
  document.getElementById("liveTimestamp").textContent = `Live ${formatObserved(feed.t)}`;
  document.getElementById("feedTitle").textContent = `${country.name} country feed`;
  document.getElementById("feedRegion").textContent = `${country.iso} · ${country.region}`;
  document.getElementById("ediValue").textContent = feed.edi.toFixed(2);
  document.getElementById("fragilityValue").textContent = feed.fragility.toFixed(2);
  document.getElementById("vulnerabilityValue").textContent = feed.vulnerability.toFixed(2);
  document.getElementById("isoValue").textContent = feed.iso;
  document.getElementById("observedValue").textContent = formatObserved(feed.t);
  document.getElementById("hashValue").textContent = feed.ota_hash;
  document.getElementById("feedCommand").textContent = `curl -s ./data/feeds/${country.file}`;
  document.getElementById("riskSummary").textContent = riskTone(feed.vulnerability);
  document.getElementById("riskFill").style.width = `${Math.max(feed.vulnerability * 100, 6)}%`;

  const actions = document.getElementById("actionList");
  actions.innerHTML = "";
  feed.actions_next24h.forEach((actionId) => {
    const item = document.createElement("li");
    item.textContent = `Action ${actionId}: ${ACTION_COPY[actionId] ?? "Review queued operator procedure."}`;
    actions.appendChild(item);
  });
}

async function loadFeed(country) {
  return loadJson(`../data/feeds/${country.file}`);
}

function populateCountrySelect(countries) {
  const select = document.getElementById("countrySelect");
  select.innerHTML = "";
  countries.forEach((country) => {
    const option = document.createElement("option");
    option.value = country.iso;
    option.textContent = `${country.name} (${country.iso})`;
    select.appendChild(option);
  });
}

async function init() {
  try {
    const countries = await loadJson("../data/feeds/countries.json");
    populateCountrySelect(countries);

    const select = document.getElementById("countrySelect");

    async function updateSelectedFeed() {
      const country = countries.find((entry) => entry.iso === select.value) ?? countries[0];
      const feed = await loadFeed(country);
      renderFeed(country, feed);
    }

    select.value = countries[0].iso;
    select.addEventListener("change", () => {
      updateSelectedFeed().catch((error) => {
        document.getElementById("riskSummary").textContent = error.message;
      });
    });

    await updateSelectedFeed();
  } catch (error) {
    document.getElementById("liveTimestamp").textContent = "Feed unavailable";
    document.getElementById("riskSummary").textContent = error.message;
    document.getElementById("actionList").innerHTML = "<li>Feed load failed.</li>";
  }
}

init();
