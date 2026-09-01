import { Link } from 'react-router-dom'
import AssetTable from '../components/AssetTable'

function Assets() {
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

          <Link className="nav-item" to="/">
            <span>▦</span>
            Dashboard
          </Link>

          <Link className="nav-item active" to="/assets">
            <span>◈</span>
            Assets
          </Link>

          <a
            className="nav-item"
            href="#"
            onClick={(event) => event.preventDefault()}
          >
            <span>▣</span>
            Rentals
          </a>

          <a
            className="nav-item"
            href="#"
            onClick={(event) => event.preventDefault()}
          >
            <span>!</span>
            Alerts
          </a>

          <a
            className="nav-item"
            href="#"
            onClick={(event) => event.preventDefault()}
          >
            <span>✦</span>
            Recommendations
          </a>

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
              Assets
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
            <h2>Asset Inventory</h2>

            <p>
              Monitor and manage all tracked rental equipment.
            </p>
          </div>

          <Link className="view-button" to="/">
            Back to Dashboard
          </Link>

        </section>


        {/* Assets Table */}
        <section className="panel">

          <div className="panel-header">

            <div>
              <h2>
                All Assets
              </h2>

              <p>
                Current equipment status and assignment
              </p>
            </div>

          </div>

          <AssetTable />

        </section>

      </main>

    </div>
  )
}

export default Assets