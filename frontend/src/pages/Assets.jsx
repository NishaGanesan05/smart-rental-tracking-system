import { useState } from 'react'
import { assets } from '../data/assets'

function Assets() {
  const [search, setSearch] = useState('')
  const [statusFilter, setStatusFilter] = useState('ALL')

  const filteredAssets = assets.filter((asset) => {
    const matchesSearch =
      asset.id.toLowerCase().includes(search.toLowerCase()) ||
      asset.type.toLowerCase().includes(search.toLowerCase()) ||
      asset.site.toLowerCase().includes(search.toLowerCase())

    const matchesStatus =
      statusFilter === 'ALL' ||
      asset.status === statusFilter

    return matchesSearch && matchesStatus
  })

  return (
    <div className="page">

      <div className="page-header">
        <div>
          <p className="eyebrow">FLEET MANAGEMENT</p>

          <h1>Assets</h1>

          <p>
            Monitor and manage all rental equipment.
          </p>
        </div>

        <button className="primary-button">
          + Add Asset
        </button>
      </div>


      <div className="asset-controls">

        <input
          type="text"
          placeholder="Search assets..."
          value={search}
          onChange={(event) => setSearch(event.target.value)}
        />

        <select
          value={statusFilter}
          onChange={(event) =>
            setStatusFilter(event.target.value)
          }
        >
          <option value="ALL">All statuses</option>
          <option value="ACTIVE">Active</option>
          <option value="UNASSIGNED">Unassigned</option>
        </select>

      </div>


      <div className="panel">

        <div className="panel-header">

          <div>
            <h2>All Assets</h2>

            <p>
              {filteredAssets.length} assets found
            </p>
          </div>

        </div>


        <div className="asset-table">

          <div className="asset-table-header">
            <span>Asset ID</span>
            <span>Type</span>
            <span>Site</span>
            <span>Status</span>
          </div>


          {filteredAssets.map((asset) => (

            <div
              className="asset-table-row"
              key={asset.id}
            >

              <strong>
                {asset.id}
              </strong>

              <span>
                {asset.type}
              </span>

              <span>
                {asset.site}
              </span>

              <span
                className={`status ${
                  asset.status === 'ACTIVE'
                    ? 'active-status'
                    : 'warning-status'
                }`}
              >
                {asset.status}
              </span>

            </div>

          ))}


          {filteredAssets.length === 0 && (

            <div className="empty-state">
              No assets found.
            </div>

          )}

        </div>

      </div>

    </div>
  )
}

export default Assets