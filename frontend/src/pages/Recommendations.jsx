import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

function Recommendations() {
  const [recommendations, setRecommendations] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/recommendations/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch recommendations')
        }

        return response.json()
      })
      .then((data) => {
        setRecommendations(data)
        setLoading(false)
      })
      .catch((error) => {
        console.error('Error fetching recommendations:', error)
        setError('Unable to load recommendation data.')
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

          {/* Dashboard */}
          <Link
            className="nav-item"
            to="/"
          >
            <span>▦</span>
            Dashboard
          </Link>


          {/* Assets */}
          <Link
            className="nav-item"
            to="/assets"
          >
            <span>◈</span>
            Assets
          </Link>


          {/* Rentals */}
          <Link
            className="nav-item"
            to="/rentals"
          >
            <span>▣</span>
            Rentals
          </Link>


          {/* Alerts */}
          <Link
            className="nav-item"
            to="/alerts"
          >
            <span>!</span>
            Alerts
          </Link>


          {/* Recommendations */}
          <Link
            className="nav-item active"
            to="/recommendations"
          >
            <span>✦</span>
            Recommendations
          </Link>

          <Link className="nav-item" to="/ml-insights">
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

        {/* Header */}
        <header className="topbar">

          <div>

            <p className="eyebrow">
              FLEET INTELLIGENCE
            </p>

            <h1>
              Recommendations
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


        {/* Page Introduction */}
        <section className="page-intro">

          <div>

            <h2>
              AI Recommendations
            </h2>

            <p>
              Actionable recommendations generated from fleet activity and detected issues.
            </p>

          </div>


          <Link
            className="view-button"
            to="/"
          >
            Back to Dashboard
          </Link>

        </section>


        {/* Recommendations Panel */}
        <section className="panel">

          <div className="panel-header">

            <div>

              <h2>
                Recommended Actions
              </h2>

              <p>
                Prioritized actions for fleet and rental management
              </p>

            </div>

          </div>


          {/* Loading */}
          {loading && (
            <p>
              Loading recommendations...
            </p>
          )}


          {/* Error */}
          {!loading && error && (
            <p>
              {error}
            </p>
          )}


          {/* Empty */}
          {!loading && !error && recommendations.length === 0 && (
            <p>
              No recommendations found.
            </p>
          )}


          {/* Recommendations */}
          {!loading && !error && recommendations.length > 0 && (

            <div className="alert-list">

              {recommendations.map((recommendation) => (

                <div
                  className="alert-item"
                  key={recommendation.recommendation_id}
                >

                  <div
                    className={`alert-icon ${
                      recommendation.priority.toLowerCase()
                    }`}
                  >
                    ✦
                  </div>


                  <div>

                    <strong>
                      {recommendation.recommendation_type.replaceAll('_', ' ')}
                    </strong>

                    <span>
                      {recommendation.message}
                    </span>

                    <span>
                      Asset: {recommendation.asset_id}
                      {' · '}
                      Priority: {recommendation.priority}
                    </span>

                    <span>
                      Reason: {recommendation.reason}
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

export default Recommendations