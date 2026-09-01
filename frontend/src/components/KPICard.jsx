function KPICard({ label, value, description }) {
  return (
    <div className="kpi-card">
      <span className="kpi-label">{label}</span>

      <strong className="kpi-value">
        {value}
      </strong>

      <span className="kpi-description">
        {description}
      </span>
    </div>
  )
}

export default KPICard