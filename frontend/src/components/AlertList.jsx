import { alerts } from '../data/alerts'

function AlertList() {
  return (
    <div className="alert-list">
      {alerts.map((alert) => (
        <div className="alert-item" key={alert.id}>
          <div className={`alert-icon ${alert.severity}`}>
            !
          </div>

          <div>
            <strong>{alert.title}</strong>
            <span>{alert.details}</span>
          </div>
        </div>
      ))}
    </div>
  )
}

export default AlertList