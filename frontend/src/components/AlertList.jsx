import { useEffect, useState } from 'react'

function AlertList() {
  const [alerts, setAlerts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/alerts/')
      .then((response) => response.json())
      .then((data) => {
        setAlerts(data)
        setLoading(false)
      })
      .catch((error) => {
        console.error('Error fetching alerts:', error)
        setLoading(false)
      })
  }, [])

  if (loading) {
    return <p>Loading alerts...</p>
  }

  return (
    <div className="alert-list">
      {alerts.map((alert) => (
        <div className="alert-item" key={alert.alert_id}>
          <div className={`alert-icon ${alert.severity.toLowerCase()}`}>
            !
          </div>

          <div>
            <strong>{alert.alert_type.replace('_', ' ')}</strong>
            <span>{alert.message}</span>
          </div>
        </div>
      ))}
    </div>
  )
}

export default AlertList