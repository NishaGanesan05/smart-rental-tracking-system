import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Assets from './pages/Assets'
import './App.css'

import KPICard from './components/KPICard'
import AssetTable from './components/AssetTable'
import AlertList from './components/AlertList'
import RecommendationCard from './components/RecommendationCard'

function App() {
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

          <a className="nav-item active" href="#">
            <span>▦</span>
            Dashboard
          </a>

          <a className="nav-item" href="#">
            <span>◈</span>
            Assets
          </a>

          <a className="nav-item" href="#">
            <span>▣</span>
            Rentals
          </a>

          <a className="nav-item" href="#">
            <span>!</span>
            Alerts
          </a>

          <a className="nav-item" href="#">
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
              CONTROL TOWER
            </p>

            <h1>
              Smart Rental Dashboard
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


        {/* KPI Section */}
        <section className="kpi-grid">

          <KPICard
            label="Total Assets"
            value="7"
            description="Tracked equipment"
          />

          <KPICard
            label="Active Rentals"
            value="4"
            description="Currently rented"
          />

          <KPICard
            label="Utilization"
            value="76%"
            description="Fleet utilization"
          />

          <KPICard
            label="Active Alerts"
            value="3"
            description="Require attention"
          />

        </section>


        {/* Main Dashboard Panels */}
        <section className="dashboard-grid">

          {/* Asset Overview */}
          <div className="panel">

            <div className="panel-header">

              <div>
                <h2>
                  Asset Overview
                </h2>

                <p>
                  Current equipment status
                </p>
              </div>

              <button className="view-button">
                View all
              </button>

            </div>

            <AssetTable />

          </div>


          {/* Alerts */}
          <div className="panel">

            <div className="panel-header">

              <div>
                <h2>
                  Alerts
                </h2>

                <p>
                  Issues requiring attention
                </p>
              </div>

              <button className="view-button">
                View all
              </button>

            </div>

            <AlertList />

          </div>

        </section>


        {/* AI Recommendation */}
        <RecommendationCard />

      </main>

    </div>
  )
}

export default App