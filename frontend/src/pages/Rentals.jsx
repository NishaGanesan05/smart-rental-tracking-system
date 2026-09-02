import { Link } from 'react-router-dom'
import { useEffect, useMemo, useState } from 'react'

function Rentals() {
  const [rentals, setRentals] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [selectedStatus, setSelectedStatus] = useState('ALL')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/rentals/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch rentals')
        }

        return response.json()
      })
      .then((data) => {
        setRentals(data)
        setLoading(false)
      })
      .catch((error) => {
        console.error('Error fetching rentals:', error)
        setError('Unable to load rental data.')
        setLoading(false)
      })
  }, [])

  const filteredRentals = useMemo(() => {
    if (selectedStatus === 'ALL') {
      return rentals
    }

    return rentals.filter(
      (rental) => rental.status === selectedStatus
    )
  }, [rentals, selectedStatus])

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
            className="nav-item active"
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

        {/* Header */}
        <header className="topbar">

          <div>

            <p className="eyebrow">
              FLEET MANAGEMENT
            </p>

            <h1>
              Rentals
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
              Rental Management
            </h2>

            <p>
              Monitor active, overdue, and returned equipment rentals.
            </p>

          </div>

          <Link
            className="view-button"
            to="/"
          >
            Back to Dashboard
          </Link>

        </section>

        {/* Rental Table */}
        <section className="panel">

          <div className="panel-header">

            <div>

              <h2>
                Rental Contracts
              </h2>

              <p>
                View and filter equipment rental activity.
              </p>

            </div>

            {/* Rental Status Filter */}
            <div className="filter-group">

              <label htmlFor="rental-status">
                Rental Status
              </label>

              <select
                id="rental-status"
                value={selectedStatus}
                onChange={(event) =>
                  setSelectedStatus(event.target.value)
                }
                className="filter-select"
              >

                <option value="ALL">
                  All Rentals
                </option>

                <option value="ACTIVE">
                  Active
                </option>

                <option value="OVERDUE">
                  Overdue
                </option>

                <option value="RETURNED">
                  Returned
                </option>

              </select>

            </div>

          </div>

          {/* Result Count */}
          {!loading && !error && (
            <div className="filter-result-count">
              Showing {filteredRentals.length} of {rentals.length} rentals
            </div>
          )}

          {/* Loading */}
          {loading && (
            <p>
              Loading rentals...
            </p>
          )}

          {/* Error */}
          {!loading && error && (
            <p>
              {error}
            </p>
          )}

          {/* Empty */}
          {!loading &&
            !error &&
            filteredRentals.length === 0 && (
              <p>
                No rentals found for the selected status.
              </p>
            )}

          {/* Rentals */}
          {!loading &&
            !error &&
            filteredRentals.length > 0 && (

              <div className="asset-list">

                {filteredRentals.map((rental) => (

                  <div
                    className="asset-row"
                    key={rental.rental_id}
                  >

                    <div>

                      <strong>
                        {rental.rental_id}
                      </strong>

                      <span>
                        {rental.asset_id} · Customer {rental.customer_id}
                      </span>

                      <span>
                        {rental.start_date} → {rental.expected_return_date}
                      </span>

                      {rental.actual_return_date && (
                        <span>
                          Actual Return: {rental.actual_return_date}
                        </span>
                      )}

                    </div>

                    <span
                      className={`status ${
                        rental.status === 'ACTIVE'
                          ? 'active-status'
                          : rental.status === 'RETURNED'
                            ? 'returned-status'
                            : 'danger-status'
                      }`}
                    >
                      {rental.status}
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

export default Rentals