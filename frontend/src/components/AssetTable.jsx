import { useEffect, useState } from 'react'

function AssetTable() {
  const [assets, setAssets] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/assets/')
      .then((response) => response.json())
      .then((data) => {
        setAssets(data)
        setLoading(false)
      })
      .catch((error) => {
        console.error('Error fetching assets:', error)
        setLoading(false)
      })
  }, [])

  if (loading) {
    return <p>Loading assets...</p>
  }

  return (
    <div className="asset-list">
      {assets.map((asset) => (
        <div className="asset-row" key={asset.asset_id}>
          <div>
            <strong>{asset.asset_id}</strong>

            <span>
              {asset.asset_type} · {asset.site_id}
            </span>
          </div>

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
    </div>
  )
}

export default AssetTable