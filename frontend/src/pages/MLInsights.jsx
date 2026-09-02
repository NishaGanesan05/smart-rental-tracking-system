import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

function MLInsights() {
  const [anomalies, setAnomalies] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/ml/anomalies')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch ML anomaly data')
        }

        return response.json()
      })
      .then((data) => {
        console.log('ML API response:', data)

        if (Array.isArray(data)) {
          setAnomalies(data)
        } else if (Array.isArray(data.results)) {
          setAnomalies(data.results)
        } else if (Array.isArray(data.anomalies)) {
          setAnomalies(data.anomalies)
        } else {
          setAnomalies([])
        }

        setLoading(false)
      })
      .catch((error) => {
        console.error('Error fetching ML anomalies:', error)
        setError('Unable to load ML anomaly data.')
        setLoading(false)
      })
  }, [])

  const anomalyCount = anomalies.filter(
    (item) => item.is_anomaly
  ).length

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
            className="nav-item"
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
            className="nav-item active"
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
              FLEET INTELLIGENCE
            </p>

            <h1>
              ML Insights
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
              Anomaly Detection
            </h2>

            <p>
              Machine learning analysis of fleet telemetry and equipment behaviour.
            </p>

          </div>


          <Link
            className="view-button"
            to="/"
          >
            Back to Dashboard
          </Link>

        </section>


        {/* ML Summary */}
        <section className="kpi-grid">

          <div className="panel">

            <div className="panel-header">

              <div>
                <h2>
                  Telemetry Records
                </h2>

                <p>
                  Records analysed by the ML model
                </p>
              </div>

            </div>

            <strong>
              {loading ? '...' : anomalies.length}
            </strong>

          </div>


          <div className="panel">

            <div className="panel-header">

              <div>
                <h2>
                  Anomalies Detected
                </h2>

                <p>
                  Records identified as unusual
                </p>
              </div>

            </div>

            <strong>
              {loading ? '...' : anomalyCount}
            </strong>

          </div>

        </section>


        {/* ML Results */}
        <section className="panel">

          <div className="panel-header">

            <div>

              <h2>
                ML Anomaly Results
              </h2>

              <p>
                Isolation Forest analysis of telemetry behaviour
              </p>

            </div>

          </div>


          {loading && (
            <p>
              Running ML analysis...
            </p>
          )}


          {!loading && error && (
            <p>
              {error}
            </p>
          )}


          {!loading && !error && anomalies.length === 0 && (
            <p>
              No ML results found.
            </p>
          )}


          {!loading && !error && anomalies.length > 0 && (

            <div className="asset-list">

              {anomalies.map((item) => (

                <div
                  className="asset-row"
                  key={item.telemetry_id}
                >

                  <div>

                    <strong>
                      {item.asset_id}
                    </strong>

                    <span>
                      Runtime: {item.runtime_hours ?? 0} h
                      {' · '}
                      Idle: {item.idle_hours ?? 0} h
                    </span>

                    <span>
                      Fuel: {item.fuel_level ?? 0}%
                      {' · '}
                      Speed: {item.speed ?? 0}
                    </span>

                    <span>
                      Anomaly Score: {item.anomaly_score}
                    </span>

                  </div>


                  <span
                    className={`status ${
                      item.is_anomaly
                        ? 'warning-status'
                        : 'active-status'
                    }`}
                  >
                    {item.is_anomaly
                      ? item.anomaly_status
                      : 'NORMAL'}
                  </span>

                </div>

              ))}

            </div>

          )}

        </section>

      </main>

    </div>
  )
}

export default MLInsights