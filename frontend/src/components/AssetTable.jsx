import { assets } from '../data/assets'

function AssetTable() {
  return (
    <div className="asset-list">
      {assets.map((asset) => (
        <div className="asset-row" key={asset.id}>
          <div>
            <strong>{asset.id}</strong>

            <span>
              {asset.type} · {asset.site}
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