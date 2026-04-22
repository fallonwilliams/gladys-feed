from dataclasses import dataclass


@dataclass(frozen=True)
class CallSign:
    scientist: str
    strength: str
    why: str


CALL_SIGNS = {
    "gateway": CallSign("Katherine Johnson", "Precision", "Edge computer crunches raw SCADA inputs with dependable rigor."),
    "modem": CallSign("Dorothy Vaughan", "Adaptability", "The modem shifts networks quickly to preserve telemetry flow."),
    "starlink_dish": CallSign("Mary Jackson", "Boundary-breaking", "The dish extends connectivity across hard coverage boundaries."),
    "power_brick": CallSign("Christine Darden", "Endurance", "Steady power delivery mirrors long-horizon engineering discipline."),
    "ct_clamp": CallSign("Valerie Thomas", "Insight", "Turns invisible current into a usable data stream."),
    "env_sensor": CallSign("Patricia Cowings", "Resilience", "Tracks environmental stress that affects system stability."),
    "sd_firmware": CallSign("Annie Easley", "Codecraft", "Firmware operationalizes optimization and control logic at the edge."),
    "ops_bot": CallSign("Mae Jemison", "Exploration", "Explores operational patterns and emerging anomalies across the feed."),
    "policy_bot": CallSign("Alberta King", "Equity", "Supports governance workflows meant to stay human-centered."),
    "launch_director": CallSign("Charlie Blackwell-Thompson", "Decisiveness", "Represents clear go or no-go operational decision points."),
    "chief_flight_director": CallSign("Emily Nelson", "Coordination", "Coordinates multiple operational loops into one coherent response."),
    "eclss_manager": CallSign("Catherine Koerner", "Life-support stewardship", "Anchors monitoring around survivability-critical conditions."),
    "capcom_ops": CallSign("Anne McClain", "Clarity", "Favors concise, reliable communication during active operations."),
    "capcom_backup": CallSign("Nicole Mann", "Calm", "Represents backup communications continuity under pressure."),
    "tps_lead": CallSign("Sujata Gosalia", "Thermal integrity", "Maps to heat and thermal boundary monitoring responsibilities."),
    "medical_lead": CallSign("Jennifer Fogarty", "Health resilience", "Frames the feed around sustained operational health, not only uptime."),
    "egs_test_director": CallSign("Jessica Parsons", "Ground-system vigilance", "Represents disciplined readiness checks before live operations."),
    "sercom": CallSign("Kiarre Dumes", "Telemetry vigilance", "Owns the integrity of live sensor data collection and review."),
}
