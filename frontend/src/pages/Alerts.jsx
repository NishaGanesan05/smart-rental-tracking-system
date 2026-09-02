import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

function Alerts() {
  const [alerts, setAlerts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/alerts/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch alerts')
        }

        return response.json()
      })
      .then((data) => {
        setAlerts(data)
        setLoading(false)
      })
      .catch((error) => {
        console.error('Error fetching alerts:', error)
        setError('Unable to load alert data.')
        setLoading(false)
      })
  }, [])

  return (
    <div className="app">

      {/* Sidebar */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-icon">
            SR
          </div>

          <div>
            <h2>Smart Rental</h2>
            <span>Tracking System</span>
          </div>
        </div>

        <nav className="navigation">

          <Link
            className="nav-item"
            to="/"
          >
            <span>▦</span>
            Dashboard
          </Link>

          <Link
            className="nav-item"
            to="/assets"
          >
            <span>◈</span>
            Assets
          </Link>

          <Link
            className="nav-item"
            to="/rentals"
          >
            <span>▣</span>
            Rentals
          </Link>

          <Link
            className="nav-item active"
            to="/alerts"
          >
            <span>!</span>
            Alerts
          </Link>

          <Link
            className="nav-item"
            to="/recommendations"
          >
            <span>✦</span>
            Recommendations
          </Link>

          <Link
            className="nav-item"
            to="/ml-insights"
            >
            <span>◉</span>
            ML Insights
            </Link>

        </nav>

        <div className="sidebar-footer">
          <span className="status-dot"></span>
          System Operational
        </div>

      </aside>


      {/* Main Content */}
      <main className="main-content">

        <header className="topbar">

          <div>
            <p className="eyebrow">
              FLEET MANAGEMENT
            </p>

            <h1>
              Alerts
            </h1>
          </div>

          <div className="user-info">

            <div className="user-avatar">
              AD
            </div>

            <div>
              <strong>Admin</strong>
              <span>Fleet Manager</span>
            </div>

          </div>

        </header>


        <section className="page-intro">

          <div>

            <h2>
              Fleet Alerts
            </h2>

            <p>
              Monitor equipment issues and events requiring attention.
            </p>

          </div>

          <Link
            className="view-button"
            to="/"
          >
            Back to Dashboard
          </Link>

        </section>


        <section className="panel">

          <div className="panel-header">

            <div>

              <h2>
                All Alerts
              </h2>

              <p>
                Detected equipment anomalies and operational issues
              </p>

            </div>

          </div>


          {/* Loading */}
          {loading && (
            <p>
              Loading alerts...
            </p>
          )}


          {/* Error */}
          {!loading && error && (
            <p>
              {error}
            </p>
          )}


          {/* Empty State */}
          {!loading && !error && alerts.length === 0 && (
            <p>
              No alerts found.
            </p>
          )}


          {/* Alerts */}
          {!loading && !error && alerts.length > 0 && (

            <div className="alert-list">

              {alerts.map((alert) => (

                <div
                  className="alert-item"
                  key={alert.alert_id}
                >

                  <div
                    className={`alert-icon ${alert.severity.toLowerCase()}`}
                  >
                    !
                  </div>


                  <div>

                    <strong>
                      {alert.alert_type.replaceAll('_', ' ')}
                    </strong>

                    <span>
                      {alert.message}
                    </span>

                    <span>
                      Asset: {alert.asset_id} · Status: {alert.status}
                    </span>

                  </div>

                </div>

              ))}

            </div>

          )}

        </section>

      </main>

    </div>
  )
}

export default Alerts