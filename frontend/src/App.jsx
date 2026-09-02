import { useEffect, useState } from 'react'
import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from 'react-router-dom'

import './App.css'

import Assets from './pages/Assets'
import Rentals from './pages/Rentals'
import Alerts from './pages/Alerts'
import Recommendations from './pages/Recommendations'
import MLInsights from './pages/MLInsights'

import KPICard from './components/KPICard'
import AssetTable from './components/AssetTable'
import AlertList from './components/AlertList'
import RecommendationCard from './components/RecommendationCard'
import AssetStatusChart from './components/AssetStatusChart'

function Dashboard() {
  const [kpis, setKpis] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/kpis/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch KPIs')
        }

        return response.json()
      })
      .then((data) => {
        setKpis(data)
      })
      .catch((error) => {
        console.error('Error fetching KPIs:', error)
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
            className="nav-item active"
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
            className="nav-item"
            to="/recommendations"
          >
            <span>✦</span>
            Recommendations
          </Link>


          {/* ML Insights */}
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


        {/* KPI Cards */}
        <section className="kpi-grid">

          <KPICard
            label="Total Assets"
            value={
              kpis
                ? kpis.total_assets
                : '...'
            }
            description="Tracked equipment"
          />


          <KPICard
            label="Active Rentals"
            value={
              kpis
                ? kpis.active_rentals
                : '...'
            }
            description="Currently rented"
          />


          <KPICard
            label="Utilization"
            value={
              kpis
                ? `${kpis.fleet_utilization}%`
                : '...'
            }
            description="Fleet utilization"
          />


          <KPICard
            label="Active Alerts"
            value={
              kpis
                ? kpis.active_alerts
                : '...'
            }
            description="Require attention"
          />

        </section>


        {/* Dashboard Panels */}
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


              <Link
                className="view-button"
                to="/assets"
              >
                View all
              </Link>

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


              <Link
                className="view-button"
                to="/alerts"
              >
                View all
              </Link>

            </div>


            <AlertList />

          </div>

        </section>

        {/* Asset Status Analytics */}
        <section className="panel">

          <div className="panel-header">

            <div>
              <h2>Asset Status Distribution</h2>

              <p>
                Current distribution of tracked equipment
              </p>
            </div>

          </div>

          <AssetStatusChart />

        </section>



        {/* AI Recommendation */}
        <RecommendationCard />

      </main>

    </div>
  )
}


function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* Dashboard */}
        <Route
          path="/"
          element={<Dashboard />}
        />


        {/* Assets */}
        <Route
          path="/assets"
          element={<Assets />}
        />


        {/* Rentals */}
        <Route
          path="/rentals"
          element={<Rentals />}
        />


        {/* Alerts */}
        <Route
          path="/alerts"
          element={<Alerts />}
        />


        {/* Recommendations */}
        <Route
          path="/recommendations"
          element={<Recommendations />}
        />


        {/* ML Insights */}
        <Route
          path="/ml-insights"
          element={<MLInsights />}
        />

      </Routes>

    </BrowserRouter>
  )
}


export default App